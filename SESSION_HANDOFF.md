# Session Handoff

- Generated at: 2026-05-22 14:58:58Z
- Branch: `master`
- HEAD: `82e1f5d9`
- Completed task: `func_80049794`
- Summary: Tested a fresh x/z/y save-family preserve probe using existing var_f6 across apply_vehicle_rotation_offset. It compiled and lowered the relinked focused diff to CURRENT (3310), but full verify failed with calculated CRCs 0xF40EF8A9/0xF04AE6F7; source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => failed for promoted func_80049794 var_f6 preserve probe, calculated CRCs 0xF40EF8A9/0xF04AE6F7
- ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (3310)
- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_80049794, avoid the newly recorded var_f6 preserve spelling; it improved to CURRENT (3310) but used the wrong 0x78(sp) stack path instead of target f14 save/reload at 0xdc(sp), and wave a0/v1 drift remains. For func_80059208, func_8002B0F4, and trackbg_render_flashy, use ACTIVE.md before choosing a probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
