# Session Handoff

- Generated at: 2026-05-17T17:50:26Z
- Branch: `master`
- HEAD: `71ae023c`
- Completed task: `func_80049794`
- Summary: Tested a current-baseline existing-`var_t9` wave-bound carrier
  (`var_t9 = gRacerWaveCount - 1; for (var_a0 = var_t9; ...); if (var_a0 ==
  var_t9)`). It missed: full verify failed with calculated CRCs
  `0x1ED9F907/0x570DED85`, the relinked focused score worsened from promoted
  baseline `CURRENT (2430)` to `CURRENT (4460)`, and the wave block shifted
  into broader integer-register churn rather than target `v1/a0/v0`. Source
  restored and final full verify passed. Keep `func_80049794` active, but do
  not retry this current-baseline existing-`var_t9` wave-bound carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted baseline with calculated CRCs `0x5FDDE03F/0xEF7A0514`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80` after relink => baseline `CURRENT (2430)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with `var_t9` wave-bound carrier, calculated CRCs `0x1ED9F907/0x570DED85`
- `./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 90` after relink => `CURRENT (4460)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80049794 current-baseline existing-var_t9 wave-bound carrier plus prior close-branch existing-var_t0 wave-bound carrier, promotion-only object CURRENT (0), current-baseline wave-threshold-local/chained-zero/wave-bound, close save-family wave-bound, wavePtr, do-loop, while-break, threshold, preserve, first-speed, zero-carrier, and no-op families; avoid the func_80059208 register-diffZ address-of invalid probe and register-scale no-op plus prior final object-dot scale carrier, split-object-dot-after-positive-checkpoint spelling, split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants; avoid the func_8002B0F4 segment-index i carrier plus prior outer segment-loop while, pad, early-conversion, loop, population, scalar-plane, direct-cast, local-model-cache, and volatile-global probes; avoid the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes and trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
