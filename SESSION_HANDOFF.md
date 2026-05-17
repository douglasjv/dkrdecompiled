# Session Handoff

- Generated at: 2026-05-17 13:26:17Z
- Branch: `master`
- HEAD: `a378d098`
- Completed task: `trackbg_render_flashy`
- Summary: Tested an outer-ring assignment-order probe on promoted trackbg_render_flashy, moving `xPositions[5]`, `zPositions[6]`, and `zPositions[7]` earlier to mimic the target store order. It compiled but worsened focused diff to CURRENT (2786), failed full verify with calculated CRCs 0xDC7DB491/0xB2CAADCB, and increased early float-register drift. Source guard/body restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 720` => relinked focused CURRENT (2786)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded trackbg_render_flashy outer-ring assignment-order probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
