# Session Handoff

- Generated at: 2026-05-23 01:27:08Z
- Branch: `master`
- HEAD: `b1419513`
- Completed task: `trackbg_render_flashy`
- Summary: Promoted trackbg_render_flashy and collapsed the UV scale setup from var_f14 = 1280.0f; var_f14 *= 0.25f to var_f14 = 320.0f. Full verify failed with calculated CRCs 0x027233EC/0x55516330, and relinked ./diff.sh trackbg_render_flashy worsened to CURRENT (3510). Source was restored.

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
