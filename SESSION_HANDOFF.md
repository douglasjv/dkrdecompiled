# Session Handoff

- Generated at: 2026-05-25 03:56:39Z
- Branch: `master`
- HEAD: `6a5f31a3`
- Completed task: `func_8002B0F4`
- Summary: Rejected local levelModel pointer pressure spelling; full verify failed and relinked diff regressed to CURRENT (4208), source restored

## Validation

- Pre-build `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted local `LevelModel *levelModel` pointer pressure probe failed full
  verify with calculated CRCs `0x8632BBD2/0x4CA9FD95`.
- Relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  reported `CURRENT (4208)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The local `LevelModel *levelModel` pointer shape
  worsened the frame/register schedule, spilled the model pointer at
  `0x12c(sp)`, and did not recover the target fresh model loads or bottom
  population/sort. Do not repeat this pointer-pressure spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 distinct early model-load pressure shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
