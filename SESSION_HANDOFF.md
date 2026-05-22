# Session Handoff

- Generated at: 2026-05-22 20:22:23Z
- Branch: `master`
- HEAD: `0840fde8`
- Completed task: `func_80059208`
- Summary: Recorded vertical lower-first clamp-order miss; source restored.

## Validation

- Promoted func_80059208 vertical lower-first clamp order failed full verify with CRCs 0x53D101DF/0xB0C39AEC and relinked focused CURRENT (1035); restored source then gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80059208 only with a new non-repeated final-tail source shape, otherwise pivot among active func_80049794, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
