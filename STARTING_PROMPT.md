# DKR `/goal` Startup Prompt

Use this as the initial `/goal` prompt for the Diddy Kong Racing N64 decomp.

```text
Keep producing source-level, byte-matching C for Diddy Kong Racing in
/Users/douglas/projects/dkrdecompiled.

Startup:
- Read AGENTS.md and research/tasks/ACTIVE.md.
- Run python3 tools/query_goal_state.py next --compact --refresh.
- If routing is unclear, read only SESSION_HANDOFF.md sections:
  Next Work Packet, Validation, Blockers Or Unknowns, Ask The User Only If.
- Run python3 tools/check_active_surface.py before source edits.

Work loop:
- Choose one bounded GLOBAL_ASM/NON_MATCHING/NON_EQUIVALENT target or one very
  small coherent source family.
- Replace assembly stand-ins with ordinary C only. No inline asm, raw
  instruction words, handwritten assembly wrappers, or post-link patches.
- Use ./diff.sh <function> for focused diagnosis.
- Accept a packet only when
  gmake -j4 CROSS=tools/binutils/mips64-elf-
  still reaches Verify: OK in matching mode.
- Update ACTIVE.md and SESSION_HANDOFF.md with the result, validation, blockers,
  and next packet. Continue to the next ready target unless blocked by missing
  retail asset/setup, missing toolchain dependency, or unresolved behavior
  ambiguity.

Default reasoning: medium. Escalate only for a recorded exact-match ambiguity
with a narrow question and evidence path.
```
