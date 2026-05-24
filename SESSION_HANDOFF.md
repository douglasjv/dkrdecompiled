# Session Handoff

- Generated at: 2026-05-24 03:17:57Z
- Branch: `master`
- HEAD: post-closeout commit; run `git log -1 --oneline`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected worker negative-cosine carrier probe: promoted source with a new negScaledXCos local for first/outer negative-cosine position expressions failed CRCs 0xDC79FC91/0xA51F89F4 and worsened relinked focused diff to CURRENT (3382); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; prefer func_80049794 or a distinct active-candidate hypothesis, and for trackbg_render_flashy avoid new local/storage negative-cosine carriers; next trackbg hypothesis should preserve stack layout and target neg.s FPR allocation.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
