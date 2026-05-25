# Session Handoff

- Generated at: 2026-05-25 03:53:20Z
- Branch: `master`
- HEAD: `bebf1d38`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected all-first-ring scaledXSin reuse spelling; full verify failed and relinked diff regressed to CURRENT (13581), source restored

## Validation

- Pre-build `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted all-first-ring `scaledXSin` reuse probe failed full verify with
  calculated CRCs `0x8310DF9D/0x3EA48C03`.
- Relinked `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  reported `CURRENT (13581)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. All-first-ring `scaledXSin` reuse expanded the
  frame from target `0x158` to `0x168`, saved `$f20/$f21`, and shifted the
  early position-array/FPR schedule broadly. Do not repeat first-ring
  `scaledXSin` reuse probes.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `trackbg_render_flashy distinct early FPR allocation source shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
