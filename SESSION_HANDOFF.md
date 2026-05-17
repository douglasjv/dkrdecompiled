# Session Handoff

- Generated at: 2026-05-17 02:22:22Z
- Branch: `master`
- HEAD: `bafc7b7d`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends func_80049794, but its current recorded probe surface is saturated, so this packet used the active close alternate func_80059208 rather than parking anything. Tested a final-offset carrier shape that reused now-dead splinePos as the negated checkpoint-dot term; it compiled but worsened focused diff from baseline CURRENT (870) to CURRENT (1356), perturbing earlier splinePos/double-temp allocation and broadening final-block register drift. Restored guarded source and kept func_80059208 active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; ./diff.sh -o func_80059208 -s --compress-matching 2 --format plain --no-pager -> CURRENT (1356); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat spD8, spD0, or spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used again, do not repeat the splinePos negated-checkpoint-dot carrier probe or its recorded final-offset misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
