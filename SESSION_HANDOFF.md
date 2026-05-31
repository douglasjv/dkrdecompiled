# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `f8342403`
- Completed task: `discovery selector ranking`
- Summary: Added discovery ranking from cooldown sidecar next-useful guidance.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` now reports
  `recommended_next: discovery` when all default-routable candidates have
  cooldown evidence.
- `python3 tools/query_goal_state.py discovery` recommends `func_8002B0F4`
  and prints its sidecar next-useful mechanism note.
- `python3 tools/query_goal_state.py discovery --json` includes ordered
  `discovery_candidates` with `has_next_useful` flags.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.

## Blockers Or Unknowns

- No setup blockers recorded. The active route is a discovery-selected
  mechanism packet, not a spelling probe.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 distinct model-load lifetime/register-allocation mechanism predicting target-like in-loop gCurrentLevelModel loads or removal of the 0x60(sp) model spill`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
