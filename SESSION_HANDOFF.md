# Session Handoff

- Generated at: 2026-05-23 05:28:28Z
- Branch: `master`
- HEAD: `b9d502a2`
- Completed task: `func_80049794`
- Summary: Current-baseline first-speed boss-adjustment divide-before-subtract probe (var_f20 = (var_f20 / 2.0) - 1.0) missed; object-only focused diff first printed stale CURRENT (0), full verify failed with calculated CRCs 0xCF9C57E6/0xCC0EF4F1, and relinked focused diff regressed to CURRENT (4030). Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat first-speed boss-adjustment divide-before-subtract, spA3 course-height placement, course-height compare operand-order, current-baseline spA2 declaration-initialization, first-speed grouped z/y add, R-trigger grounded-wheel stash guard, grounded boss throttle/brake condition-order, or the recorded wave/first-speed/save-family aliases in ACTIVE.md. If staying on func_80049794, use a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, or first-speed arithmetic without repeating recorded guard compare, expression-order, accumulator-shape, condition-order, close save-family, drift-flag timing, or carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
