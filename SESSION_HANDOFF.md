# Session Handoff

- Generated at: 2026-05-22 20:45:15Z
- Branch: `master`
- HEAD: `b3e53ab4`
- Completed task: `func_8002B0F4`
- Summary: Recorded live-var_a1 Z-grid barrier miss; source restored.

## Validation

- Promoted func_8002B0F4 with live-var_a1 Z-grid barrier failed full verify with CRCs 0x7856718A/0x66208CAA and relinked focused CURRENT (2860); restored source then gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK.

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
