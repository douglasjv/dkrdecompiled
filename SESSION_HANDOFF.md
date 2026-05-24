# Session Handoff

- Generated at: 2026-05-24 04:57:04Z
- Branch: `master`
- HEAD: `33a24a09`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted func_8002B0F4 sp108 > 7 early guard spelling; focused diff stayed at CURRENT (2860).

## Validation

- Probe failed CRCs 0x7856718A/0x66208CAA; restored source; gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s reported 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Pivot away from func_8002B0F4 early sp108 guard spellings and plain promotion; choose a distinct model-spill/register-family hypothesis or another routable candidate.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
