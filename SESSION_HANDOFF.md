# Session Handoff

- Generated at: 2026-05-17 14:58:03Z
- Branch: `master`
- HEAD: `3294463f`
- Completed task: `func_8002B0F4`
- Summary: Tested a declaration-only stack-shape probe in `func_8002B0F4`: promoted source and removed unused `pad2`. It compiled but worsened the relinked focused score to `CURRENT (2878)`, shifted the `spB0`/inside-segment output from target `0xb0(sp)` to `0xb4(sp)`, preserved the early `gCurrentLevelModel` spill at `0x64(sp)`, and full verify failed with calculated CRCs `0x78567132/0xCBE53596`. Source restored; final full verify passed. Keep `func_8002B0F4` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 after relink => CURRENT (2878); failed full verify CRCs 0x78567132/0xCBE53596

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 pad2-removal stack-shape probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
