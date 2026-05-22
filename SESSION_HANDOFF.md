# Session Handoff

- Generated at: 2026-05-22 16:57:27Z
- Branch: `master`
- HEAD: `5d7cc433`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected single-site z0 scaled-sine spelling; source restored after evidence capture.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore; zPositions[0] = -scaledXCos + scaledXSin probe failed with CRCs 0x218F9FFA/0x18F4A6D6 and ./diff.sh trackbg_render_flashy => relinked CURRENT (13471).

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate; func_80049794 remains selector-recommended but saturated, so inspect ACTIVE.md before choosing whether to continue it or a narrower active target.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
