# Session Handoff

- Generated at: 2026-05-17 13:18:42Z
- Branch: `master`
- HEAD: `01ceda9a`
- Completed task: `func_8002B0F4`
- Summary: Tested a scalar plane-carrier variant on promoted func_8002B0F4 with the dead pad3 removed (`planeX`/`planeY`/`planeZ`/`planeW` replacing `Vec4f tempVec4f`). It compiled but regressed the relinked focused score to CURRENT (2868), failed full verify with calculated CRCs 0x785671AA/0x0D6F6A4A, and still showed the unwanted pre-loop gCurrentLevelModel spill to 0x64(sp). Source guard/body restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900` => relinked focused CURRENT (2868)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4 or func_80059208; keep close functions active and avoid the recorded func_8002B0F4 scalar plane-carrier probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
