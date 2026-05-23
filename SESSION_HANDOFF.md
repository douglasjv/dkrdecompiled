# Session Handoff

- Generated at: 2026-05-23 05:11:59Z
- Branch: `master`
- HEAD: `0df159b7`
- Completed task: `trackbg_render_flashy`
- Summary: Center position store-order probe missed; object-only focused diff first printed stale CURRENT (0), full verify failed with calculated CRCs 0x93D338FF/0xC989AC94, and relinked focused diff regressed from CURRENT (1808) to CURRENT (1880). Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat trackbg_render_flashy center position store-order spelling (zPositions[4] before xPositions[4]) or the recorded trackbg position/UV aliases in ACTIVE.md. If staying on func_80049794, use a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, or first-speed arithmetic without repeating recorded guard compare, expression-order, accumulator-shape, condition-order, close save-family, or carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
