#!/usr/bin/env python3
"""Compare byte ranges between the baserom and built ROM."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_int(text: str) -> int:
    return int(text, 0)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Diff a ROM byte range between baseroms/baserom.us.v77.z64 and build/dkr.us.v77.z64."
    )
    parser.add_argument("--rom-offset", required=True, type=parse_int, help="Start ROM offset")
    parser.add_argument("--size", required=True, type=parse_int, help="Range size in bytes")
    parser.add_argument(
        "--base-rom",
        default="baseroms/baserom.us.v77.z64",
        help="Reference ROM path",
    )
    parser.add_argument(
        "--built-rom",
        default="build/dkr.us.v77.z64",
        help="Built ROM path",
    )
    parser.add_argument("--limit", type=int, default=64, help="Maximum mismatch rows to print")
    parser.add_argument("--show-all", action="store_true", help="Print all mismatches")
    return parser.parse_args()


def read_range(path: Path, offset: int, size: int) -> bytes:
    with path.open("rb") as rom:
        rom.seek(offset)
        data = rom.read(size)
    if len(data) != size:
        raise SystemExit(f"error: short read from {path}: wanted {size}, got {len(data)}")
    return data


def main() -> int:
    args = parse_args()
    base_path = ROOT / args.base_rom
    built_path = ROOT / args.built_rom
    if not base_path.exists():
        raise SystemExit(f"error: base ROM missing: {args.base_rom}")
    if not built_path.exists():
        raise SystemExit(f"error: built ROM missing: {args.built_rom}")

    base = read_range(base_path, args.rom_offset, args.size)
    built = read_range(built_path, args.rom_offset, args.size)
    mismatches = [
        (args.rom_offset + index, expected, actual)
        for index, (expected, actual) in enumerate(zip(base, built, strict=True))
        if expected != actual
    ]

    print(
        f"range 0x{args.rom_offset:X}..0x{args.rom_offset + args.size:X}: "
        f"{len(mismatches)} mismatches / {args.size} bytes"
    )
    rows = mismatches if args.show_all else mismatches[: args.limit]
    for offset, expected, actual in rows:
        print(f"0x{offset:08X}: base=0x{expected:02X} built=0x{actual:02X}")
    if not args.show_all and len(mismatches) > args.limit:
        print(f"... {len(mismatches) - args.limit} more mismatches")
    return 1 if mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
