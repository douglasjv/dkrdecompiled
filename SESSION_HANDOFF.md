# Session Handoff

- Generated at: 2026-05-17T03:44:26Z
- Branch: `master`
- HEAD: `b605168a`
- Completed task: `DKR-MATCH-FUNC-80049794-VARF2-EARLY-ZERO-PROBE`
- Summary: No new source match landed. Selector still recommends `func_80049794`. This packet tested routing the initial grounded-wheel zero stores through the existing `var_f2` local. The branch compiled but stayed in the promoted-baseline miss family: focused `--max-size 520` diff was `CURRENT (759)`, full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the early zero still allocated in `$f16` instead of target `$f14`. Guarded source was restored and the function remains active rather than parked.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; existing-`var_f2` initial grounded-wheel zero carrier compiled; full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`; focused diff with `--max-size 520` -> `CURRENT (759)`; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Treat object-only CURRENT (0) as stale unless relink/full verify agrees. Do not repeat the x/z/y pre-sqrt save-family mutating post-sqrt subtraction split, direct-player-index save-family combination, nested computer-player branch spelling, split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, the simple var_f2 early-zero carrier, the standalone racerVelocity register hint, the simple wave-speed var_f0 carrier, the simple spEC or segmentZVelocity early-zero carriers, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not repeat the recorded final-block pad/pad2/pad3/distance/tempY/diffY/splinePos carrier families, the pad/pad2 axis-swap temporary probes, or the `tempZ * -diffZ` sibling term-negation spelling. If func_8002B0F4 is used as a close alternate, do not repeat the direct levelModel loop-local cache spelling, volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard. If trackbg_render_flashy is used as a close alternate, avoid the recorded first-four position temp/store-order and scaled-sine/source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
