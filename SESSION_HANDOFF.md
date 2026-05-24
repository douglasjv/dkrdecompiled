# Session Handoff

- Generated at: 2026-05-24 03:52:50Z
- Branch: `master`
- HEAD: `eee1bf07`
- Completed task: `func_80059208-final-vertical-and-func_80049794-wave-while`
- Summary: Rejected two promoted probes: func_80059208 final vertical negation spelling failed verify with CRCs 0x53D45BB5/0x11D3A734 and focused CURRENT (1125); func_80049794 wave-scan while/threshold carrier failed verify with CRCs 0xC81C158F/0x7475EA56 and focused CURRENT (6105). Sources restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.29%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended, but do not repeat wave-scan while/threshold-carrier promotion, final-vertical negation in func_80059208, or prior direct/object-only promotion families without a distinct allocation hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
