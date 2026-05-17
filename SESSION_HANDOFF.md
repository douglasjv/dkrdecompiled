# Session Handoff

- Generated at: 2026-05-17 13:33:07Z
- Branch: `master`
- HEAD: `c39e7a52`
- Completed task: `func_8002B0F4`
- Summary: Tested a pad3-removal plus post-call coordinate-hoist probe in func_8002B0F4: promoted source, removed dead `pad3`, kept the original `get_inside_segment_count_xz(xIn, zIn, spB0)` call shape, and moved `XInInt = xIn; ZInInt = zIn;` out of the per-segment loop to just after `yOutCount = 0`. It compiled but failed full verify with calculated CRCs 0x785671AA/0x0D6F6A4A, regressed relinked focused diff to CURRENT (2853), and preserved the unwanted early `gCurrentLevelModel` spill at `0x64(sp)`. Source guard/body restored; final full verify passed. Keep func_8002B0F4 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 520` => relinked focused CURRENT (2853)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 pad3-removal plus post-call coordinate-hoist probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
