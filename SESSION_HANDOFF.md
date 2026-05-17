# Session Handoff

- Generated at: 2026-05-17 14:54:43Z
- Branch: `master`
- HEAD: `82a944c7`
- Completed task: `trackbg_render_flashy`
- Summary: Tested a first-ring position store-order probe in trackbg_render_flashy: promoted source and reordered the first four x/z position assignments to pair target-equivalent values (`x0/z1`, `z0/x1`, `x2/z3`, `z2/x3`) without changing expressions. It compiled but regressed the relinked focused score to CURRENT (4034), and full verify failed with calculated CRCs 0x93E03BFF/0x3B5D2DFE. Source restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 1200 after relink => CURRENT (4034); failed full verify CRCs 0x93E03BFF/0x3B5D2DFE

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded trackbg_render_flashy first-ring store-order grouping.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
