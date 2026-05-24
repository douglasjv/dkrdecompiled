# Session Handoff

- Generated at: 2026-05-24 05:14:09Z
- Branch: `master`
- HEAD: `ba2f202b`
- Completed task: `func_80049794`
- Summary: Worker rejected promoted close save-family plus target-bound while wave-scan probe: full verify failed with calculated CRCs 0x57263252/0x731465D5; relinked focused diff regressed to CURRENT (8135). The shape preserved the close save-family base but the wave scan compiled into a1/a0/v0/v1 churn with indexed reloads instead of target pointer-predecrement allocation. Worker source was restored.

## Validation

- Worker fork: restored source and final gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK. Main checkout: gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok; git diff --check clean.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Avoid func_80049794 close save-family plus explicit var_v0/var_v1/var_a0 while wave-scan spellings; either find a distinct saved-FPR wave pointer-predecrement source shape or pivot to another routable candidate such as func_8002B0F4 model-spill/register-family work.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
