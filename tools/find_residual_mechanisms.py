#!/usr/bin/env python3
"""Find compiled C functions with a register-role pattern near a target asm window.

Unlike whole-function similarity, this helper preserves register equality across
the selected window. It is advisory: a hit is a source-shape precedent, not a
matching candidate.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from find_similar_functions import NUMBER_RE, resolve_target


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ELF = ROOT / "build" / "dkr.us.v77.elf"
DEFAULT_OBJDUMP = ROOT / "tools" / "binutils" / "mips64-elf-objdump"
DEFAULT_SIGNATURES = ROOT / "research" / "tasks" / "residual_signatures.json"
TARGET_INST_RE = re.compile(
    r"/\*\s+[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+[0-9A-Fa-f]{8}\s+\*/\s+(\S+)(?:\s+(.*?))?\s*$"
)
OBJDUMP_INST_RE = re.compile(r"^\s*([0-9A-Fa-f]+):\s+[0-9A-Fa-f]{8}\s+(\S+)(?:\s+(.*?))?\s*$")
SYMBOL_RE = re.compile(
    r"^([0-9A-Fa-f]+)\s+\w\s+F\s+\.(?:main|text)\s+([0-9A-Fa-f]+)\s+(\S+)$"
)
REGISTER_RE = re.compile(
    r"(?<![A-Za-z0-9_])\$?(f\d+|zero|at|v[01]|a[0-3]|t[0-9]|s[0-8]|k[01]|gp|sp|fp|ra)(?![A-Za-z0-9_])"
)


@dataclass(frozen=True)
class Instruction:
    address: int
    opcode: str
    operands: str


@dataclass(frozen=True)
class Function:
    name: str
    address: int
    size: int
    instructions: tuple[Instruction, ...]


def run_objdump(objdump: Path, *args: str) -> str:
    result = subprocess.run(
        [str(objdump), *args], check=True, text=True, capture_output=True
    )
    return result.stdout


def parse_target(path: Path) -> tuple[Instruction, ...]:
    rows: list[Instruction] = []
    started = False
    for line in path.read_text(errors="replace").splitlines():
        if line.strip() == f"glabel {path.stem}":
            started = True
            continue
        if started and line.startswith("glabel "):
            break
        if not started:
            continue
        match = TARGET_INST_RE.search(line)
        if match:
            rows.append(
                Instruction(
                    int(match.group(1), 16), match.group(2), match.group(3) or ""
                )
            )
    if not rows:
        raise SystemExit(f"error: no addressed instructions parsed from {path}")
    return tuple(rows)


def parse_elf(elf: Path, objdump: Path) -> tuple[Function, ...]:
    symbols: list[tuple[int, int, str]] = []
    for line in run_objdump(objdump, "-t", str(elf)).splitlines():
        match = SYMBOL_RE.match(line)
        if match:
            size = int(match.group(2), 16)
            if size:
                symbols.append((int(match.group(1), 16), size, match.group(3)))

    instructions: list[Instruction] = []
    for line in run_objdump(objdump, "-d", str(elf)).splitlines():
        match = OBJDUMP_INST_RE.match(line)
        if match:
            instructions.append(
                Instruction(
                    int(match.group(1), 16), match.group(2), match.group(3) or ""
                )
            )
    instructions.sort(key=lambda row: row.address)

    functions: list[Function] = []
    cursor = 0
    for address, size, name in sorted(symbols):
        while cursor < len(instructions) and instructions[cursor].address < address:
            cursor += 1
        end = address + size
        index = cursor
        body: list[Instruction] = []
        while index < len(instructions) and instructions[index].address < end:
            body.append(instructions[index])
            index += 1
        if body:
            functions.append(Function(name, address, size, tuple(body)))
    return tuple(functions)


def role_pattern(rows: tuple[Instruction, ...] | list[Instruction]) -> tuple[str, ...]:
    roles: dict[str, str] = {}
    gpr_count = 0
    fpr_count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal gpr_count, fpr_count
        register = match.group(1)
        if register not in roles:
            if register.startswith("f") and register[1:].isdigit():
                roles[register] = f"$f{fpr_count}"
                fpr_count += 1
            else:
                roles[register] = f"$g{gpr_count}"
                gpr_count += 1
        return roles[register]

    result: list[str] = []
    for row in rows:
        operands = REGISTER_RE.sub(replace, row.operands)
        operands = re.sub(r"%(?:hi|lo)\([^)]+\)", "SYM", operands)
        operands = NUMBER_RE.sub("IMM", operands)
        operands = re.sub(
            r"\b(?:\.L|jtbl_|D_|g[A-Za-z_]|func_)[A-Za-z0-9_$.]*\b",
            "SYM",
            operands,
        )
        operands = re.sub(r"\s+", "", operands)
        result.append(f"{row.opcode} {operands}".strip())
    return tuple(result)


def source_locations(symbol: str) -> list[str]:
    pattern = re.compile(
        rf"^[A-Za-z_][^;{{}}\n]*\b{re.escape(symbol)}\s*\(", re.MULTILINE
    )
    results: list[str] = []
    for root in (ROOT / "src", ROOT / "libultra" / "src"):
        if not root.exists():
            continue
        for path in root.rglob("*.c"):
            text = path.read_text(errors="replace")
            match = pattern.search(text)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                results.append(f"{path.relative_to(ROOT)}:{line}")
    return results[:3]


def similarity(left: tuple[str, ...], right: tuple[str, ...]) -> float:
    if len(left) != len(right) or not left:
        return 0.0
    return sum(a == b for a, b in zip(left, right)) / len(left)


def candidate_windows(
    instructions: tuple[Instruction, ...], opcodes: tuple[str, ...], max_gap: int
):
    for start, instruction in enumerate(instructions):
        if instruction.opcode != opcodes[0]:
            continue
        indexes = [start]
        cursor = start
        for opcode in opcodes[1:]:
            limit = min(len(instructions), cursor + max_gap + 2)
            match = next(
                (index for index in range(cursor + 1, limit) if instructions[index].opcode == opcode),
                None,
            )
            if match is None:
                break
            indexes.append(match)
            cursor = match
        if len(indexes) == len(opcodes):
            yield tuple(instructions[index] for index in indexes)


def parse_int(value: str) -> int:
    return int(value, 0)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("function", help="Target function name or asm path")
    offsets = parser.add_mutually_exclusive_group()
    offsets.add_argument("--offset", type=parse_int, help="Byte offset of a contiguous target window")
    offsets.add_argument(
        "--offsets",
        help="Comma-separated byte offsets for a selected residual signature",
    )
    parser.add_argument("--window", type=int, default=6, help="Instruction count in the residual window")
    parser.add_argument("--top", type=int, default=20)
    parser.add_argument(
        "--max-gap",
        type=int,
        default=0,
        help="Maximum skipped candidate instructions between signature opcodes",
    )
    parser.add_argument("--elf", type=Path, default=DEFAULT_ELF)
    parser.add_argument("--objdump", type=Path, default=DEFAULT_OBJDUMP)
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--signature-file", type=Path, default=DEFAULT_SIGNATURES)
    parser.add_argument(
        "--include-known",
        action="store_true",
        help="Include references recorded as already audited in the signature file",
    )
    args = parser.parse_args()

    target_path = resolve_target(args.function)
    target_rows = parse_target(target_path)
    signature: dict[str, object] = {}
    if args.offset is None and not args.offsets:
        if not args.signature_file.exists():
            raise SystemExit("error: --offset/--offsets required when no signature file exists")
        signatures = json.loads(args.signature_file.read_text())
        signature = signatures.get(target_path.stem, {})
        if not signature:
            raise SystemExit(f"error: no residual signature recorded for {target_path.stem}")
        args.offsets = ",".join(str(value) for value in signature["offsets"])
        args.max_gap = int(signature.get("max_gap", args.max_gap))
    if args.offsets:
        selected_offsets = [parse_int(value.strip()) for value in args.offsets.split(",")]
        by_offset = {row.address - target_rows[0].address: row for row in target_rows}
        missing = [offset for offset in selected_offsets if offset not in by_offset]
        if missing:
            raise SystemExit(
                "error: offsets are not instruction boundaries: "
                + ", ".join(f"0x{offset:X}" for offset in missing)
            )
        target_window = tuple(by_offset[offset] for offset in selected_offsets)
        args.window = len(target_window)
        display_offset: object = selected_offsets
    else:
        target_address = target_rows[0].address + args.offset
        start = next((i for i, row in enumerate(target_rows) if row.address == target_address), None)
        if start is None:
            raise SystemExit(f"error: offset 0x{args.offset:X} is not an instruction boundary")
        target_window = target_rows[start : start + args.window]
        if len(target_window) != args.window:
            raise SystemExit("error: target window extends beyond the function")
        display_offset = args.offset
    target_pattern = role_pattern(target_window)

    hits: list[dict[str, object]] = []
    target_name = target_path.stem
    target_opcodes = tuple(row.opcode for row in target_window)
    known_references = set(str(value) for value in signature.get("known_references", []))
    for function in parse_elf(args.elf, args.objdump):
        if (
            function.name == target_name
            or (not args.include_known and function.name in known_references)
            or len(function.instructions) < args.window
        ):
            continue
        for window in candidate_windows(function.instructions, target_opcodes, args.max_gap):
            pattern = role_pattern(window)
            score = similarity(target_pattern, pattern)
            hits.append(
                {
                    "score": score,
                    "function": function.name,
                    "function_offset": window[0].address - function.address,
                    "address": window[0].address,
                    "pattern": pattern,
                }
            )
    hits.sort(key=lambda hit: (-float(hit["score"]), str(hit["function"]), int(hit["function_offset"])))
    hits = hits[: args.top]
    for hit in hits:
        hit["source"] = source_locations(str(hit["function"]))

    result = {
        "target": str(target_path.relative_to(ROOT)),
        "offset": display_offset,
        "window": args.window,
        "target_pattern": target_pattern,
        "hard_gates": signature.get("hard_gates", ""),
        "known_references": sorted(known_references),
        "hits": hits,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        if isinstance(display_offset, list):
            offset_text = ",".join(f"0x{offset:X}" for offset in display_offset)
        else:
            offset_text = f"0x{display_offset:X}"
        print(f"target: {result['target']} offsets={offset_text} window={args.window}")
        print("target_pattern:")
        for instruction in target_pattern:
            print(f"  {instruction}")
        if result["hard_gates"]:
            print(f"hard_gates: {result['hard_gates']}")
        if known_references:
            print("known_references: " + ",".join(sorted(known_references)))
        print("score function+offset source")
        for hit in hits:
            sources = ",".join(hit["source"]) or "-"
            print(
                f"{hit['score']:.3f} {hit['function']}+0x{hit['function_offset']:X} {sources}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
