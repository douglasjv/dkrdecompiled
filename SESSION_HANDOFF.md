# Session Handoff

- Generated at: 2026-05-24 07:08:53Z
- Branch: `master`
- HEAD: `640467c2`
- Completed task: `func_8002B0F4-s16-surface`
- Summary: Rejected promoted s16 surface local-width probe for func_8002B0F4; full verify failed with promoted baseline CRCs and relinked focused diff stayed CURRENT (2860), source restored.

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

- Task: `func_80049794 remains selector-recommended only with a distinct saved-FPR/wave allocation idea; otherwise choose func_80059208, trackbg_render_flashy, or func_8002B0F4 with a non-repeat hypothesis from ACTIVE.md. For func_8002B0F4 do not repeat s8 surface -> s16/s32 local-width probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
