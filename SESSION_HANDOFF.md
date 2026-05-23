# Session Handoff

- Generated at: 2026-05-23 08:09:55Z
- Branch: `master`
- HEAD: `aa925365`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline brake lower-clamp zero literal spelling: changed racer->brake < 0.0f / racer->brake = 0.0f to racer->brake < 0 / racer->brake = 0. Full verify failed with calculated CRCs 0xDDB58EAF/0x090C564F, and relinked focused diff regressed to CURRENT (4835): no target $f20/$f21 saves, early zero stayed $f16 instead of target $f14, wave scan stayed current a0-bound/v1-loop, and later gravity/buoyancy float-register scheduling widened. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline brake lower-clamp zero literal, A-button throttle clamp literal, low-speed drag multiply grouping, low-speed drag condition-order, vertical drag scale grouping, lateral drag scale grouping, trick lift scale constant-grouping, brake negative-velocity double-zero, forwardVel damping sum-order, grounded stick-scale operand-order, boost non-positive-first branch-order, implicit wave-count gate, terminal wave-bound inverted empty-if, wave-height upper-reset constant-left compare, direct selected-wave height subtraction, buoyancy single-precision nonzero guard, gravity else-if spelling, 5.5f gravity literal, OBJ_EMIT_9 store-before-5.5 gravity assignment, grouped x/y or grouped z/y first-speed expression, throttle-rate single-precision literal, brake direct dataflow, exit-throttle direct dataflow, opening update-rate single-precision multiplier, exit-throttle single-precision literal, explicit exitObj pointer-test, trick divisor branch-polarity, later vehicleID upper-guard operand-order, first-speed boss guard operand-order, drift-direction nonzero spelling, split drift-reset condition, wave-lift divided-speed grouping, wave-lift single-precision literal spelling, trailing pad3/pad4 removal, explicit first-compare/do-loop wave scan, split wave-bound spelling, selected-wave pointer/index cache, course-height upper-cap compare-order spelling, course-height buoyancy subtract spelling, wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound/course-height aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order without stack-byte traffic/frame shrinkage, course-height grouping, first-speed arithmetic, drift-reset condition splitting/nonzero spelling, late-physics float scheduling, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
