# Session Handoff

- Generated at: 2026-05-23 09:11:07Z
- Branch: `master`
- HEAD: `ae4c0162`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline wave-height threshold commute; promoting source with gRacerCurrentWave[var_a0]->waveHeight < 5 + obj->trans.y_position failed verify with CRCs 0x5FE1E03F/0x88CC2028 and relinked focused diff worsened to CURRENT (2770), then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but consider another active alternate if no fresh func_80049794 hypothesis exists beyond saturated CURRENT (2760) family. For func_80049794, do not repeat current-baseline wave-height threshold commute, attach-point model-index postincrement, attach-point grounded-wheel branch-order, late boost-emitter branch-order, race-start y-velocity double-literal, brake lower-clamp zero literal, A-button throttle clamp literal, low-speed drag multiply grouping, or other recorded wave-scan/early-zero/current-baseline spellings in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
