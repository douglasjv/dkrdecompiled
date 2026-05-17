# Session Handoff

- Generated at: 2026-05-17 02:13:33Z
- Branch: `master`
- HEAD: `3d72ca0c`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Tested func_80049794 x/z/y pre-sqrt save-family branch with var_f14 preserved through existing spD4 across apply_vehicle_rotation_offset; it compiled but widened the frame to 0x100, worsened focused diff to CURRENT (4335), and spilled f4 at 0xdc(sp) instead of target f14. Restored guarded matching source and kept func_80049794 active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; ./diff.sh -o func_80049794 -s --compress-matching 4 --format plain --no-pager -> CURRENT (4335); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; next useful angle is still likely early zero/f20 allocation or local-slot scheduling from the best spCC preserve branch.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
