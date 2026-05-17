# Session Handoff

- Generated at: 2026-05-17T17:40:27Z
- Branch: `master`
- HEAD: `f6fc3f6c`
- Completed task: `func_80049794`
- Summary: Tested the close save-family branch with x/z/y pre-`sqrtf`
  accumulation, chained grounded-wheel zero, steer-vel no-op, removed trailing
  `pad3`/`pad4`, and a new existing-`var_t0` wave-bound carrier
  (`var_t0 = gRacerWaveCount - 1; for (var_a0 = var_t0; ...); if (var_a0 ==
  var_t0)`). It kept the target `0xf8` frame and `$f20/$f21` prologue saves,
  but worsened the relinked focused score to `CURRENT (5115)`, failed full
  verify with calculated CRCs `0x2364AB01/0x1E30A2A8`, and shifted the wave
  block into a broader `t0/v0/t2` register family rather than target
  `v1/a0/v0`. Source restored and final full verify passed. Keep
  `func_80049794` active, but do not retry this close-branch existing-`var_t0`
  wave-bound carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted with calculated CRCs `0x2364AB01/0x1E30A2A8`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 60` after relink => `CURRENT (5115)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80049794 close-branch existing-var_t0 wave-bound carrier plus prior promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families; avoid the func_8002B0F4 segment-index i carrier plus prior outer segment-loop while, pad, early-conversion, loop, population, scalar-plane, direct-cast, local-model-cache, and volatile-global probes; avoid the func_80059208 split-object-dot-after-positive-checkpoint spelling plus prior final object-dot scale carrier, split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants; avoid the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes and trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
