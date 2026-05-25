# Session Handoff

- Generated at: 2026-05-25 04:11:03Z
- Branch: `master`
- HEAD: `ba67e1a1`
- Completed task: `func_80049794`
- Summary: Rejected pointer-cursor wave-scan spelling; full verify failed and relinked diff reported CURRENT (8562), source restored

## Validation

- Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted pointer-cursor wave-scan probe failed full verify with calculated
  CRCs `0xED20BE1F/0xDF1B0F4F`.
- Relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  reported `CURRENT (8562)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The pointer-cursor wave-scan probe got pointer
  decrement in the loop and avoided the target-exit array reload, but it still
  placed the decrement index in current `v1` instead of target `a0`, shifted the
  frame to `0x100`, and still lacked target `$f20/$f21` prologue saves. Do not
  repeat this spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 independent saved-FPR lifetime/wave allocation source shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
