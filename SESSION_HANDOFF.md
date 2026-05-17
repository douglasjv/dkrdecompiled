# Session Handoff

- Generated at: 2026-05-17 15:11:01Z
- Branch: `master`
- HEAD: `4a426fdb`
- Completed task: `trackbg_render_flashy`
- Summary: Tested a single-site outer-ring subtract-chain probe in `trackbg_render_flashy`: promoted source and rewrote only `zPositions[5]` from `scaledXSin - (2.0f * scaledXCos)` to `scaledXSin - scaledXCos - scaledXCos`. It compiled but worsened the focused score from baseline `CURRENT (1808)` to `CURRENT (4558)`, failed full verify with calculated CRCs `0xD68DF16F/0x5A429915`, and shifted the outer-ring position store schedule much earlier. Source restored; final full verify passed. Keep `trackbg_render_flashy` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 1200 after relink => CURRENT (4558), baseline CURRENT (1808); failed full verify CRCs 0xD68DF16F/0x5A429915

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded trackbg_render_flashy zPositions[5] subtract-chain probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
