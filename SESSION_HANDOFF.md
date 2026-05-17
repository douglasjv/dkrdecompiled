# Session Handoff

- Generated at: 2026-05-17 16:31:51Z
- Branch: `master`
- HEAD: `eaed9793`
- Completed task: `func_8002B0F4`
- Summary: Tested rewriting the bottom gTrackWaves population loop from the existing backslash-preserved for into an explicit while (var_v0 < yOutCount) while promoting func_8002B0F4. It compiled but missed: relinked focused score worsened to CURRENT (3080), full verify failed with calculated CRCs 0x7856718A/0x4AA98304, and the diff shifted the bottom pointer-population/unrolled-copy schedule while preserving the early gCurrentLevelModel spill family. Source restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 1200 -U 4 => CURRENT (3080); failed full verify CRCs 0x7856718A/0x4AA98304

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_8002B0F4 bottom population-loop while spelling plus prior func_8002B0F4 pad/early-conversion/loop probes, func_80049794 chained-zero/wave-bound/save-family probes, func_80059208 final-offset variants, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
