# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `e90c0c4a`
- Completed task: `revival selector for parked candidates`
- Summary: Added an explicit revival route for intentionally returning to parked candidates when all live sidecars are cooldown/tooling-first.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery` because all default-routable candidates have
  cooldown evidence.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery` because all default-routable candidates have
  cooldown evidence.
- `python3 tools/query_goal_state.py discovery` reports `func_8002B0F4`,
  `func_80059208`, and `trackbg_render_flashy` as `kind=tooling_first`, with
  `func_80049794` as `kind=fallback_note`.
- Updated `python3 tools/query_goal_state.py discovery` reports
  `discovery_next: tooling` when no mechanism-ready candidate remains.
- `python3 tools/query_goal_state.py revival` recommends `func_8008FF1C`
  from `research/tasks/PARKED.md`.
- `python3 tools/query_goal_state.py revival --json` includes parked notes for
  `func_8008FF1C`, `func_80017A18`, and `init_particle_buffers`.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. All live sidecar candidates are cooldown-routed;
  revival is now the explicit route for parked candidates.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8008FF1C direct-table selected-track branch with target delay-slot hubName store`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `xhigh worker`
- Step: Evidence path `research/tasks/PARKED.md`; parked baseline is close at `CURRENT (10)` but full verify fails. Rejected families include selected-track temp/register carriers, direct-table branch alone, RHS comma-side-effect store, duplicated/common hub-name stores, compare-carrier, declaration-order, current-shape temp removal, and condition-assignment spellings. Delegate only a source shape that predicts the direct-table `t2` selected-track load/branch while preserving the target branch-delay-slot `sw v0,0(s0)` hubName store; accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies.
