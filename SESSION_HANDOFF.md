# Session Handoff

- Generated at: 2026-05-24T06:54:56Z
- Branch: `master`
- HEAD: `9761a141`
- Completed task: `func_8002B0F4-surface-local-widening`
- Summary: Rejected promoted `s8 surface` -> `s32 surface` local-type probe for func_8002B0F4; source restored and packet remains routable.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK
- ./score.sh -s -> Decomp progress [us.v77]: 97.30%; Documentation progress: 65.47%
- python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; prefer func_80049794 only with a distinct saved-FPR/frame-pressure idea, otherwise choose func_80059208, trackbg_render_flashy, or func_8002B0F4 only with a non-repeat hypothesis from ACTIVE.md. For func_8002B0F4 do not repeat the rejected surface-local widening probe; target the early model pointer spill/segment setup or pivot.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
