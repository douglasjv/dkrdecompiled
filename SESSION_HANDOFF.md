# Session Handoff

- Generated at: 2026-05-25 04:22:35Z
- Branch: `master`
- HEAD: `ca513d2c`
- Completed task: `func_80059208`
- Summary: Rejected final-tail checkpoint-dot-first ordering; full verify failed with baseline CRCs and relinked diff stayed CURRENT (870), source restored

## Validation

- Promoted baseline `func_80059208` failed full verify with calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked `./diff.sh func_80059208
  --compress-matching 2 --no-pager` reported `CURRENT (870)`.
- Checkpoint-dot-first ordering moved only the final-tail source order:
  `pad2 = -((tempZ * diffZ) + (diffX * tempX));` before loading object
  `x/z` locals and computing `pad`.
- The probe failed full verify with the same calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked focused diff stayed `CURRENT (870)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat checkpoint-dot-first final-tail
  ordering for `func_80059208`; it left the known `0x5a260` object/checkpoint
  dot FPR carrier drift unchanged.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 distinct spline dataflow/FPR allocation shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
