# Session Handoff

- Generated at: 2026-05-17 16:09:38Z
- Branch: `master`
- HEAD: `92aaabeb`
- Completed task: `func_80049794`
- Summary: Tested a current-baseline wave-scan predecrement probe while promoting func_80049794: rewrote the wave loop as for (var_a0 = gRacerWaveCount; --var_a0 >= 0 && ...;). It compiled but missed: relinked focused diff worsened to CURRENT (3680), full verify failed with calculated CRCs 0x77882035/0x6FF367A8, and the wave scan introduced broader integer-register churn rather than matching the target v1/a0/v0 family. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 4 => CURRENT (3680); failed full verify CRCs 0x77882035/0x6FF367A8

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80049794 current-baseline predecrement wave-scan loop plus prior func_80049794 chained-zero/wave-bound/save-family probes, func_80059208 final-offset variants, func_8002B0F4 pad/early-conversion/loop probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
