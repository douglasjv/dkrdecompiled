# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `93d90573`
- Completed task: `func_8008FF1C revival miss and cooldown ranking`
- Summary: Recorded a restored xhigh worker miss for `func_8008FF1C` and cooled down recently revived parked candidates in the revival selector.

## Validation

- Worker full build for promoted `func_8008FF1C` direct-table branch plus
  duplicated first-side-effect `hubName` stores failed verify with CRCs
  `0xAED257D4/0xAE31DFED` versus expected `0x53D440E7/0x7519B011`.
- Worker focused relinked diff reported `CURRENT (475)`.
- Worker restored `src/menu.c`; restored validation reached `Verify: OK`.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery` because all default-routable candidates have
  cooldown evidence.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling`.
- `python3 tools/query_goal_state.py revival` now recommends `func_80017A18`
  and lists `func_8008FF1C` after applying recent-revival cooldown.
- `python3 tools/query_goal_state.py revival --json` marks `func_8008FF1C`
  with `revival_cooldown: true`.
- `python3 -m py_compile tools/query_goal_state.py` passed.
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

- No setup blockers recorded. `func_8008FF1C` direct-table plus duplicated
  first-side-effect `hubName` store variants are saturated and cooled down.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80017A18 narrow float-temp lifetime and saved-register allocation`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `high worker`
- Step: Evidence path `research/tasks/PARKED.md`; parked note says promoted C compiles but focused diff is far. Baseline promotion score `8246` with frame `0x138` vs target `0x120`; removing dead `dx/dy/dz` improved to `7950` and frame `0x130`; fully inlining edge-plane locals reached target frame but worsened to `8600`; `register s32 var_s6` did not move the bitmask into `s6`. Delegate only a narrow float-temp lifetime and saved-register allocation hypothesis with predicted frame/register movement, not those same probes.
