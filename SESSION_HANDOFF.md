# Session Handoff

- Generated at: 2026-05-23 03:29:08Z
- Branch: `master`
- HEAD: `64a8c779`
- Completed task: `func_80049794`
- Summary: Current-baseline wave-count carrier spelling (`var_v0 = gRacerWaveCount; var_v1 = var_v0 - 1; for (var_a0 = var_v1; ...)`) missed; full verify failed with CRCs 0xC88B59B4/0xF77ED7E9 and relinked focused diff worsened to CURRENT (6185). The probe still lacked target $f20/$f21 prologue saves, kept early zero in $f16 instead of target $f14, inserted spA2 stack-byte traffic, and shifted the wave scan into current v1-count/a0-bound/v0-loop order rather than target v0-count/v1-bound/a0-loop order. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline var_v0 wave-count carrier, post-scan wave-index increment spelling, explicit-subtract wave speed spelling, spEC/spCC first-speed carriers, z-first, y-first, or x/y/z speed magnitude expression orders, current-baseline in-place var_f20 first-speed magnitude spelling, current-baseline segmentXVelocity/segmentZVelocity first-speed component-carrier spelling, current-baseline positive-break wave scan, current-baseline wave-gate condition reorder, current-baseline var_a0/var_v1 declaration-order swap, current-baseline drift_direction integer reset spelling, current-baseline s32 spA2 drift-flag type probe, current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, close save-family explicit-break wave scan, close save-family segmentXVelocity/segmentZVelocity/racerVelocity first-speed carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating recorded expression-order, wave-speed spelling, first-speed carrier, drift-flag type, count/bound-carrier aliases, or drift-flag stack-byte shapes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
