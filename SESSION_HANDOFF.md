# Session Handoff

- Generated at: 2026-05-17T18:31:01Z
- Branch: `master`
- HEAD: `2bd03a96`
- Completed task: `func_80049794`
- Summary: Continued selector `func_80049794`. Recreated the close save-family
  branch with chained grounded-wheel zero, x/z/y pre-`sqrtf` accumulation,
  removed trailing `pad3`/`pad4`, and steer-vel no-op, then tested a
  predecrement wave-loop spelling
  (`for (var_a0 = gRacerWaveCount; --var_a0 >= 0 && ...;)`). It missed: full
  verify failed with calculated CRCs `0xCE58DA51/0x62A7B089`, relinked focused
  diff reported `CURRENT (4660)`, and the wave scan shifted into an
  `a0/v0/v1` register/order family with extra post-loop compare math rather
  than target `v1/a0/v0`. Source was restored and final full verify passed.
  Keep `func_80049794` active, and do not repeat this close-branch
  predecrement wave-loop spelling.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with close save-family
  predecrement wave-loop spelling, calculated CRCs `0xCE58DA51/0x62A7B089`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80` =>
  `CURRENT (4660)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing active no-park near-match. For func_80049794, avoid newly recorded close save-family predecrement wave-loop spelling plus previously recorded close save-family existing-var_t9 wave-bound carrier, save-family double-multiply inverse spelling, save-family in-place inverse-gravity split, current-baseline existing-var_t9 wave-bound carrier, close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families recorded in ACTIVE.md. Keep func_80049794 active, not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect
  the selected source/asm pair, write ordinary C, diagnose with
  `./diff.sh <function>`, and accept only after
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
