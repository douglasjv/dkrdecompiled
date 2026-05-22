# Session Handoff

- Generated at: 2026-05-22 15:29:28Z
- Branch: `master`
- HEAD: `b2f68874`
- Completed task: `func_8002B0F4`
- Summary: Rejected early sp108 return-split spelling; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted func_8002B0F4 early sp108 return-split spelling with calculated CRCs 0x701EEB7B/0xA3DBFC65; ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (3535) with bnez/inserted-return branch drift; restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_8002B0F4, do not repeat the early sp108 return-split spelling; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
