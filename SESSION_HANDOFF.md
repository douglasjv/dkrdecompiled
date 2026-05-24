# Session Handoff

- Generated at: 2026-05-24 00:22:16Z
- Branch: `master`
- HEAD: `c6ec3858`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected UV scale multiplier-order probe; source restored

## Validation

- probe failed gmake -j4 CROSS=tools/binutils/mips64-elf- CRC 0xCBC5BBA5/0xBDF6EEC6; relinked ./diff.sh trackbg_render_flashy CURRENT (2028); restored gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `trackbg_render_flashy: avoid UV scale multiplier-order and saturated position/UV expression families; try only a fresh position-array scheduling hypothesis or pivot to another selector-routable candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
