# Session Handoff

- Generated at: 2026-05-24 03:23:43Z
- Branch: `master`
- HEAD: post-closeout commit; run `git log -1 --oneline`
- Completed task: `func_8002B0F4`
- Summary: Rejected scaled collision-plane index local: promoted source stored basePlaneIndex * 4 in temp and indexed collisionPlanes[temp + n]; full gate failed CRCs 0x7E74218A/0xA93D6001 and relinked focused diff improved to CURRENT (2725) but still retained the early gCurrentLevelModel spill at 0x60(sp); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_8002B0F4 scaled collision-plane index local was a useful miss (CURRENT 2725) but still needs a separate fix for the early gCurrentLevelModel spill/register family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
