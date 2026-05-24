# Session Handoff

- Generated at: 2026-05-24 12:00:20Z
- Branch: `master`
- HEAD: `8b72cbad`
- Completed task: `func_80049794-wave-countdown-derived-index`
- Summary: Rejected worker-probed early wave count-down-derived-index spelling: promoted func_80049794 scanned with var_v1 = gRacerWaveCount and gRacerCurrentWave[var_v1 - 1], then derived var_a0 = var_v1 - 1; full verify failed with CRCs 0xA80DF324/0x1C0D36A7; relinked ./diff.sh func_80049794 --compress-matching 2 --no-pager regressed to CURRENT (6300). Worker restored source.

## Validation

- worker final `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached Verify: OK after restore; parent `gmake -j4 CROSS=tools/binutils/mips64-elf-` also reached Verify: OK; `./score.sh -s` remained 97.30%; `python3 tools/check_active_surface.py` reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Avoid further pure func_80049794 wave-bound/index micro-variants unless paired with a distinct saved-FPR/frame-pressure source family; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
