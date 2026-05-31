# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `c910cd4c`
- Completed task: `func_8002B0F4`
- Summary: Worker rejected bbox-before-segment ordering; source restored.

## Validation

- Worker promoted `func_8002B0F4` and reordered initial loop setup to assign
  `currentBoundingBox` before `currentSegment`.
- Full verify failed with CRCs `0x7856718A/0xA6A743D8`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3965)`.
- Key drift worsened the early model-load family: current hoisted
  `gCurrentLevelModel` before the segment loop and spilled it to `0x60(sp)`,
  while target loads it inside the loop. Worker restored source and restored
  validation reached `Verify: OK`.
- Parent `gmake -j4 CROSS=tools/binutils/mips64-elf-` also reached
  `Verify: OK`.
- After recording this sidecar, `python3 tools/query_goal_state.py next
  --compact --refresh` reports `cooldown_notes=4` and recommends cooldown
  evidence for `func_80049794`.

## Blockers Or Unknowns

- No setup blockers recorded. Do not repeat `func_8002B0F4` initial
  segment/bbox assignment-order pressure probes unless the next hypothesis
  specifically predicts removal of the early model stack spill. Evidence is in
  `research/tasks/func_8002B0F4_evidence.md`.

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
