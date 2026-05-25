# Session Handoff

- Generated at: 2026-05-25 04:07:14Z
- Branch: `master`
- HEAD: `79ab2deb`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected removing fake var_a2 recomputation; full verify failed and relinked diff reported CURRENT (12107), source restored

## Validation

- Pre-build `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted removed fake `var_a2` recomputation probe failed full verify with
  calculated CRCs `0xC5B710C5/0x71187E4F`.
- Relinked `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  reported `CURRENT (12107)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Removing the fake `var_a2` recomputation still
  left broad early FPR/position-array drift and did not recover the target
  negative-cosine carrier. Do not repeat this spelling.

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
