# Session Handoff

- Generated at: 2026-05-25 03:36:46Z
- Branch: `master`
- HEAD: `91d82bc2`
- Completed task: `func_8002B0F4`
- Summary: Rejected direct bottom gTrackWaves population spelling; restored source after relinked diff stayed in early gCurrentLevelModel spill family

## Validation

- `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` after the rejected
  probe relinked at `CURRENT (2855)`.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` after source restore reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.

## Blockers Or Unknowns

- `func_8002B0F4` direct bottom `gTrackWaves` population is rejected evidence,
  not a blocker. It still introduced the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and shifted bottom population/sort labels.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 saved-FPR/wave allocation, or distinct func_8002B0F4 model-load pressure shape`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
