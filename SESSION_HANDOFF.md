# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `b9b4058f`
- Completed task: `cooldown-aware selector routing`
- Summary: Updated selector tooling to demote active cooldown/saturated evidence ledgers and route to `func_8002B0F4`.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` now reports
  `cooldown_notes=3` and recommends `func_8002B0F4` in `src/tracks.c:2686`.
- Cooldown sidecars currently demote `func_80049794`, `func_80059208`, and
  `trackbg_render_flashy` without parking them.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.

## Blockers Or Unknowns

- No setup blockers recorded. `func_80049794`, `func_80059208`, and
  `trackbg_render_flashy` remain active but cooldown-demoted until a distinct
  compiler-mechanism hypothesis is available.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 distinct model-load pressure or segment/grid scheduling probe; avoid prior entry-guard, loop-bound, local-levelModel, texture-index carrier, pointer-arithmetic setup, bottom-store-order, and condition-order spellings`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
