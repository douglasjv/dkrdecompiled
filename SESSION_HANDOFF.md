# Session Handoff

- Generated at: 2026-05-17T12:29:23Z
- Branch: `master`
- HEAD: `06d139c0`
- Completed task: `DKR-MATCH-TRACKBG-RENDER-FLASHY-Z0-SCALEDXSIN-PROBE`
- Summary: No new source match landed. After the func_80049794 closeout commit,
  intentionally chose the active alternate trackbg_render_flashy and tested a
  single-site first-ring spelling: `zPositions[0] = -scaledXCos + scaledXSin`.
  The probe fell into the bad scaled-sine family, shrinking the frame to
  `0x150` and sharply worsening the focused diff, so source was restored and
  trackbg_render_flashy remains active rather than parked.

## Validation

- Startup: read AGENTS.md and research/tasks/ACTIVE.md; `python3
  tools/query_goal_state.py next --compact --refresh` -> recommended
  `func_80049794`; `python3 tools/check_active_surface.py` -> active surface
  ok.
- Follow-up selector/check: `python3 tools/query_goal_state.py next --compact
  --refresh` -> recommended `func_80049794`; `python3
  tools/check_active_surface.py` -> active surface ok; active alternate
  `trackbg_render_flashy` chosen intentionally.
- trackbg_render_flashy z0 scaledXSin probe: full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`; relinked `./diff.sh
  trackbg_render_flashy --format plain --no-pager --max-size 760` ->
  `CURRENT (13376)`.
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
  recorded first-ring/outer-ring position-array source-shape families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
