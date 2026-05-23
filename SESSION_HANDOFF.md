# Session Handoff

- Generated at: 2026-05-23 00:24:29Z
- Branch: `master`
- HEAD: `6513e0c1`
- Completed task: `func_8002B0F4`
- Summary: Promoted func_8002B0F4 and combined the current-layout texture-index temp carrier with a three-level water-surface guard split. Full verify failed with calculated CRCs 0x7C4CE18A/0x3A298210 and relinked focused score stayed CURRENT (2435), matching the standalone texture-index carrier family with the same early gCurrentLevelModel spill at 0x60(sp). Source was restored and final verify passed; do not repeat this current-layout texture-index plus three-level guard split.

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
