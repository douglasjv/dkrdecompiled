# Session Handoff

- Generated at: 2026-05-23 22:27:35Z
- Branch: `master`
- HEAD: `935841d6`
- Completed task: `func_80049794`
- Summary: Recorded first-speed suffix single-precision miss: changing only the initial sqrtf speed expression suffix from - 2.0 to - 2.0f failed full verify with CRCs 0x12F152B3/0x7EB3E947; relinked focused diff regressed to CURRENT (4560), still missing target f20/f21 saves, keeping early zero in f16 instead of f14, and leaving wave scan in the current a0/v1 family while widening later gravity/buoyancy scheduling.

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
