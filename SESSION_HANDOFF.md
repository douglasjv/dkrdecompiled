# Session Handoff

- Generated at: 2026-05-17 16:56:56Z
- Branch: `master`
- HEAD: `38b7328c`
- Completed task: `func_8008FF1C`
- Summary: Revisited default-skipped func_8008FF1C with a narrow `register s16 temp` lifetime hint for the selected-track halfword carrier. It compiled, but missed: full verify failed with calculated CRCs 0x55C240E7/0x18E4F9B4, focused diff stayed CURRENT (10), and the selected-track load/branch still used v1 instead of target t2. Source restored; final full verify passed. Keep func_8008FF1C parked-by-default but available for a different allocator/lifetime hypothesis.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8008FF1C --format plain --no-pager --max-size 900 -U 6 => CURRENT (10); failed full verify CRCs 0x55C240E7/0x18E4F9B4

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; only revisit default-skipped func_8008FF1C with a new allocator/lifetime idea, and avoid the newly recorded func_8008FF1C register-temp probe plus prior func_8008FF1C temp/selectedTrack probes, func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, func_80049794 chained-zero/wave-bound/save-family probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
