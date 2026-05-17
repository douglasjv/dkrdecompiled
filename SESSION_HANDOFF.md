# Session Handoff

- Generated at: 2026-05-17 16:52:36Z
- Branch: `master`
- HEAD: `a3a394ec`
- Completed task: `func_8002B0F4`
- Summary: Tested declaration-only `register s32 XInInt` / `register s32 ZInInt` hints in func_8002B0F4. It compiled, but missed: full verify failed with calculated CRCs 0x7856718A/0x66208CAA, focused diff worsened to CURRENT (2860), and the diff introduced the known early gCurrentLevelModel spill at 0x60(sp) with broad grid-loop integer-register churn. Source restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 1000 -U 6 => CURRENT (2860); failed full verify CRCs 0x7856718A/0x66208CAA

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_8002B0F4 X/Z integer register-hint probe plus prior func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, func_80049794 chained-zero/wave-bound/save-family probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
