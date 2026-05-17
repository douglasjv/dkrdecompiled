# Session Handoff

- Generated at: 2026-05-17 16:37:12Z
- Branch: `master`
- HEAD: `8ba94d96`
- Completed task: `func_80049794`
- Summary: Tested a close save-family continuation for func_80049794: x/z/y pre-sqrt accumulation, steer-vel no-op, chained grounded-wheel zero, removed trailing pad3/pad4, plus a new while/break wave scan using var_v1 as the saved bound and var_a0 as the loop index. It compiled and kept the target 0xf8 frame plus $f20/$f21 saves, but missed badly: relinked focused score worsened to CURRENT (11495), full verify failed with calculated CRCs 0xE586A191/0x17A5E745, and the wave block shifted into a broad a3/v1/a0 register family with downstream scheduling churn. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 1200 -U 4 => CURRENT (11495); failed full verify CRCs 0xE586A191/0x17A5E745

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80049794 close-branch while/break wave-scan spelling plus prior chained-zero/wave-bound/save-family probes, func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
