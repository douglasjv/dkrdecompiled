# Session Handoff

- Generated at: 2026-05-24 03:29:28Z
- Branch: `master`
- HEAD: post-closeout commit; run `git log -1 --oneline`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected single-site x2 scaled-sine left-operand spelling: promoted source changed xPositions[2] to scaledXSin + scaledXCos; full gate failed CRCs 0x218F9FFA/0x18F4A6D6 and relinked focused diff regressed to CURRENT (12478) with frame shrunk to 0x150 and broad early position-array/UV scheduling drift; source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; trackbg_render_flashy remains active but do not repeat single-site x2 scaled-sine left-operand spelling, which collapsed into the known bad frame-shrink family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
