# Session Handoff

- Generated at: 2026-05-17 14:34:44Z
- Branch: `master`
- HEAD: `40bd7739`
- Completed task: `func_8002B0F4`
- Summary: Tested a narrow declaration-only probe in func_8002B0F4: promoted source and removed the unused `WaterProperties *wave2` local. It compiled but collapsed into the same failed family as plain pad3 removal: relinked focused CURRENT (2868), early `gCurrentLevelModel` spill still present, and full verify failed with calculated CRCs 0x785671AA/0x0D6F6A4A. Source restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 => relinked focused CURRENT (2868); failed full verify CRCs 0x785671AA/0x0D6F6A4A

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 unused-wave2 declaration probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
