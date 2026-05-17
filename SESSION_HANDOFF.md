# Session Handoff

- Generated at: 2026-05-17T18:04:19Z
- Branch: `master`
- HEAD: `eeaf5b0b`
- Completed task: `func_8008FF1C`
- Summary: Intentionally revisited default-skipped `func_8008FF1C` because it
  is a near-match no-park target. Fresh promotion confirmed the known full-gate
  failure: calculated CRCs `0x55C240E7/0x18E4F9B4`, focused `CURRENT (10)`,
  with only the selected-track `lh`/branch using `v1` instead of target `t2`.
  A direct table-branch spelling moved that load/branch into target `t2`, but
  missed because `cur->hubName = levelName` hoisted before the `lh` instead of
  landing in the branch delay slot; full verify failed with calculated CRCs
  `0x53D440E3/0x6E70641F` and focused diff widened to `CURRENT (125)`.
  Duplicating the hub-name store in both branch arms missed worse
  (`0xAED257D4/0xAE31DFED`, focused `CURRENT (500)`) by adding a
  `move v1,v0` / duplicate-store family. Source restored and final full verify
  passed. Keep the function revisitable, but do not retry those two shapes.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with baseline `func_8008FF1C` promotion, calculated CRCs `0x55C240E7/0x18E4F9B4`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 1400 -U 80` after baseline relink => `CURRENT (10)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with direct table-branch probe, calculated CRCs `0x53D440E3/0x6E70641F`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 1400 -U 90` after direct table-branch relink => `CURRENT (125)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with duplicated hub-name store probe, calculated CRCs `0xAED257D4/0xAE31DFED`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 1400 -U 90` after duplicated-store relink => `CURRENT (500)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally revisiting a no-park near-match such as func_8008FF1C. For func_8008FF1C, avoid the newly recorded direct table-branch probe and duplicated hub-name store probe plus prior s32 temp carrier and s16/register selectedTrack/temp probes; the useful new evidence is that direct table branch gives target t2 but loses the target branch-delay sw v0,0(s0). For func_80049794, avoid current-baseline existing-var_t9 wave-bound carrier plus prior close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families. Active alternates remain func_8002B0F4, func_80059208, and trackbg_render_flashy; avoid their recorded probe families in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
