# Session Handoff

- Generated at: 2026-05-23 01:50:05Z
- Branch: `master`
- HEAD: `97104733`
- Completed task: `func_80049794`
- Summary: Promoted func_80049794 and tested a current-baseline top-speed multiply regrouping, var_f14 = var_f14 * (handle_racer_top_speed(obj, racer) * 1.8). Full verify failed with calculated CRCs 0xAC61AD1B/0xFE0F8158; relinked ./diff.sh func_80049794 stayed CURRENT (2760) with missing target f20/f21 saves, early zero in f16, and the known wave a0/v1 drift. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but avoid repeating the now-rejected current-baseline top-speed regrouping and saturated early-zero/wave families. If staying on func_80049794, prefer a fresh x/z/y save-family or wave-register hypothesis from ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
