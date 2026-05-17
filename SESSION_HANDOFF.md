# Session Handoff

- Generated at: 2026-05-17 15:15:11Z
- Branch: `master`
- HEAD: `db8734fd`
- Completed task: `func_8002B0F4`
- Summary: Tested a prologue statement-order probe in `func_8002B0F4`: promoted source, moved `XInInt = xIn` / `ZInInt = zIn` immediately after `D_8011D308 = 0`, stored `*arg3 = NULL` after those conversions, passed the integer locals to `get_inside_segment_count_xz`, and removed the per-segment reassignments. It compiled and matched the target early integer call shape, but recreated the known early-conversion miss: relinked focused score `CURRENT (2860)`, failed full verify with calculated CRCs `0x7856718A/0x66208CAA`, and still introduced the unwanted pre-loop `gCurrentLevelModel` spill. Source restored; final full verify passed. Keep `func_8002B0F4` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 after relink => CURRENT (2860); failed full verify CRCs 0x7856718A/0x66208CAA

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_8002B0F4 D_8011D308-first early-conversion call-shape probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
