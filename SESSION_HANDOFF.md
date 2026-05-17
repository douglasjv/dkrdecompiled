# Session Handoff

- Generated at: 2026-05-17T18:47:38Z
- Branch: `master`
- HEAD: `29a0d7c6`
- Completed task: `func_8002B0F4`
- Summary: Continued the active no-park matching lane. `func_80059208` was
  promoted only long enough to reconfirm the relinked baseline miss
  (`CURRENT (870)`, calculated CRCs `0x53D141DF/0xB9D4B481`), then restored
  because the apparent fresh checkpoint-dot shapes were already recorded in
  `ACTIVE.md`. Pivoted to `func_8002B0F4` and tested a fresh segment-index
  carrier through the existing `temp` local. It missed: full verify failed with
  calculated CRCs `0x7DF5F18A/0xA4BAA9BB`, relinked focused diff worsened to
  `CURRENT (3280)`, and the unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` remained. Source was restored and final full verify passed.
  Functions remain active; do not park them solely because this probe missed.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed for promoted
  `func_80059208` baseline, calculated CRCs `0x53D141DF/0xB9D4B481`
- `./diff.sh func_80059208 --format plain --no-pager --max-size 1200 -U 80`
  => `CURRENT (870)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed for promoted
  `func_8002B0F4` baseline, calculated CRCs `0x7856718A/0x66208CAA`
- `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 1400 -U 120`
  => `CURRENT (2875)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed for
  `func_8002B0F4` segment-index `temp` carrier, calculated CRCs
  `0x7DF5F18A/0xA4BAA9BB`
- `./diff.sh func_8002B0F4 --format plain --no-pager --max-size 800 -U 90`
  => `CURRENT (3280)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `Run the selector again and continue one active candidate without parking
  it. For func_8002B0F4, avoid the newly recorded segment-index temp carrier in
  addition to the prior pad/removal, global-model, loop-shape, and segment-index
  i carrier misses in ACTIVE.md. For func_80059208, avoid the recorded
  final-offset checkpoint/object-dot families; its current promoted baseline is
  still CURRENT (870). For func_80049794 and trackbg_render_flashy, use
  ACTIVE.md before choosing a probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect
  the selected source/asm pair, write ordinary C, diagnose with
  `./diff.sh <function>`, and accept only after
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
