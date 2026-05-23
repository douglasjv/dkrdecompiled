# Session Handoff

- Generated at: 2026-05-23 00:52:18Z
- Branch: `master`
- HEAD: `91faf54e`
- Completed task: `func_8002B0F4`
- Summary: Recorded bottom SURFACE_WATER_WAVY store-order miss: promoted current source failed full verify with CRCs 0x77D5718A/0x18F6F0C5, relinked focused diff worsened to CURRENT (3730), and source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default routing remains func_80049794 unless pivoting to active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
