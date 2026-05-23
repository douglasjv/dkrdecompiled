# Session Handoff

- Generated at: 2026-05-23 03:25:42Z
- Branch: `master`
- HEAD: `406be74f`
- Completed task: `func_80049794`
- Summary: Current-baseline post-scan wave-index increment spelling (`var_a0++` then `gRacerCurrentWave[var_a0]`) missed; full verify failed with CRCs 0x6763F03F/0xAFC9BBAD and relinked focused diff was CURRENT (3315). The probe still lacked target $f20/$f21 prologue saves, kept early zero in $f16 instead of target $f14, shifted the wave scan into an a1/v1/a0-style register family rather than target v1/a0 bound/index allocation, and inserted post-scan pointer/index adjustment drift. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restoring source)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline post-scan wave-index increment spelling, explicit-subtract wave speed spelling, spEC/spCC first-speed carriers, z-first, y-first, or x/y/z speed magnitude expression orders, current-baseline in-place var_f20 first-speed magnitude spelling, current-baseline segmentXVelocity/segmentZVelocity first-speed component-carrier spelling, current-baseline positive-break wave scan, current-baseline wave-gate condition reorder, current-baseline var_a0/var_v1 declaration-order swap, current-baseline drift_direction integer reset spelling, current-baseline s32 spA2 drift-flag type probe, current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, close save-family explicit-break wave scan, close save-family segmentXVelocity/segmentZVelocity/racerVelocity first-speed carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating recorded expression-order, wave-speed spelling, first-speed carrier, drift-flag type, or bound-carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
