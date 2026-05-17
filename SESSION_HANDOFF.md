# Session Handoff

- Generated at: 2026-05-17T12:52:38Z
- Branch: `master`
- HEAD: `6587fba5`
- Completed task: `DKR-MATCH-FUNC-80049794-WAVE-THRESHOLD-PROBE`
- Summary: No new source match landed. Followed the selector-recommended
  func_80049794 route and tested a narrow `5.0f` wave-height threshold spelling
  on the close save-family branch with removed trailing pads, x/z/y pre-`sqrtf`
  accumulation, steer-vel no-op, and chained grounded-wheel zero. The threshold
  spelling produced no object movement from that known close branch, so source
  was restored and func_80049794 remains active rather than parked.

## Validation

- Startup: read AGENTS.md and research/tasks/ACTIVE.md; `python3
  tools/query_goal_state.py next --compact --refresh` -> recommended
  `func_80049794`; `python3 tools/check_active_surface.py` -> active surface
  ok.
- func_80049794 close save-family `5.0f` wave-threshold probe: full verify
  failed with calculated CRCs `0xB8DD79CD/0xE47454ED`; relinked `./diff.sh
  func_80049794 --format plain --no-pager --max-size 760` -> `CURRENT
  (2132)`, with the same wave `a0`/`v1` register/order swap as the known close
  chained-zero branch.
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
  save-family wave-bound probes, the close-branch `5.0f` wave-threshold
  spelling, plus standalone register hints for racerThrottle/racerVelocity/
  var_f20/var_f14/segmentZVelocity/spEC/spD8/spD4/spD0 and the recorded
  early-zero/wave-speed/wave-count/top-speed/buoyancy/source-shape probes. For
  func_80059208, avoid the
  object-local-before-pad2 no-op, both split-negated checkpoint-dot orders, and
  recorded final-offset source-shape families. For trackbg_render_flashy, avoid
  the existing-`var_f16` double-sine carrier, the single-site
  `zPositions[0] = -scaledXCos + scaledXSin` scaled-sine spelling plus the
  recorded first-ring/outer-ring position-array source-shape families. For
  func_8002B0F4, avoid the texture-pointer replacement shape, the
  `pad3`-removed pointer-increment `gTrackWaves` population loop, the
  `pad3`-removed early `XInInt`/`ZInInt` conversion call shape, plus the
  recorded gCurrentLevelModel/cache/copy-loop/pad source-shape families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
