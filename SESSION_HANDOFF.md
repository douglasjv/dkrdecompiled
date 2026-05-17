# Session Handoff

- Generated at: 2026-05-17 17:00:31Z
- Branch: `master`
- HEAD: `91c923f9`
- Completed task: `func_80049794`
- Summary: Tested a current-baseline wave-height threshold local in func_80049794 by naming `obj->trans.y_position + 5.0f` in `var_f0` before the wave scan. It compiled, but missed: full verify failed with calculated CRCs 0x5F811F98/0x9CE14139, focused diff worsened to CURRENT (5590), and the target prologue `$f20`/`$f21` saves plus early `$f14` zero were still absent. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 1200 -U 8 => CURRENT (5590); failed full verify CRCs 0x5F811F98/0x9CE14139

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions routable and avoid the newly recorded func_80049794 current-baseline wave-threshold-local probe plus prior func_80049794 chained-zero/wave-bound/save-family probes, func_8008FF1C temp/selectedTrack probes, func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
