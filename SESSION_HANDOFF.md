# Session Handoff

- Generated at: 2026-05-24 12:44:57Z
- Branch: `master`
- HEAD: `26c0db97`
- Completed task: `func_80059208-splinepos-zero-constant-left`
- Summary: Rejected promoted func_80059208 splinePos lower-clamp constant-left spelling: changed the NON_MATCHING guard to #if 1 and rewrote only if (splinePos < 0.0f) as if (0.0f > splinePos). Full verify failed with calculated CRCs 0x53D141DF/0xB9D4B481; relinked ./diff.sh func_80059208 --compress-matching 2 --no-pager stayed at CURRENT (870), with no movement in the lower clamp and the same final object-dot/checkpoint-dot plus vertical FPR tail drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_80059208 splinePos lower-clamp constant-left, pre-fill counter expression/guard, fill-loop, upper-half decrement/alternate-route, normalization, wrong-way counter, final object-dot, and final-tail clamp/negation microvariants unless paired with a distinct spline dataflow fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
