# Session Handoff

- Generated at: 2026-05-22 15:37:11Z
- Branch: `master`
- HEAD: `8295bc93`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected single-pair x2/z3 first-ring store-order probe; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted trackbg_render_flashy single-pair x2/z3 first-ring store-order probe with calculated CRCs 0xDC9ABB91/0xDA2977C2; ./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (4433), shifted early first-ring/outer-ring float schedule; restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For trackbg_render_flashy, do not repeat the single-pair x2/z3 first-ring store-order probe; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
