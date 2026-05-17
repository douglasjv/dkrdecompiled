# Session Handoff

- Generated at: 2026-05-17 14:14:21Z
- Branch: `master`
- HEAD: `17759ca6`
- Completed task: `func_8002B0F4`
- Summary: Tested the intact-pad3 early-coordinate call shape in func_8002B0F4: promoted source, moved `XInInt = xIn; ZInInt = zIn;` before `get_inside_segment_count_xz`, passed those integer locals to the call, and removed the duplicate per-segment conversions. It matched the target prologue conversion/call shape but still inserted the unwanted pre-loop `gCurrentLevelModel` spill, regressed the relinked focused diff to CURRENT (2860), and full verify failed with calculated CRCs 0x7856718A/0x66208CAA. Source guard/body restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 760 => relinked focused CURRENT (2860); failed full verify CRCs 0x7856718A/0x66208CAA

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 intact-pad3 early-coordinate call shape.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
