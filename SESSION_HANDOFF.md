# Session Handoff

- Generated at: 2026-05-24 03:20:18Z
- Branch: `master`
- HEAD: post-closeout commit; run `git log -1 --oneline`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected grouped first-ring negative-sum spelling: promoted source changed xPositions[0] to -((xSin * 1280.0f) + scaledXCos); full gate failed CRCs 0xD6EC5F94/0xFD1467AB and relinked focused diff worsened to CURRENT (10447); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid trackbg_render_flashy new-local negative-cosine carriers and single-site grouped first-ring negative-sum spelling; only continue trackbg if the next hypothesis preserves the 0x158 frame and existing stack layout.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
