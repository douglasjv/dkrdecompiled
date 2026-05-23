# Session Handoff

- Generated at: 2026-05-23T04:20:41Z
- Branch: `master`
- HEAD: `06938c84`
- Completed task: `func_80049794`
- Summary: Current-baseline `ABSF` spelling for both absolute-velocity temporaries (`var_f14 = ABSF(racer->velocity); var_f0 = ABSF(racer->velocity)`) missed; full verify failed with calculated CRCs 0x40ED9F86/0xDE608AA0 and relinked focused diff worsened to CURRENT (4250). The probe still lacked target $f20/$f21 prologue saves, kept early zero in $f16 instead of target $f14, and left the wave loop reversed as current a0-bound/v1-loop instead of target v1-bound/a0-loop. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline ABSF absolute-velocity spelling, current-baseline nested course-height guard spelling, current-baseline existing-var_f0 first-speed accumulator spelling, current-baseline wave-reset constant-left condition spelling, current-baseline register var_f2 allocation hint, current-baseline selected-wave pointer cache, current-baseline course-height range-guard order, current-baseline existing-spD0 early-zero carrier, current-baseline existing-var_f6 first-speed carrier, current-baseline grouped course-height subtraction spelling, current-baseline first-speed upper-clamp operand-order spelling, boss-branch polarity spelling, wave-speed lower-clamp operand-order spelling, first-speed 2.0f subtract spelling, grouped z/y first-speed expression, selected-wave index carrier, var_v0 wave-count carrier, post-scan wave-index increment spelling, explicit-subtract wave speed spelling, spEC/spCC first-speed carriers, z-first, y-first, or x/y/z speed magnitude expression orders, current-baseline in-place var_f20 first-speed magnitude spelling, current-baseline segmentXVelocity/segmentZVelocity first-speed component-carrier spelling, current-baseline positive-break wave scan, current-baseline wave-gate condition reorder, current-baseline var_a0/var_v1 declaration-order swap, current-baseline drift_direction integer reset spelling, current-baseline s32 spA2 drift-flag type probe, current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, close save-family explicit-break wave scan, close save-family segmentXVelocity/segmentZVelocity/racerVelocity first-speed carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order, course-height grouping, or first-speed arithmetic without repeating recorded expression-order, accumulator-shape, absolute-velocity macro spelling, upper-clamp operand-order, branch-polarity, constant-spelling, wave-reset condition aliases, wave-speed spelling, lower-clamp operand-order, first-speed carrier, drift-flag type, count/bound-carrier aliases, selected-wave pointer/index aliases, grouped first-speed aliases, current-baseline register-allocation aliases, early-zero carrier aliases, course-height guard-order aliases, or drift-flag stack-byte shapes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
