# Session Handoff

- Generated at: 2026-05-23 11:51:48Z
- Branch: `master`
- HEAD: `8be3bbe9`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected vCoords[8] plus-negative UV spelling; source restored after CURRENT (2358) miss

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, with active alternates only for fresh bounded probes. Do not repeat the recorded trackbg_render_flashy vCoords[8] plus-negative/additive/operand/grouped-negated UV spellings or earlier outer-ring/store-order/triangle probes. Choose a fresh bounded source-shape probe or another active alternate with unrecorded evidence.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
