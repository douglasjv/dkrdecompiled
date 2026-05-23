# Session Handoff

- Generated at: 2026-05-23 22:54:25Z
- Branch: `master`
- HEAD: `56cfc8a6`
- Completed task: `func_80049794`
- Summary: Vertical stick-rate grouping probe missed: changing unk1E8 update to var_v0 * (updateRateF * 0.0625) failed full verify with calculated CRCs 0x4B47F76E/0xEC3D5C69 and relinked ./diff.sh func_80049794 regressed to CURRENT (7755); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source: Verify: OK)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
