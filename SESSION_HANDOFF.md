# Session Handoff

- Generated at: 2026-05-17T12:26:28Z
- Branch: `master`
- HEAD: `650186e7`
- Completed task: `DKR-MATCH-FUNC-80049794-SPLIT-VAR-V1-WAVE-BOUND-PROBE`
- Summary: No new source match landed. Followed the selector to func_80049794,
  promoted the existing C, then tested the close save-family branch with
  chained grounded-wheel zero, removed trailing pads, x/z/y pre-sqrtf
  accumulation, steer-vel no-op, and a split `var_v1 = gRacerWaveCount - 1`
  wave-bound spelling. The split spelling compiled to the same bad family as
  the prior comma-assignment wave-bound probe, so source was restored and
  func_80049794 remains active rather than parked.

## Validation

- Startup: read AGENTS.md and research/tasks/ACTIVE.md; `python3
  tools/query_goal_state.py next --compact --refresh` -> recommended
  `func_80049794`; `python3 tools/check_active_surface.py` -> active surface
  ok.
- func_80049794 promoted baseline: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked `./diff.sh func_80049794 --format plain
  --no-pager --max-size 900` -> `CURRENT (2430)`.
- Split-`var_v1` wave-bound save-family probe: full verify failed with
  calculated CRCs `0x2E4A9A41/0xD04D4E64`; relinked focused diff was
  `CURRENT (6100)`, matching the prior bad comma-assignment wave-bound family.
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
  parked. For func_80049794, avoid both comma-assignment and split-assignment
  save-family wave-bound probes, plus standalone register hints for
  racerThrottle/racerVelocity/var_f20/var_f14/segmentZVelocity/spEC/spD8/
  spD4/spD0 and the recorded early-zero/wave-speed/wave-count/top-speed/
  buoyancy/source-shape probes. For func_80059208, avoid the
  object-local-before-pad2 no-op and recorded final-offset source-shape
  families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
