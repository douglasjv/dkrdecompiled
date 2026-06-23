#!/usr/bin/env python3
"""Rank unresolved DKR asm functions by rough difficulty or reference similarity."""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

from find_similar_functions import iter_candidates, parse_asm, score as similarity_score


ROOT = Path(__file__).resolve().parents[1]
BRANCH_OP_RE = re.compile(r"^(?:b|beq|bne|bgez|bgtz|blez|bltz|bc1[ft])\b")
JUMP_OP_RE = re.compile(r"^(?:j|jal)\b")


@dataclass(frozen=True)
class AsmScore:
    name: str
    path: Path
    instructions: int
    branches: int
    jumps: int
    stack_frame: int
    difficulty: float
    similar_to: str = ""
    similarity: float = 0.0


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def is_function_asm(path: Path) -> bool:
    if path.suffix != ".s":
        return False
    parts = path.relative_to(ROOT).parts
    if "data" in parts or "hasm" in parts:
        return False
    if path.name in {"header.s", "libm_vals.s", "llmuldiv_gcc.s"}:
        return False
    return True


def iter_asm_paths(root: Path) -> list[Path]:
    if root.is_file():
        return [root] if is_function_asm(root) else []
    return [path for path in sorted(root.glob("**/*.s")) if is_function_asm(path)]


def rough_difficulty(instructions: int, branches: int, jumps: int, stack_frame: int) -> float:
    return instructions + (branches * 8.0) + (jumps * 6.0) + min(stack_frame, 0x100) / 8.0


def make_score(path: Path) -> AsmScore | None:
    parsed = parse_asm(path)
    if not parsed.instructions:
        return None
    jumps = sum(1 for opcode in parsed.opcodes if JUMP_OP_RE.match(opcode))
    branches = sum(1 for opcode in parsed.opcodes if BRANCH_OP_RE.match(opcode))
    return AsmScore(
        name=path.stem,
        path=path,
        instructions=len(parsed.instructions),
        branches=branches,
        jumps=jumps,
        stack_frame=parsed.stack_frame,
        difficulty=rough_difficulty(
            len(parsed.instructions), branches, jumps, parsed.stack_frame
        ),
    )


def with_similarity(rows: list[AsmScore]) -> list[AsmScore]:
    references = [parse_asm(path) for path in iter_candidates(accepted_only=True)]
    if not references:
        references = [parse_asm(row.path) for row in rows]
    scored: list[AsmScore] = []
    for row in rows:
        target = parse_asm(row.path)
        best_path = ""
        best_score = 0.0
        for reference in references:
            if reference.path.resolve() == row.path.resolve():
                continue
            value = similarity_score(target, reference)
            if value > best_score:
                best_score = value
                best_path = rel(reference.path)
        scored.append(
            AsmScore(
                name=row.name,
                path=row.path,
                instructions=row.instructions,
                branches=row.branches,
                jumps=row.jumps,
                stack_frame=row.stack_frame,
                difficulty=row.difficulty,
                similar_to=best_path,
                similarity=best_score,
            )
        )
    scored.sort(key=lambda item: (-item.similarity, item.difficulty, item.name))
    return scored


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Rank asm functions for DKR discovery. This is advisory only; "
            "matching still requires source-level C and full Verify: OK."
        )
    )
    parser.add_argument(
        "path",
        nargs="?",
        default="asm/nonmatchings",
        help="asm file or directory to rank (default: asm/nonmatchings)",
    )
    parser.add_argument("--top", type=int, default=20, help="Rows to print")
    parser.add_argument(
        "--by-similarity",
        action="store_true",
        help="Rank by similarity to available asm references; falls back to unresolved peer similarity when no matched asm references are present",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON rows")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.path)
    if not root.is_absolute():
        root = ROOT / root
    if not root.exists():
        raise SystemExit(f"error: path not found: {root}")

    rows = [score for path in iter_asm_paths(root) if (score := make_score(path))]
    if args.by_similarity:
        rows = with_similarity(rows)
    else:
        rows.sort(key=lambda item: (item.difficulty, item.instructions, item.name))

    rows = rows[: args.top]
    if args.json:
        print(
            json.dumps(
                [
                    {
                        "function": row.name,
                        "path": rel(row.path),
                        "difficulty": round(row.difficulty, 3),
                        "instructions": row.instructions,
                        "branches": row.branches,
                        "jumps": row.jumps,
                        "stack_frame": row.stack_frame,
                        "similarity": round(row.similarity, 3),
                        "similar_to": row.similar_to,
                    }
                    for row in rows
                ],
                indent=2,
            )
        )
        return 0

    header = "function difficulty inst branch jump stack"
    if args.by_similarity:
        header += " similarity similar_to"
    print(header)
    for row in rows:
        line = (
            f"{row.name} {row.difficulty:0.1f} {row.instructions} "
            f"{row.branches} {row.jumps} 0x{row.stack_frame:X}"
        )
        if args.by_similarity:
            line += f" {row.similarity:0.3f} {row.similar_to}"
        print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
