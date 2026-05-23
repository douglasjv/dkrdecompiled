# Session Handoff

- Generated at: 2026-05-23 08:18:28Z
- Branch: `master`
- HEAD: `0b819f16`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline attach-point grounded-wheel branch-order spelling: changed the late wheel visibility guard from racer->groundedWheels != 0 || spA2 != FALSE to spA2 != FALSE || racer->groundedWheels != 0. Full verify failed with calculated CRCs 0x5FDDE03F/0x16726463, and relinked focused diff stayed CURRENT (2760): no target $f20/$f21 saves, early zero stayed $f16 instead of target $f14, wave scan stayed current a0-bound/v1-loop, and only constants/later call targets shifted in the promoted current-baseline family. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline attach-point grounded-wheel branch-order, late boost-emitter branch-order, or the other recorded func_80049794 probe aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order without stack-byte traffic/frame shrinkage, course-height grouping, first-speed arithmetic, drift-reset condition splitting/nonzero spelling, late-physics float scheduling, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
