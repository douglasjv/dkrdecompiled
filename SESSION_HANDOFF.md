# Session Handoff

- Generated at: 2026-05-24 12:33:48Z
- Branch: `master`
- HEAD: `e9ca9450`
- Completed task: `func_80059208-spline-fill-loop-plain-bound`
- Summary: Rejected promoted func_80059208 spline fill-loop plain-bound spelling: changed the NON_MATCHING guard to #if 1 and rewrote only for (i = 0; (i < 5) ^ 0; i++) as for (i = 0; i < 5; i++). Full verify failed with CRCs 0x53905373/0x65198BEE; relinked ./diff.sh func_80059208 --compress-matching 2 --no-pager worsened to CURRENT (1515), changing the control-point fill-loop pointer/index schedule from sltu-based pointer compare to bne and carrying FPR drift into the final object/checkpoint-dot and vertical tail. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_80059208 spline fill-loop plain-bound, upper-half decrement/alternate-route, normalization-boolean, final object-dot, and final-tail clamp/negation microvariants unless paired with a distinct spline dataflow fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
