# Session Handoff

- Generated at: 2026-05-23 05:25:21Z
- Branch: `master`
- HEAD: `c9229717`
- Completed task: `func_8002B0F4`
- Summary: Bottom default-water store-order probe (rot.x, rot.z, waveHeight, then rot.y) missed; object-only focused diff first printed stale CURRENT (0), full verify failed with calculated CRCs 0x281EE85B/0xEE22BD90, and relinked focused diff regressed from CURRENT (2780) to CURRENT (3745). Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but func_8002B0F4 remains active. Do not repeat func_8002B0F4 bottom default-water store-order spelling or the recorded model-spill, pad-removal, grid-loop, segment-index carrier, bottom sort/population, texture-index carrier, surface-guard, collision-output store-order, or bottom wave-type store-order aliases in ACTIVE.md. If staying on func_80049794, use a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, or first-speed arithmetic without repeating recorded guard compare, expression-order, accumulator-shape, condition-order, close save-family, drift-flag timing, or carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
