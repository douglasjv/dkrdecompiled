# Session Handoff

- Generated at: 2026-05-17T02:48:44Z
- Branch: `master`
- HEAD: `7ba21e0a`
- Completed task: `DKR-MATCH-ACTIVE-NO-PARK-PROBES`
- Summary: No new source match landed. Selector still recommends func_80049794, but this packet used active close alternate trackbg_render_flashy for one localized first-four position probe. Replacing only `xPositions[3]` with `-scaledXCos + scaledXSin` compiled but regressed the relinked focused score to CURRENT (9344) / CURRENT (12161), shrinking the frame to 0x150 and reshuffling the early position stores. Restored guarded source and kept trackbg_render_flashy active.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; python3 tools/check_active_surface.py -> active surface ok; gmake build/src/tracks.c.o CROSS=tools/binutils/mips64-elf- -> probe compiles; gmake -j4 CROSS=tools/binutils/mips64-elf- while trackbg_render_flashy was promoted/probed -> verify failed as expected for nonmatching source; ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 260 after relink -> CURRENT (9344); ./diff.sh trackbg_render_flashy -s --format plain --no-pager after relink -> CURRENT (12161); gmake -j4 CROSS=tools/binutils/mips64-elf- after restore -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794. Do not repeat the split boss-adjustment spelling, spD8/spD0/spD4 preserve-across-apply on the x/z/y pre-sqrt branch, inverse-gravity var_f0 staging, x-only/y-only/z-only/z-y var_f2 first-speed component carrier shapes, or the other recorded allocation/wave/early-zero/source-shape misses. Keep close candidates active rather than parked; if trackbg_render_flashy is used as a close alternate, do not repeat the xPositions[3] single-site scaled-sine rewrite, first-four grouped temp probe, xPositions[2] scaled-sine probes, outer-ring additive doubles, named negScaledXCos/register-hint probes, or recorded store-order misses.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
