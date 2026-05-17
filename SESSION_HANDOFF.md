# Session Handoff

- Generated at: 2026-05-17T03:15:15Z
- Branch: `master`
- HEAD: `60d8c3e4`
- Completed task: `DKR-MATCH-FUNC-80059208-AXIS-TEMP-PROBES`
- Summary: No new source match landed. Selector still recommends `func_80049794`, but this packet used close active candidate `func_80059208` without parking it. Promoted baseline stayed at relinked focused `CURRENT (870)`. Reusing `pad` or `pad2` as the final axis-swap temporary compiled and produced a deceptive compressed-window score (`--max-size 260`: `CURRENT (20)`), but full relinked focused score worsened to `CURRENT (1698)` and verify failed with calculated CRCs `0x0A689858/0x4CFBB1F6`, so guarded source was restored.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; promoted `func_80059208` baseline full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`; relinked `./diff.sh func_80059208 -s --format plain --no-pager` -> `CURRENT (870)`; `pad` axis-swap temporary full verify failed with calculated CRCs `0x0A689858/0x4CFBB1F6`, relinked focused diff -> `CURRENT (1698)`, and `--max-size 260` -> `CURRENT (20)`; `pad2` axis-swap temporary produced the same relinked score and CRC family; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Treat object-only CURRENT (0) as stale unless relink/full verify agrees. Do not repeat the x/z/y pre-sqrt save-family mutating post-sqrt subtraction split, split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not repeat the recorded final-block pad/pad2/pad3/distance/tempY/diffY/splinePos carrier families or the pad/pad2 axis-swap temporary probes. If func_8002B0F4 is used as a close alternate, do not repeat the direct levelModel loop-local cache spelling, volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard. If trackbg_render_flashy is used as a close alternate, avoid the recorded first-four position temp/store-order and scaled-sine/source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
