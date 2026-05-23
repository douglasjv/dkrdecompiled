# Session Handoff

- Generated at: 2026-05-23 00:48:07Z
- Branch: `master`
- HEAD: `e13c9194`
- Completed task: `trackbg_render_flashy`
- Summary: Recorded single-site xPositions[0] scaledXSin replacement miss: object-only focused diff printed stale CURRENT (0), full verify failed with CRCs 0x218F9FFA/0x18F4A6D6, relinked focused diff CURRENT (13821), frame shrank to 0x150, and source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default routing remains func_80049794 unless pivoting to active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
