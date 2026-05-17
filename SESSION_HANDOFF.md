# Session Handoff

- Generated at: 2026-05-17T17:59:30Z
- Branch: `master`
- HEAD: `2102cb03`
- Completed task: `func_80059208`
- Summary: Selected active alternate `func_80059208` because the selector's
  `func_80049794` wave-bound family is saturated, then tested a final
  `pad + pad2` sum carrier through the now-dead `diffX` local (`diffX = pad;
  diffX += pad2; diffX = -(diffX / divisor)`). It missed: full verify failed
  with calculated CRCs `0x63E46DB5/0x591D1D44`, the relinked focused score
  worsened from baseline `CURRENT (870)` to `CURRENT (1165)`, and the final
  tail added stack traffic/register drift instead of matching the target
  object-dot plus negated-checkpoint-dot schedule. Source restored and final
  full verify passed. Keep `func_80059208` active, but do not retry this
  `diffX` final-sum carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with `diffX` final-sum carrier, calculated CRCs `0x63E46DB5/0x591D1D44`
- `./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 70` after relink => `CURRENT (1165)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80059208 diffX final-sum carrier plus prior old-diffZ-through-pad axis-swap carrier, register-diffZ address-of invalid probe, register-scale no-op, final object-dot scale carrier, split-object-dot-after-positive-checkpoint spelling, split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants; avoid the func_80049794 current-baseline existing-var_t9 wave-bound carrier plus prior close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families; avoid the func_8002B0F4 segment-index i carrier plus prior outer segment-loop while, pad, early-conversion, loop, population, scalar-plane, direct-cast, local-model-cache, and volatile-global probes; avoid the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes and trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
