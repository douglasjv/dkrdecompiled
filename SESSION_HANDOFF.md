# Session Handoff

- Generated at: 2026-05-17 13:59:10Z
- Branch: `master`
- HEAD: `23dd7f0d`
- Completed task: `func_8002B0F4`
- Summary: Tested a narrower standalone Z grid mask loop unroll in func_8002B0F4: promoted source and rewrote the Z-axis mask loop as a two-iteration `i += 4` loop with four explicit checks per body. It compiled and preserved the target prologue, but regressed the relinked focused diff to CURRENT (3325), introduced the unwanted early gCurrentLevelModel spill family before the segment loop, and full verify failed with calculated CRCs 0x7856718A/0xC40F5151. Source guard/body restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 760 => relinked focused CURRENT (3325)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 two-iteration Z-loop unroll.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
