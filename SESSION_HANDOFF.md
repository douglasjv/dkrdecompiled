# Session Handoff

- Generated at: 2026-05-17T17:26:22Z
- Branch: `master`
- HEAD: `d988f300`
- Completed task: `func_80049794`
- Summary: Rechecked `func_80049794` against the real acceptance gate after
  focused object diff printed `CURRENT (0)`. Promotion-only still failed full
  verify with the known CRC family, and the relinked focused diff returned to
  `CURRENT (2430)` with missing target `$f20/$f21` saves, shifted
  saved-register stack slots, early zero in `$f16` instead of target `$f14`,
  and the wave `a0`/`v1` register/order swap. Source restored and final full
  verify passed. Keep `func_80049794` active, but do not accept or retry
  promotion-only evidence from object-only `CURRENT (0)`.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted with calculated CRCs `0x5FDDE03F/0xEF7A0514`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 18` after relink => `CURRENT (2430)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid promotion-only func_80049794 acceptance from object-only CURRENT (0), the newly recorded func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes, the func_8002B0F4 outer segment-loop while spelling plus prior pad/early-conversion/loop probes, the func_80059208 final object-dot scale carrier plus prior split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants, the trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, and func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
