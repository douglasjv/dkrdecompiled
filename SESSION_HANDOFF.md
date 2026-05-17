# Session Handoff

- Generated at: 2026-05-17 12:10:40Z
- Branch: `master`
- HEAD: `a70c8ce9`
- Completed task: `DKR-MATCH-FUNC-80049794-RACERTHROTTLE-REGISTER-PROBE`
- Summary: No new source match landed. Promoted selector-recommended `func_80049794` and tested a standalone `register f32 racerThrottle` lifetime/allocation hint. It compiled but produced no object movement from the promoted baseline and still did not introduce the target `$f20/$f21` prologue saves, so guarded source was restored. `func_80049794` remains active rather than parked.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; promoted baseline after relink failed full verify with calculated CRCs `0x5FDDE03F/0xEF7A0514`; uncompressed `./diff.sh func_80049794 --format plain --no-pager --max-size 760` -> `CURRENT (1926)` with first visible drift at missing `$f20/$f21` prologue saves, shifted saved `$ra/$s1/$s0` stack slots, and early zero allocation in `$f16` instead of target `$f14`; standalone `register f32 racerThrottle` probe stayed `CURRENT (1926)` and same CRC family; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Keep close candidates active rather than parked. For func_80049794, avoid standalone register hints for racerThrottle, racerVelocity, var_f20, var_f14, segmentZVelocity, spEC/spD8/spD4/spD0, and the recorded early-zero/wave-speed/wave-count/top-speed/buoyancy/source-shape probes. If trackbg_render_flashy is used as a close alternate, avoid the first-ring xPositions[2] xCos-multiply spelling, minimal xPositions[3]/xPositions[2] reorder, register var_f16 hint, and previously recorded scaledXSin/outer-ring/negScaledXCos/store-order probes. If func_80059208 is used as a close alternate, avoid the delayed-diffZ positive-checkpoint-dot spelling from this packet plus the previously recorded final-offset carrier, term-negation, axis-swap, object-dot, clamp, and final-vertical source-shape misses.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
