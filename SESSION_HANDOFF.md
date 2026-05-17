# Session Handoff

- Generated at: 2026-05-17T12:32:07Z
- Branch: `master`
- HEAD: `ab8f2626`
- Completed task: `DKR-MATCH-FUNC-8002B0F4-PAD3-POINTER-COPY-PROBE`
- Summary: No new source match landed. Intentionally chose active alternate
  func_8002B0F4, used the known better `pad3`-removed branch, then tested a
  pointer-increment `gTrackWaves` population loop. The pointer-copy spelling
  worsened the relinked focused diff and shifted early register scheduling, so
  source was restored and func_8002B0F4 remains active rather than parked.

## Validation

- Startup: read AGENTS.md and research/tasks/ACTIVE.md; `python3
  tools/query_goal_state.py next --compact --refresh` -> recommended
  `func_80049794`; `python3 tools/check_active_surface.py` -> active surface
  ok.
- func_8002B0F4 pad3-removed pointer-copy probe: full verify failed with
  calculated CRCs `0x47E07C97/0x7D45A79C`; relinked `./diff.sh func_8002B0F4
  --format plain --no-pager --max-size 900` -> `CURRENT (6366)`.
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
  families. For trackbg_render_flashy, avoid the single-site
  `zPositions[0] = -scaledXCos + scaledXSin` scaled-sine spelling plus the
  recorded first-ring/outer-ring position-array source-shape families. For
  func_8002B0F4, avoid the `pad3`-removed pointer-increment `gTrackWaves`
  population loop plus the recorded gCurrentLevelModel/cache/copy-loop/pad
  source-shape families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
