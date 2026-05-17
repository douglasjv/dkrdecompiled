# Session Handoff

- Generated at: 2026-05-17 14:06:51Z
- Branch: `master`
- HEAD: `3b2c64a8`
- Completed task: `func_80049794`
- Summary: Tested a save-family wave-threshold carrier in func_80049794: promoted source on the close chained-zero/x/z/y/steer-noop branch and carried `obj->trans.y_position + 5.0f` through existing `var_f0` before the wave scan. It kept the target 0xf8 frame and $f20/$f21 saves, but regressed the relinked focused diff to CURRENT (7555), shifted the wave block into worse a0/v1/f12/f14 register churn with extra stack traffic, and full verify failed with calculated CRCs 0x2B7A77D5/0x5B507890. Source guard/body restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 900 => relinked focused CURRENT (7555); failed full verify CRCs 0x2B7A77D5/0x5B507890

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80049794 var_f0 wave-threshold carrier.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
