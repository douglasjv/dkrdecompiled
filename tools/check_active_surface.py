#!/usr/bin/env python3
"""Validate the compact DKR /goal startup surface."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "STARTING_PROMPT.md",
    "SESSION_HANDOFF.md",
    "research/tasks/ACTIVE.md",
    "research/tasks/GOAL_LOOP.md",
    ".agents/skills/n64-ido-matching-packet/SKILL.md",
    ".agents/skills/n64-ido-nonmatch-triage/SKILL.md",
]


def validate_frontmatter(path: Path) -> list[str]:
    text = path.read_text(errors="replace")
    if not text.startswith("---\n"):
        return [f"{path.relative_to(ROOT)}: missing YAML frontmatter"]
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        return [f"{path.relative_to(ROOT)}: malformed YAML frontmatter"]
    frontmatter = match.group(1)
    errors = []
    for key in ("name:", "description:"):
        if key not in frontmatter:
            errors.append(f"{path.relative_to(ROOT)}: missing {key}")
    return errors


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    for rel_path in REQUIRED:
        path = ROOT / rel_path
        if not path.exists():
            errors.append(f"missing {rel_path}")

    for path in sorted((ROOT / ".agents" / "skills").glob("*/SKILL.md")):
        errors.extend(validate_frontmatter(path))

    if not any((ROOT / "baseroms").glob("*.z64")):
        warnings.append("no .z64 file found in baseroms/")

    if not (ROOT / "build").exists():
        warnings.append("build/ is absent; run setup/extract/build before exact-match validation")

    for warning in warnings:
        print(f"WARNING: {warning}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("active surface ok")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

