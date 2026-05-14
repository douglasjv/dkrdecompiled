---
name: n64-ido-matching-packet
description: Use when landing one bounded N64 IDO byte-matching C function or source family in a decompilation repo with GLOBAL_ASM, NON_MATCHING, asm-differ, and a matching ROM verification gate.
---

# N64 IDO Matching Packet

Use this for one source-level matching packet, not for broad reverse
engineering or mod builds.

## Operating Rules

- Matching progress means ordinary C that keeps the matching ROM byte-identical.
- Do not use inline asm, raw instruction words, handwritten assembly wrappers,
  or post-link patching.
- Keep the target narrow: one `GLOBAL_ASM`, one guarded `NON_MATCHING` /
  `NON_EQUIVALENT` function, or a very small coupled family.
- Prefer repo-local typedefs, macros, include order, and formatting.
- Treat `NON_MATCHING=1` as a sandbox only. The acceptance gate is the normal
  matching build.

## DKR Flow

1. Run `python3 tools/query_goal_state.py next --compact --refresh`.
2. Inspect the selected source file and original asm path.
3. Write the smallest plausible C replacement.
4. Run `./diff.sh <function>` for focused diagnosis.
5. Run `gmake -j4 CROSS=tools/binutils/mips64-elf-`; accept only if it reaches
   `Verify: OK`.
6. Update `SESSION_HANDOFF.md` with validation, result, next packet, and any
   rejected source-shape families.

## Common IDO Levers

- signedness and exact integer width
- pointer depth and field offset spelling
- early-return polarity
- temporary lifetime and declaration order
- `volatile` only for real MMIO or ordering-sensitive globals
- expression grouping for multiply/add/shift sequences
- switch case ordering and fallthrough shape

If two bounded probes do not improve the focused diff, park the packet with the
best evidence and select another target instead of widening indefinitely.
