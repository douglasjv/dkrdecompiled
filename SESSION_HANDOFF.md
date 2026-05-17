# Session Handoff

- Generated at: 2026-05-17T18:08:34Z
- Branch: `master`
- HEAD: `827ade96`
- Completed task: `func_8002B0F4`
- Summary: Selected active alternate `func_8002B0F4` instead of the broad
  default selector `func_80049794`. Fresh promotion of the current C failed
  with calculated CRCs `0x7856718A/0x66208CAA`; the relinked focused diff was
  `CURRENT (2860)` and the first useful drift was an unwanted early
  `gCurrentLevelModel` stack spill before the segment loop. Removing the first
  dead `pad` local missed worse: full verify failed with calculated CRCs
  `0x7856713A/0x0D9BD727`, focused diff widened to `CURRENT (2886)`, `spB0`
  shifted from target `0xb0(sp)` to `0xb4(sp)`, `sp108` shifted to
  `0x10c(sp)`, and the same `gCurrentLevelModel` spill stayed at `0x64(sp)`.
  Source was restored and final full verify passed. Keep `func_8002B0F4`
  active; do not repeat the first-dead-`pad` removal.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with baseline `func_8002B0F4` promotion, calculated CRCs `0x7856718A/0x66208CAA`
- `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 1200 -U 80` after baseline relink => `CURRENT (2860)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed with first-dead-`pad` removal, calculated CRCs `0x7856713A/0x0D9BD727`
- `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 1200 -U 70` after first-dead-`pad` removal relink => `CURRENT (2886)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless intentionally choosing an active no-park near-match. For func_8002B0F4, avoid the newly recorded first-dead-pad removal plus prior X/Z register hints, pad3 removal, pad2 removal, pad2+pad3 removal, wave2 removal, texture-pointer replacement, pointer-copy population, early-conversion/direct-cast call shapes, D_8011D308-first order variant, segment-index i carrier, Z-loop unrolls, bubble-sort bound carrier, Z-grid barrier removal, bottom while loop, outer while loop, and other probe families recorded in ACTIVE.md. Keep func_8002B0F4 active, not parked.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
