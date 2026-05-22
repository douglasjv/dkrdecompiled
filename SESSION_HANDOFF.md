# Session Handoff

- Generated at: 2026-05-22 16:47:52Z
- Branch: `master`
- HEAD: `5525014f`
- Completed task: `func_8002B0F4`
- Summary: Rejected bottom bubble-sort wave2 next-pointer carrier; source restored after evidence capture.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore; rejected promoted probe failed with calculated CRCs 0x7D23AFD2/0x75CB7537 and ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 100 => relinked CURRENT (5200).

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate; func_80049794 remains selector-recommended but saturated, so inspect ACTIVE.md before choosing whether to continue it or a narrower active target.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
