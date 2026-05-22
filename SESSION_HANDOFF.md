# Session Handoff

- Generated at: 2026-05-22 15:49:34Z
- Branch: `master`
- HEAD: `238eed61`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected single-site x1 scaled-sine rewrite; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted trackbg_render_flashy xPositions[1] scaled-sine rewrite with calculated CRCs 0x218F9FFA/0x18F4A6D6; ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (13471), frame shrank to 0x150 and first-ring position-array schedule drifted broadly; restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For trackbg_render_flashy, do not repeat the single-site x1 scaled-sine rewrite; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
