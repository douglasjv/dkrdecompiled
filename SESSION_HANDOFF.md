# Session Handoff

- Generated at: 2026-05-22 19:25:10Z
- Branch: `master`
- HEAD: `8e6c5bc7`
- Completed task: `func_80049794`
- Summary: Rejected close save-family var_f2 z-product carrier; full verify failed with calculated CRCs 0xB8DECACD/0x023D0D27 and relinked focused diff worsened to CURRENT (4640), so source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source): Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_80049794 from close x/z/y save-family evidence only if there is a new source shape that does not repeat recorded wave-bound, wave-threshold, early-zero, or first-speed carrier misses; otherwise pivot to another active candidate such as func_80059208 or trackbg_render_flashy after selector review.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
