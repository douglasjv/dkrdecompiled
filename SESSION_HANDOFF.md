# Session Handoff

- Generated at: 2026-05-17 14:51:35Z
- Branch: `master`
- HEAD: `dffbde88`
- Completed task: `func_80059208`
- Summary: Tested a narrow final object-dot multiply-order probe in func_80059208: promoted source and commuted only the x-position product from `splinePos * diffX` to `diffX * splinePos`, leaving the z product and checkpoint-dot shape intact. It compiled but regressed the relinked focused score from baseline CURRENT (870) to CURRENT (875), and full verify failed with calculated CRCs 0x53D0C1DF/0xC593C532. Source restored; final full verify passed. Keep func_80059208 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80059208 --format plain --no-pager --max-size 900 after relink => CURRENT (875); failed full verify CRCs 0x53D0C1DF/0xC593C532

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80059208 final object-dot x-multiply commute.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
