# Session Handoff

- Generated at: 2026-05-24 07:05:56Z
- Branch: `master`
- HEAD: `516ea0e3`
- Completed task: `trackbg_render_flashy-register-xcos`
- Summary: Rejected promoted register-xCos allocation hint for trackbg_render_flashy; full verify failed with promoted baseline CRCs and relinked focused diff stayed CURRENT (1808), source restored.

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

- Task: `func_80049794 remains selector-recommended only with a distinct saved-FPR/wave allocation idea; otherwise choose func_80059208, trackbg_render_flashy, or func_8002B0F4 with a non-repeat hypothesis from ACTIVE.md. For trackbg_render_flashy do not repeat register xCos allocation hints.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
