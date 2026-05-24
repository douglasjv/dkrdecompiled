# Session Handoff

- Generated at: 2026-05-24 02:17:16Z
- Branch: `master`
- HEAD: `8423cfa0`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted collision-plane scalar-local probe; full verify failed with baseline CRCs 0x7856718A/0x66208CAA and relinked focused diff stayed CURRENT (2860), then source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; keep func_8002B0F4 routable only with a fresh hypothesis that attacks the early gCurrentLevelModel spill/register family rather than plane local spelling, or pivot to another active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
