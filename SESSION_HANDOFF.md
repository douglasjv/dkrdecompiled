# Session Handoff

- Generated at: 2026-05-17 15:01:41Z
- Branch: `master`
- HEAD: `7e02b131`
- Completed task: `func_80049794`
- Summary: Tested a current-baseline wave-bound split in `func_80049794`: promoted source, introduced `var_v1 = gRacerWaveCount - 1`, looped `for (var_a0 = var_v1; ...)`, and compared `if (var_a0 == var_v1)`. It compiled but worsened the focused score from promoted baseline `CURRENT (2430)` to `CURRENT (4920)`, failed full verify with calculated CRCs `0x5790053C/0x1C8C0179`, introduced `spA2` stack-byte traffic, and widened wave-scan register churn rather than matching the target `v1` bound and `a0` loop-index family. Source restored; final full verify passed. Keep `func_80049794` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 900 after relink => baseline CURRENT (2430), split wave-bound probe CURRENT (4920); failed full verify CRCs 0x5790053C/0x1C8C0179

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80049794 current-baseline split wave-bound probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
