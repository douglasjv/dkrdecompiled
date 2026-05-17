# Session Handoff

- Generated at: 2026-05-17 16:07:11Z
- Branch: `master`
- HEAD: `afa48048`
- Completed task: `func_80049794`
- Summary: Tested a narrow early-zero timing probe while promoting func_80049794: inserted var_f14 = 0.0f after grounded-wheel unk84/unk88 zeroing and before the spinout check. It compiled but missed with the current baseline CRC family 0x5FDDE03F/0xEF7A0514; focused diff stayed CURRENT (2430), still lacked target f20/f21 prologue saves, and kept the early zero in f16 instead of target f14. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 4 => CURRENT (2430); failed full verify CRCs 0x5FDDE03F/0xEF7A0514

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80049794 pre-spinout var_f14 zero timing probe plus prior func_80049794 chained-zero/wave-bound/save-family probes, func_80059208 final-offset variants, func_8002B0F4 pad/early-conversion/loop probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
