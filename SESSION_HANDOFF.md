# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `3ba2fb88`
- Completed task: `func_80049794 promoted object-slice audit`
- Summary: Audited promoted `func_80049794`; focused diff reports `CURRENT (0)`, but the full gate cannot reach ROM CRC comparison because promoted `racer.c.o` does not provide the DRM helper symbols needed by restored `tracks.c.o`/`object_models.c.o`, and objdump still lacks the target saved-FPR/early-zero shape.

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
- Follow-up high discovery for `func_8002B0F4` found no safe ordinary-C packet:
  remaining levers collapse into rejected local segment-index, local model
  pointer, bottom-only segment-pointer split, assignment/order, texture/flag
  carrier, pointer-arithmetic setup, condition/literal/local-width, or bottom
  store-order families. Next useful work is a promoted-object slice audit
  around the hoist/spill sites, not another source probe.
- High discovery for `init_particle_buffers` found no safe mechanism packet.
  The unresolved gap is freeing `s2` from the line-count role while keeping
  five count parameters in target `s1/s3/s7/s4/s8` order and colour tag in
  `s2`. Remaining source levers collapse into rejected register hints,
  explicit count aliases, local triangle-buffer pointer, all-call colour-tag,
  unused-pad removal, initial-only colour-tag, or focused-`CURRENT (0)`
  acceptance families. Next useful work is promoted object-slice tooling around
  the first `mempool_alloc_safe` calls.
- Promoted object-slice tooling for `init_particle_buffers` confirmed the
  focused false positive. Promoted `build/src/particles.c.o` made
  `./diff.sh init_particle_buffers --compress-matching 2 --no-pager` report
  `CURRENT (0)`, but full ROM verify failed with calculated CRCs
  `0x45663544/0x7C66D688`. Objdump showed the promoted object still using
  counts `s3/s1/s7/s2/s4` and colour tag `s0`, not target counts
  `s1/s3/s7/s4/s8` and colour tag `s2`. Matching object was restored and final
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- Promoted object-slice tooling for `func_80017A18` confirmed another focused
  false positive. Promoted `build/src/objects.c.o` made
  `./diff.sh func_80017A18 --compress-matching 2 --no-pager` report
  `CURRENT (0)`, but full ROM verify failed with calculated CRCs
  `0xD0505FD8/0xE965F5F5`. Objdump showed the promoted object still using
  frame `0x138` instead of target `0x120`, with the bitmask initialized in
  `ra` instead of target `s6`. Matching object was restored and final
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- Promoted object-slice tooling for `func_80049794` reproduced the focused
  false-positive pattern. Promoted `build/src/racer.c.o` made
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` report
  `CURRENT (0)`, but the full gate could not reach ROM CRC comparison because
  restored `tracks.c.o`/`object_models.c.o` reference racer-provided DRM
  helper symbols (`drm_checksum_balloon`, `drm_vehicle_traction`) that are
  unavailable in the promoted racer object. Objdump still lacked target
  `$f20/$f21` saves and early zero in `$f14`; matching `racer.c.o` was
  restored and final `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
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
  pointer-to-selected-track-cell packet and `func_8002B0F4`
  model-load-lifetime probe families should not be retried. For
  `init_particle_buffers` or `func_80049794`, do not trust focused
  `CURRENT (0)`; require a distinct saved-register mechanism before any
  further source probe. For
  `func_80017A18`, require a mechanism predicting target frame `0x120` and
  bitmask in `s6`.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling for next mechanism-ready packet`
- Packet class: `routing_tooling`
- Packet status: `no ready source packet`
- Reasoning tier: `high` for delegated mechanism discovery
- Step: Run `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py tooling`, and targeted `packet --function <candidate>` reads to choose one bounded target. Before any probe or delegation, produce a complete packet with target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier. Do not reopen `func_8008FF1C` with pointer-to-selected-track-cell, direct-table branch, duplicated hub-name store, or temp-carrier families. For `func_8002B0F4`, do promoted object-slice/tooling before any further source probe; for `init_particle_buffers`, require a new saved-register allocation mechanism that predicts target count registers and colour tag before any source probe; for `func_80017A18`, require a mechanism that predicts target frame `0x120` and bitmask in `s6`; for `func_80049794`, do not repeat promoted-object `CURRENT (0)` acceptance unless the audit method preserves racer-provided DRM helper symbols and reaches the full ROM verify gate.
