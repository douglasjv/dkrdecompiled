# Session Handoff

- Generated at: 2026-05-24 00:05:40Z
- Branch: `master`
- HEAD: `e795ffdf`
- Completed task: `func_8002B0F4`
- Summary: Rejected bottom func_800BB2F4 rot address spelling; restored GLOBAL_ASM baseline

## Validation

- probe failed gmake -j4 CROSS=tools/binutils/mips64-elf- CRC 0x7A567F98/0xC658B8F4; relinked ./diff.sh func_8002B0F4 CURRENT (4298); restored gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4: pivot away from bottom address/store-order families; inspect outer segment/grid model-spill family or select another bounded active candidate if no fresh hypothesis`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
