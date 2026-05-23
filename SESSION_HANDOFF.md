# Session Handoff

- Generated at: 2026-05-23 23:10:56Z
- Branch: `master`
- HEAD: `8d5045b9`
- Completed task: `func_80049794`
- Summary: Recorded current-baseline `spA3` `s32` type miss; restored source passes Verify: OK

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source: Verify: OK; rejected probe CRCs 0x8FDDDF9D/0x16677070, diff CURRENT (4010))

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
- Step: Continue with another bounded unrecorded source-shape probe; do not repeat the `spA3` `s32` type probe, zipper fallback damping single-precision literal, `spA3` boolean guard spelling, horizontal steer-rate divide-before-multiply, horizontal steer-rate operand-order, vertical stick-rate grouping, throttle/brake rate operand-order, or prior transform/store/cast probes. Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
