# Session Handoff

- Generated at: 2026-05-17 15:27:40Z
- Branch: `master`
- HEAD: `2a4cd5a2`
- Completed task: `func_8002B0F4`
- Summary: Tested a bubble-sort bound probe in `func_8002B0F4`: promoted source and hoisted `yOutCount - 1` into the existing `i` local before the outer sort loop, using `for (var_v0 = 0; var_v0 < i; var_v0++)`. It compiled but missed: relinked focused score `CURRENT (3175)` and failed full verify with calculated CRCs `0xAC7CA404/0x71455330`. Source restored; final full verify passed. Keep `func_8002B0F4` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 after relink => CURRENT (3175); failed full verify CRCs 0xAC7CA404/0x71455330

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 sort-limit-hoist probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
