# Session Handoff

- Generated at: 2026-05-17 15:49:10Z
- Branch: `master`
- HEAD: `4f0d36f6`
- Completed task: `func_8002B0F4`
- Summary: Tested a combined stack-shape probe in `func_8002B0F4` by promoting the C and removing both unused `pad2` and dead `pad3`. It compiled but missed: frame shrank from target `0x128` to `0x120`, relinked focused score `CURRENT (2928)`, and full verify failed with calculated CRCs `0x78566FC2/0xC14E0CEA`. Source restored; final full verify passed. Keep `func_8002B0F4` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 4 after relink => CURRENT (2928); failed full verify CRCs 0x78566FC2/0xC14E0CEA

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 combined pad2/pad3 removal, func_80059208 positive-numerator variants, current-baseline func_80049794 chained-zero probe, and prior trackbg_render_flashy pad-spill probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
