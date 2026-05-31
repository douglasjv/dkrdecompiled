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
MECHANISM_PACKETS_PATH = ROOT / "research" / "tasks" / "MECHANISM_PACKETS.md"
TASKS_ROOT = ROOT / "research" / "tasks"
PRAGMA_RE = re.compile(r'#pragma\s+GLOBAL_ASM\("([^"]+)"\)')
GUARD_RE = re.compile(r"^\s*#ifdef\s+(NON_MATCHING|NON_EQUIVALENT)\b")
EVIDENCE_FUNC_RE = re.compile(r"`([A-Za-z_][A-Za-z0-9_]*)`")
COOLDOWN_RE = re.compile(r"\b(cooling down|saturated|pivot/discovery|pivot to another)\b", re.IGNORECASE)
NEXT_USEFUL_RE = re.compile(r"^\s*-?\s*Next useful work\b.*", re.MULTILINE)
AUDIT_NOTE_RE = re.compile(
    r"\b(promoted[- ]object[- ]slice(?: audit)?|focused[- ](?:object[- ])?false positive|stale `?CURRENT \(0\)`?|Do not trust focused `?CURRENT \(0\)`?)",
    re.IGNORECASE,
)
DISCOVERY_FIRST_RE = re.compile(
    r"\b(discovery/tooling|pivot/discovery|tooling)\b|^\s*-?\s*Next useful work\s+should\s+pivot\b",
    re.IGNORECASE,
)
RECENT_REVIVAL_RE = re.compile(r"\b2026-05-31\b.*\b(?:revival worker|worker)\b", re.IGNORECASE)
REQUIRED_PACKET_FIELDS = [
    "target",
    "evidence_checked",
    "rejected_families",
    "mechanism_hypothesis",
    "predicted_asm_movement",
    "stop_condition",
    "reasoning_tier",
]
PACKET_HEADING_RE = re.compile(r"^###\s+`?([A-Za-z_][A-Za-z0-9_]*)`?\s*$")
PACKET_FIELD_RE = re.compile(
    r"^-\s+(Target|Evidence checked|Rejected families|Mechanism hypothesis|Predicted asm movement|Stop condition|Reasoning tier):\s*(.*)$",
    re.IGNORECASE,
)


def discovery_kind(note: str, has_next_useful: bool) -> str:
    if not has_next_useful:
        return "fallback_note"
    if DISCOVERY_FIRST_RE.search(note):
        return "tooling_first"
    return "mechanism_hypothesis"


def discovery_readiness_gap(kind: str) -> str:
    if kind == "mechanism_hypothesis":
        return ""
    if kind == "tooling_first":
        return "sidecar asks for discovery/tooling before another source probe"
    return "sidecar does not expose a Next useful work mechanism packet"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def function_from_asm(asm_path: str) -> str:
    return Path(asm_path).stem


def exhausted_probe_details() -> dict[str, str]:
    if not EVIDENCE_PATH.exists():
        return {}
    notes: dict[str, str] = {}
    current_function: str | None = None
    current_lines: list[str] = []
    for line in EVIDENCE_PATH.read_text(errors="replace").splitlines():
        stripped = line.strip()
        if line.startswith("-"):
            if current_function and current_lines:
                notes[current_function] = " ".join(" ".join(current_lines).split())
            current_lines = [stripped.removeprefix("-").strip()]
            match = EVIDENCE_FUNC_RE.search(stripped)
            current_function = match.group(1) if match else None
            continue
        if current_function and stripped:
            current_lines.append(stripped)
    if current_function and current_lines:
        notes[current_function] = " ".join(" ".join(current_lines).split())
    return notes


def exhausted_probe_notes() -> set[str]:
    return set(exhausted_probe_details())


def has_recent_revival_cooldown(note: str) -> bool:
    return bool(RECENT_REVIVAL_RE.search(note))


def latest_audit_note_from_text(text: str) -> str:
    lines = text.splitlines()
    if len(lines) <= 1 and len(text) > 1000:
        matches = list(AUDIT_NOTE_RE.finditer(text))
        if matches:
            match = matches[-1]
            start = max(text.rfind(" A ", 0, match.start()), text.rfind(" - ", 0, match.start()))
            start = match.start() if start == -1 else start + 1
            end = text.find(" Do not trust focused `CURRENT (0)`", match.end())
            if end == -1:
                end = text.find(" Do not treat promoted-object `CURRENT (0)`", match.end())
            if end != -1:
                end = text.find(".", end)
            end = len(text) if end == -1 else end + 1
            return " ".join(text[start:end].split())
    match_indexes = [
        index for index, line in enumerate(lines) if AUDIT_NOTE_RE.search(line)
    ]
    for index in reversed(match_indexes):
        start = index
        if lines[start].lstrip().startswith("##"):
            start += 1
            while start < len(lines) and not lines[start].strip():
                start += 1
        collected: list[str] = []
        for line in lines[start : start + 10]:
            stripped = line.strip()
            if not stripped:
                if collected:
                    break
                continue
            if collected and stripped.startswith(("#", "- ")) and not lines[start].strip().startswith(("#", "- ")):
                break
            collected.append(stripped)
            if "Do not trust focused `CURRENT (0)`" in stripped or "Do not treat promoted-object `CURRENT (0)`" in stripped:
                break
        if collected:
            return " ".join(" ".join(collected).split())
    return ""


def latest_audit_note(path: str) -> str:
    full_path = ROOT / path
    if not full_path.exists():
        return ""
    return latest_audit_note_from_text(full_path.read_text(errors="replace"))


def compact_note(note: object, limit: int = 520) -> str:
    text = " ".join(str(note).split())
    if len(text) > limit:
        return f"{text[:limit - 3]}..."
    return text


def cooldown_notes() -> dict[str, str]:
    notes: dict[str, str] = {}
    for path in sorted(TASKS_ROOT.glob("*_evidence.md")):
        function = path.name.removesuffix("_evidence.md")
        text = path.read_text(errors="replace")
        match = COOLDOWN_RE.search(text)
        if match:
            notes[function] = rel(path)
    return notes


def mechanism_packets() -> dict[str, dict[str, object]]:
    if not MECHANISM_PACKETS_PATH.exists():
        return {}
    packets: dict[str, dict[str, object]] = {}
    current_function: str | None = None
    for line in MECHANISM_PACKETS_PATH.read_text(errors="replace").splitlines():
        heading_match = PACKET_HEADING_RE.match(line.strip())
        if heading_match:
            current_function = heading_match.group(1)
            packets[current_function] = {
                "function": current_function,
                "packet_path": rel(MECHANISM_PACKETS_PATH),
                "packet_fields": {},
            }
            continue
        if not current_function:
            continue
        field_match = PACKET_FIELD_RE.match(line.strip())
        if not field_match:
            continue
        key = field_match.group(1).lower().replace(" ", "_")
        value = field_match.group(2).strip()
        packets[current_function]["packet_fields"][key] = value
    return packets


def packet_missing_fields(packet: dict[str, object]) -> list[str]:
    fields = packet.get("packet_fields", {})
    if not isinstance(fields, dict):
        return REQUIRED_PACKET_FIELDS
    missing: list[str] = []
    for field in REQUIRED_PACKET_FIELDS:
        if not str(fields.get(field, "")).strip():
            missing.append(field)
    return missing


def discovery_note(path: str) -> tuple[str, bool]:
    text = (ROOT / path).read_text(errors="replace")
    match = NEXT_USEFUL_RE.search(text)
    if match:
        return " ".join(match.group(0).lstrip(" -").split()), True
    for line in reversed(text.splitlines()):
        stripped = line.strip()
        if stripped:
            return stripped, False
    return "No sidecar guidance recorded.", False


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
    exhausted_details = exhausted_probe_details()
    exhausted = set(exhausted_details)
    cooldown = cooldown_notes()
    for item in all_candidates:
        function = str(item["function"])
        if function in cooldown:
            item["priority"] = int(item["priority"]) + 100
            item["cooldown_evidence"] = cooldown[function]
        if function in exhausted_details and has_recent_revival_cooldown(exhausted_details[function]):
            item["priority"] = int(item["priority"]) + 100
            item["revival_cooldown"] = True
    all_candidates.sort(key=lambda item: (item["priority"], item["source"], item["line"]))
    candidates = [
        item for item in all_candidates if include_exhausted or item["function"] not in exhausted
    ]
    baseroms = sorted(path.name for path in (ROOT / "baseroms").glob("*.z64"))
    maps = sorted(path.name for path in (ROOT / "build").glob("*.map")) if (ROOT / "build").exists() else []
    recommended = next(
        (
            item
            for item in candidates
            if "cooldown_evidence" not in item and "revival_cooldown" not in item
        ),
        None,
    )
    discovery_route = recommended is None and bool(candidates)
    return {
        "repo": str(ROOT),
        "baseroms": baseroms,
        "build_maps": maps,
        "counts": {
            "candidates": len(candidates),
            "exhausted_notes": sum(1 for item in all_candidates if item["function"] in exhausted),
            "cooldown_notes": sum(1 for item in all_candidates if item["function"] in cooldown),
            "revival_cooldown_notes": sum(1 for item in all_candidates if item.get("revival_cooldown")),
            "skipped_exhausted": 0 if include_exhausted else sum(1 for item in all_candidates if item["function"] in exhausted),
            "source_global_asm": sum(1 for item in candidates if item["kind"] == "GLOBAL_ASM"),
            "non_matching_or_equivalent": sum(1 for item in candidates if item["kind"] != "GLOBAL_ASM"),
        },
        "recommended_next": recommended,
        "discovery_route": discovery_route,
        "exhausted_probe_notes": sorted(exhausted),
        "cooldown_probe_notes": dict(sorted(cooldown.items())),
        "include_exhausted": include_exhausted,
        "candidates": candidates[:25],
    }


def discovery_candidates(state: dict[str, object]) -> list[dict[str, object]]:
    items: list[dict[str, object]] = []
    packets = mechanism_packets()
    for candidate in state["candidates"]:
        evidence = candidate.get("cooldown_evidence")
        if not evidence:
            continue
        packet = packets.get(str(candidate["function"]))
        note, has_next_useful = discovery_note(str(evidence))
        audit_note = latest_audit_note(str(evidence))
        if packet and not packet_missing_fields(packet):
            kind = "mechanism_hypothesis"
            readiness_gap = ""
            ready_for_probe = True
            required_packet_fields: list[str] = []
        else:
            kind = discovery_kind(note, has_next_useful)
            readiness_gap = discovery_readiness_gap(kind)
            ready_for_probe = False
            required_packet_fields = REQUIRED_PACKET_FIELDS
        items.append(
            {
                "function": candidate["function"],
                "source": candidate["source"],
                "line": candidate["line"],
                "asm": candidate["asm"],
                "evidence": evidence,
                "next_useful": note,
                "latest_audit": audit_note,
                "has_next_useful": has_next_useful,
                "discovery_kind": kind,
                "ready_for_probe": ready_for_probe,
                "readiness_gap": readiness_gap,
                "required_packet_fields": required_packet_fields,
                "mechanism_packet": packet,
            }
        )
    kind_rank = {
        "mechanism_hypothesis": 0,
        "tooling_first": 1,
        "fallback_note": 2,
    }
    items.sort(key=lambda item: (kind_rank[str(item["discovery_kind"])], item["function"]))
    return items


def revival_candidates(state: dict[str, object]) -> list[dict[str, object]]:
    exhausted_details = exhausted_probe_details()
    packets = mechanism_packets()
    items: list[dict[str, object]] = []
    for candidate in state["candidates"]:
        function = str(candidate["function"])
        if function not in exhausted_details:
            continue
        item = dict(candidate)
        item["parked_note"] = exhausted_details[function]
        item["latest_audit"] = latest_audit_note_from_text(exhausted_details[function])
        packet = packets.get(function)
        if packet and not packet_missing_fields(packet):
            item["mechanism_packet"] = packet
            item["ready_for_probe"] = True
            item["readiness_gap"] = ""
            item["required_packet_fields"] = []
        else:
            item["mechanism_packet"] = packet
            item["ready_for_probe"] = not item.get("revival_cooldown", False)
            item["readiness_gap"] = (
                "parked candidate has recent revival cooldown evidence"
                if item.get("revival_cooldown")
                else ""
            )
            item["required_packet_fields"] = (
                []
                if not item.get("revival_cooldown")
                else packet_missing_fields(packet) if packet else REQUIRED_PACKET_FIELDS
            )
        items.append(item)
    items.sort(
        key=lambda item: (
            0 if item.get("ready_for_probe") else 1,
            int(item["priority"]),
            str(item["source"]),
            int(item["line"]),
        )
    )
    return items


def packet_context(state: dict[str, object], function: str) -> dict[str, object] | None:
    packets = mechanism_packets()
    discovery_by_function = {
        str(item["function"]): item for item in discovery_candidates(state)
    }
    revival_by_function = {
        str(item["function"]): item for item in revival_candidates(state)
    }
    for candidate in state["candidates"]:
        if candidate["function"] != function:
            continue
        context: dict[str, object] = {
            "target": candidate["function"],
            "source": candidate["source"],
            "line": candidate["line"],
            "asm": candidate["asm"],
            "kind": candidate["kind"],
            "packet_fields": {field: "" for field in REQUIRED_PACKET_FIELDS},
        }
        if function in discovery_by_function:
            discovery = discovery_by_function[function]
            context.update(
                {
                    "evidence_checked": discovery["evidence"],
                    "next_useful": discovery["next_useful"],
                    "latest_audit": discovery["latest_audit"],
                    "ready_for_probe": discovery["ready_for_probe"],
                    "readiness_gap": discovery["readiness_gap"],
                    "required_packet_fields": discovery["required_packet_fields"],
                }
            )
            packet = packets.get(function)
            if packet:
                context["mechanism_packet"] = packet
                context["ready_for_probe"] = not packet_missing_fields(packet)
                context["readiness_gap"] = ""
                context["required_packet_fields"] = packet_missing_fields(packet)
        elif function in revival_by_function:
            revival = revival_by_function[function]
            context.update(
                {
                    "evidence_checked": rel(EVIDENCE_PATH),
                    "parked_note": revival["parked_note"],
                    "latest_audit": revival["latest_audit"],
                    "ready_for_probe": revival["ready_for_probe"],
                    "readiness_gap": revival["readiness_gap"],
                    "required_packet_fields": revival["required_packet_fields"],
                }
            )
            packet = packets.get(function)
            if packet:
                context["mechanism_packet"] = packet
        else:
            context.update(
                {
                    "evidence_checked": "",
                    "ready_for_probe": "cooldown_evidence" not in candidate
                    and "revival_cooldown" not in candidate,
                    "readiness_gap": "",
                    "required_packet_fields": [],
                }
            )
        return context
    return None


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
        f"cooldown_notes={counts['cooldown_notes']} "
        f"skipped_exhausted={counts['skipped_exhausted']}"
    )
    recommended = state["recommended_next"]
    if not recommended:
        if state.get("discovery_route"):
            print("recommended_next: discovery")
            print("recommended_note: all default-routable candidates have cooldown evidence; name a distinct compiler-mechanism hypothesis before probing one")
            return
        print("recommended_next: none")
        return
    print(
        "recommended_next: "
        f"{recommended['function']} "
        f"kind={recommended['kind']} "
        f"source={recommended['source']}:{recommended['line']} "
        f"asm={recommended['asm']}"
    )
    if "cooldown_evidence" in recommended:
        print(f"recommended_note: cooldown_evidence={recommended['cooldown_evidence']}")


def print_discovery(state: dict[str, object]) -> None:
    print(f"repo: {state['repo']}")
    items = discovery_candidates(state)
    if not items:
        print("discovery_next: none")
        return
    if items[0]["discovery_kind"] != "mechanism_hypothesis":
        print("discovery_next: tooling")
        print("discovery_note: no cooldown sidecar currently names a mechanism-ready packet; improve discovery/tooling or write a distinct compiler-mechanism packet before probing")
        for item in items:
            print(
                "cooldown_candidate: "
                f"{item['function']} "
                f"evidence={item['evidence']} "
                f"kind={item['discovery_kind']} "
                f"gap={item['readiness_gap']}"
            )
            if item.get("latest_audit"):
                print(f"latest_audit: {compact_note(item['latest_audit'], 360)}")
        return
    print(f"discovery_next: {items[0]['function']} evidence={items[0]['evidence']} kind={items[0]['discovery_kind']}")
    if items[0].get("mechanism_packet"):
        print(f"discovery_packet: {items[0]['mechanism_packet']['packet_path']}")
    print(f"discovery_note: {items[0]['next_useful']}")
    if items[0].get("latest_audit"):
        print(f"latest_audit: {compact_note(items[0]['latest_audit'], 360)}")
    for item in items[1:]:
        print(f"cooldown_candidate: {item['function']} evidence={item['evidence']} kind={item['discovery_kind']}")


def print_revival(state: dict[str, object]) -> None:
    print(f"repo: {state['repo']}")
    items = revival_candidates(state)
    if not items:
        print("revival_next: none")
        return
    if not items[0].get("ready_for_probe"):
        print("revival_next: tooling")
        print("revival_note: all parked candidates have recent revival cooldown evidence; improve revival ranking or name a distinct compiler-mechanism packet before probing")
        for item in items:
            cooldown = " cooldown=recent" if item.get("revival_cooldown") else ""
            print(
                "parked_candidate: "
                f"{item['function']} "
                f"kind={item['kind']} "
                f"source={item['source']}:{item['line']} "
                f"asm={item['asm']}"
                f"{cooldown}"
            )
            if item.get("latest_audit"):
                print(f"latest_audit: {compact_note(item['latest_audit'], 360)}")
        return
    first = items[0]
    print(
        "revival_next: "
        f"{first['function']} "
        f"kind={first['kind']} "
        f"source={first['source']}:{first['line']} "
        f"asm={first['asm']}"
    )
    if first.get("mechanism_packet"):
        print(f"revival_packet: {first['mechanism_packet']['packet_path']}")
    note = str(first["parked_note"])
    print(f"revival_note: {compact_note(note, 420)}")
    if first.get("latest_audit"):
        print(f"latest_audit: {compact_note(first['latest_audit'], 360)}")
    for item in items[1:]:
        print(
            "parked_candidate: "
            f"{item['function']} "
            f"kind={item['kind']} "
            f"source={item['source']}:{item['line']} "
            f"asm={item['asm']}"
        )


def print_tooling(state: dict[str, object]) -> None:
    print(f"repo: {state['repo']}")
    discovery_items = discovery_candidates(state)
    revival_items = revival_candidates(state)
    ready = [item for item in discovery_items if item.get("ready_for_probe")]
    ready_parked = [item for item in revival_items if item.get("ready_for_probe")]
    if ready:
        first = ready[0]
        print(
            "tooling_next: "
            f"probe_ready function={first['function']} "
            f"evidence={first['evidence']}"
        )
        if first.get("mechanism_packet"):
            print(f"mechanism_packet: {first['mechanism_packet']['packet_path']}")
        return
    if ready_parked:
        first = ready_parked[0]
        print(
            "tooling_next: "
            f"probe_ready function={first['function']} "
            f"evidence={rel(EVIDENCE_PATH)}"
        )
        if first.get("mechanism_packet"):
            print(f"mechanism_packet: {first['mechanism_packet']['packet_path']}")
        return
    print("tooling_next: discovery_packet")
    print(
        "tooling_note: no live or parked candidate is probe-ready; write a "
        "complete mechanism packet before source edits"
    )
    for item in discovery_items:
        print(
            "blocked_candidate: "
            f"{item['function']} "
            f"evidence={item['evidence']} "
            f"gap={item['readiness_gap']} "
            f"required={','.join(str(field) for field in item['required_packet_fields'])}"
        )
        print(f"next_useful: {item['next_useful']}")
        if item.get("latest_audit"):
            print(f"latest_audit: {compact_note(item['latest_audit'], 360)}")
    for item in revival_items:
        if item.get("ready_for_probe") or not item.get("revival_cooldown"):
            continue
        print(
            "blocked_parked_candidate: "
            f"{item['function']} "
            f"evidence={rel(EVIDENCE_PATH)} "
            "gap=parked candidate has recent revival cooldown evidence "
            f"required={','.join(str(field) for field in item['required_packet_fields'])}"
        )
        if item.get("latest_audit"):
            print(f"latest_audit: {compact_note(item['latest_audit'], 360)}")


def print_packet(context: dict[str, object]) -> None:
    print(f"target: {context['target']}")
    print(
        "location: "
        f"{context['kind']} "
        f"{context['source']}:{context['line']} "
        f"asm={context['asm']}"
    )
    print(f"evidence_checked: {context.get('evidence_checked') or 'missing'}")
    print(f"ready_for_probe: {str(context['ready_for_probe']).lower()}")
    if context.get("readiness_gap"):
        print(f"readiness_gap: {context['readiness_gap']}")
    if context.get("next_useful"):
        print(f"next_useful: {context['next_useful']}")
    if context.get("parked_note"):
        print(f"parked_note: {compact_note(context['parked_note'])}")
    if context.get("latest_audit"):
        print(f"latest_audit: {compact_note(context['latest_audit'])}")
    if context.get("required_packet_fields"):
        print("required_packet_fields: " + ", ".join(str(field) for field in context["required_packet_fields"]))
    packet = context.get("mechanism_packet")
    if isinstance(packet, dict):
        print(f"mechanism_packet: {packet['packet_path']}")
        fields = packet.get("packet_fields", {})
        if isinstance(fields, dict):
            for field in REQUIRED_PACKET_FIELDS:
                print(f"{field}: {fields.get(field, '')}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("command", nargs="?", default="next", choices=["next", "list", "discovery", "revival", "tooling", "packet"])
    parser.add_argument("--compact", action="store_true")
    parser.add_argument("--refresh", action="store_true", help="accepted for /goal parity; source scan is always fresh")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--include-exhausted", action="store_true", help="include functions with recorded exhausted probe notes")
    parser.add_argument("--function", help="function name for packet context")
    args = parser.parse_args()

    state = build_state(include_exhausted=args.include_exhausted or args.command in {"revival", "tooling", "packet"})
    if args.command == "packet":
        if not args.function:
            parser.error("packet requires --function")
        context = packet_context(state, args.function)
        if context is None:
            print(f"packet_error: unknown function {args.function}")
            return 1
        if args.json:
            print(json.dumps(context, indent=2))
        else:
            print_packet(context)
        return 0
    if args.command == "revival" and not args.json:
        print_revival(state)
        return 0
    if args.command == "revival":
        state["revival_candidates"] = revival_candidates(state)
    if args.command == "tooling" and not args.json:
        print_tooling(state)
        return 0
    if args.command == "tooling":
        state["discovery_candidates"] = discovery_candidates(state)
        state["revival_candidates"] = revival_candidates(state)
    if args.command == "discovery" and not args.json:
        print_discovery(state)
        return 0
    if args.command == "discovery":
        state["discovery_candidates"] = discovery_candidates(state)
    if args.json or not args.compact:
        print(json.dumps(state, indent=2))
    else:
        print_compact(state)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
