# Session Handoff

- Generated at: 2026-05-23 03:13:00Z
- Branch: `master`
- HEAD: `23184cf6`
- Completed task: `func_80049794`
- Summary: Current-baseline drift flag type probe (`s32 spA2` instead of `s8 spA2`) missed; full verify failed with CRCs 0x37DDDF63/0x9ECDB374 and relinked focused diff worsened to CURRENT (3417). The probe widened the frame to 0x100, shifted stack slots, still lacked $f20/$f21 prologue saves, kept early zero in $f16, and left the wave bound/index allocation reversed as current a0/v1 instead of target v1/a0. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline z-first, y-first, or x/y/z speed magnitude expression orders, current-baseline in-place var_f20 first-speed magnitude spelling, current-baseline segmentXVelocity/segmentZVelocity first-speed component-carrier spelling, current-baseline positive-break wave scan, current-baseline wave-gate condition reorder, current-baseline var_a0/var_v1 declaration-order swap, current-baseline drift_direction integer reset spelling, current-baseline s32 spA2 drift-flag type probe, current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, close save-family explicit-break wave scan, close save-family segmentXVelocity/segmentZVelocity/racerVelocity first-speed carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating recorded expression-order, drift-flag type, or bound-carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
