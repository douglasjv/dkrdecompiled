# Session Handoff

- Generated at: 2026-05-17T03:03:50Z
- Branch: `master`
- HEAD: `b9272c79`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends `func_80049794`; promoted baseline remains `CURRENT (2760)` with the known `$f20/$f21` save drift. This packet checked close alternates, skipped already-recorded `func_80059208` final-block shapes, confirmed `trackbg_render_flashy` promoted baseline at `CURRENT (1753)`, and tested one fresh `func_8002B0F4` direct `LevelModel *levelModel` loop-local cache. That probe compiled but widened the frame to `0x130` and worsened the relinked focused score from `CURRENT (2780)` to `CURRENT (2900)`, so guarded source was restored and `func_8002B0F4` remains active rather than parked.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; promoted `func_80049794` baseline -> `CURRENT (2760)`, restored before alternate checks; promoted `func_80059208` baseline -> `CURRENT (870)`, restored without repeating recorded final-block probes; promoted `trackbg_render_flashy` baseline -> `CURRENT (1753)`, restored without repeating recorded position-array probes; promoted `func_8002B0F4` baseline -> `CURRENT (1435)` with `--max-size 260`; direct `levelModel` loop-local probe -> compiles, promoted full verify fails as expected, `./diff.sh func_8002B0F4 -s --format plain --no-pager` -> `CURRENT (2900)` and `--max-size 260` -> `CURRENT (1470)`; `gmake -j4 CROSS=tools/binutils/mips64-elf-` after restore -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not repeat the recorded final-block pad/pad2/pad3/distance/tempY/diffY/splinePos carrier families. If func_8002B0F4 is used as a close alternate, do not repeat the direct levelModel loop-local cache spelling, volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard. If trackbg_render_flashy is used as a close alternate, avoid the recorded first-four position temp/store-order and scaled-sine/source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
