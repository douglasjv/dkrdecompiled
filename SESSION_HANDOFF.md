# Session Handoff

- Generated at: 2026-05-17 12:17:31Z
- Branch: `master`
- HEAD: `3e489081`
- Completed task: `DKR-MATCH-FUNC-80049794-SAVE-FAMILY-WAVE-BOUND-PROBE`
- Summary: No new source match landed. Recreated the close func_80049794 save-family branch with chained grounded-wheel zero, removed trailing pads, x/z/y pre-sqrtf accumulation, and steer-vel no-op, then tested a comma-assignment wave-bound spelling. It kept the target frame and f20/f21 saves but regressed the relinked focused score, so guarded source was restored and func_80049794 remains active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; promoted baseline full verify failed with calculated CRCs 0x5FDDE03F/0xEF7A0514; probe full verify failed with calculated CRCs 0x2E4A9A41/0xD04D4E64 and relinked ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -> CURRENT (6100); source restored; final gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Keep close candidates active rather than parked. For func_80049794, avoid the save-family comma-assignment wave-bound probe plus standalone register hints for racerThrottle/racerVelocity/var_f20/var_f14/segmentZVelocity/spEC/spD8/spD4/spD0 and the recorded early-zero/wave-speed/wave-count/top-speed/buoyancy/source-shape probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
