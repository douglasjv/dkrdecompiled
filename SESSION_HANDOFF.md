# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `c5c4cb0a`
- Completed task: `func_80017A18 loop-control bitmask evidence`
- Summary: Recorded a restored worker miss for the revival-selected `func_80017A18` saved-register packet.

## Validation

- Worker full build for promoted `func_80017A18` dead-local removal plus
  loop-control bitmask carrier failed verify with CRCs
  `0x00C3F5F7/0x853E5357` versus expected `0x53D440E7/0x7519B011`.
- Worker focused relinked diff reported `CURRENT (8555)`.
- Worker restored `src/objects.c`; restored validation reached `Verify: OK`.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery` because all default-routable candidates have
  cooldown evidence.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling`.
- `python3 tools/query_goal_state.py revival` now recommends
  `init_particle_buffers`.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. `func_80017A18` loop-control bitmask-carrier
  variants are saturated and cooled down.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `init_particle_buffers narrow saved-register/lifetime strategy`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `high worker`
- Step: Evidence path `research/tasks/PARKED.md`; parked note says promoted C compiles but focused diff is saved-register allocation drift. Baseline promotion score `1816` with target frame `0x68`; target keeps counts in `s1/s3/s7/s4/s8` and allocator colour tag in `s2`, while current keeps counts in `s3/s1/s7/s2/s4` and tag in `s0`. Rejected families include register hints on count parameters, explicit local aliases for all counts, pointer-to-`gParticleTriangleBuffer`, fresh promotion, named `colourTag`, and removing only unused `pad`. Delegate only a narrower saved-register/lifetime strategy with predicted register movement.
