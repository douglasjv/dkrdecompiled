# Session Handoff

- Generated at: 2026-05-22 20:07:16Z
- Branch: `master`
- HEAD: `bb99ef0a`
- Completed task: `trackbg_render_flashy`
- Summary: Recorded uCoords[3] plus-negative UV miss; source restored after relinked focused CURRENT (8410).

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source): Verify: OK
- ./diff.sh trackbg_render_flashy --format plain --no-pager -U 80 (promoted uCoords[3] plus-negative UV): CURRENT (8410), failed full verify CRCs 0x511B5709/0xE130E098

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80049794 only with a new non-repeated close save-family source shape, otherwise pivot among active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
