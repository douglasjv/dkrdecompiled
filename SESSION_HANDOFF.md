# Session Handoff

- Generated at: 2026-05-17T18:16:58Z
- Branch: `master`
- HEAD: `b40def38`
- Completed task: `func_8008FF1C`
- Summary: Intentionally revisited default-skipped no-park near-match
  `func_8008FF1C`. Baseline promotion still failed with calculated CRCs
  `0x55C240E7/0x18E4F9B4`; focused diff stayed `CURRENT (10)` with only the
  selected-track `lh`/branch using `v1` instead of target `t2`, while the
  `cur->hubName = levelName` store remained in the target branch delay slot.
  A compare-carrier spelling (`temp = -1; if (selectedTrack != temp)`) was a
  no-op and kept the same CRCs/focused score/register miss. Moving the
  `selectedTrack` declaration after `temp` was worse: calculated CRCs
  `0x55C24297/0x59444A08`, focused `CURRENT (58)`, shifted stack slots, and
  still used `v1`. Source was restored and final full verify passed. Keep the
  function revisitable, but do not retry these two shapes.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with baseline `func_8008FF1C` promotion, calculated CRCs `0x55C240E7/0x18E4F9B4`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 400 -U 30` after baseline relink => `CURRENT (10)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with compare-carrier probe, calculated CRCs `0x55C240E7/0x18E4F9B4`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 400 -U 30` after compare-carrier relink => `CURRENT (10)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with selectedTrack declaration-order probe, calculated CRCs `0x55C24297/0x59444A08`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 500 -U 35` after declaration-order relink => `CURRENT (58)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing an active no-park near-match. For func_8008FF1C, avoid the newly recorded compare-carrier and selectedTrack declaration-order probes plus prior direct table-branch, duplicated hub-name store, s32 temp carrier, s16/register selectedTrack, and temp/register probes; the useful boundary remains target t2 load plus delay-slot sw v0,0(s0). For func_80049794, avoid recorded probe families in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
