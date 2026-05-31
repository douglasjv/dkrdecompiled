# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `57de5d6f`
- Completed task: `discovery readiness routing`
- Summary: Updated selector tooling so discovery output reports whether cooldown sidecars contain a probe-ready mechanism packet and which fields are still required.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling` and lists each cooldown candidate with a `gap=` reason.
- `python3 tools/query_goal_state.py discovery --json` reports all four live
  cooldown candidates as `tooling_first`, `ready_for_probe: false`, and lists
  the required packet fields for delegation/source edits.
- `python3 tools/query_goal_state.py revival` now reports `revival_next:
  tooling` because all parked candidates have recent revival cooldown evidence.
- `python3 tools/query_goal_state.py list --json --include-exhausted` reports
  `recommended_next: null` and marks the three parked candidates with
  `revival_cooldown: true`.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. All live sidecar candidates and parked revival
  candidates are cooldown-routed; next progress should be discovery/tooling or
  a distinct compiler-mechanism packet with target, evidence checked, rejected
  families, mechanism hypothesis, predicted asm movement, and stop condition.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/revival tooling after all live and parked candidates are cooldown-routed`
- Packet class: `discovery`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py discovery --json`, `python3 tools/query_goal_state.py revival`, and `python3 tools/query_goal_state.py list --json --include-exhausted`; select a bounded target only if a candidate is `ready_for_probe: true` or a new packet explicitly names a distinct compiler-mechanism hypothesis and full-verify stop condition. Treat focused `CURRENT (0)` on parked/guarded candidates as stale until the promoted full gate verifies.
