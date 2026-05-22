# Session Handoff

- Generated at: 2026-05-22 23:08:55Z
- Branch: `master`
- HEAD: `301df4c2`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected single-site zPositions[8] multiply-order spelling; source restored after no focused movement.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80049794 only with a new non-repeated source shape, otherwise pivot among active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
