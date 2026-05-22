# Session Handoff

- Generated at: 2026-05-22 21:12:13Z
- Branch: `master`
- HEAD: `6b34db85`
- Completed task: `trackbg_render_flashy`
- Summary: Recorded z5 plus-negative equivalence miss; source restored.

## Validation

- Promoted trackbg_render_flashy with zPositions[5] plus-negative spelling failed full verify with CRCs 0x53DC5E0F/0x8B102C25 and relinked focused CURRENT (2831), matching the recorded z5 plus-negated-double miss family; restored source then gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80049794 only with a new non-repeated close save-family or wave-register source shape, otherwise pivot among active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
