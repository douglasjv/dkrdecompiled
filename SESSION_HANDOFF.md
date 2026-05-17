# Session Handoff

- Generated at: 2026-05-17T17:46:41Z
- Branch: `master`
- HEAD: `c942bcb0`
- Completed task: `func_80059208`
- Summary: Selected active alternate `func_80059208` and tested two
  final-tail allocation hints. `register f32 diffZ` is invalid in this
  function because `diffZ` is passed by address to
  `cubic_spline_interpolation`; the compiler rejected it with
  `address of register variable requested`. `register f32 scale` compiled, but
  produced no movement from the promoted baseline: full verify failed with the
  same calculated CRC family `0x53D141DF/0xB9D4B481`, relinked focused score
  stayed `CURRENT (870)`, and the same final object-dot plus
  negated-checkpoint-dot load/register drift remained. Source restored and
  final full verify passed. Keep `func_80059208` active, but do not retry
  either of these register-hint probes.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => compile failed for `register f32 diffZ` with `address of register variable requested`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted with `register f32 scale`, calculated CRCs `0x53D141DF/0xB9D4B481`
- `./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 50` after relink => `CURRENT (870)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80059208 register-diffZ address-of invalid probe and register-scale no-op plus prior final object-dot scale carrier, split-object-dot-after-positive-checkpoint spelling, split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants; avoid the newly recorded func_80049794 close-branch existing-var_t0 wave-bound carrier plus prior promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families; avoid the func_8002B0F4 segment-index i carrier plus prior outer segment-loop while, pad, early-conversion, loop, population, scalar-plane, direct-cast, local-model-cache, and volatile-global probes; avoid the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes and trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
