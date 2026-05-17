# Session Handoff

- Generated at: 2026-05-17 02:45:16Z
- Branch: `master`
- HEAD: `1763e036`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends func_80049794, but this packet used active close alternate func_80059208 for one localized final-offset probe. Routing the final object-dot `diffZ * distance` product through the existing `distance` local compiled but regressed the relinked focused score from CURRENT (870) to CURRENT (2043), pulling object-position scheduling too early. Restored guarded source and kept func_80059208 active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; gmake -j4 CROSS=tools/binutils/mips64-elf- while func_80059208 was promoted/probed -> verify failed as expected for nonmatching source; ./diff.sh func_80059208 -s --compress-matching 2 --format plain --no-pager after relink -> CURRENT (2043); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as the close alternate, do not repeat the final distance-product object-dot carrier, ObjectTransform pointer, pad3-slot-compensated pointer, distance/pad/pad3/tempY/diffY final-vertical carrier family, or recorded final-offset misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
