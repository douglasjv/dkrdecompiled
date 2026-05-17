# Session Handoff

- Generated at: 2026-05-17T18:35:36Z
- Branch: `master`
- HEAD: `5c168c7d`
- Completed task: `func_8008FF1C`
- Summary: Intentionally chose the active no-park near-match `func_8008FF1C`
  from the include-exhausted selector. Removed the `s16 temp` carrier and
  unsequenced temp assignment while promoting the function. It missed: full
  verify failed with calculated CRCs `0x553930E7/0x227AD4A3`, focused diff
  reported `CURRENT (935)`, and the selected-track load/branch still used `v1`
  instead of target `t2`; the delay-slot `sw v0,0(s0)` remained in place.
  Source was restored and final full verify passed. Keep active functions in
  the no-park lane, and do not repeat this no-temp cleanup shape.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with no-temp
  selectedTrack-only probe, calculated CRCs `0x553930E7/0x227AD4A3`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 500 -U 40` =>
  `CURRENT (935)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing active no-park near-match. For func_8008FF1C, avoid newly recorded no-temp selectedTrack-only cleanup plus previously recorded compare-carrier, selectedTrack declaration-order, direct table-branch, duplicated hub-name store, s32 temp carrier, s16/register selectedTrack, and temp/register probes; the useful boundary remains target t2 load plus delay-slot sw v0,0(s0). For func_80049794, avoid recorded probe families in ACTIVE.md. Keep active functions not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect
  the selected source/asm pair, write ordinary C, diagnose with
  `./diff.sh <function>`, and accept only after
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
