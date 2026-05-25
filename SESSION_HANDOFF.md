# Session Handoff

- Generated at: 2026-05-25 04:37:24Z
- Branch: `master`
- HEAD: `5bb48bb8`
- Completed task: `func_80059208`
- Summary: Rejected tempZ-through-distance spline result carrier; full verify failed with CRCs 0x53D141DF/0xB9D4B481 and relinked diff stayed CURRENT (870), source restored

## Validation

- Promoted `func_80059208` with only the third spline result changed from
  `tempZ = cubic_spline_interpolation(...)` to `distance =
  cubic_spline_interpolation(...); tempZ = distance;`.
- Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`.
- Full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  focused diff stayed at `CURRENT (870)`.
- The diff retained the same final-tail FPR drift around `0x5a260`, including
  current `$f12/$f0` object loads and folded `sub.s` where target uses
  `$f16/$f6`, an early checkpoint-dot `neg.s`, and `add.s`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat this `tempZ`-through-`distance`
  spline result carrier; it produced no movement from the promoted baseline.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 distinct spline-call argument or diffX/diffZ lifetime probe, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
