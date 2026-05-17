# Session Handoff

- Generated at: 2026-05-17T02:57:42Z
- Branch: `master`
- HEAD: `056ded59`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends `func_80049794`, but this packet used active close alternate `func_8002B0F4` for one localized `gCurrentLevelModel` reload probe. Forcing direct volatile global-pointer reads at the initial `currentSegment` and `currentBoundingBox` setup sites compiled, but regressed the relinked focused score from `CURRENT (2780)` to `CURRENT (4395)` and shifted the same global-offset/tail-label drift family. Restored guarded source and kept `func_8002B0F4` active rather than parked.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; promoted `func_8002B0F4` baseline check -> relinked focused score `CURRENT (2780)`; `gmake build/src/tracks.c.o CROSS=tools/binutils/mips64-elf-` -> volatile reload probe compiles; `gmake -j4 CROSS=tools/binutils/mips64-elf-` while `func_8002B0F4` was promoted/probed -> verify failed as expected for nonmatching source; `./diff.sh func_8002B0F4 -s --format plain --no-pager` after relink -> `CURRENT (4395)`; `gmake -j4 CROSS=tools/binutils/mips64-elf-` after restore -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not repeat the pad2/pad3/pad/distance/tempY/diffY final-vertical carrier family, final distance-product object-dot carrier, ObjectTransform pointer, pad3-slot-compensated pointer, or recorded final-offset source-shape misses. If func_8002B0F4 is used as a close alternate, do not repeat the volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
