# Session Handoff

- Generated at: 2026-05-25 03:59:23Z
- Branch: `master`
- HEAD: `bf5ac54b`
- Completed task: `func_80049794`
- Summary: Rejected early var_f14 zero carrier spelling; full verify failed and relinked diff stayed at CURRENT (2760), source restored

## Validation

- Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted early `var_f14` zero-carrier probe failed full verify with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`.
- Relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  stayed at `CURRENT (2760)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The early `var_f14 = 0.0f` carrier shape did not
  move the zero stores from current `$f16` to target `$f14`, did not recover
  target `$f20/$f21` prologue saves, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Do not repeat this spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 independent saved-FPR lifetime or wave allocation shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
