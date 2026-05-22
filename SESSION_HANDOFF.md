# Session Handoff

- Generated at: 2026-05-22 15:06:00Z
- Branch: `master`
- HEAD: `5747052d`
- Completed task: `func_80049794`
- Summary: Tested current-baseline explicit var_t1 PLAYER_COMPUTER allocation reused for the early wave gate and trickType -1 check; it created the early li t1,-1 shape but widened the frame, missed with relinked CURRENT (2879), failed CRCs 0x5FDDDF87/0x4196D76A, source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => failed for promoted explicit var_t1 PLAYER_COMPUTER allocation probe, calculated CRCs 0x5FDDDF87/0x4196D76A
- ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (2879)
- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_80049794, avoid the newly recorded standalone var_t1 PLAYER_COMPUTER allocation probe; it created early li t1,-1 but widened the frame to 0x100, still lacked f20/f21 saves, kept early f16 zero, and left wave a0/v1 drift. For func_80059208, func_8002B0F4, and trackbg_render_flashy, use ACTIVE.md before choosing a probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
