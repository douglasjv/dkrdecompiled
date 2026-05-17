# Session Handoff

- Generated at: 2026-05-17 02:37:58Z
- Branch: `master`
- HEAD: `3bd68741`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends func_80049794, but this packet used active close alternate func_8002B0F4 for one bounded conversion-lifetime probe. Promoting the existing C relinked to the documented baseline CURRENT (2780) and failed verify. Moving only `XInInt = xIn` / `ZInInt = zIn` immediately after `*arg3 = NULL`, while still passing original `xIn`/`zIn` to `get_inside_segment_count_xz`, compiled but stayed relinked CURRENT (2780). Restored guarded source and kept func_8002B0F4 active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/tracks.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; gmake -j4 CROSS=tools/binutils/mips64-elf- while promoted/probed -> verify failed as expected for nonmatching source; ./diff.sh func_8002B0F4 -s --compress-matching 3 --no-pager after relink -> CURRENT (2780); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_8002B0F4 is used as the close alternate, do not repeat the early XInInt/ZInInt conversion probe, the get_inside_segment_count_xz converted-argument probe, the bounding-box-before-segment setup probe, the volatile LevelModel local probe, or the explicit gTrackWaves remainder plus unrolled-copy spelling.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
