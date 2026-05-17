# Session Handoff

- Generated at: 2026-05-17 13:35:39Z
- Branch: `master`
- HEAD: `4074f1fd`
- Completed task: `trackbg_render_flashy`
- Summary: Tested a first-ring positive-sum carrier in trackbg_render_flashy: promoted source and routed only the duplicated `scaledXCos + scaledXSin` value through existing `pad_sp108` for `xPositions[2]` and `zPositions[3]`. It compiled but collapsed into the bad frame-shrink family: frame `0x150`, relinked focused diff CURRENT (13456), and full verify failed with calculated CRCs 0x218EDFFA/0xDD1EF586. Source guard/body restored; final full verify passed. Keep trackbg_render_flashy active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 720` => relinked focused CURRENT (13456)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded trackbg_render_flashy existing-pad_sp108 positive-sum carrier.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
