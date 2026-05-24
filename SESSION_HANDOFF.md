# Session Handoff

- Generated at: 2026-05-24 04:27:47Z
- Branch: `master`
- HEAD: `07203f50`
- Completed task: `trackbg_render_flashy-z2-scaledXSin`
- Summary: Rejected promoted trackbg_render_flashy single-site zPositions[2] direct scaledXSin replacement; it collapsed into the bad first-ring direct-scaledXSin frame-shrink family.

## Validation

- Probe gmake -j4 CROSS=tools/binutils/mips64-elf- failed with calculated CRCs 0x218F9FFA/0x18F4A6D6; relinked ./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager reported CURRENT (13821) and shrank the frame from 0x158 to 0x150. After source restore, gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s reports 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Pivot away from trackbg_render_flashy direct first-ring scaledXSin replacements; choose a different routable candidate or a distinct non-frame-shrinking FPR allocation hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
