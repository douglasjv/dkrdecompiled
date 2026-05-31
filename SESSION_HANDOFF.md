# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `c22b82fb`
- Completed task: `func_8008FF1C pointer-cell revival miss`
- Summary: Added a compact parked-note excerpt to `query_goal_state.py packet --function <parked>`, taught revival/tooling routes to honor complete parked mechanism packets, tested the high-reasoning `func_8008FF1C` pointer-to-selected-track-cell packet in an isolated worker, then recorded and cleared the miss.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling` after the rejected `trackbg_render_flashy` packet was removed from
  `research/tasks/MECHANISM_PACKETS.md`.
- `python3 tools/query_goal_state.py tooling` reports `tooling_next:
  discovery_packet` and lists blocked live/parked candidates with evidence
  paths, readiness gaps, next-useful notes, and required packet fields.
- `python3 tools/query_goal_state.py discovery --json` reports all four live
  cooldown candidates as `tooling_first`, `ready_for_probe: false`, and lists
  `reasoning_tier` in the required packet fields.
- `python3 tools/query_goal_state.py packet --function trackbg_render_flashy`
  reports `ready_for_probe: false` after the first-ring pair-result scratch
  miss.
- `python3 tools/query_goal_state.py packet --function func_80059208` reports
  `ready_for_probe: false` after the high discovery pass found no safe
  final-tail mechanism packet beyond rejected families.
- `python3 tools/query_goal_state.py packet --function init_particle_buffers`
  reports `ready_for_probe: false` and lists `reasoning_tier` for the parked
  revival packet as well. The parked initial-only colour-tag focused
  `CURRENT (0)` remains rejected because full ROM verify failed.
- Worker-promoted `func_8008FF1C` with a pointer-to-selected-track-cell
  lifetime shape. Full verify failed with calculated CRCs
  `0x553930E7/0x227AD4A3`; focused
  `./diff.sh func_8008FF1C --compress-matching 2 --no-pager` reported
  `CURRENT (935)`. The target delay-slot `sw v0,0(s0)` appeared, but the
  selected-track load still emitted `lh v1,0(s1)` instead of target
  `lh t2,0(s1)`. Worker restored `src/menu.c` and final full verify passed.
- `python3 tools/query_goal_state.py packet --function func_8008FF1C` reports
  `ready_for_probe: false`, prints a compact `parked_note` excerpt from
  `research/tasks/PARKED.md`, and lists required packet fields because the
  ready packet was rejected and removed.
- Worker-promoted `trackbg_render_flashy` with two short-lived first-ring
  pair-result scratch locals for the duplicated negative-cos stores. Full
  verify failed with CRCs `0x218FA01A/0x6CF4BEC1`; focused diff regressed to
  `CURRENT (13795)`. The probe moved the initial `neg.s` into `$f18`, but
  badly disturbed stack slots and downstream scheduling. Worker restored
  `src/tracks.c`.
- High discovery for `func_80059208` found no safe mechanism packet. Remaining
  target drift still requires object X into `$f16`, `5.0f` before object Z,
  object Z into `$f6`, `neg.s $f0,$f0`, and vertical math through target
  `$f6/$f10`; all named source-level levers overlapped rejected families.
- High tooling for `func_8002B0F4` found no safe mechanism packet. The worker
  captured a promoted object slice with `NON_EQUIVALENT=1`: current hoists
  `gCurrentLevelModel` before the segment loop at `0x5D7C/0x5D80`, spills it
  to `0x60(sp)` at `0x5D94`, and reloads it at `0x5DA4`/`0x5FE8`; target
  reloads the global at each use around `0x2BDD4/0x2BDD8` and
  `0x2C020/0x2C024`.
- `python3 tools/query_goal_state.py tooling` reports `tooling_next:
  discovery_packet`.
- `python3 tools/query_goal_state.py revival` reports `revival_next: tooling`
  because all parked candidates have recent revival cooldown evidence and
  `research/tasks/MECHANISM_PACKETS.md` has no ready packets.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. All live sidecar candidates and parked revival
  candidates are cooldown-routed; next progress should be discovery/tooling or
  a new distinct compiler-mechanism packet with target, evidence checked,
  rejected families, mechanism hypothesis, predicted asm movement, stop
  condition, and reasoning tier. The rejected `func_8008FF1C`
  pointer-to-selected-track-cell packet should not be retried.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling for next mechanism-ready packet`
- Packet class: `routing_tooling`
- Packet status: `no ready source packet`
- Reasoning tier: `high` for delegated mechanism discovery
- Step: Run `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py tooling`, and targeted `packet --function <candidate>` reads to choose one bounded target. Before any probe or delegation, produce a complete packet with target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier. Do not reopen `func_8008FF1C` with pointer-to-selected-track-cell, direct-table branch, duplicated hub-name store, or temp-carrier families.
