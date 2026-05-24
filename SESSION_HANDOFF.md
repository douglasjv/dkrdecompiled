# Session Handoff

- Generated at: 2026-05-24 04:53:18Z
- Branch: `master`
- HEAD: `bf0356b6`
- Completed task: `func_80049794`
- Summary: Rejected promoted func_80049794 selected-wave byte-offset carrier; relinked focused diff regressed to CURRENT (5460).

## Validation

- Probe failed CRCs 0x784EE4A7/0x63167E71; restored source; gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s reported 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Pivot away from func_80049794 selected-wave index/pointer/byte-offset carriers unless paired with a proven save-pressure fix; choose a different routable candidate or a distinct non-wave source-shape hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
