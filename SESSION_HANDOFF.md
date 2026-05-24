# Session Handoff

- Generated at: 2026-05-24 10:30:40Z
- Branch: `master`
- HEAD: `98134dfb`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted batch-loop currentBatch pointer-carry probe; relinked diff regressed to CURRENT (4310) with early gCurrentLevelModel spill still at 0x60(sp).

## Validation

- Rejected probe full build failed with calculated CRCs
  `0x5FB2D180/0x62259969`; relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` regressed to `CURRENT (4310)`. After
  source restore, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with func_8002B0F4 only for a distinct model-spill fix, or pivot to another routable candidate if no independent source-shape is available.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
