# Session Handoff

- Generated at: 2026-05-23 22:30:12Z
- Branch: `master`
- HEAD: `9b33af54`
- Completed task: `func_80049794`
- Summary: Recorded normal-flight side-force guard condition-order miss: changing only the guard to test racer->groundedWheels == 0 before the R_TRIG input test failed full verify with CRCs 0x605DE9ED/0x38B1F9D8; relinked focused diff stayed CURRENT (2760), so it remained in the promoted-baseline family with f20/f21 saves absent, early zero in f16, and wave a0/v1 drift unchanged.

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
