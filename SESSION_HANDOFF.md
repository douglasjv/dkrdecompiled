# Session Handoff

- Generated at: 2026-05-17T18:24:54Z
- Branch: `master`
- HEAD: `fa485687`
- Completed task: `func_80049794`
- Summary: Continued selector `func_80049794`. Recreated the close save-family
  branch with chained grounded-wheel zero, x/z/y pre-`sqrtf` accumulation,
  removed trailing `pad3`/`pad4`, and steer-vel no-op, then tested the
  target-looking inverse-gravity spelling
  (`var_f20 = 1.0 - (var_f20 * 0.25)`). It missed: full verify failed with the
  same close-branch calculated CRCs `0xB8DD79CD/0xE47454ED`, relinked focused
  diff reported `CURRENT (3260)`, the target `0xf8` frame and `$f20/$f21`
  saves stayed present, but the wave `a0`/`v1` drift remained and the target
  `$f14` reload after `apply_vehicle_rotation_offset` was still absent. Source
  was restored and final full verify passed. Keep `func_80049794` active, and
  do not repeat this double-multiply inverse spelling on the save-family
  branch.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with save-family
  double-multiply inverse spelling, calculated CRCs `0xB8DD79CD/0xE47454ED`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80` =>
  `CURRENT (3260)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing active no-park near-match. For func_80049794, avoid newly recorded save-family double-multiply inverse spelling plus previously recorded save-family in-place inverse-gravity split, current-baseline existing-var_t9 wave-bound carrier, close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families recorded in ACTIVE.md. Keep func_80049794 active, not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect
  the selected source/asm pair, write ordinary C, diagnose with
  `./diff.sh <function>`, and accept only after
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
