# Session Handoff

- Generated at: 2026-05-23 06:38:42Z
- Branch: `master`
- HEAD: `9cd1155d`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline explicit exitObj pointer-test spelling: if (racer->exitObj != NULL). Object-only diff first showed stale CURRENT (0), full verify failed with promoted-baseline CRCs 0x5FDDE03F/0xEF7A0514, and relinked diff stayed CURRENT (2760): no target $f20/$f21 saves, GPR save slots shifted down, early zero stayed $f16, wave scan current a0-bound/v1-loop. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline explicit exitObj pointer-test, trick divisor branch-polarity, later vehicleID upper-guard operand-order, first-speed boss guard operand-order, drift-direction nonzero spelling, split drift-reset condition, wave-lift divided-speed grouping, wave-lift single-precision literal spelling, trailing pad3/pad4 removal, explicit first-compare/do-loop wave scan, split wave-bound spelling, course-height upper-cap compare-order spelling, course-height buoyancy subtract spelling, wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound/course-height aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order without stack-byte traffic/frame shrinkage, course-height grouping, first-speed arithmetic, drift-reset condition splitting/nonzero spelling, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
