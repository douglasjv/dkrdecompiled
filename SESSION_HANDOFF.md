# Session Handoff

- Generated at: 2026-05-25 04:25:29Z
- Branch: `master`
- HEAD: `8d2aff7f`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected zPositions[3] commuted scaled carrier ordering; full verify failed with baseline CRCs and relinked diff stayed CURRENT (1808), source restored

## Validation

- Promoted baseline `trackbg_render_flashy` failed full verify with calculated
  CRCs `0x93D338FF/0x03D9C8FE`; relinked `./diff.sh trackbg_render_flashy
  --compress-matching 2 --no-pager` reported `CURRENT (1808)`.
- The probe changed only `zPositions[3] = scaledXCos + scaledXSin;` to
  `zPositions[3] = scaledXSin + scaledXCos;`.
- The probe failed full verify with the same calculated CRCs
  `0x93D338FF/0x03D9C8FE`; relinked focused diff stayed `CURRENT (1808)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat this commuted `zPositions[3]`
  scaled-carrier ordering; it left the known early negative-cosine and
  first/outer position-array FPR drift unchanged.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `trackbg_render_flashy distinct early FPR allocation shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
