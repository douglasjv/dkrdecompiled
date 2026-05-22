# Session Handoff

- Generated at: 2026-05-22 15:59:16Z
- Branch: `master`
- HEAD: `966311d3`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected exact first-ring target store-order probe; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted trackbg_render_flashy exact first-ring target store-order probe with calculated CRCs 0x8E7C21EA/0x33457650; ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 -U 90 => relinked CURRENT (4432), frame shrank to 0x150 and early position-array schedule shifted into a different f16/f18 stack-slot family; restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For trackbg_render_flashy, do not repeat the exact first-ring target store-order probe; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
