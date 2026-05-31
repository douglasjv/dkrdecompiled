# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `9438e02f`
- Completed task: `trackbg_render_flashy first-ring pair-result miss`
- Summary: Tightened mechanism-packet readiness so a packet is not probe-ready without `reasoning_tier`, routed a high-reasoning `trackbg_render_flashy` first-ring pair-result scratch packet, then rejected and cleared it after worker validation.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling` after the rejected `trackbg_render_flashy` packet was removed from
  `research/tasks/MECHANISM_PACKETS.md`.
- `python3 tools/query_goal_state.py discovery --json` reports all four live
  cooldown candidates as `tooling_first`, `ready_for_probe: false`, and lists
  `reasoning_tier` in the required packet fields.
- `python3 tools/query_goal_state.py packet --function trackbg_render_flashy`
  reports `ready_for_probe: false` after the first-ring pair-result scratch
  miss.
- `python3 tools/query_goal_state.py packet --function init_particle_buffers`
  reports `ready_for_probe: false` and lists `reasoning_tier` for the parked
  revival packet as well. The parked initial-only colour-tag focused
  `CURRENT (0)` remains rejected because full ROM verify failed.
- Worker-promoted `trackbg_render_flashy` with two short-lived first-ring
  pair-result scratch locals for the duplicated negative-cos stores. Full
  verify failed with CRCs `0x218FA01A/0x6CF4BEC1`; focused diff regressed to
  `CURRENT (13795)`. The probe moved the initial `neg.s` into `$f18`, but
  badly disturbed stack slots and downstream scheduling. Worker restored
  `src/tracks.c`.
- `python3 tools/query_goal_state.py revival` reports `revival_next: tooling`
  because all parked candidates have recent revival cooldown evidence.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. All live sidecar candidates and parked revival
  candidates are cooldown-routed; next progress should be discovery/tooling or
  a new distinct compiler-mechanism packet with target, evidence checked,
  rejected families, mechanism hypothesis, predicted asm movement, stop
  condition, and reasoning tier. `func_8002B0F4` discovery returned no safe
  packet and recommended tooling around the `gCurrentLevelModel` hoist/spill
  site before another probe.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling after trackbg_render_flashy pair-result miss`
- Packet class: `discovery`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py discovery --json`, and `python3 tools/query_goal_state.py revival`. Do not edit source until a candidate has a new mechanism packet with target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier. For `trackbg_render_flashy`, do not repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, pair-result scratch locals, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes.
