# Session Handoff

- Generated at: 2026-05-17 02:31:17Z
- Branch: `master`
- HEAD: `c2190c0e`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends func_80049794, but this packet used active close alternate func_80059208 for one localized object-position load probe. Routing final object-position loads through a named `ObjectTransform *trans = &obj->trans` local compiled and produced the target-like `lw v0, 0xc0(sp)` timing in the tail, but worsened focused diff from baseline CURRENT (870) to CURRENT (1096) by shifting spline/local stack slots down by 4 bytes. Restored guarded source and kept func_80059208 active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; ./diff.sh -o func_80059208 -s --compress-matching 2 --format plain --no-pager -> CURRENT (1096); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if func_80059208 is used as the close alternate, do not repeat the ObjectTransform pointer probe, distance/pad/pad3/tempY/diffY final-vertical carrier family, or its recorded final-offset misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
