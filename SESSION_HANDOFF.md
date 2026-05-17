# Session Handoff

- Generated at: 2026-05-17T18:40:53Z
- Branch: `master`
- HEAD: `fde71239`
- Completed task: `func_8008FF1C`
- Summary: Intentionally continued the active no-park near-match
  `func_8008FF1C` from the include-exhausted selector. A direct-table branch
  with the existing carriers reproduced the recorded direct-branch miss:
  target `t2` appeared, but `cur->hubName = levelName` hoisted before the
  halfword load, full verify failed with calculated CRCs
  `0x53D440E3/0x6E70641F`, and focused diff reported `CURRENT (125)`. A
  comma-store dependency probe
  (`cur->hubName = (selectedTrack = ..., levelName)`) was a no-op from the
  close baseline: CRCs `0x55C240E7/0x18E4F9B4`, focused `CURRENT (10)`, still
  `v1` instead of target `t2`. A `register s16 selectedTrack` probe collapsed
  into the known bad `s16 selectedTrack` family: CRCs
  `0x5B5E4609/0x72935A6E`, focused `CURRENT (1340)`, extra
  sign-extension/register churn, and still `v1`. Source was restored and final
  full verify passed. Keep active functions in the no-park lane.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with direct-table
  branch plus existing carriers, calculated CRCs `0x53D440E3/0x6E70641F`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 800 -U 80` =>
  `CURRENT (125)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with comma-store
  dependency probe, calculated CRCs `0x55C240E7/0x18E4F9B4`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 500 -U 45` =>
  `CURRENT (10)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with
  `register s16 selectedTrack`, calculated CRCs `0x5B5E4609/0x72935A6E`
- `./diff.sh func_8008FF1C --format plain --no-pager --max-size 500 -U 45` =>
  `CURRENT (1340)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing active no-park near-match. For func_8008FF1C, avoid newly recorded comma-store dependency and register-s16 selectedTrack probes plus previously recorded no-temp cleanup, compare-carrier, selectedTrack declaration-order, direct table-branch, duplicated hub-name store, s32 temp carrier, s16/register selectedTrack, and temp/register probes; the useful boundary remains target t2 load plus delay-slot sw v0,0(s0). For func_80049794, avoid recorded probe families in ACTIVE.md. Keep active functions not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect
  the selected source/asm pair, write ordinary C, diagnose with
  `./diff.sh <function>`, and accept only after
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
