# Session Handoff

- Generated at: 2026-05-23 23:41:21Z
- Branch: `master`
- HEAD: `d8b0f9d6`
- Completed task: `func_8002B0F4`
- Summary: Recorded current-source surface-skip inverted empty-if miss; restored source passes Verify: OK

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source: Verify: OK; rejected probe CRCs 0x77D9E18A/0xB9F696E2, diff CURRENT (2995))

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 or next selector-recommended bounded packet`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
