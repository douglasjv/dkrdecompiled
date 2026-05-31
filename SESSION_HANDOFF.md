# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `2c686df5`
- Completed task: `func_8002B0F4 bottomSegment lifetime miss`
- Summary: Rejected a worker-guided `func_8002B0F4` bottomSegment lifetime split because it widened the frame and retained the early model spill.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling` and lists each cooldown candidate with a `gap=` reason.
- `python3 tools/query_goal_state.py discovery --json` reports all four live
  cooldown candidates as `tooling_first`, `ready_for_probe: false`, and lists
  the required packet fields for delegation/source edits.
- `python3 tools/query_goal_state.py packet --function func_8002B0F4` reports
- Promoted `func_8002B0F4` with a separate `LevelModelSegment *bottomSegment`
  used only in the post-loop `levelSegmentIndex` water block. Full verify
  failed with CRCs `0x76D9116A/0x07C0B726`.
- Relinked focused `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  reported `CURRENT (3123)`. The frame widened from target `0x128` to current
  `0x130`, `spB0` shifted to `0xB4(sp)`, and `gCurrentLevelModel` still hoisted
  before the segment loop and spilled at `0x64(sp)`.
- Source was restored to asm-backed state.
- `python3 tools/query_goal_state.py revival` now reports `revival_next:
  tooling` because all parked candidates have recent revival cooldown evidence.
- `python3 tools/query_goal_state.py list --json --include-exhausted` reports
  `recommended_next: null` and marks the three parked candidates with
  `revival_cooldown: true`.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reported decomp progress 97.30%.

## Blockers Or Unknowns

- No setup blockers recorded. `func_8002B0F4` bottom-only segment-pointer
  lifetime split is rejected. All live sidecar candidates and parked revival
  candidates are cooldown-routed; next progress should be discovery/tooling or
  a new distinct compiler-mechanism packet with target, evidence checked,
  rejected families, mechanism hypothesis, predicted asm movement, and stop
  condition.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling after func_8002B0F4 bottomSegment miss`
- Packet class: `discovery`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py discovery --json`, and `python3 tools/query_goal_state.py revival`. Do not edit source until a candidate has a new mechanism packet with target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, and stop condition. For `func_8002B0F4`, do not repeat bottom-only `bottomSegment`, simple segment-index, bbox-before-segment, or local model-pointer lifetime probes.
