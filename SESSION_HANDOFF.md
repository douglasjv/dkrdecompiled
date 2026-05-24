# Session Handoff

- Generated at: 2026-05-24 10:55:58Z
- Branch: `master`
- HEAD: `b397af40`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted pad3-slot LevelModel carrier plus three-level surface guard and texture-index temp carrier; full verify failed and relinked diff remained in model-spill/grid drift

## Validation

- Rejected probe full build failed with calculated CRCs
  `0x7C2820DA/0x9A7063A4`; relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` reported `CURRENT (2503)`. The
  pad3-slot `LevelModel *levelModel` carrier plus three-level surface guard
  and `textureIndex` temp carrier improved over the promoted baseline, but
  still inserted an early `gCurrentLevelModel` load/spill at `0x94(sp)`,
  shifted the outer grid register family, and left bottom/tail labels drifting.
  After source restore, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended but saturated, so continue only with a distinct independent source family or pivot to another active routable candidate.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
