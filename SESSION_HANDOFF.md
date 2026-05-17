# Session Handoff

- Generated at: 2026-05-17 15:53:53Z
- Branch: `master`
- HEAD: `5f727b1b`
- Completed task: `trackbg_render_flashy`
- Summary: Tested an exact outer-ring x5/z5/z6/x6 store-order probe while promoting trackbg_render_flashy. It compiled but missed: relinked focused score CURRENT (3043), full verify failed with calculated CRCs 0xDC7DFA91/0xC168DB3D, and the early position-array float-register schedule shifted rather than matching. Source restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 -U 4 after relink => CURRENT (3043); failed full verify CRCs 0xDC7DFA91/0xC168DB3D

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded trackbg_render_flashy exact x5/z5/z6/x6 outer-order probe plus prior func_8002B0F4 pad removals, func_80059208 positive-numerator variants, and func_80049794 chained-zero/wave-bound families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
