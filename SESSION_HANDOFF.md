# Session Handoff

- Generated at: 2026-05-17 16:12:18Z
- Branch: `master`
- HEAD: `5d1df0a4`
- Completed task: `func_80059208`
- Summary: Tested a final lateral negative-divisor spelling while promoting func_80059208: diffX = (pad + pad2) / -divisor. It compiled but missed: relinked focused score worsened to CURRENT (1295), full verify failed with calculated CRCs 0x53B0B9DF/0x4E71FC94, and the target post-division negation became a divisor-negation family with shifted final vertical registers. Source restored; final full verify passed. Keep func_80059208 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 4 => CURRENT (1295); failed full verify CRCs 0x53B0B9DF/0x4E71FC94

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80059208 final lateral negative-divisor spelling plus prior func_80059208 final-offset variants, func_80049794 chained-zero/wave-bound/save-family probes, func_8002B0F4 pad/early-conversion/loop probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
