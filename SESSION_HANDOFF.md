# Session Handoff

- Generated at: 2026-05-25 03:50:51Z
- Branch: `master`
- HEAD: `31ea7682`
- Completed task: `func_80059208`
- Summary: Rejected vertical pad3 alias final-tail spelling; full verify failed and relinked diff regressed to CURRENT (1840), source restored

## Validation

- Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted vertical `pad3` alias final-tail probe failed full verify with
  calculated CRCs `0x5AD1197F/0xF56ACA5E`.
- Relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  reported `CURRENT (1840)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The vertical `pad3` alias worsened the final tail
  by adding extra `0x50(sp)` store/load traffic before the clamp while retaining
  the known object-dot/checkpoint-dot and vertical FPR carrier drift.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 distinct spline/FPR allocation source shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
