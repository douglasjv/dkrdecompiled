# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `43cc898e`
- Completed task: `trackbg inverted primary cos carrier miss`
- Summary: Rejected a worker-guided `trackbg_render_flashy` source probe and added a packet-context selector command for future delegations.

## Validation

- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next:
  tooling` and lists each cooldown candidate with a `gap=` reason.
- `python3 tools/query_goal_state.py discovery --json` reports all four live
  cooldown candidates as `tooling_first`, `ready_for_probe: false`, and lists
  the required packet fields for delegation/source edits.
- `python3 tools/query_goal_state.py packet --function trackbg_render_flashy`
  reports the trackbg evidence path and required packet fields.
- `python3 tools/query_goal_state.py packet --function func_8008FF1C` reports
  parked evidence from `research/tasks/PARKED.md` and recent revival cooldown.
- `python3 tools/query_goal_state.py packet --function func_8002B0F4` reports
  the next bounded worker context.
- Promoted `trackbg_render_flashy` with an inverted primary cos carrier
  (`pad_sp108` positive cos, `scaledXCos = -pad_sp108`) failed full verify with
  CRCs `0xDC79F591/0x31DBA03C`.
- Relinked focused `./diff.sh trackbg_render_flashy --compress-matching 2
  --no-pager` reported `CURRENT (3108)`. The initial `0x28d00` negation stayed
  current `neg.s $f16,$f12` instead of target `$f18`; only a later UV-block
  negation moved to `$f18`, with broader scheduling/register drift.
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

- No setup blockers recorded. `trackbg_render_flashy` inverted primary cos
  carrier is rejected. Next progress should use the `func_8002B0F4` worker
  mechanism packet or another distinct compiler-mechanism packet with target,
  evidence checked, rejected families, mechanism hypothesis, predicted asm
  movement, and stop condition.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 bottomSegment lifetime probe`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `high`
- Step: Target `func_8002B0F4` in `src/tracks.c`, evidence `research/tasks/func_8002B0F4_evidence.md`, asm `asm/nonmatchings/tracks/func_8002B0F4.s`. Rejected families: `sp108 <= 0`, inner `!=` face loop, local `LevelModel *levelModel`, texture/flags carriers, pointer-arithmetic segment setup, bottom store-order, condition/literal/cast/local-width spellings, bbox-before-segment ordering, and simple `segmentIndex` local lifetime. Hypothesis: split the bottom-water use of `currentSegment` into a separate `LevelModelSegment *bottomSegment` local used only in the post-loop `levelSegmentIndex` block, leaving outer-loop `currentSegment` only for traversal. Predicted movement: shorten `currentSegment` live range, remove early model spill at `0x60(sp)`/`0x64(sp)`, keep frame `0x128`, and reload `gCurrentLevelModel` after `.L8002B688` for the bottom block. Stop after one promoted source probe; reject immediately if the frame widens or early model spill remains.
