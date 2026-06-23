#!/usr/bin/env python3
"""Rank asm functions that look similar to a target function.

This is a lightweight discovery helper for DKR routing. It compares normalized
opcode/operand n-grams from assembly files and prints likely source-shape
references. It does not prove behavior equivalence.
"""

from __future__ import annotations

import argparse
import math
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTER_RE = re.compile(r"\$(?:f\d+|zero|at|v[01]|a[0-3]|t[0-9]|s[0-8]|k[01]|gp|sp|fp|ra)")
NUMBER_RE = re.compile(r"(?<![A-Za-z_])[-+]?(?:0x[0-9A-Fa-f]+|\d+)")
STACK_RE = re.compile(r"\baddiu\s+\$sp\s*,\s*\$sp\s*,\s*(-?(?:0x[0-9A-Fa-f]+|\d+))")
BRANCH_RE = re.compile(r"^(?:b|beq|bne|bgez|bgtz|blez|bltz|bc1[ft])\b")


@dataclass(frozen=True)
class FunctionAsm:
    path: Path
    instructions: tuple[str, ...]
    opcodes: tuple[str, ...]
    stack_frame: int
    branches: int


def parse_int(text: str) -> int:
    return int(text, 16) if text.lower().startswith(("0x", "-0x")) else int(text)


def resolve_target(target: str) -> Path:
    path = Path(target)
    if path.exists():
        return path.resolve()
    if not path.is_absolute() and (ROOT / path).exists():
        return (ROOT / path).resolve()

    name = target[:-2] if target.endswith(".s") else target
    matches = sorted((ROOT / "asm").glob(f"**/{name}.s"))
    if not matches:
        raise SystemExit(f"error: no asm found for {target!r}")
    if len(matches) > 1:
        rels = "\n  ".join(str(match.relative_to(ROOT)) for match in matches)
        raise SystemExit(f"error: multiple asm files match {target!r}:\n  {rels}")
    return matches[0].resolve()


def strip_asm_prefix(line: str) -> str:
    if "*/" in line:
        line = line.split("*/", 1)[1]
    return line.split("#", 1)[0].strip()


def normalize_operands(operands: str) -> str:
    operands = REGISTER_RE.sub(lambda m: "$f" if m.group(0).startswith("$f") else "$r", operands)
    operands = re.sub(r"%(?:hi|lo)\([^)]+\)", "SYM", operands)
    operands = NUMBER_RE.sub("IMM", operands)
    operands = re.sub(r"\b(?:\.L|jtbl_|D_|g[A-Za-z_]|func_)[A-Za-z0-9_$.]*\b", "SYM", operands)
    operands = re.sub(r"\s+", "", operands)
    return operands


def parse_asm(path: Path) -> FunctionAsm:
    instructions: list[str] = []
    opcodes: list[str] = []
    stack_frame = 0
    branches = 0

    for raw in path.read_text(errors="ignore").splitlines():
        line = strip_asm_prefix(raw)
        if not line or line.startswith(".") or line.endswith(":"):
            continue
        parts = line.split(None, 1)
        opcode = parts[0]
        if opcode.endswith(":") or opcode.startswith("."):
            continue
        operands = parts[1] if len(parts) > 1 else ""
        normalized = f"{opcode} {normalize_operands(operands)}".strip()
        instructions.append(normalized)
        opcodes.append(opcode)
        if BRANCH_RE.match(opcode):
            branches += 1
        match = STACK_RE.search(line)
        if match:
            stack_frame = max(stack_frame, abs(parse_int(match.group(1))))

    return FunctionAsm(path, tuple(instructions), tuple(opcodes), stack_frame, branches)


def ngrams(items: tuple[str, ...], width: int) -> set[tuple[str, ...]]:
    if len(items) < width:
        return {items} if items else set()
    return {items[index : index + width] for index in range(len(items) - width + 1)}


def jaccard(left: set[object], right: set[object]) -> float:
    if not left and not right:
        return 1.0
    if not left or not right:
        return 0.0
    return len(left & right) / len(left | right)


def closeness(left: int, right: int) -> float:
    if left == right:
        return 1.0
    high = max(left, right, 1)
    return max(0.0, 1.0 - (abs(left - right) / high))


def score(target: FunctionAsm, candidate: FunctionAsm) -> float:
    inst_score = jaccard(ngrams(target.instructions, 3), ngrams(candidate.instructions, 3))
    opcode_score = jaccard(set(target.opcodes), set(candidate.opcodes))
    frame_score = closeness(target.stack_frame, candidate.stack_frame)
    branch_score = closeness(target.branches, candidate.branches)
    length_score = math.sqrt(closeness(len(target.instructions), len(candidate.instructions)))
    return (
        0.55 * inst_score
        + 0.20 * opcode_score
        + 0.10 * frame_score
        + 0.10 * branch_score
        + 0.05 * length_score
    )


def is_function_asm(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    if "data" in parts or "hasm" in parts:
        return False
    if path.name in {"header.s", "libm_vals.s", "llmuldiv_gcc.s"}:
        return False
    return True


def iter_candidates(accepted_only: bool) -> list[Path]:
    paths = [path for path in sorted((ROOT / "asm").glob("**/*.s")) if is_function_asm(path)]
    if accepted_only:
        return [path for path in paths if "nonmatchings" not in path.parts]
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Find asm functions with a similar normalized instruction shape."
    )
    parser.add_argument("target", help="Function name or asm path to compare")
    parser.add_argument("--top", type=int, default=10, help="Number of results to print")
    parser.add_argument(
        "--accepted-only",
        action="store_true",
        help="Only compare against non-data asm outside asm/nonmatchings",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target_path = resolve_target(args.target)
    target = parse_asm(target_path)
    if not target.instructions:
        raise SystemExit(f"error: no instructions parsed from {target_path}")

    rows: list[tuple[float, FunctionAsm]] = []
    for path in iter_candidates(args.accepted_only):
        if path.resolve() == target_path:
            continue
        parsed = parse_asm(path)
        if not parsed.instructions:
            continue
        rows.append((score(target, parsed), parsed))

    rows.sort(key=lambda row: row[0], reverse=True)
    print(f"target: {target_path.relative_to(ROOT)}")
    print(
        "score   insts  frame branches path\n"
        "------  -----  ----- -------- ----"
    )
    for value, parsed in rows[: args.top]:
        rel = parsed.path.relative_to(ROOT)
        print(
            f"{value:0.3f}  {len(parsed.instructions):5d}  "
            f"{parsed.stack_frame:5d} {parsed.branches:8d} {rel}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
