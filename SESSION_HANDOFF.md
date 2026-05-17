# Session Handoff

- Generated at: 2026-05-17 13:30:04Z
- Branch: `master`
- HEAD: `49a59f2a`
- Completed task: `func_80049794`
- Summary: Tested an existing-`var_v0` wave-count carrier on the close func_80049794 save-family branch: promoted source, removed trailing `pad3`/`pad4`, used chained grounded-wheel zero, kept the x/z/y pre-`sqrtf` accumulation plus steer-vel no-op, then loaded `gRacerWaveCount` into `var_v0` for the loop bound and comparison. It compiled, kept the target `0xf8` frame and `$f20/$f21` saves, but regressed relinked focused diff to CURRENT (4557), failed full verify with calculated CRCs 0xA637D7C4/0x633471A3, and widened wave-register churn. Source guard/body restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh func_80049794 --format plain --no-pager --max-size 760` => relinked focused CURRENT (4557)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80049794 existing-var_v0 wave-count carrier.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
