# Session Handoff

- Generated at: 2026-05-25 03:48:38Z
- Branch: `master`
- HEAD: `bcde5846`
- Completed task: `func_80059208`
- Summary: Rejected positive checkpoint-dot/subtract final-tail spelling; full verify failed and relinked diff stayed CURRENT (870), source restored

## Validation

- Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted positive checkpoint-dot/subtract final-tail probe failed full verify
  with calculated CRCs `0x53D141DF/0xB9D4B481`.
- Relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed
  at `CURRENT (870)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The positive checkpoint-dot/subtract final-tail
  spelling collapsed to the known final-tail drift family: object
  dot/checkpoint dot and vertical tail FPR carriers remained off target around
  `0x5a260`.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 distinct spline/vertical FPR allocation source shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
