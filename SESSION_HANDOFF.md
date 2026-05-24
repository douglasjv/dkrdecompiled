# Session Handoff

- Generated at: 2026-05-24 07:32:36Z
- Branch: `master`
- HEAD: `8b2b3705`
- Completed task: `func_80049794`
- Summary: Plain guarded-C promotion rejected after stale pre-promotion diff

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> Verify: OK; `./score.sh -s` -> 97.30%; `python3 tools/check_active_surface.py` -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 only with distinct saved-FPR plus wave bound/index allocation fix, otherwise pivot to another routable packet`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
