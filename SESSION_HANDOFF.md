# Session Handoff

- Generated at: 2026-05-17 16:18:18Z
- Branch: `master`
- HEAD: `7eb35e08`
- Completed task: `trackbg_render_flashy`
- Summary: Tested a narrow UV-tail additive-double spelling while promoting trackbg_render_flashy: `vCoords[7] = (s16) ((pos.x + pos.x) - var_f16) + var_v1`. It compiled but missed: relinked focused score stayed CURRENT (1808), full verify failed with calculated CRCs 0x93D338FF/0x03D9C8FE, and the visible drift remained in the earlier position-array schedule. Source restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 -U 4 => CURRENT (1808); failed full verify CRCs 0x93D338FF/0x03D9C8FE

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded trackbg_render_flashy vCoords[7] additive-double UV spelling plus prior trackbg_render_flashy position/UV order-carrier probes, func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, and func_80049794 chained-zero/wave-bound/save-family probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
