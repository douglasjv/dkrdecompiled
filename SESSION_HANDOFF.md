# Session Handoff

- Generated at: 2026-05-25 03:45:37Z
- Branch: `master`
- HEAD: `f3eb1c22`
- Completed task: `func_80049794`
- Summary: Rejected wave-scan top-bound var_v1/index var_a0 spelling; full verify failed and relinked diff regressed to CURRENT (5755), source restored

## Validation

- Worker pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted wave-scan top-bound carrier probe failed full verify with calculated
  CRCs `0x5790053C/0x1C8C0179`.
- Relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported `CURRENT (5755)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The explicit `var_v1 = gRacerWaveCount - 1`
  top-bound carrier spelling did not recover the target wave scan: current used
  `v1` for count, `a3` for top bound, and `v0` for the decrementing loop index,
  with repeated pointer recomputation instead of the target `v1` bound / `a0`
  decrement / pointer-decrement family.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 independent saved-FPR lifetime source shape, or distinct live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
