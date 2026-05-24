# Session Handoff

- Generated at: 2026-05-24 07:53:23Z
- Branch: `master`
- HEAD: `0842bcad`
- Completed task: `trackbg-render-flashy-register-scaledxcos`
- Summary: Rejected promoted register scaledXCos allocation hint; relinked diff stayed at CURRENT (1808), source restored.

## Validation

- ./diff.sh trackbg_render_flashy --no-pager before full build: misleading CURRENT (0) against the pre-relink object
- gmake -j4 CROSS=tools/binutils/mips64-elf- after promotion: failed, calculated CRCs 0x93D338FF/0x03D9C8FE
- ./diff.sh trackbg_render_flashy --no-pager after promotion/relink: CURRENT (1808), early negative-cosine still current `$f16` instead of target `$f18`
- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK
- ./score.sh -s: Decomp progress [us.v77]: 97.30%
- python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default remains func_80049794 unless choosing a fresh non-repeat alternate hypothesis such as trackbg_render_flashy early FPR allocation without declaration-only register hints`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
