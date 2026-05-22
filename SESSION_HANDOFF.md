# Session Handoff

- Generated at: 2026-05-22 18:40:44Z
- Branch: `master`
- HEAD: `9331c8c7`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected uCoords[3] operand-order UV spelling; source restored after evidence capture.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore; uCoords[3] operand-order failed with CRCs 0x511B5709/0xE130E098 and ./diff.sh trackbg_render_flashy => relinked CURRENT (8410).

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate; func_80049794 remains selector-recommended but saturated, while func_80059208, trackbg_render_flashy, and func_8002B0F4 remain active fallback packets with recorded no-repeat notes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
