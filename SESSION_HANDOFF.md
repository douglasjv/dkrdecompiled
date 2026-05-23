# Session Handoff

- Generated at: 2026-05-23 22:58:20Z
- Branch: `master`
- HEAD: `52e293d8`
- Completed task: `func_80049794`
- Summary: Horizontal steer-rate operand-order probe missed: changing the steerAngle update to updateRateF * var_v0 / var_f2 produced the promoted-baseline CRCs 0x5FDDE03F/0xEF7A0514 and relinked ./diff.sh func_80049794 stayed CURRENT (2760); source restored.

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
- Step: Continue with another bounded unrecorded source-shape probe; do not repeat horizontal steer-rate operand-order, vertical stick-rate grouping, throttle/brake rate operand-order, or prior transform/store/cast probes. Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
