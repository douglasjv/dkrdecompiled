# Session Handoff

- Generated at: 2026-05-17T12:22:57Z
- Branch: `master`
- HEAD: `6b051cb4`
- Completed task: `DKR-MATCH-FUNC-80059208-OBJECT-LOCAL-PAD2-ORDER-PROBE`
- Summary: No new source match landed. Intentionally chose the close active
  alternate func_80059208 after selector startup still recommended
  func_80049794. Promoted func_80059208 and tested loading final object x/z
  locals before computing the negated checkpoint dot, then computing `pad2`
  before `pad`. The probe produced no object movement from the promoted
  baseline and stayed `CURRENT (870)`, so guarded source was restored.
  func_80059208 and func_80049794 both remain active, not parked.

## Validation

- Startup: read AGENTS.md and research/tasks/ACTIVE.md; `python3
  tools/query_goal_state.py next --compact --refresh` -> recommended
  `func_80049794`; `python3 tools/check_active_surface.py` -> active surface
  ok.
- func_80059208 promoted baseline: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked `./diff.sh func_80059208 --format plain
  --no-pager --max-size 760` -> `CURRENT (870)`.
- Object-local-before-pad2 probe: full verify failed with the same calculated
  CRCs `0x53D141DF/0xB9D4B481`; relinked focused diff stayed `CURRENT (870)`,
  with no object movement from the promoted baseline.
- Source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` ->
  `Verify: OK`.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active
  alternate is intentionally chosen. Keep close candidates active rather than
  parked. For func_80059208, avoid the object-local-before-pad2 no-op and the
  recorded final-offset source-shape families. For func_80049794, avoid the
  save-family comma-assignment wave-bound probe plus standalone register hints
  for racerThrottle/racerVelocity/var_f20/var_f14/segmentZVelocity/spEC/spD8/
  spD4/spD0 and the recorded early-zero/wave-speed/wave-count/top-speed/
  buoyancy/source-shape probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
