#!/usr/bin/env python3
"""Generate repo-local mips_to_c snapshots without editing live source."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def resolve_asm(function: str) -> Path:
    name = function[:-2] if function.endswith(".s") else function
    matches = sorted((ROOT / "asm").glob(f"**/{name}.s"))
    if not matches:
        raise SystemExit(f"error: no asm found for {function!r}")
    if len(matches) > 1:
        rels = "\n  ".join(str(path.relative_to(ROOT)) for path in matches)
        raise SystemExit(f"error: multiple asm files match {function!r}:\n  {rels}")
    return matches[0]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run tools/m2c for one or more functions into research/task output."
    )
    parser.add_argument("functions", nargs="+", help="Function names to translate")
    parser.add_argument(
        "--output-dir",
        default="research/tasks/m2c_one_shot",
        help="Directory for generated C snapshots",
    )
    parser.add_argument(
        "--context",
        default="ctx.c",
        help="Context file to pass to m2c (default: ctx.c)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=120,
        help="Per-function timeout in seconds",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    context = ROOT / args.context
    if not context.exists():
        raise SystemExit(
            f"error: context file missing: {args.context}\n"
            "Run ./generate_ctx.sh first if this checkout needs a fresh context."
        )

    out_dir = ROOT / args.output_dir
    out_dir.mkdir(parents=True, exist_ok=True)
    python = ROOT / ".venv" / "bin" / "python3"
    if not python.exists():
        python = Path(sys.executable)
    m2c = ROOT / "tools" / "m2c" / "m2c.py"
    if not m2c.exists():
        raise SystemExit("error: tools/m2c/m2c.py is missing; update submodules first")

    status = 0
    for function in args.functions:
        asm_path = resolve_asm(function)
        out_path = out_dir / f"{asm_path.stem}.c"
        cmd = [
            str(python),
            str(m2c),
            "--target",
            "mips-ido-c",
            "--pointer-style",
            "right",
            "--context",
            str(context),
            "-f",
            asm_path.stem,
            str(asm_path),
        ]
        print(f"m2c {asm_path.stem} -> {out_path.relative_to(ROOT)}")
        try:
            result = subprocess.run(
                cmd,
                cwd=ROOT,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=args.timeout,
                check=False,
            )
        except subprocess.TimeoutExpired:
            print(f"error: timed out after {args.timeout}s: {asm_path.stem}")
            status = 124
            continue

        include_path = os.path.relpath(context, start=out_path.parent)
        out_path.write_text(f'#include "{include_path}"\n{result.stdout}', encoding="utf-8")
        if result.stderr:
            (out_path.with_suffix(".stderr.txt")).write_text(result.stderr, encoding="utf-8")
        if result.returncode != 0:
            print(f"warning: m2c exited {result.returncode} for {asm_path.stem}")
            status = result.returncode
    return status


if __name__ == "__main__":
    raise SystemExit(main())
