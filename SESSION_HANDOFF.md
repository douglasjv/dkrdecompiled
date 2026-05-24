# Session Handoff

- Generated at: 2026-05-24 08:09:20Z
- Branch: `master`
- HEAD: `acaedcb2`
- Completed task: `trackbg-render-flashy-direct-var-f16-uv`
- Summary: Rejected direct var_f16 UV sine-carrier spelling; relinked diff regressed to CURRENT (15227), source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK; ./score.sh -s: 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default may still recommend func_80049794, but current routing should pivot away from func_80049794 save/wave micro-variants, func_80059208 final object-dot micro-variants, and trackbg_render_flashy direct var_f16 UV alias-removal unless a new independent source family is found. Otherwise choose another routable packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
