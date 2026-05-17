# Session Handoff

- Generated at: 2026-05-17 15:58:54Z
- Branch: `master`
- HEAD: `77ba50a5`
- Completed task: `func_8002B0F4`
- Summary: Tested a direct-cast call-shape probe while promoting func_8002B0F4: get_inside_segment_count_xz((s32) xIn, (s32) zIn, spB0) without hoisting XInInt/ZInInt locals. It compiled but recreated the early-conversion miss: relinked focused score CURRENT (2860), full verify failed with calculated CRCs 0x7856718A/0x66208CAA, and the diff still showed the unwanted early gCurrentLevelModel spill at 0x60(sp). Source restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 4 after relink => CURRENT (2860); failed full verify CRCs 0x7856718A/0x66208CAA

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_8002B0F4 direct-cast get_inside_segment_count_xz call-shape probe plus prior func_8002B0F4 pad/early-conversion/loop probes, trackbg_render_flashy order/carrier probes, func_80059208 final-offset variants, and func_80049794 chained-zero/wave-bound families.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
