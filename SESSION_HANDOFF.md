# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `119872cb`
- Completed task: `init_particle_buffers initial-only colour-tag evidence`
- Summary: Rejected a focused-diff-zero promoted source because full ROM verify failed.

## Validation

- Promoted `init_particle_buffers` with an `initialColourTag` local used only
  for the initial vertex and triangle allocations produced focused
  `./diff.sh init_particle_buffers --compress-matching 2 --no-pager`
  `CURRENT (0)`.
- The canonical full gate failed for that promoted source with calculated CRCs
  `0xEF29C961/0xF604264D` versus expected `0x53D440E7/0x7519B011`.
- Source was restored to asm-backed state.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling`.
- `python3 tools/query_goal_state.py revival` now reports `revival_next:
  tooling` because all parked candidates have recent revival cooldown evidence.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. `init_particle_buffers` initial-only colour-tag
  local is rejected; focused `CURRENT (0)` is insufficient without full verify.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/revival tooling after all live and parked candidates are cooldown-routed`
- Packet class: `discovery`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, and `python3 tools/query_goal_state.py revival`; select a bounded target only if it names a distinct compiler-mechanism hypothesis and full-verify stop condition. Treat focused `CURRENT (0)` on parked/guarded candidates as stale until the promoted full gate verifies.
