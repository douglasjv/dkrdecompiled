# Session Handoff

- Generated at: 2026-05-17 16:43:04Z
- Branch: `master`
- HEAD: `b6f7f3fe`
- Completed task: `trackbg_render_flashy`
- Summary: Tested moving only the duplicated first-ring `zPositions[1] = -scaledXCos - (xSin * 1280.0f)` store immediately after `xPositions[0]` in trackbg_render_flashy. It compiled and kept the 0x158 frame, but missed: relinked focused score worsened to CURRENT (2938), full verify failed with calculated CRCs 0x93D342FF/0x71E01805, and the diff shifted the early position-array float-register/store schedule instead of matching the target. Source restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 1200 -U 5 => CURRENT (2938); failed full verify CRCs 0x93D342FF/0x71E01805

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded trackbg_render_flashy single-pair x0/z1 store-order probe plus prior trackbg_render_flashy position/UV order-carrier probes, func_80059208 final-offset variants, func_80049794 chained-zero/wave-bound/save-family probes, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
