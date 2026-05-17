# Session Handoff

- Generated at: 2026-05-17T04:07:54Z
- Branch: `master`
- HEAD: `f46ab64b`
- Completed task: `DKR-MATCH-FUNC-80059208-SPLIT-OBJECT-DOT-PROBE`
- Summary: No new source match landed. Selector still recommends `func_80049794`, but this packet intentionally used the smaller active alternate `func_80059208` because its drift is localized to the final offset block. The probe computed the negated checkpoint dot first, then split the final object dot into `pad = splinePos * diffX; pad += diffZ * distance`. It compiled to the promoted baseline shape with no focused improvement, so guarded source was restored. `func_80059208` remains active rather than parked.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; intentionally selected smaller active alternate `func_80059208`; `python3 tools/check_active_surface.py` -> active surface ok; promoted baseline failed full verify with calculated CRCs `0x53D141DF/0xB9D4B481`; relinked focused `./diff.sh func_80059208 -s --format plain --no-pager --max-size 520` -> `CURRENT (870)`; split-object-dot-after-checkpoint probe failed full verify with the same calculated CRCs `0x53D141DF/0xB9D4B481`; relinked focused `--max-size 520` stayed `CURRENT (870)` with the same final object-load/arithmetic drift; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Treat object-only CURRENT (0) as stale unless relink/full verify agrees. Do not repeat the var_f6 pre-sqrt sum carrier or x/z-in-var_f20 plus y-in-call-argument carrier from the prior func_80049794 packet; both lose the target frame/save family. Also avoid the chained-zero save-family shape, comparison-only wave operand spelling, x/z/y pre-sqrt save-family mutating post-sqrt subtraction split, combined spEC early-zero spill shape, direct-player-index save-family combination, nested computer-player branch spelling, split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, the simple var_f2 early-zero carrier, the standalone racerVelocity register hint, the simple wave-speed var_f0 carrier, the simple spEC or segmentZVelocity early-zero carriers, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not trust the stale promoted CURRENT (0), and do not repeat the split-object-dot-after-checkpoint spelling from this packet, recorded final-block pad/pad2/pad3/distance/tempY/diffY/splinePos carrier families, positive `splinePos` checkpoint-dot carrier, pad/pad2 axis-swap temporary probes, or the `tempZ * -diffZ` sibling term-negation spelling. If func_8002B0F4 is used as a close alternate, do not repeat the direct levelModel loop-local cache spelling, volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard. If trackbg_render_flashy is used as a close alternate, avoid the recorded first-four position temp/store-order and scaled-sine/source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
