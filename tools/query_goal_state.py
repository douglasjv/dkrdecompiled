#!/usr/bin/env python3
"""Compact routing helper for DKR matching sessions."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_ROOTS = [ROOT / "src", ROOT / "libultra" / "src"]
EVIDENCE_PATH = ROOT / "research" / "tasks" / "PARKED.md"
PRAGMA_RE = re.compile(r'#pragma\s+GLOBAL_ASM\("([^"]+)"\)')
GUARD_RE = re.compile(r"^\s*#ifdef\s+(NON_MATCHING|NON_EQUIVALENT)\b")
EVIDENCE_FUNC_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*)`")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def function_from_asm(asm_path: str) -> str:
    return Path(asm_path).stem


def exhausted_probe_notes() -> set[str]:
    if not EVIDENCE_PATH.exists():
        return set()
    noted: set[str] = set()
    for line in EVIDENCE_PATH.read_text(errors="replace").splitlines():
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        match = EVIDENCE_FUNC_RE.search(stripped)
        if match:
            noted.add(match.group(1))
    return noted


def scan_sources() -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for source_root in SOURCE_ROOTS:
        if not source_root.exists():
            continue
        for path in sorted(source_root.rglob("*.c")):
            text = path.read_text(errors="replace").splitlines()
            active_guard: tuple[str, int] | None = None
            for index, line in enumerate(text, start=1):
                guard_match = GUARD_RE.match(line)
                if guard_match:
                    active_guard = (guard_match.group(1), index)
                pragma_match = PRAGMA_RE.search(line)
                if not pragma_match:
                    continue
                asm_path = pragma_match.group(1)
                function = function_from_asm(asm_path)
                guard = active_guard[0] if active_guard else "GLOBAL_ASM"
                priority = 0
                if rel(path).startswith("src/hasm/"):
                    priority += 50
                if rel(path).startswith("libultra/"):
                    priority += 20
                if "asm/nonmatchings/" in asm_path:
                    priority -= 10
                candidates.append(
                    {
                        "function": function,
                        "source": rel(path),
                        "line": index,
                        "asm": asm_path,
                        "kind": guard,
                        "priority": priority,
                    }
                )
    candidates.sort(key=lambda item: (item["priority"], item["source"], item["line"]))
    return candidates


def build_state(include_exhausted: bool = False) -> dict[str, object]:
    all_candidates = scan_sources()
    exhausted = exhausted_probe_notes()
    candidates = [
        item for item in all_candidates if include_exhausted or item["function"] not in exhausted
    ]
    baseroms = sorted(path.name for path in (ROOT / "baseroms").glob("*.z64"))
    maps = sorted(path.name for path in (ROOT / "build").glob("*.map")) if (ROOT / "build").exists() else []
    recommended = candidates[0] if candidates else None
    return {
        "repo": str(ROOT),
        "baseroms": baseroms,
        "build_maps": maps,
        "counts": {
            "candidates": len(candidates),
            "exhausted_notes": sum(1 for item in all_candidates if item["function"] in exhausted),
            "skipped_exhausted": 0 if include_exhausted else sum(1 for item in all_candidates if item["function"] in exhausted),
            "source_global_asm": sum(1 for item in candidates if item["kind"] == "GLOBAL_ASM"),
            "non_matching_or_equivalent": sum(1 for item in candidates if item["kind"] != "GLOBAL_ASM"),
        },
        "recommended_next": recommended,
        "exhausted_probe_notes": sorted(exhausted),
        "include_exhausted": include_exhausted,
        "candidates": candidates[:25],
    }


def print_compact(state: dict[str, object]) -> None:
    print(f"repo: {state['repo']}")
    print(f"baseroms: {', '.join(state['baseroms']) if state['baseroms'] else 'missing'}")
    print(f"build_maps: {', '.join(state['build_maps']) if state['build_maps'] else 'none'}")
    counts = state["counts"]
    print(
        "counts: "
        f"candidates={counts['candidates']} "
        f"global_asm={counts['source_global_asm']} "
        f"guarded={counts['non_matching_or_equivalent']} "
        f"exhausted_notes={counts['exhausted_notes']} "
        f"skipped_exhausted={counts['skipped_exhausted']}"
    )
    recommended = state["recommended_next"]
    if not recommended:
        print("recommended_next: none")
        return
    print(
        "recommended_next: "
        f"{recommended['function']} "
        f"kind={recommended['kind']} "
        f"source={recommended['source']}:{recommended['line']} "
        f"asm={recommended['asm']}"
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="next", choices=["next", "list"])
    parser.add_argument("--compact", action="store_true")
    parser.add_argument("--refresh", action="store_true", help="accepted for /goal parity; source scan is always fresh")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--include-exhausted", action="store_true", help="include functions with recorded exhausted probe notes")
    args = parser.parse_args()

    state = build_state(include_exhausted=args.include_exhausted)
    if args.json or not args.compact:
        print(json.dumps(state, indent=2))
    else:
        print_compact(state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
