#!/usr/bin/env python3
"""Write a compact DKR session handoff and optionally commit it."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def git_output(*args: str) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), *args], text=True).strip()
    except subprocess.CalledProcessError:
        return "unknown"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--validation", action="append", default=[])
    parser.add_argument("--blocker", action="append", default=[])
    parser.add_argument("--next-task", default="Run tools/query_goal_state.py for the next target")
    parser.add_argument("--packet-status", default="ready")
    parser.add_argument("--reasoning-tier", default="medium")
    parser.add_argument("--commit", action="store_true")
    args = parser.parse_args()

    branch = git_output("branch", "--show-current")
    head = git_output("rev-parse", "--short", "HEAD")
    validations = args.validation or ["not recorded"]
    blockers = args.blocker or ["No open blockers recorded."]

    handoff = ROOT / "SESSION_HANDOFF.md"
    handoff.write_text(
        "\n".join(
            [
                "# Session Handoff",
                "",
                f"- Generated at: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%SZ')}",
                f"- Branch: `{branch}`",
                f"- HEAD: `{head}`",
                f"- Completed task: `{args.task}`",
                f"- Summary: {args.summary}",
                "",
                "## Validation",
                "",
                *[f"- {item}" for item in validations],
                "",
                "## Blockers Or Unknowns",
                "",
                *[f"- {item}" for item in blockers],
                "",
                "## Ask The User Only If",
                "",
                "- The retail baserom or extracted assets are missing.",
                "- A required setup dependency cannot be installed or initialized.",
                "- A behavior question cannot be resolved from code, symbols, or focused diff evidence.",
                "",
                "## Next Work Packet",
                "",
                f"- Task: `{args.next_task}`",
                "- Packet class: `matching_impl`",
                f"- Packet status: `{args.packet_status}`",
                f"- Reasoning tier: `{args.reasoning_tier}`",
                "- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.",
                "",
            ]
        )
    )

    if args.commit:
        subprocess.check_call(["git", "-C", str(ROOT), "add", "AGENTS.md", "STARTING_PROMPT.md", "SESSION_HANDOFF.md", "research/tasks", ".agents", "tools/query_goal_state.py", "tools/check_active_surface.py", "tools/session_closeout.py"])
        subprocess.check_call(["git", "-C", str(ROOT), "commit", "-m", f"{args.task}: update DKR matching handoff"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
