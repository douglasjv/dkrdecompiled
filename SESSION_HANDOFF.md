# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `fc996947`
- Completed task: `discovery route selector`
- Summary: Updated selector to emit `recommended_next: discovery` when all default candidates are cooldown-demoted.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` now reports
  `recommended_next: discovery` when all default-routable candidates have
  cooldown evidence.
- `python3 tools/query_goal_state.py list --json --refresh` reports
  `"discovery_route": true`, `"recommended_next": null`, and four
  `cooldown_probe_notes`.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.

## Blockers Or Unknowns

- No setup blockers recorded. The active route is discovery/tooling because all
  default-routable guarded candidates have cooldown sidecars.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling route: all default-routable guarded candidates have cooldown sidecars; only probe a cooled-down function after naming a distinct compiler-mechanism hypothesis and predicted asm movement`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
