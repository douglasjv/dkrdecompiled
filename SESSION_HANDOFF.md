# Session Handoff

- Generated at: 2026-05-17T17:34:58Z
- Branch: `master`
- HEAD: `50384659`
- Completed task: `func_8002B0F4`
- Summary: Tested a segment-index carrier through the existing `i` local:
  `i = spB0[var_fp]`, then indexed both `gCurrentLevelModel->segments` and
  `segmentsBoundingBoxes` with `i`. It compiled but worsened the relinked
  focused score to `CURRENT (2925)`, failed full verify with calculated CRCs
  `0x78BF118A/0x21FC9F7D`, kept the unwanted early `gCurrentLevelModel` spill
  at `0x60(sp)`, and drifted the segment-index register family from
  target/baseline `t1` toward `a3`/`t1`. Source restored and final full verify
  passed. Keep `func_8002B0F4` active, but do not retry this segment-index
  `i` carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted with calculated CRCs `0x78BF118A/0x21FC9F7D`
- `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 28` after relink => `CURRENT (2925)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_8002B0F4 segment-index i carrier plus prior outer segment-loop while, pad, early-conversion, loop, population, scalar-plane, direct-cast, local-model-cache, and volatile-global probes; avoid the func_80059208 split-object-dot-after-positive-checkpoint spelling plus prior final object-dot scale carrier, split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants; avoid promotion-only func_80049794 acceptance from object-only CURRENT (0), the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes, the trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, and func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
