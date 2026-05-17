# Session Handoff

- Generated at: 2026-05-17T18:11:56Z
- Branch: `master`
- HEAD: `2e8bc3a2`
- Completed task: `func_80049794`
- Summary: Followed the selector to `func_80049794`. Fresh promotion of the
  current C failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`; focused diff
  showed the known prologue miss with no target `$f20/$f21` saves, shifted
  saved-register slots, and early grounded-wheel zero in `$f16` instead of
  target `$f14`. Reconfirmed the already-recorded early-`var_f20` zero carrier
  (`var_f20 = 0.0f; racer->unk84 = var_f20; racer->unk88 = var_f20`): it
  failed with the same CRCs, stayed in the relinked focused compressed
  `CURRENT (2430)` family, and did not move the prologue or zero-register
  allocation. Source was restored and final full verify passed. Keep
  `func_80049794` active; do not repeat this early-`var_f20` zero carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with baseline `func_80049794` promotion, calculated CRCs `0x5FDDE03F/0xEF7A0514`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 1400 -U 90` after baseline relink => `CURRENT (3315)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with early-`var_f20` zero carrier, calculated CRCs `0x5FDDE03F/0xEF7A0514`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80` after early-`var_f20` zero-carrier relink => `CURRENT (2430)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing an active no-park near-match. For func_80049794, avoid the newly reconfirmed early-var_f20 zero carrier plus current-baseline existing-var_t9 wave-bound carrier, close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families recorded in ACTIVE.md. Keep func_80049794 active, not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
