# Session Handoff

- Generated at: 2026-05-24 06:33:07Z
- Branch: `master`
- HEAD: `585e3b6a`
- Completed task: `func_80017A18`
- Summary: Rejected plain guarded-C promotion; compressed focused diff was misleadingly CURRENT (0), but full verify failed and uncompressed diff showed CURRENT (8376).

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restore
- ./score.sh -s -> Decomp progress [us.v77]: 97.30%
- python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; use func_80049794 only with a distinct save-pressure/wave allocation family, otherwise choose func_80017A18, trackbg_render_flashy, func_8002B0F4, or func_80059208 only with a non-repeat hypothesis from ACTIVE.md`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
