# Session Handoff

- Generated at: 2026-05-25 04:13:30Z
- Branch: `master`
- HEAD: `368a25fc`
- Completed task: `func_80049794`
- Summary: Rejected register var_f20 storage-class hint; full verify failed and relinked diff stayed CURRENT (2760), source restored

## Validation

- Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted `register f32 var_f20` storage-class hint failed full verify with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`.
- Relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported `CURRENT (2760)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The `register f32 var_f20` storage-class hint did
  not recover target `$f20/$f21` prologue saves; the diff stayed in the same
  `CURRENT (2760)` family with early zero in current `$f16` instead of target
  `$f14` and the current `a0`-bound/`v1`-loop wave scan. Do not repeat this
  spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 distinct saved-FPR lifetime/wave allocation source shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
