# Session Handoff

- Generated at: 2026-05-17T03:59:32Z
- Branch: `master`
- HEAD: `1c17f0f8`
- Completed task: `DKR-MATCH-FUNC-80049794-CHAINED-ZERO-SAVE-FAMILY-PROBE`
- Summary: No new source match landed. Selector still recommends `func_80049794`, and the function remains active rather than parked. This packet tried the x/z/y pre-`sqrtf` save-family plus steer-noop branch with chained early grounded-wheel zero (`racer->unk88 = (racer->unk84 = 0.0f)`) and removed trailing `pad3`/`pad4`. The candidate kept the target `0xf8` frame and `$f20/$f21` saves, removed the previous `spEC` early-zero spill, and improved the relinked compressed `--max-size 620` score to `CURRENT (620)`, but still failed full verify with calculated CRCs `0xB8DD79CD/0xE47454ED`. A comparison-only wave operand spelling did not change the result. Guarded source was restored.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; chained-zero save-family candidate compiled; initial focused object-only `./diff.sh func_80049794 -s --format plain --no-pager --max-size 620` misleadingly printed `CURRENT (0)`; full `gmake -j4 CROSS=tools/binutils/mips64-elf-` failed with calculated CRCs `0xB8DD79CD/0xE47454ED`; relinked focused `--max-size 620` -> `CURRENT (620)`; comparison-only wave operand spelling also failed full verify with the same CRCs and relinked focused `CURRENT (620)`; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Treat object-only CURRENT (0) as stale unless relink/full verify agrees. Do not repeat the chained-zero save-family shape or comparison-only wave operand spelling from this packet. Also avoid the x/z/y pre-sqrt save-family mutating post-sqrt subtraction split, combined spEC early-zero spill shape, direct-player-index save-family combination, nested computer-player branch spelling, split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, the simple var_f2 early-zero carrier, the standalone racerVelocity register hint, the simple wave-speed var_f0 carrier, the simple spEC or segmentZVelocity early-zero carriers, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as a close alternate, do not trust the stale promoted CURRENT (0), and do not repeat the recorded final-block pad/pad2/pad3/distance/tempY/diffY/splinePos carrier families, positive `splinePos` checkpoint-dot carrier, pad/pad2 axis-swap temporary probes, or the `tempZ * -diffZ` sibling term-negation spelling. If func_8002B0F4 is used as a close alternate, do not repeat the direct levelModel loop-local cache spelling, volatile gCurrentLevelModel reload spelling, gTrackWaves remainder/unrolled-copy spelling, early XInInt/ZInInt conversion spelling, local volatile levelModel spelling, setup-order swap, or empty gCurrentLevelModel guard. If trackbg_render_flashy is used as a close alternate, avoid the recorded first-four position temp/store-order and scaled-sine/source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
