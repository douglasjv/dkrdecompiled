# Session Handoff

- Generated at: 2026-05-17 14:20:41Z
- Branch: `master`
- HEAD: `b915d413`
- Completed task: `trackbg_render_flashy`
- Summary: Tested a narrow doubled-cosine carrier in trackbg_render_flashy: promoted source, assigned `pad_sp108 = scaledXCos + scaledXCos`, and used that existing local for the outer-ring `zPositions[5-8]` doubled-cosine terms. It compiled but produced no focused improvement from the promoted baseline: relinked focused diff stayed CURRENT (1808), and full verify failed with calculated CRCs 0x93D338FF/0x03D9C8FE, matching the broader additive-double family. Source guard/body restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 => relinked focused CURRENT (1808); failed full verify CRCs 0x93D338FF/0x03D9C8FE

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded trackbg_render_flashy pad_sp108 double-cosine carrier.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
