# Session Handoff

- Generated at: 2026-05-22 20:48:34Z
- Branch: `master`
- HEAD: `9f1dd5e8`
- Completed task: `func_80059208`
- Summary: Recorded split old-diffX checkpoint-dot miss; source restored.

## Validation

- Promoted func_80059208 with split old-diffX checkpoint-dot schedule failed full verify with CRCs 0x543A5FDF/0x5F70BBBB and relinked focused CURRENT (2165); restored source then gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80049794 only with a new non-repeated close save-family or wave-register source shape, otherwise pivot among active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
