# Active Matching Surface

## Goal Context

- End goal: every original Diddy Kong Racing function has source-level C that
  keeps the matching ROM byte-identical.
- Loop: `research/tasks/GOAL_LOOP.md`.
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`.
- Exhausted probe notes: `research/tasks/PARKED.md`; these notes prevent
  blind retries and are skipped by default, but they are not permanent removal
  from the project.
- Default work: bounded `matching_impl` packets against one `GLOBAL_ASM`,
  `NON_MATCHING`, or `NON_EQUIVALENT` target.
- Default validation: `gmake -j4 CROSS=tools/binutils/mips64-elf-` in matching
  mode, then focused `./diff.sh` only for diagnosis.

## Current Route

- First route: run the selector and start with its `recommended_next`.
- Current repository baseline from README: `us.v77` reports 97.30% decompiled,
  with 7 `GLOBAL_ASM`, 4 `NON_MATCHING`, and 3 `NON_EQUIVALENT` functions.
- Current selector surface: 4 default-routable candidates and 3 functions with
  exhausted probe notes. Recommended next packet is `func_80049794` in
  `src/racer.c`.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted head-turn branch-order spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the
  player/computer head-turn branch from `gCurrentPlayerIndex !=
  PLAYER_COMPUTER` with `handle_racer_head_turning` first to
  `gCurrentPlayerIndex == PLAYER_COMPUTER` with `slowly_reset_head_angle`
  first. Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x3C39E22F/0x8EC77BBA`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3090)`. The diff dropped the target `$f20`/`$f21` prologue saves,
  kept early `$f16` zero allocation instead of target `$f14`, and broadened
  wave-scan/global-offset drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this head-turn branch-order spelling.
- Latest parked-packet revisit note: `func_8008FF1C` remains parked after a
  2026-05-24 current-shape selected-track `temp` removal probe missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and removed only the
  unused `s16 temp` declaration plus `temp = (temp =
  gTrackSelectIDs[trackY][trackX])`, leaving the existing `selectedTrack =
  gTrackSelectIDs[trackY][trackX]` and delay-slot-friendly
  `cur->hubName = levelName` before the branch. Pre-build
  `./diff.sh func_8008FF1C --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with calculated CRCs `0x553930E7/0x227AD4A3`;
  relinked `./diff.sh func_8008FF1C --no-pager` worsened from parked baseline
  `CURRENT (10)` to `CURRENT (935)`. The selected-track load/branch shifted
  away from target `t2` into `v1` and broadened register drift through the
  visible-track block. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this current-shape selected-track `temp` removal.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted wrong-way `WRAP` explicit-if expansion missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `WRAP(angle, -0x8000, 0x8000)` after `arctan2_f(diffX, diffZ)` into explicit
  `if (angle > 0x8000) angle -= 0xFFFF;` / `if (angle < -0x8000) angle +=
  0xFFFF;` statements. Pre-build `./diff.sh func_80059208 --compress-matching
  2 --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed
  with calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The wrong-way wrap block was not the source of drift; the
  diff remained in the final lateral object-dot plus vertical FPR tail family.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat this
  wrong-way `WRAP` explicit-if expansion.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted post-hit `yOutCount > 19` limit spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (yOutCount >= 20)` after incrementing `yOutCount` to
  `if (yOutCount > 19)`. Pre-build `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The diff retained the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and broad segment/grid/tail drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat
  this post-hit `yOutCount > 19` limit spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted batch-loop `currentBatch` pointer-carry spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  the batch loop from recomputing `currentBatch =
  &currentSegment->batches[batchNum]` inside the loop to initializing
  `currentBatch = currentSegment->batches` in the `for` header and incrementing
  it with `batchNum`. Pre-build `./diff.sh func_8002B0F4 --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x5FB2D180/0x62259969`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (4310)`. The diff kept the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and broadened the segment/grid/batch/tail register
  schedule. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this batch-loop `currentBatch` pointer-carry
  spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted edge-comparison `> -1` spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the three
  `temp_ra_*` edge tests from `>= 0` to `> -1`. Pre-build
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x7856718A/0x66208CAA`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The diff retained the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and broad segment/grid/tail drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat
  this edge-comparison `> -1` spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted texture-mask multiply spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `uCoordMask = (texHeader->width << 5) - 1` /
  `vCoordMask = (texHeader->height << 5) - 1` as `* 32` expressions.
  Pre-build `./diff.sh trackbg_render_flashy --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed
  with the promoted-baseline calculated CRCs `0x93D338FF/0x03D9C8FE`;
  relinked `./diff.sh trackbg_render_flashy --compress-matching 2
  --no-pager` stayed at `CURRENT (1808)`. The diff remained in the same early
  negative-cosine/position-array FPR/order family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat
  this texture-mask `* 32` spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted `level_id()` logical-not guard spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `if ((level_id() == 0) && (racer->nextCheckpoint >= temp_v0))` as
  `if (!level_id() && (racer->nextCheckpoint >= temp_v0))`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff retained the final object-dot/checkpoint-dot plus
  vertical FPR tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported
  active surface ok; do not repeat this `level_id()` logical-not guard
  spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted checkpoint-count logical-not guard spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `if (temp_v0 == 0)` as `if (!temp_v0)` after `get_checkpoint_count()`.
  Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with the
  promoted-baseline calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff retained the final object-dot/checkpoint-dot plus
  vertical FPR tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported
  active surface ok; do not repeat this checkpoint-count logical-not guard
  spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted collision-plane scalar boolean guard spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (tempVec4f.y != 0.0)` as `if (tempVec4f.y)`. Pre-build
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xF02BAC35/0xBB39E015`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3390)`. The diff retained the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and broadened collision-plane/default-water/tail FPR
  drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported
  active surface ok; do not repeat this collision-plane scalar boolean guard
  spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted normalization boolean guard spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `if (distance != 0.0f)` as `if (distance)` in the unit-vector
  normalization block. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff retained the final object-dot/checkpoint-dot plus
  vertical FPR tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported
  active surface ok; do not repeat this normalization boolean guard spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted bottom `hasWaves` explicit-nonzero condition spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote
  only `if (currentSegment->hasWaves && gWaveBlockCount != 0)` as
  `if (currentSegment->hasWaves != 0 && gWaveBlockCount != 0)`. Pre-build
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The diff retained the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` and bottom/default tail drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this bottom `hasWaves` explicit-nonzero condition spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted checkpoint-distance single-precision literal spelling
  missed. The source changed the `NON_MATCHING` guard to `#if 1` and rewrote
  only `splinePos = 1.0 - racer->checkpoint_distance` as
  `splinePos = 1.0f - racer->checkpoint_distance`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xC0802A15/0xAB5B7DB7`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3020)`. The diff replaced the target double subtraction with a
  single-precision subtract, shifted the early rewind threshold rodata
  reference, and broadly moved calls/labels. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this checkpoint-distance `1.0f` literal spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted final vertex store-order spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only the final vertex
  loop store order from `x`, `y`, `z`, RGB, alpha to `y`, `x`, RGB, `z`,
  alpha. Pre-build `./diff.sh trackbg_render_flashy --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x93D338FF/0x8D381EFE`; relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  worsened to `CURRENT (2263)`. The diff stayed in the early
  negative-cosine/position-array FPR/order family and then shifted the final
  vertex store schedule. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this final vertex store-order spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted wrong-way counter explicit-add assignment spelling
  missed. The source changed the `NON_MATCHING` guard to `#if 1` and rewrote
  only `racer->wrongWayCounter += updateRate` as
  `racer->wrongWayCounter = racer->wrongWayCounter + updateRate`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The explicit add did not address the
  earlier spline-math FPR/order drift around `0x5a260`. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this wrong-way counter explicit-add assignment spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted post-physics landing-crash guard condition-order
  spelling missed. The source changed the `NON_EQUIVALENT` guard to `#if 1`
  and rewrote only the guard from `var_t0 == 0 &&
  racer->groundedWheels != 0 && racer->spinout_timer != 0` to
  `racer->spinout_timer != 0 && var_t0 == 0 &&
  racer->groundedWheels != 0`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x23E5E3D7/0x8A077140`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2760)`. The diff still lacked target `$f20/$f21` prologue saves,
  kept early zero in current `$f16` instead of target `$f14`, and retained the
  known wave scan drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this post-physics landing-crash guard-order
  spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted airborne throttle-min guard condition-order spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote
  only the later guard from `racer->groundedWheels == 0 &&
  racerThrottle < 0.4 && racer->vehicleID != VEHICLE_CARPET` to
  `racerThrottle < 0.4 && racer->groundedWheels == 0 &&
  racer->vehicleID != VEHICLE_CARPET`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0x546B28B8`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2760)`. The diff still lacked target `$f20/$f21` prologue saves,
  kept early zero in current `$f16` instead of target `$f14`, and retained the
  known wave scan drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this airborne throttle-min guard-order spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted main B-button brake condition-order spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the
  main brake guard from `gCurrentRacerInput & B_BUTTON &&
  (gCurrentStickY < -40 || racer->velocity < 0.0f)` to
  `(gCurrentStickY < -40 || racer->velocity < 0.0f) &&
  (gCurrentRacerInput & B_BUTTON)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xF33115D9/0x3A459663`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (4150)`. The diff still lacked target `$f20/$f21` prologue saves,
  kept early zero in current `$f16` instead of target `$f14`, retained the
  known wave scan drift, and broadened later scheduling. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this main B-button brake guard-order spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted low-boost fallback condition-order spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the
  fallback boost-emitter branch from `boostObj->unk70 < 2 &&
  boostObj->unk74 > 0.0f` to `boostObj->unk74 > 0.0f &&
  boostObj->unk70 < 2`. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x105BE9DA/0x11DA74B9`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at the
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this low-boost fallback condition-order spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted early `sp108` return guard condition-order spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote
  only the initial `if (sp108 == 0 || sp108 >= 8)` guard as
  `if (sp108 >= 8 || sp108 == 0)`. Pre-build
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x7856718E/0xC7219F23`; relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (2930)`. The diff inverted the early `slti`/zero-test order,
  introduced the known unwanted early `gCurrentLevelModel` spill at `0x60(sp)`,
  and broadened segment/grid/tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this early `sp108` guard-order spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted early A-button throttle branch-polarity spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  the throttle update branch from `if (gCurrentRacerInput & A_BUTTON) { add
  throttle } else { subtract throttle }` to the behavior-equivalent inverted
  `if (!(gCurrentRacerInput & A_BUTTON)) { subtract throttle } else { add
  throttle }`. Pre-build `./diff.sh func_80049794 --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0xC592EE11/0x5932D245`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (6090)`. The diff still lacked target `$f20/$f21` prologue saves,
  kept early zero in current `$f16` instead of target `$f14`, changed the
  branch shape around the early input block, and retained the known wave scan
  `a0`-bound/`v1`-loop drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this A-button throttle branch-polarity spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight side-force multiply grouping missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `var_f20 = racer->velocity * var_t0 * 0.00015` as
  `var_f20 = racer->velocity * (var_t0 * 0.00015)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5F87643D/0xC95EBDF1`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at the
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this side-force multiply grouping.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted early lap-reset zero-store order spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only the
  reset block from `lap`, `nextCheckpoint`, `courseCheckpoint` zero stores to
  `nextCheckpoint`, `lap`, `courseCheckpoint`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x53D141DF/0xB7822901`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed to
  `CURRENT (880)`. The top block showed the reset stores opposite target
  (`0x192` then `0x193` instead of target `0x193` then `0x192`), while the
  known final object-dot/checkpoint-dot plus vertical FPR drift remained.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this early lap-reset zero-store order spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted angle subtract grouping spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `arctan2_f(diffX, diffZ) - (racer->steerVisualRotation & 0xFFFF) - 0x8000`
  as
  `arctan2_f(diffX, diffZ) - ((racer->steerVisualRotation & 0xFFFF) + 0x8000)`.
  Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The wrong-way angle block stayed
  target-like, while the final object-dot/checkpoint-dot plus vertical FPR
  drift remained. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this angle subtract grouping spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight `xRotationOffset` denominator spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and
  rewrote only `var_t0 *= (f32) (1.0 - ((f32) xRotationOffset / 4096))` as
  `var_t0 *= (1.0 - ((f32) xRotationOffset / 4096.0))`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5F88CFDD/0xCE72FB1A`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at the
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this `4096.0` denominator spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted pitch damping multiplier-carrier spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1`, kept the pitch damping
  factor-out shape, and replaced the duplicated `R_TRIG` branch-specific
  `19`/`30` pitch input stores with `var_v1 = 19/30` followed by one shared
  `obj->trans.rotation.x_rotation -= ((var_t0 >> 1) * var_v1 * updateRate) >>
  1`. Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, full verify failed with calculated CRCs
  `0x830ECE16/0x21DD0D2A`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to the
  promoted baseline `CURRENT (2760)` instead of preserving the factor-out-only
  `CURRENT (2480)` improvement. The known missing `$f20/$f21` prologue saves,
  early `$f16` zero, and wave scan `a0`-bound/`v1`-loop drift remained. Source
  was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this pitch multiplier-carrier spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight pitch damping factor-out spelling missed
  but improved focused drift. The source changed the `NON_EQUIVALENT` guard to
  `#if 1` and moved the shared
  `obj->trans.rotation.x_rotation -= (obj->trans.rotation.x_rotation *
  updateRate) >> 4` subtraction out of the adjacent `R_TRIG` if/else before
  the branch-specific `19`/`30` pitch input terms. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, full verify failed with calculated CRCs
  `0x81BCA331/0x35054A7B`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` improved from
  the promoted baseline `CURRENT (2760)` to `CURRENT (2480)`. The diff still
  lacked target `$f20/$f21` prologue saves, kept early zero in current `$f16`
  instead of target `$f14`, and retained wave scan `a0`-bound/`v1`-loop drift,
  so the factor-out alone is not acceptable. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this pitch damping factor-out spelling by itself.
  Next hypothesis may combine this improvement with an independent family, but
  acceptance still requires full `Verify: OK`.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight pitch damping factor-out plus `R_TRIG`-
  first branch-polarity spelling missed. The source changed the
  `NON_EQUIVALENT` guard to `#if 1`, hoisted the shared
  `obj->trans.rotation.x_rotation -= (obj->trans.rotation.x_rotation *
  updateRate) >> 4` subtraction before the branch, then tested
  `if (gCurrentRacerInput & R_TRIG)` with the `30` term first and the `19`
  term in `else`. Pre-build `./diff.sh func_80049794 --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x81BCA333/0xB748193D`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed in the
  factor-out family at `CURRENT (2480)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the current wave scan `a0`-bound/`v1`-loop
  allocation. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this pitch damping factor-out plus `R_TRIG`-first
  polarity spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight `tappedR` boolean spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the
  trick-entry branch from `if (racer->tappedR)` to
  `if (racer->tappedR != FALSE)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the plain promoted
  calculated CRCs `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at the
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift,
  with no useful movement at the `tappedR` branch. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this `tappedR != FALSE` spelling. Next hypothesis should use an
  independent `func_80049794` family or pivot to another routable packet,
  avoiding saved-FPR/wave-scan micro-variants already recorded.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted late attach-point guard-merge spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and merged only the two
  adjacent late `obj->attachPoints != NULL && obj->attachPoints->count >= 3`
  checks into one outer guard covering propeller model-index advancement plus
  the grounded/airborne propeller visibility update. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xDA53E0EB/0x04A68346`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at the
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this late attach-point guard-merge spelling. Next hypothesis should
  use an independent `func_80049794` family or pivot to another routable
  packet, avoiding saved-FPR/wave-scan micro-variants already recorded.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted final `spA1` R-trigger restore boolean spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  the final restore check from `if (spA1 != FALSE)` to `if (spA1)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan `a0`-bound/`v1`-loop drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this final `spA1` boolean spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted wrong-way counter limit spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `racer->wrongWayCounter < 200` as `racer->wrongWayCounter <= 199` in the
  wrong-way branch. Pre-build `./diff.sh func_80059208 --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  the promoted-baseline calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff stayed in the same final lateral/vertical
  object-dot FPR drift family, with no useful movement at the wrong-way branch.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this wrong-way counter `<= 199` spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted upper-half courseCheckpoint decrement spelling missed.
  The source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `racer->courseCheckpoint--` as `racer->courseCheckpoint += -1`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff stayed in the same final lateral/vertical offset
  tail family, with no useful movement in the courseCheckpoint decrement block.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this courseCheckpoint `+= -1` spelling. Next hypothesis should avoid
  this upper-half courseCheckpoint decrement, lap guard `>= 1`, alternate-route
  clear literal, and saturated final-tail object-dot/clamp variants.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted upper-half nextCheckpoint predecrement spelling missed.
  The source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `racer->nextCheckpoint--; if (racer->nextCheckpoint < 0)` as
  `if (--racer->nextCheckpoint < 0)`. Pre-build
  `./diff.sh func_80059208 --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with the promoted-baseline calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked `./diff.sh func_80059208
  --compress-matching 2 --no-pager` stayed at `CURRENT (870)`. The diff stayed
  in the same final lateral/vertical offset tail family, including the target
  preserving the negated pad term while current folds the equivalent math into
  subtract. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this nextCheckpoint predecrement spelling. Next
  hypothesis should avoid this upper-half decrement spelling and saturated
  final-tail object-dot/clamp variants.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted upper-half lap guard comparison spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only the
  rewind lap-decrement guard from `racer->lap > 0` to `racer->lap >= 1`.
  Pre-build `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with the
  promoted-baseline calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff stayed in the same final lateral/vertical offset
  tail family, with no useful movement in the rewind lap branch. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok; do not repeat this lap guard `>= 1` spelling.
  Next hypothesis should avoid this upper-half lap comparison and saturated
  final-tail object-dot/clamp variants.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted alternate-route clear literal spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only the two early
  alternate-route clears from `racer->isOnAlternateRoute = FALSE` to
  `racer->isOnAlternateRoute = 0`. Pre-build `./diff.sh func_80059208
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with the promoted-baseline calculated CRCs
  `0x53D141DF/0xB9D4B481`; relinked `./diff.sh func_80059208
  --compress-matching 2 --no-pager` stayed at `CURRENT (870)`. The diff stayed
  in the same final lateral/vertical offset tail family, with no useful
  movement in the alternate-route branch. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this alternate-route clear literal spelling. Next
  hypothesis should avoid this upper-half alternate-route spelling and
  saturated final-tail object-dot/clamp variants.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted alternate-route guard boolean spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only the early
  guard from `if (racer->isOnAlternateRoute)` to
  `if (racer->isOnAlternateRoute != FALSE)`. Pre-build
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x53D141DF/0xB9D4B481`; relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The diff stayed in the same final lateral/vertical
  object-dot/checkpoint-dot tail family, with no useful movement in the
  alternate-route branch. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this alternate-route guard boolean spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted pointer-sentinel comparison spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote only the two
  `unk74` sentinel checks from `(u32) pointer !=/== -1U` to pointer comparisons
  against `(LevelHeader_70 *) -1`. Pre-build `./diff.sh trackbg_render_flashy
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with the promoted-baseline calculated CRCs
  `0x93D338FF/0x03D9C8FE`; relinked `./diff.sh trackbg_render_flashy
  --compress-matching 2 --no-pager` stayed at `CURRENT (1808)`. The diff stayed
  in the same early negative-cosine and first/outer position-array register
  drift, with no useful movement at the selected-color sentinel block. Source
  was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this pointer-sentinel comparison spelling. Next hypothesis should avoid
  `trackbg_render_flashy` sentinel/color-order variants and saturated
  position/UV micro-variants.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted selected-color load-order spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and reordered only the
  `if (var_t2 != NULL)` color assignments so
  `var_a3 = levelHeader->rgba.word & (~0xFF)` executed before
  `var_a2 = var_t2->rgba.word`, matching the apparent target load order near
  the `gfx_init_basic_xlu` arguments. Pre-build
  `./diff.sh trackbg_render_flashy --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with the promoted-baseline calculated
  CRCs `0x93D338FF/0x03D9C8FE`; relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed
  at `CURRENT (1808)`. The diff stayed in the same early negative-cosine and
  first/outer position-array register-order family, with no useful movement at
  the selected-color block. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this selected-color load-order spelling. Next
  hypothesis should avoid `trackbg_render_flashy` selected-color ordering and
  saturated first/outer position arithmetic/store-order variants.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted header pointer-load spelling missed. The source changed
  the `NON_MATCHING` guard to `#if 1` and rewrote only
  `var_t2 = *gCurrentLevelHeader2->unk74` as
  `var_t2 = gCurrentLevelHeader2->unk74[0]`. Pre-build
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x93D338FF/0x03D9C8FE`; relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (1808)`. The diff remained in the earlier
  position-array/FPR scheduling drift with no useful movement at the header
  pointer load. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this explicit `unk74[0]` header-load spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted final triangle flags store-order spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and moved only
  `tris->flags = 0x40` from the start of the final triangle loop body to after
  the three vertex/UV stores. Pre-build `./diff.sh trackbg_render_flashy
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x93C6F83F/0x0C9FB0E5`; relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  regressed to `CURRENT (2018)`. The diff stayed in the early
  negative-cosine/position-array FPR family and then showed the expected tail
  flags-store movement. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this final triangle flags store-order spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted triangle-hit nested-predicate spelling missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (temp_ra_1 == temp_ra_2 && temp_ra_2 != temp_ra_3)` as nested
  `if (temp_ra_1 == temp_ra_2) { if (temp_ra_2 != temp_ra_3) { ... } }`.
  Pre-build `./diff.sh func_8002B0F4 --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with the promoted-baseline calculated
  CRCs `0x7856718A/0x66208CAA`; relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` stayed at `CURRENT (2860)`. The diff kept
  the same early `gCurrentLevelModel` load/spill at `0x60(sp)` plus broad
  segment/grid/tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this triangle-hit nested-predicate spelling. Next
  hypothesis should avoid early model hoisting/spilling or pivot to another
  independent routable packet.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted final vertical additive-negation spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `diffY = (obj->trans.y_position - tempY) / divisor` as
  `diffY = (obj->trans.y_position + -tempY) / divisor`. Pre-build
  `./diff.sh func_80059208 --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`;
  relinked `./diff.sh func_80059208 --no-pager` stayed at promoted baseline
  `CURRENT (870)`. The spelling produced no useful final-tail object-code
  movement. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this final vertical additive-negation spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted final lateral correction outer-negate spelling missed.
  The source changed the `NON_MATCHING` guard to `#if 1` and rewrote only
  `diffX = -((pad + pad2) / divisor)` as `diffX = -(pad + pad2) / divisor`.
  Pre-build `./diff.sh func_80059208 --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x53C0B5DF/0xF31038C3`; relinked
  `./diff.sh func_80059208 --no-pager` regressed to `CURRENT (1600)`.
  The spelling perturbed the final lateral/object-dot and vertical tail rather
  than resolving the remaining final offset drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this outer-negate final lateral correction spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted final triangle indexed-table spelling missed. The source
  changed the `NON_MATCHING` guard to `#if 1`, removed the `var_v0_3 =
  D_800DC92C` cursor, and populated the eight final triangles with direct
  `D_800DC92C[(i * 3) + n]` index expressions for each vertex/UV lookup.
  Pre-build `./diff.sh trackbg_render_flashy --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xEF56CD99/0xECCC3EA5`; relinked
  `./diff.sh trackbg_render_flashy --no-pager` regressed to
  `CURRENT (12773)`. The relinked object perturbed early negative-cosine and
  doubled-trig FPR allocation (`$f18`/`$f16` and `$f8`/`$f18`) long before the
  triangle loop, then broadly shifted the later vertex/triangle tail. Source
  was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat final triangle indexed-table spellings. Next hypothesis should use a
  different `trackbg_render_flashy` family or pivot to another routable packet.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted Z grid-mask four-way unroll spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the Z
  bounding-box mask loop from `for (i = 0; i < 8; i++)` to `i += 4` with four
  inlined copies of the same mask/update body. Pre-build
  `./diff.sh func_8002B0F4 --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with calculated CRCs `0x7856718A/0xC40F5151`;
  relinked `./diff.sh func_8002B0F4 --no-pager` regressed to
  `CURRENT (3325)`. The relinked object hoisted `gCurrentLevelModel` before the
  candidate loop and spilled it to `0x60(sp)`, shifting the segment setup and
  later loops by four bytes despite the Z mask block shape. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok; do not repeat Z grid-mask four-way unroll
  spellings. Next hypothesis should avoid early model hoisting/spilling or
  pivot to another routable packet.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted first-ring full `scaledXSin` reuse spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1` and reused the existing
  `scaledXSin` local for all first-ring x/z position expressions that had
  repeated `(xSin * 1280.0f)`, while preserving the `xCos = var_f16` UV alias.
  Pre-build `./diff.sh trackbg_render_flashy --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x8310DF9D/0x03EA48C03`; relinked
  `./diff.sh trackbg_render_flashy --no-pager` regressed to
  `CURRENT (13581)`. The relinked object widened the frame to `0x168`, added
  `s2` plus `$f20`/`$f21` saves, and shifted early position-array FP
  temporaries and stack slots immediately away from the target. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok; do not repeat all-first-ring `scaledXSin` reuse
  spellings. Next hypothesis should pivot to another independent
  `trackbg_render_flashy` family or another routable packet.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted loop-local `LevelModel *levelModel` setup probe missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1`, declared
  `LevelModel *levelModel`, assigned `levelModel = gCurrentLevelModel` at the
  top of the candidate segment loop, and derived only `currentSegment` and
  `currentBoundingBox` from that local pointer. Pre-build
  `./diff.sh func_8002B0F4 --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with calculated CRCs `0xAB0F899E/0x6AB2A43D`;
  relinked `./diff.sh func_8002B0F4 --no-pager` improved the count to
  `CURRENT (1678)` while still missing the target. The relinked object widened
  the frame to `0x130`, hoisted `gCurrentLevelModel` before the loop, and
  spilled it to `0x12c(sp)` and `0x64(sp)` instead of keeping the target
  in-loop register load. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat a normal loop-local model pointer for segment setup.
  Next hypothesis should prevent hoisting/spilling while still targeting the
  segment/bounding-box model load, or pivot to another routable packet.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted direct `var_f16` UV sine-carrier spelling missed. The
  source changed the `NON_MATCHING` guard to `#if 1`, removed the
  post-scale `xCos = var_f16` alias, and used `var_f16` directly in the
  `uCoords[0]`, `uCoords[1]`, `uCoords[5]`, `uCoords[6]`, `uCoords[7]`, and
  `uCoords[8]` expressions. Pre-build `./diff.sh trackbg_render_flashy
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x07616968/0xE7EACAF4`; relinked
  `./diff.sh trackbg_render_flashy --no-pager` regressed to
  `CURRENT (15227)`. The probe widened the frame to `0x160`, added
  `$f20`/`$f21` saves, and immediately shifted the early position and UV FPR
  schedule away from the target. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat direct `var_f16` UV sine-carrier alias removal.
  Next `trackbg_render_flashy` hypothesis should preserve the `xCos` alias or
  pivot to a different early position/store family.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 inline final object-dot object-load spelling missed. The source
  promoted the `NON_MATCHING` guard to `#if 1`, removed the `splinePos` and
  `distance` temporaries from the final object-dot calculation, and used
  `obj->trans.x_position` / `obj->trans.z_position` directly in `pad`.
  Pre-build `./diff.sh func_80059208 --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x53A81EDF/0x116C7718`; relinked
  `./diff.sh func_80059208 --no-pager` worsened to `CURRENT (1356)` from the
  promoted baseline `CURRENT (870)`. The relinked diff introduced early
  checkpoint-distance FPR/stack-slot drift around `$f0`/`$f2` and
  `0x2c`/`0x58`/`0x28`, while the final object/checkpoint-dot tail remained
  unresolved. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat direct inline final object x/z load object-dot
  spelling. Next hypothesis should use an independent `func_80059208` family or
  pivot away from final object-dot micro-variants.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 plain current-C promotion missed. The source changed only the
  `NON_EQUIVALENT` guard to `#if 1`. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` returned
  `CURRENT (2760)`. The relinked object lost target `$f20/$f21` prologue saves,
  moved saved GPR slots down by eight bytes, used current `$f16` for early zero
  stores instead of target `$f14`, and kept the wave scan bound/index allocation
  reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat plain current-C promotion. Next hypothesis should
  pivot away from `func_80049794` save/wave micro-variants unless a new
  independent source family is found.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 combined close-save plus cached wave-bound split missed. The
  source promoted the `NON_EQUIVALENT` guard to `#if 1`, removed trailing
  `pad3`/`pad4`, chained grounded-wheel zero stores, split the pre-`sqrtf`
  x/z/y accumulation, and added explicit `var_v1 = gRacerWaveCount - 1` with
  `var_a0` as cursor. Pre-build `./diff.sh func_80049794 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x5F138B9C/0x62404784`; relinked
  `./diff.sh func_80049794 --no-pager` returned `CURRENT (6743)`. The relinked
  object shrank the frame to current `0xf0`, lost target `$f20/$f21` prologue
  saves, used current `$f16`/stack slots for early float state, and still
  assigned the wave split to `a3/v0` rather than target `v1/a0`. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok; do not repeat this combined close-save plus
  cached-bound spelling. Next hypothesis should pivot away from `func_80049794`
  save/wave micro-variants unless a new independent source family is found.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 explicit wave bound/index split missed. The source promoted the
  `NON_EQUIVALENT` guard to `#if 1`, assigned
  `var_v1 = gRacerWaveCount - 1`, started the loop with
  `for (var_a0 = var_v1; ...)`, and compared `var_a0 == var_v1`. Pre-build
  `./diff.sh func_80049794 --no-pager` misleadingly reported `CURRENT (0)`,
  but full verify failed with calculated CRCs `0x5790053C/0x1C8C0179`;
  relinked `./diff.sh func_80049794 --no-pager` returned `CURRENT (5755)`.
  The relinked object lost target `$f20/$f21` prologue saves, used current
  `$f16` for early zeroing, and assigned the wave split to `a3/v0` rather than
  target `v1/a0`. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat explicit cached wave-bound/index split alone.
  Next hypothesis should combine a known save-family shape with a different
  cursor-addressing form, or pivot to another routable packet.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 declaration-only `register f32 var_f20` saved-FPR pressure hint
  missed. The source promoted the `NON_EQUIVALENT` guard to `#if 1` and changed
  only `var_f20` to `register`. Pre-build `./diff.sh func_80049794
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --no-pager` returned `CURRENT (2760)`. The object
  still missed target `$f20/$f21` prologue saves, kept early zeroing in current
  `$f16` instead of target `$f14`, and retained current `a0`-bound/`v1`-loop
  wave allocation instead of target `v1`-bound/`a0`-loop. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok; do not repeat declaration-only `register
  var_f20` hints. Next hypothesis needs a distinct saved-FPR/frame-pressure
  plus wave bound/index allocation fix, or a pivot to another routable packet.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 plain guarded-C promotion recheck missed. Before promotion,
  `./diff.sh func_80049794 --no-pager` misleadingly reported `CURRENT (0)`
  against the guarded source. Promoting only the `NON_EQUIVALENT` guard to
  `#if 1` failed the full gate with the known current-baseline CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --no-pager` showed `CURRENT (2760)`. The promoted
  object still missed target `$f20/$f21` prologue saves, used `$f16` for early
  zeroing instead of target `$f14`, and kept the wave scan in current
  `a0`-bound/`v1`-loop allocation instead of target `v1`-bound/`a0`-loop.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  accept pre-promotion object-only `CURRENT (0)` evidence or repeat plain
  guarded-C promotion without a distinct saved-FPR plus wave bound/index fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 close save-family nested wave-gate split missed. The source
  promoted the guarded C, recreated the close save-family base
  (x/z/y pre-`sqrtf` accumulation, chained grounded-wheel zero, steer-vel
  no-op, and removed trailing `pad3`/`pad4`), then changed only the early wave
  eligibility gate from one `&&` chain into nested `if` guards for
  player/vehicle/wave-count. Compressed focused diff misleadingly reported
  `CURRENT (0)`, but full verify failed with the known close-family CRCs
  `0xB8DD79CD/0xE47454ED`; uncompressed relinked
  `./diff.sh func_80049794 --no-pager` showed `CURRENT (4365)`. The diff kept
  the target `0xf8` frame and `$f20/$f21` prologue saves, but the wave
  bound/index allocation stayed reversed with current `a0` as bound and `v1`
  as loop index instead of target `v1` bound and `a0` loop index. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat close save-family wave-gate split/register variants without a
  distinct bound/index allocation fix.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted declaration-only `register f32 scaledXCos` allocation
  hint missed. The source changed only the `NON_MATCHING` guard to `#if 1` and
  declared `scaledXCos` as `register`, targeting the early negative scaled
  cosine FPR allocation without adding a new carrier local. Pre-build
  `./diff.sh trackbg_render_flashy --no-pager` misleadingly reported
  `CURRENT (0)`, but full verify failed with promoted-baseline calculated CRCs
  `0x93D338FF/0x03D9C8FE`; relinked uncompressed
  `./diff.sh trackbg_render_flashy --no-pager` stayed at promoted baseline
  `CURRENT (1808)`. The early negative-cosine carrier still allocated current
  `$f16` instead of target `$f18`, with the same doubled sine/cosine and
  outer-ring register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat declaration-only `register scaledXCos` allocation
  hints.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted UV dimension shift spelling missed. The source changed
  only the `NON_MATCHING` guard to `#if 1` and rewrote the UV scale products
  from `texHeader->width * 16` / `texHeader->height * 16` to explicit
  `<< 4` products, including the fake duplicate `var_a2` assignment. Compressed
  focused diff misleadingly reported `CURRENT (0)`, but full verify failed
  with promoted-baseline CRCs `0x93D338FF/0x03D9C8FE`; uncompressed relinked
  `./diff.sh trackbg_render_flashy --no-pager` stayed at `CURRENT (1808)`.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this UV dimension `<< 4` product spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted outer-ring `zPositions[6]` plus-negative spelling
  missed. The source changed only the `NON_MATCHING` guard to `#if 1` and
  rewrote `zPositions[6] = -(2.0f * scaledXCos) - scaledXSin` as
  `zPositions[6] = -(2.0f * scaledXCos) + -scaledXSin`. Compressed focused
  diff misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x93D438FF/0x1A841372`; uncompressed relinked
  `./diff.sh trackbg_render_flashy --no-pager` showed `CURRENT (1813)`. The
  diff stayed in the early negative-cosine `$f18`/`$f16` mismatch and broadened
  first/outer position-array register-order drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this single-site `zPositions[6]` plus-negative spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted first-ring `xPositions[2]` scaled-sine reuse probe
  missed. The source changed only the `NON_MATCHING` guard to `#if 1` and
  rewrote `xPositions[2] = scaledXCos + (xSin * 1280.0f)` as
  `xPositions[2] = scaledXCos + scaledXSin`. Compressed focused diff
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x218EDFFA/0xDD1EF586`; uncompressed relinked
  `./diff.sh trackbg_render_flashy --no-pager` showed `CURRENT (13681)`.
  The probe shrank the frame from target `0x158` to `0x150`, shifted stack
  slots, and broadened the early position-array schedule. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this single-site `xPositions[2]` scaledXSin reuse.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted segment setup assignment-order probe missed. The source
  changed only the `NON_EQUIVALENT` guard to `#if 1` and reordered the segment
  loop setup so `currentBoundingBox =
  &gCurrentLevelModel->segmentsBoundingBoxes[spB0[var_fp]]` came before
  `currentSegment = &gCurrentLevelModel->segments[spB0[var_fp]]`, attempting to
  mirror the target member load order. Pre-build `./diff.sh func_8002B0F4
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0x7856718A/0xA6A743D8`; relinked uncompressed
  `./diff.sh func_8002B0F4 --no-pager` regressed to `CURRENT (3965)`. The diff
  introduced an early hoisted `gCurrentLevelModel` load/spill to `0x60(sp)`,
  shifted the segment/grid loop by four bytes, and still diverged broadly from
  the target. Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  reached `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this assignment-order/member-load-order spelling. Next hypothesis for
  this packet should target segment loop setup without hoisting/spilling
  `gCurrentLevelModel`, or pivot to another routable packet.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted `surface` local halfword-width probe missed. The source
  changed only the `NON_EQUIVALENT` guard to `#if 1` and changed the batch
  `surface` local from `s8` to `s16`. Full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and the relinked uncompressed focused diff stayed
  at promoted baseline `CURRENT (2860)`. The diff retained the known unwanted
  early `gCurrentLevelModel` spill at `0x60(sp)` plus broad segment/grid/tail
  register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat `s8 surface` -> `s16` or `s32` local-width probes.
  Next hypothesis for this packet should target the early model pointer
  spill/segment setup or pivot to another routable packet.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted declaration-only `register f32 xCos` allocation hint
  missed. The source changed only the `NON_MATCHING` guard to `#if 1` and
  declared `xCos` as `register`. Full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and the relinked uncompressed focused diff stayed
  at promoted baseline `CURRENT (1808)`. The early position-array drift still
  used current `$f16` for the first negative-cosine carrier instead of target
  `$f18`, with broad first/outer position-array register-order drift. Source
  was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this `register xCos` allocation hint. Next `trackbg_render_flashy`
  hypothesis should pivot away from declaration-only allocation hints and
  target a distinct early position expression/store family, or choose another
  routable packet.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted five-node `posZ` subtract-product regrouping probe
  missed. The source changed only the `NON_MATCHING` guard to `#if 1` and
  rewrote `temp_v0_4->z + ((scale * (-rotationXFrac)) * unk1BA)` as
  `temp_v0_4->z - ((scale * rotationXFrac) * unk1BA)`. Compressed
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xC7A9F9F0/0x58059DF2`; uncompressed
  `./diff.sh func_80059208 --no-pager` showed `CURRENT (1575)`. The probe
  converted the target loop's explicit `neg.s` plus add family into a
  sub-product family and shifted later addresses by one instruction. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this `posZ` subtract-product regrouping. Next hypothesis for this
  packet should pivot away from sampling-loop sign spelling toward the final
  object/checkpoint dot-product tail, or choose another routable packet.
- Latest alternate-packet note: `func_80017A18` remains active after a
  2026-05-24 plain guarded-C promotion missed. The source changed only the
  `NON_EQUIVALENT` guard to `#if 1`. Compressed
  `./diff.sh func_80017A18 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x0075F167/0x927B806A`, and uncompressed
  `./diff.sh func_80017A18 --no-pager` showed `CURRENT (8376)`. The promoted C
  widened the frame from `0x120` to `0x138` and shifted stack slots plus FPR/GPR
  allocation across the plane-intersection loops. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  treat compressed `CURRENT (0)` as acceptance evidence for this packet.
- Latest parked-packet revisit note: `func_8008FF1C` remains parked after a
  2026-05-24 plain current guarded-C promotion recheck missed. Before
  promotion, `./diff.sh func_8008FF1C --no-pager` misleadingly reported
  `CURRENT (0)`. Promoting only the `NON_MATCHING` guard to `#if 1` failed the
  full gate with baseline CRCs `0x55C240E7/0x18E4F9B4`; relinked
  `./diff.sh func_8008FF1C --no-pager` showed `CURRENT (10)`, with only the
  selected-track halfword load/branch still using current `v1` instead of
  target `t2` while the hub-name store stayed in the target branch delay slot.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  accept pre-promotion object-only `CURRENT (0)` or repeat plain current
  guarded-C promotion for this parked packet.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted pointer-object current-wave cursor probe missed. The
  source removed the `NON_EQUIVALENT` guard, introduced
  `WaterProperties **wave`, cached `var_v1 = gRacerWaveCount - 1`, scanned
  with `while (var_a0 >= 0 && (*wave)->waveHeight < obj->trans.y_position + 5)
  { var_a0--; wave--; }`, and reused `wave[1]` for selected wave height and
  `rot.y`. Full verify failed with calculated CRCs
  `0x56B32B55/0xCE72FDA3`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (7008)`. The new pointer local widened the frame to `0x100`, lost
  target `$f20/$f21` saves, kept early zero in `$f16`, and shifted the wave
  scan into a `a0/a3/v0/v1` family rather than target `v0/v1/a0` with cursor
  at `v0`. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this new-local pointer-cursor
  wave scan without a separate saved-FPR/frame-pressure fix. Pivot to another
  routable packet if no distinct allocation family is available.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-tested cached-bound `for` spelling missed. The worker
  promoted guarded C, cached `var_v1 = gRacerWaveCount - 1`, started
  `for (var_a0 = var_v1; ...)`, and compared the final selected wave against
  `var_v1`. Full verify failed with calculated CRCs
  `0x5790053C/0x1C8C0179`, and focused
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (5755)`. The wave setup drifted to `v1/a3/v0` instead of target
  `v0/v1/a0`, kept indexed reload churn instead of pointer-predecrement, and
  still missed target `$f20/$f21` saves plus early `$f14` zeroing. Worker
  source was restored and the main worktree stayed clean; do not repeat this
  scalar cached-bound `for` spelling. Next hypothesis should be a distinct
  pointer-object current-wave cursor with independent integer bound and saved
  FPR pressure, or a pivot to another routable packet.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-tested integer-local current-wave cursor probe missed. The
  worker promoted guarded C, scanned from `&gRacerCurrentWave[var_a0]` using an
  integer pointer cursor, kept `var_v1` as the last index, decremented `var_a0`
  as the scan index, and read the selected wave through `(var_v0 + 4)`. Full
  verify failed with calculated CRCs `0xD9ECC055/0xCEF62DE7`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (6590)`. The probe recovered pointer-predecrement behavior but in
  the wrong register family: current still allocated as indexed/cursor
  `a0/a3/v1` instead of target pointer `v0`, bound `v1`, index `a0`; target
  `$f20/$f21` saves were still absent and the early zero remained in `$f16`
  instead of `$f14`. Worker source was restored, the main worktree was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this integer-local cursor family. The next distinct probe should fix
  saved-FPR/frame pressure before more wave pointer allocation variants, or
  pivot to another routable selector packet.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted `surface` local widening probe missed. The source removed
  the `NON_EQUIVALENT` guard and changed only the batch `surface` local from
  `s8` to `s32`, leaving the texture read expression unchanged. Compressed
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x78567172/0xAF051F1E`; uncompressed `./diff.sh func_8002B0F4 --no-pager`
  showed `CURRENT (2936)`. The probe widened the frame to `0x130`, shifted the
  output pointer and segment-count stack slots, and kept the unwanted early
  `gCurrentLevelModel` spill at `0x64(sp)` with broad segment/grid/tail drift.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this `s8 surface` -> `s32 surface` local-type probe. Next hypothesis
  for this packet should target the early model pointer spill/segment loop setup
  or pivot to another routable packet.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted final byte-cast spelling missed. The source removed the
  `NON_EQUIVALENT` guard and changed only `D_8011D308 = yOutCount;` to
  `D_8011D308 = (s8) yOutCount;`. Full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The explicit cast still emitted the same final `sb s5`
  store while retaining the known unwanted early `gCurrentLevelModel` spill and
  broad segment/grid/tail register drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this final byte-cast spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted register-parameter plus texture-index carrier probe
  missed. The source removed the `NON_EQUIVALENT` guard, added `register` to
  the `xIn`/`zIn` float parameters, and changed the batch surface read to
  `temp = currentBatch->textureIndex; surface =
  gCurrentLevelModel->textures[temp].surfaceType;`. Full verify failed with
  calculated CRCs `0x7C4CE18A/0x3A298210`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` reported
  `CURRENT (2435)`, collapsing into the existing standalone texture-index
  `temp` carrier family. The early unwanted `gCurrentLevelModel` spill remained
  at `0x60(sp)` and broad segment/grid/tail drift persisted. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this register-parameter plus texture-index carrier combination.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted return-through-global spelling missed. The source
  removed the `NON_EQUIVALENT` guard, preserved the final target store order,
  and changed only `return yOutCount;` to `return D_8011D308;`. Full verify
  failed with calculated CRCs `0x6C3561EA/0x2B3CC6FB`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3535)`. The final tail inserted a reload from `D_8011D308` instead
  of target `move v0,s5`, and the known unwanted early `gCurrentLevelModel`
  spill plus broad register drift remained. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this return-through-global spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted final store-order probe missed. The source removed the
  `NON_EQUIVALENT` guard and swapped only the final tail from
  `*arg3 = gTrackWaves; D_8011D308 = yOutCount;` to
  `D_8011D308 = yOutCount; *arg3 = gTrackWaves;`. Full verify failed with
  calculated CRCs `0x7856718A/0x9DAD43C2`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3305)`. The tail now stored `D_8011D308` before the output pointer,
  opposite the target, while retaining the known unwanted early
  `gCurrentLevelModel` spill and broad register drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this final store-order swap.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted final output-pointer assignment spelling missed. The
  source removed the `NON_EQUIVALENT` guard and changed only the final output
  assignment from `*arg3 = gTrackWaves` to `arg3[0] = gTrackWaves`, leaving the
  initial `*arg3 = NULL` clear unchanged. Full verify failed with the promoted
  current-source calculated CRCs `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The known unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` plus broad segment/grid/tail register drift remained. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this final output-pointer assignment spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted current-source output-pointer clear spelling missed. The
  source removed the `NON_EQUIVALENT` guard and changed only `*arg3 = NULL` to
  `arg3[0] = NULL`. Full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2860)`. The diff retained the known unwanted
  early `gCurrentLevelModel` spill at `0x60(sp)` plus broad segment/grid/tail
  register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this output-pointer clear `arg3[0]` spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted `pad3` removal plus output-pointer clear spelling
  missed. The source removed the `NON_EQUIVALENT` guard, removed the dead
  `pad3` slot, and changed only the initial clear from `*arg3 = NULL` to
  `arg3[0] = NULL`. Full verify failed with the plain `pad3`-removal
  calculated CRCs `0x785671AA/0x0D6F6A4A`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` reported
  `CURRENT (2868)`. The `arg3[0]` spelling did not improve the `pad3`-removed
  branch: the unwanted early `gCurrentLevelModel` spill remained at `0x64(sp)`
  with broad segment/grid/tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this combined `pad3` removal plus
  output-pointer clear spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-suggested saved-FPR pressure carrier before the wave scan
  missed. The source removed the `NON_EQUIVALENT` guard, assigned
  `var_f20 = updateRateF` before the wave scan, then restored
  `updateRateF = var_f20` after the wave block. Compressed focused diff
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x60DDDE6F/0x79AAF0F1`; uncompressed
  `./diff.sh func_80049794 --no-pager` showed `CURRENT (8068)`. The function
  still missed the target `$f20/$f21` prologue saves, kept the current early
  zero/FPR allocation drift, and moved later gravity scheduling away from the
  target. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not trust compressed `CURRENT (0)` evidence for this
  packet or repeat this narrow pre-wave `var_f20` update-rate carrier without
  a distinct allocation family.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted early wave speed `var_f14` carrier missed. The source
  removed the `NON_EQUIVALENT` guard, removed the dedicated `racerVelocity`
  local, and routed the early wave speed clamp/lift through existing
  `var_f14`. Full verify failed with calculated CRCs
  `0x5FD89617/0xF4C6A984`, and relinked
  `./diff.sh -o func_80049794 --compress-matching 2 --no-pager` worsened from
  promoted object baseline `CURRENT (2550)` to `CURRENT (2704)`. The probe
  still lacked target `$f20/$f21` prologue saves, kept early zero in `$f16`
  instead of target `$f14`, left the wave bound/index allocation reversed as
  current `a0`/`v1`, and shifted later gravity scheduling into the `$f14`
  family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  reported 97.30%; do not repeat this early wave speed `var_f14` carrier
  without a separate saved-FPR and wave bound/index allocation fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-tested close save-family plus target-bound while
  wave-scan probe missed. The worker promoted guarded C, applied the close
  save-family base shape, then rewrote the wave scan with explicit
  `var_v0 = gRacerWaveCount`, `var_v1 = var_v0 - 1`, `var_a0 = var_v1`, and a
  `while` loop intended to keep `var_v1` as bound and `var_a0` as loop index.
  Full verify failed with calculated CRCs `0x57263252/0x731465D5`, and the
  relinked focused diff regressed to `CURRENT (8135)`. The wave scan still
  missed target `v0/v1/a0`, compiling into `a1/a0/v0/v1` churn with indexed
  reloads instead of target pointer-predecrement allocation. Worker source was
  restored, main `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat close
  save-family plus explicit `var_v0`/`var_v1`/`var_a0` while wave-scan
  spellings without a distinct pointer-predecrement or saved-FPR allocation
  fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-tested close save-family predecrement wave-loop probe
  missed. The source promoted guarded C, applied the close save-family base
  shape, then rewrote the wave scan with `count = gRacerWaveCount`, saved
  `bound = count - 1`, `index = bound`, a first-load check, and explicit
  predecrement of index plus wave pointer before later compares. Full verify
  failed with calculated CRCs `0x11949F63/0x3C85367C`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (6209)`. The frame stayed `0xf8`, but `$f20/$f21` prologue saves
  were lost, the wave scan allocated into an `a1/a0/v1` count/bound/index
  drift instead of target `v0/v1/a0`, the pointer predecrement compiled as
  `lw -4(v0)` before `addiu v0,-4`, and extra `spA2` stack-byte traffic
  appeared. Worker source was restored, main `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat wave pointer/predecrement/cache spellings
  until the close save-family pressure keeps `$f20/$f21` saves alive.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted selected-wave byte-offset carrier probe missed. The
  source removed the `NON_EQUIVALENT` guard, kept the wave scan intact,
  computed `var_t9 = var_a0 << 2`, conditionally subtracted four bytes when
  `var_a0 == gRacerWaveCount - 1`, and reused
  `(*(WaterProperties **)((u8 *) gRacerCurrentWave + var_t9 + 4))` for both
  selected-wave `waveHeight` and `rot.y` accesses. Full verify failed with
  calculated CRCs `0x784EE4A7/0x63167E71`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed from
  promoted baseline `CURRENT (2760)` to `CURRENT (5460)`. The probe reused an
  offset but shifted it into an `a2` family instead of target `a1`, dropped the
  target `$f20/$f21` prologue saves, kept early zero in `$f16`, and inserted
  `spA2` stack-byte traffic. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat selected-wave byte-offset carriers without a
  distinct save-pressure or wave register-family fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted final `playerObjectMoved` boolean-check spelling
  missed. The source removed the `NON_EQUIVALENT` guard and changed only
  `if (playerObjectMoved != FALSE)` to `if (playerObjectMoved)`. Full verify
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (2760)`: target `$f20/$f21` prologue saves were still absent,
  early zeroing still allocated `$f16` instead of target `$f14`, and wave
  scan registers stayed in the current `a0`/`v1` family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` reported 97.30%; do not repeat final `playerObjectMoved`
  boolean-check spellings without a distinct save-pressure or wave allocation
  fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted wave-scan while/threshold-carrier probe missed. The
  source removed the `NON_EQUIVALENT` guard and rewrote the wave scan so
  `var_v1 = gRacerWaveCount - 1`, `var_a0 = var_v1`, and an explicit `while`
  loop compared `gRacerCurrentWave[var_a0]->waveHeight` against a `var_f0 =
  obj->trans.y_position + 5.0f` threshold. Full verify failed with calculated
  CRCs `0xC81C158F/0x7475EA56`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (6105)`. The target `$f20/$f21` prologue saves were still absent,
  early zeroing still allocated `$f16` instead of target `$f14`, and the wave
  loop broadened into a different integer-register family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` reported 97.29%; do not repeat this wave-scan while /
  threshold-carrier promotion.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted final vertical negative-divisor spelling missed. The
  source removed the `NON_MATCHING` guard and changed only the final vertical
  correction from `(obj->trans.y_position - tempY) / divisor` to
  `(tempY - obj->trans.y_position) / -divisor`. Full verify failed with
  calculated CRCs `0x53C47BB5/0x00B78968`, and relinked
  `./diff.sh func_80059208 --no-pager` regressed from promoted baseline to
  `CURRENT (1930)`. The tail stayed in the final object-dot/checkpoint-dot
  plus vertical FPR drift family, with broader scheduling drift than the
  existing final-vertical sign variants. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  reported 97.30%; do not repeat final vertical negative-divisor spellings
  unless paired with a distinct object/checkpoint-dot allocation fix.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted final update-order spelling missed. The source removed
  the `NON_MATCHING` guard and moved only `racer->unk1BA += (s32) diffX` after
  the final vertical correction/clamp/update, applying `unk1BC` before
  `unk1BA`. Full verify failed with calculated CRCs
  `0x53ACFAA7/0x47C757C4`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3135)`. The tail moved the final lateral cast/store below the
  vertical block, broadened the final vertical FPR/cast scheduling, and still
  retained the object-dot/checkpoint-dot drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this final `unk1BC` before `unk1BA` update-order spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted final lateral object-minus-spline delta-form probe
  missed. The source removed the `NON_MATCHING` guard and changed only the
  final lateral numerator from separate object/checkpoint dot terms to
  `pad = splinePos - tempX; pad2 = distance - tempZ; diffX = -(((pad * diffX)
  + (pad2 * diffZ)) / divisor);`. Initial compressed focused diff
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x0FBA7B07/0x87E4E665`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed to
  `CURRENT (2527)`. The final tail loaded the object pointer earlier,
  changed the object/checkpoint dot FPR schedule, and broadened the vertical
  update FPR allocation. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this final lateral delta-form spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted inverse-gravity quarter-multiply spelling missed in a
  worker probe. The source changed only `var_f20 = 1.0 - (var_f20 / 4.0)` to
  `var_f20 = 1.0 - (var_f20 * 0.25)`. Full verify failed with calculated CRCs
  `0x4555932A/0x3BB0F237`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` again reported
  `CURRENT (2760)`: target `$f20/$f21` prologue saves were still absent, saved
  register slots shifted, early zeroing still allocated `$f16` instead of
  target `$f14`, and wave scan registers stayed in the current `a0`/`v1`
  family. Source was restored, and main validation after restore reached
  `Verify: OK`; do not repeat the inverse-gravity `0.25` multiply spelling
  without a distinct lifetime/pressure fix before the wave scan.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted zipper-wrap ternary spelling missed. A worker found
  object-only `CURRENT (0)` while the function stayed guarded, but promoting
  the source and changing only the `steerVisualRotationOffset` wrap
  corrections from two `if` statements to ternary reassignments failed the
  full gate with calculated CRCs `0x5FDDE03F/0xEF7A0514`. Relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` again reported
  `CURRENT (2760)`: target `$f20/$f21` prologue saves were still absent, saved
  register slots shifted, early zeroing still allocated `$f16` instead of
  target `$f14`, and wave scan registers stayed in the current `a0`/`v1`
  family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat zipper-wrap ternary reassignment promotion
  without a distinct save-pressure or wave allocation fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 direct guarded-C promotion probe missed. Removing only the
  `NON_EQUIVALENT` wrapper failed the full gate with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` reported `CURRENT (2760)`. The promoted
  source still lacked target `$f20/$f21` prologue saves, kept early zeroing in
  `$f16` instead of target `$f14`, and left the wave bound/index allocation in
  the current `a0`/`v1` family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat direct guard removal / object-only
  `CURRENT (0)` promotion unless paired with a distinct save-pressure or wave
  allocation fix.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted `var_f14` grounded-wheel zero carrier missed. A worker
  found object-only `CURRENT (0)` while the function stayed under
  `NON_EQUIVALENT`, but promoting the source and adding
  `var_f14 = 0.0f; racer->unk84 = var_f14; racer->unk88 = var_f14` failed the
  full gate with calculated CRCs `0x5FDDE03F/0xEF7A0514`. Relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (2760)`: target `$f20/$f21` prologue saves were still absent, saved
  register slots shifted, early zeroing still allocated `$f16` instead of
  target `$f14`, and wave scan registers stayed in the current `a0`/`v1`
  family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this guarded object-only `CURRENT (0)` /
  `var_f14` grounded-wheel zero carrier without a distinct save-pressure fix.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted `splineIndex` assignment-order probe missed. The source
  removed the `NON_MATCHING` guard and changed only the threshold branch body
  from `splinePos -= 1.0; splineIndex = TRUE;` to
  `splineIndex = TRUE; splinePos -= 1.0;`. Focused
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with the promoted-baseline
  calculated CRCs `0x53D141DF/0xB9D4B481`. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this `splineIndex` assignment-order spelling
  or trust object-only `CURRENT (0)` for this packet.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted `splineIndex` boolean-assignment probe missed. The source
  removed the `NON_MATCHING` guard and changed the setup from `splineIndex =
  FALSE` plus in-branch `TRUE` assignment to `splineIndex = splinePos >= 1.0`
  followed by `if (splineIndex)`. Full verify failed with calculated CRCs
  `0x73555B47/0x49EFC995`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed from
  promoted baseline to `CURRENT (1440)`. The spelling inserted an extra `v0`
  boolean branch around the splineIndex test, then cascaded the same final
  object-dot plus vertical FPR drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  reported 97.30%; do not repeat this `splineIndex` boolean-assignment spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted five-node pointer-fill loop probe missed. The source
  removed the `NON_MATCHING` guard and rewrote only the checkpoint fill from
  the indexed `i` loop to pointer locals over `posX`/`posY`/`posZ`, with
  `posZPtr++` before the stores, `*posXPtr`/`*posYPtr`, `posZPtr[-1]`, and
  post-body `posYPtr++` to imitate the target pointer schedule. Full verify
  failed with calculated CRCs `0x53D13B3F/0xB6EAEAF5`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` reported
  `CURRENT (1499)`. The loop moved toward the target `sltu` pointer family,
  but the frame grew from `0xc0` to `0xc8`, local arrays shifted by eight
  bytes, and final object-dot/vertical tail drift remained. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` reported 97.30%; do not repeat this five-node
  pointer-fill loop spelling without a distinct frame/stack-slot fix.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted five-node fill-loop counter-wrap comparison probe
  missed. The source removed the `NON_MATCHING` guard and changed only
  `if (counter == temp_v0)` to behavior-equivalent `if (counter >= temp_v0)`
  inside the one-step checkpoint sampling loop. Full verify failed with
  calculated CRCs `0x52D04491/0x026BB530`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed from
  promoted baseline `CURRENT (870)` to `CURRENT (1575)`: the target
  `bne s0,t0` wrap check became an `slt at,s0,t0` / `bnez at` family, the
  sampling-loop pointer increments moved, and the final object-dot/checkpoint-
  dot plus vertical FPR tail shifted. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this five-node fill-loop counter-wrap comparison spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted crossed final object-dot spelling missed. The source
  removed the `NON_MATCHING` guard and changed only the final lateral object
  dot from `pad = (objX * diffX) + (diffZ * objZ)` to
  `pad = (objZ * diffX) + (diffZ * objX)`. Full verify failed with calculated
  CRCs `0x53CD81DF/0xC82CEDAE`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (875)`. The tail shifted into
  the same small object-dot multiply-order family as the x/z product commutes,
  with final vertical FPR drift still present. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat crossed-coordinate final object-dot
  spellings.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted normalization positive-distance guard probe missed. The
  source removed the `NON_MATCHING` guard and changed only
  `if (distance != 0.0f)` to `if (distance > 0.0f)`. Full verify failed with
  calculated CRCs `0x53B461F3/0x9A237E15`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed from
  promoted baseline to `CURRENT (1270)`. The normalization branch changed to
  `c.lt.s`/`bc1f`, while the final object/checkpoint plus vertical FPR drift
  remained. Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  reached `Verify: OK`, and `./score.sh -s` reported 97.30%; do not repeat
  this normalization positive-distance guard spelling.
- Latest alternate-packet note: `func_80059208` remains active but saturated
  after a 2026-05-24 promoted final-vertical double-literal clamp probe missed.
  The source changed only the final vertical clamp constants from
  `100.0f`/`-100.0f` to `100.0`/`-100.0`. Full verify failed with calculated
  CRCs `0x01672C72/0xAF96E3E2`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (3605)`. The tail introduced
  double compare/conversion traffic for the vertical clamp, shifted rodata
  references, and broadened final object-dot/checkpoint-dot plus vertical FPR
  drift. Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  reached `Verify: OK`, and `./score.sh -s` reported 97.29%; do not repeat
  this final vertical double-literal clamp spelling.
- Latest alternate-packet note: `func_80059208` remains active but saturated
  after a 2026-05-24 promoted final-vertical negation spelling missed. The
  source changed only the vertical correction from
  `(obj->trans.y_position - tempY) / divisor` to
  `-(tempY - obj->trans.y_position) / divisor`. Full verify failed with
  calculated CRCs `0x53D45BB5/0x11D3A734`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1125)`. The final vertical
  block inserted an extra `neg.s`, shifted the object-dot/checkpoint-dot FPR
  family, and broadened the final vertical clamp/register drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` reported 97.29%; do not repeat this final vertical
  negation spelling.
- Latest alternate-packet note: `func_80059208` remains active but saturated
  after a 2026-05-24 promoted existing-C diagnostic. Removing the
  `NON_MATCHING` guard without source-shape changes failed the full gate with
  calculated CRCs `0x53D141DF/0xB9D4B481`; `cmp` put the first real code drift
  at ROM byte offset 369250 (`0x5A262`) in the final
  object-dot/checkpoint-dot tail, while racer object `.rodata` still carried
  the `-0.2` bytes at the expected object rodata offset. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not treat the promoted existing-C miss as
  a simple rodata-placement problem or repeat final-tail micro-variants without
  a distinct codegen-family hypothesis.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted named-rodata probe missed. The source shape removed the
  `NON_MATCHING` guard, added `const f64 D_800E6920 = -0.2`, and changed the
  early rewind guard to `if (splinePos < D_800E6920)`. Full verify failed with
  calculated CRCs `0x53CFD9B3/0xC564A533`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed from
  the promoted text-only `CURRENT (0)` family to `CURRENT (900)`. The named
  const was placed at the wrong rodata address, shifted later racer constants
  by eight bytes, and the final object-dot/checkpoint-dot FPR drift remained.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this plain
  source-level `D_800E6920` constant naming as the rodata placement fix. A
  promoted function-local `static const f64 rewindThreshold = -0.2` spelling
  also missed in the same family: full verify failed with calculated CRCs
  `0x53CFD9B3/0xC564A533`, and relinked `./diff.sh func_80059208
  --compress-matching 2 --no-pager` reported `CURRENT (900)`. The diff still
  referenced the wrong late-rodata address, shifted later racer constants by
  eight bytes, and left the final object-dot/checkpoint-dot drift. Source was
  restored and final full verify passed; do not repeat local/static/file-scope
  f64 naming for this threshold.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 early rewind threshold single-precision spelling missed. The
  promoted source changed only `splinePos < -0.2` to `splinePos < -0.2f`.
  Full verify failed with calculated CRCs `0xA4F54F99/0xA2F49F7F`, and
  relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (870)` to `CURRENT (3342)`.
  The diff replaced the target double compare against `D_800E6920` with a
  single-precision compare, shifted downstream spline stack slots, and
  broadened the final object-dot/checkpoint-dot tail drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  early rewind threshold `-0.2f` single-precision spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted first-ring paired-store reuse probe missed. The source
  changed the `NON_MATCHING` guard to `#if 1` and rewrote the first-ring
  position stores to reuse paired array slots (`zPositions[1] = xPositions[0]`,
  `zPositions[2] = xPositions[1]`, `xPositions[3] = zPositions[0]`,
  `zPositions[3] = xPositions[2]`). Full verify failed with calculated CRCs
  `0x0A819FB5/0x0003CE66`, and relinked uncompressed
  `./diff.sh trackbg_render_flashy --no-pager` regressed to `CURRENT (7643)`.
  The frame shrank from target `0x158` to `0x150`, early negative-cosine still
  used current `$f16` instead of target `$f18`, and first-ring store scheduling
  broadened. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and active surface
  remained ok; do not repeat first-ring paired array-slot reuse/store-carrier
  spellings.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted selected-color shift-mask spelling missed. The source
  removed the `NON_MATCHING` guard and changed only
  `levelHeader->rgba.word & (~0xFF)` to `(levelHeader->rgba.word >> 8) << 8`.
  Compressed `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x19BC4411/0xC7375025`; uncompressed
  `./diff.sh trackbg_render_flashy --no-pager` showed `CURRENT (3463)`. The
  shift-mask spelling unexpectedly moved the early position-array FPR schedule,
  keeping current `$f16` instead of target `$f18` for the negative scaled
  cosine and broadening outer-ring/global-offset drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this selected-color shift-mask spelling. Next `trackbg_render_flashy`
  hypothesis should still target the early negative-cosine FPR allocation or
  pivot to another routable packet.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted compound scaled trig temporary setup missed. The source
  removed the `NON_MATCHING` guard and changed only
  `scaledXSin = xSin * 1280.0f; scaledXCos = xCos * 1280.0f;` to
  assignment-then-multiply form for both locals. Full verify failed with
  calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (1808)`. The early negative-cosine carrier still
  allocated current `$f16` instead of target `$f18`, with the same doubled
  sine/cosine and outer-ring register drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this compound scaled trig temporary setup.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 worker-assisted promoted direct `xCos * 1280.0f` first-ring
  expression probe missed. The source removed the `NON_MATCHING` guard and
  changed only the first-ring `xPositions[0..3]` / `zPositions[0..3]` terms to
  direct `xCos * 1280.0f` expressions while preserving `scaledXSin` and the
  `0x158` frame. Full verify failed with calculated CRCs
  `0x93BF98FF/0x27187E1D`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` improved
  from promoted baseline to `CURRENT (1668)`. The early negative-cosine carrier
  still allocated current `$f16` instead of target `$f18`, doubled-cosine/
  doubled-sine FPRs shifted, and outer-ring store scheduling drifted. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` reported 97.30%; do not repeat direct `xCos * 1280.0f`
  first-ring rewrites without a distinct early FPR allocation fix.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted existing-`var_f16` negative-cosine carrier probe missed.
  The source promoted the function, assigned `var_f16 = -scaledXCos`, and used
  that existing local for the first/outer negative scaled-cosine position
  expressions. Full verify failed with calculated CRCs
  `0xDC79F591/0x31DBA03C`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported
  `CURRENT (3108)`. The frame stayed target-sized at `0x158`, but the early
  `neg.s` still allocated current `$f16` instead of target `$f18`, and outer
  position/global scheduling shifted in the same carrier-local family as the
  `pad_sp108` miss. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat existing-local negative-cosine carriers for
  `trackbg_render_flashy`.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted UV scroll scale division-commute probe missed. The
  source changed the scroll offsets from `position * (var_f14 / dimension)` to
  `(position / dimension) * var_f14` for both X and Z. Full verify failed with
  calculated CRCs `0x93BF9907/0x8148592D`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported
  `CURRENT (3120)`. The frame stayed `0x158`, but the early negative-cosine
  carrier still used current `$f16` instead of target `$f18`, with broad
  UV/FPR and vertex scheduling drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this UV scroll scale division-commute spelling
  as the FPR allocation fix.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted color-mask carrier through `var_a3` missed. The source
  shape kept `var_a3 = -0x100` as the fallback mask and changed only the
  selected-color path from `levelHeader->rgba.word & (~0xFF)` to
  `levelHeader->rgba.word & var_a3`. Full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (1808)`. The diff remained in the early
  position-array `$f18`/`$f16` drift family; source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this color-mask `var_a3`
  carrier spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 worker negative-cosine carrier probe missed. The promoted source
  added a new `negScaledXCos = -scaledXCos` local and used it for first-ring
  and outer negative-cosine position expressions. Full verify failed with
  calculated CRCs `0xDC79FC91/0xA51F89F4`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` worsened
  from promoted baseline `CURRENT (1808)` to `CURRENT (3382)`. The frame stayed
  `0x158`, but temp stack slots shifted, early negative cosine still used
  `$f16` instead of target `$f18`, and first position-array scheduling
  broadened. Source was restored, main `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat new-local/storage negative-cosine carriers.
  Next `trackbg_render_flashy` hypothesis should preserve the existing stack
  layout while influencing the target `neg.s` FPR allocation.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 grouped first-ring negative-sum spelling missed. The promoted
  source changed only `xPositions[0]` from
  `-scaledXCos - (xSin * 1280.0f)` to
  `-((xSin * 1280.0f) + scaledXCos)`. Full verify failed with calculated CRCs
  `0xD6EC5F94/0xFD1467AB`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` worsened
  from promoted baseline `CURRENT (1808)` to `CURRENT (10447)`. The frame
  widened to `0x160`, stack offsets shifted, and the early negative-cosine
  carrier still missed target `$f18`. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this single-site grouped first-ring
  negative-sum spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 single-site x2 scaled-sine left-operand spelling missed. The
  promoted source changed only `xPositions[2]` from
  `scaledXCos + (xSin * 1280.0f)` to `scaledXSin + scaledXCos`. Full verify
  failed with calculated CRCs `0x218F9FFA/0x18F4A6D6`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  regressed from promoted baseline `CURRENT (1773)` to `CURRENT (12478)`.
  The frame shrank from target `0x158` to `0x150`, stack slots shifted, and
  early position-array/UV scheduling broadened. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this single-site x2
  scaled-sine left-operand spelling. A promoted single-site
  `zPositions[2] = scaledXCos - scaledXSin` direct replacement also missed in
  the same direct-`scaledXSin` frame-shrink family: full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`, and relinked `./diff.sh
  trackbg_render_flashy --compress-matching 2 --no-pager` regressed to
  `CURRENT (13821)`. The frame shrank from target `0x158` to `0x150` and the
  first/outer position-array stack schedule shifted broadly. Source was
  restored and final full verify passed; do not repeat direct first-ring
  `scaledXSin` replacements as the FPR allocation fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted `pad3` removal plus scaled collision-plane index local
  probe missed. The source removed the `NON_EQUIVALENT` guard, removed the
  dead `pad3` slot, then stored `basePlaneIndex * 4` in `temp` and used
  `collisionPlanes[temp + n]`. Full verify failed with calculated CRCs
  `0x7E7421AA/0xA14ED9A9`, and relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` reported `CURRENT (2733)`, slightly worse
  than the scaled-index-only `CURRENT (2725)`. The unwanted early
  `gCurrentLevelModel` load/spill remained, shifted to `0x64(sp)`, with broad
  segment/grid/tail register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat `pad3` removal plus scaled collision-plane
  index local without a distinct model-spill/register-family fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted collision-hit post-increment limit equality probe
  missed. The source removed the `NON_EQUIVALENT` guard and changed only the
  post-hit limit check from `if (yOutCount >= 20)` to
  `if (yOutCount == 20)`. Full verify failed with calculated CRCs
  `0xA74DDBBC/0xC4B262D4`, and relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` regressed from promoted baseline
  `CURRENT (2860)` to `CURRENT (8360)`. The hit-limit site compiled into a
  constant-register equality compare (`li s7,0x14`; `bne s5,s7`) instead of
  the target post-increment `slti`/`bnez` shape, while the known early
  `gCurrentLevelModel` load/spill family remained. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat post-hit `yOutCount == 20`
  or equality-limit spellings without a distinct model-spill/register-family
  fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted early `sp108 > 7` guard spelling missed. The source
  removed the `NON_EQUIVALENT` guard and changed only the second half of the
  initial return guard from `sp108 >= 8` to `sp108 > 7`. Full verify failed
  with calculated CRCs `0x7856718A/0x66208CAA`, and relinked `./diff.sh
  func_8002B0F4 --compress-matching 2 --no-pager` stayed at promoted baseline
  `CURRENT (2860)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` load/spill at `0x60(sp)` and broadened segment/grid/tail
  register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this early `sp108 > 7` guard spelling.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted X-grid mask accumulator late-zero scheduling probe
  missed. The source removed the `NON_EQUIVALENT` guard and moved only
  `var_s1 = 0` from immediately after `var_a1 = 1` to just before the first
  grid loop, after the X-grid bound temporaries were derived. Full verify
  failed with calculated CRCs `0x7856718A/0xCA7F3062`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed from
  promoted baseline toward `CURRENT (3070)`. The target-like later accumulator
  zero did not fix the model-cache family: the diff still inserted the
  unwanted early `gCurrentLevelModel` load/spill at `0x60(sp)` and broadened
  segment/grid/tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this X-grid mask late-zero scheduling
  spelling without a separate model-spill/register-family fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted direct batch skip-offset assignment probe missed. The
  source kept the current surface-skip condition but assigned
  `currentFaceOffset = currentBatch[1].facesOffset` instead of using the
  existing `nextFaceOffset` local. Full verify failed with calculated CRCs
  `0x2A78E7DF/0xC1A5BFE8`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` reported
  `CURRENT (3190)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` load/spill at `0x60(sp)` and broadened segment/grid/tail
  drift beyond the promoted baseline. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat direct batch skip-offset assignment without a
  separate model-spill fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 pointer-addition model-access probe missed. The promoted source
  changed only the initial segment and bounding-box setup from
  `&gCurrentLevelModel->segments[spB0[var_fp]]` /
  `&gCurrentLevelModel->segmentsBoundingBoxes[spB0[var_fp]]` to pointer-add
  forms. The focused diff reported `CURRENT (2940)` and stayed in the known
  early cached `gCurrentLevelModel` spill family, loading the model pointer
  before the outer segment loop and spilling it at `0x60(sp)`. The full gate
  stopped at link with unresolved `drm_checksum_balloon` and
  `drm_vehicle_traction` after the asm block was removed, so this is rejection
  evidence rather than ROM-CRC evidence. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this pointer-addition segment/bounding-box
  setup without a separate model-spill/linkage-family fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 direct guarded-C promotion probe missed. Removing only the
  `NON_EQUIVALENT` wrapper failed the full gate with calculated CRCs
  `0x7856718A/0x66208CAA`; relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` reported `CURRENT (2860)`. The promoted
  source inserted the known unwanted early `gCurrentLevelModel` load/spill at
  `0x60(sp)` and broadened segment/grid/tail register drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` remained 97.30%; do not repeat plain guard removal
  without a separate model-spill/register-family fix.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 scaled collision-plane index local probe missed. The promoted
  source stored `basePlaneIndex * 4` in `temp` and used
  `collisionPlanes[temp + n]`. Full verify failed with calculated CRCs
  `0x7E74218A/0xA93D6001`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` improved from
  promoted baseline `CURRENT (2860)` to `CURRENT (2725)` but still inserted
  the unwanted early `gCurrentLevelModel` load/spill at `0x60(sp)` and kept
  broad segment/grid/tail drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this scaled collision-plane index local
  without a separate model-spill/register-family fix.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted normalization direct-division spelling missed. The source
  shape changed the guarded unit-vector normalization from
  `scale = 1.0f / distance; diffX *= scale; diffZ *= scale;` to direct
  `diffX /= distance; diffZ /= distance;`. Full verify failed with calculated
  CRCs `0xB8B3F2FC/0x19670549`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (2580)`. The diff replaced the
  target reciprocal/multiply family with two divides, shifted labels by
  sixteen bytes, and broadened the final object-dot/checkpoint-dot plus
  vertical FPR drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this normalization
  direct-division spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted wrong-way angle explicit positive-bound spelling missed.
  The source shape changed only the positive half of the wrong-way angle guard
  from `angle > 0x4000` to equivalent `angle >= 0x4001`, preserving the
  existing operand order. Full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The final object-dot/checkpoint-dot plus
  vertical FPR drift was unchanged; source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this wrong-way angle
  explicit positive-bound spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted wrong-way angle explicit negative-bound spelling missed.
  The source removed the `NON_MATCHING` guard and changed only the negative
  half of the wrong-way angle guard from `angle < -0x4000` to equivalent
  `angle <= -0x4001`, preserving the existing operand order. Full verify
  failed with the promoted-baseline calculated CRCs
  `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The key drift remained the final object-dot/checkpoint-dot
  plus vertical FPR allocation tail; source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this wrong-way angle explicit negative-bound spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted post-rewind zero-clamp inclusive comparison probe
  missed. The source removed the `NON_MATCHING` guard and changed only
  `if (splinePos < 0.0f)` to the behavior-equivalent
  `if (splinePos <= 0.0f)` before assigning `splinePos = 0.0f`. Full verify
  failed with calculated CRCs `0x53D141DF/0xF191E9CE`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` regressed from
  promoted baseline `CURRENT (870)` to `CURRENT (1070)`: the local compare
  changed from target `c.lt.s` to `c.le.s`, while the final object-dot/
  checkpoint-dot plus vertical FPR drift remained. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this post-rewind zero-clamp inclusive comparison spelling. A
  sidecar-suggested positive checkpoint-dot/object-dot ordering was not applied
  because it overlaps existing no-repeat positive checkpoint-dot and
  target-dataflow final-tail notes.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted lateral dot explicit pad-minus-pad2 spelling missed.
  The source shape changed the final lateral numerator from negative
  checkpoint-dot plus sum (`pad2 = -checkpointDot; diffX = -((pad + pad2) /
  divisor)`) to positive checkpoint-dot with explicit subtraction
  (`pad2 = checkpointDot; diffX = -((pad - pad2) / divisor)`). Full verify
  failed with calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The final object-dot/checkpoint-dot FPR
  allocation drift was unchanged; source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this lateral
  pad-minus-positive-checkpoint-dot spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted top-tested wave threshold carrier probe missed. The
  source shape kept the current wave loop structure but materialized
  `obj->trans.y_position + 5.0f` through existing local `spCC` before the loop.
  Full verify failed with calculated CRCs `0x5F811F98/0x9CE14139`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (2760)` to `CURRENT (5425)`. The diff hoisted the
  threshold add before the wave pointer load, broadened early wave/FPR drift,
  still lacked target `$f20/$f21` prologue saves, and kept early zeroing in
  `$f16` instead of target `$f14`. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this top-tested `spCC`
  threshold carrier spelling.
- Latest parked-packet revisit note: `func_8008FF1C` remains parked after a
  RHS comma-side-effect direct-table branch probe collapsed into the known
  `CURRENT (125)` family; detailed evidence is in `research/tasks/PARKED.md`.
- Latest alternate-packet note: `func_8002B0F4` remains active after a
  2026-05-24 promoted Z-grid fake marker removal missed. The source shape
  removed only the no-op `if (1) {}` after the `// @fake for s3 vs s2` comment
  before the Z grid loop. Full verify failed with calculated CRCs
  `0x7884718A/0x8596E436`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (2860)` to `CURRENT (2900)`. The diff changed the
  target-like `s3` constant holder to `s2`, preserved the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)`, and broadened grid/tail register
  drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this Z-grid fake-marker
  removal shape.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 promoted five-node fill loop-condition spelling missed. The
  source shape changed only `for (i = 0; (i < 5) ^ 0; i++)` to
  `for (i = 0; i != 5; i++)`. Full verify failed with calculated CRCs
  `0x53905373/0x65198BEE`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1515)`. The fill loop changed
  from target `sltu at,v1,t8`/`bnez at` pointer scheduling to `bne v1,t8`,
  shifted `a2`/`v1` increments and stores, and left the final
  object-dot/checkpoint-dot plus vertical FPR drift unresolved. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  `i != 5` five-node fill loop-condition spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted grounded-wheel integer-zero literal probe missed. The
  source changed only the `NON_EQUIVALENT` guard to `#if 1` and rewrote the
  early grounded-wheel zero stores from `0.0f` to integer `0`. Compressed
  focused diff misleadingly reported `CURRENT (0)`, but full verify failed
  with calculated CRCs `0x5F5DCE35/0xD7FC778D`; uncompressed relinked
  `./diff.sh func_80049794 --no-pager` showed `CURRENT (4895)`. The diff still
  lacked target `$f20/$f21` prologue saves, shifted saved GPR slots down by
  eight bytes, put the two zero stores in separate `$f4`/`$f6` FPRs instead of
  target `$f14`, and left the wave bound/index allocation reversed as current
  `a0` bound / `v1` loop instead of target `v1` bound / `a0` loop. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat literal-only early-zero spelling.
- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 close save-family wave scan probe missed. The promoted shape
  removed the trailing pads, chained the grounded-wheel zero, accumulated the
  first speed `sqrtf` numerator through `var_f6`, and rewrote the wave scan as
  a bottom-tested loop with `var_v1` as the high bound plus `var_f0 =
  obj->trans.y_position + 5.0f` as the threshold carrier. Worker object-only
  focused diff first reported stale `CURRENT (0)`, but the main promoted full
  gate failed with calculated CRCs `0x4FA0E2A5/0x9BEC6D73`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` showed
  `CURRENT (8583)`. Key drift: the frame shrank to `0xf0`, the target
  `$f20/$f21` prologue saves disappeared, early zeroing still used `$f16`
  rather than target `$f14`, and the wave block moved into a different
  register family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this bottom-tested wave
  threshold carrier / pad-removal shape, and do not trust object-only
  `CURRENT (0)` for this function without a promoted full gate plus relinked
  focused diff.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 early lap-reset comparison operand spelling missed. The promoted
  shape changed the lap-reset guard from `racer->nextCheckpoint >= temp_v0` to
  `temp_v0 <= racer->nextCheckpoint`. Full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)` with the final object-dot/checkpoint-dot
  plus vertical FPR drift unchanged. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this early lap-reset
  comparison operand spelling.
- Latest alternate-packet note: `func_80059208` remains active after a
  2026-05-24 early lap-reset `level_id` boolean spelling missed. The promoted
  source removed the `NON_MATCHING` guard and changed only
  `level_id() == 0` to `!level_id()` while preserving the existing
  `racer->nextCheckpoint >= temp_v0` comparison. Full verify failed with the
  promoted-baseline calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  `CURRENT (870)`. The final object-dot/checkpoint-dot plus vertical FPR drift
  remained unchanged; source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and
  `python3 tools/check_active_surface.py` reported active surface ok; do not
  repeat this early lap-reset `level_id` boolean spelling.
- Latest alternate-packet note: `trackbg_render_flashy` remains active after a
  2026-05-24 promoted first-ring raw-sine continuation (`zPositions[3] =
  scaledXCos + (xSin * 1280.0f)` instead of the lone `scaledXSin` use there)
  missed: full verify failed with calculated CRCs `0xF82B92BE/0x5DCC04AE`, and
  relinked `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (1808)` to `CURRENT (5579)`. The
  diff moved the early negative-cosine carrier from target `$f18` toward
  `$f16`, inserted an extra `swc1 $f0,0x110(sp)`, and broadly shifted
  first/outer position-array plus UV scheduling. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this `zPositions[3]` raw
  `xSin * 1280.0f` spelling. A 2026-05-24 color fallback mask literal spelling
  (`var_a3 = ~0xFF` instead
  of `-0x100`) missed with no focused movement: promoted full verify failed
  with calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed
  at promoted baseline `CURRENT (1808)`. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this color fallback
  `~0xFF` mask literal spelling. A 2026-05-24 final vertex `vertY`
  explicit-cast probe (`vertY = (s16)
  (camera->trans.y_position + 192.0f)`) missed with no focused movement:
  object-only focused diff first printed stale `CURRENT (0)`, promoted full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy --no-pager` stayed at promoted baseline
  `CURRENT (1808)`. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this final vertex `vertY`
  explicit-cast spelling. A 2026-05-24 UV carrier probe (`pos.x = pos.z`
  instead of recomputing
  `var_a1 * xCos`) collapsed into the bad first-ring frame-shrink family:
  promoted full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (1808)` to `CURRENT (13821)` with
  frame `0x150` and broad early position-array/global-offset drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  `pos.x = pos.z` UV carrier. A 2026-05-23 `vCoords[8]` plus-negative UV probe
  (`vCoords[8] = (s16) ((2.0f * pos.x) - -var_f16) + var_v1`) missed: full
  verify failed with calculated CRCs `0x1FC35A27/0x9CAAD958`, and relinked
  `./diff.sh trackbg_render_flashy` worsened from promoted baseline
  `CURRENT (1808)` to `CURRENT (2358)` while keeping the early
  negative-cosine register drift and shifting later scheduling. Source was
  restored and final full verify passed; do not repeat this `vCoords[8]`
  plus-negative UV spelling. A sibling 2026-05-23 outer-ring x6
  multiply-order probe (`xPositions[6] =
  scaledXCos - (scaledXSin * 2.0f)`) missed with no relinked focused movement:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy` stayed at promoted baseline
  `CURRENT (1808)`. Source was restored and final full verify passed; do not
  repeat this x6 multiply-order spelling. A sibling 2026-05-23 outer-ring z7
  multiply-order probe (`zPositions[7] = (scaledXCos * 2.0f) - scaledXSin`)
  missed in the same no-movement family: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and relinked `./diff.sh trackbg_render_flashy`
  stayed at promoted baseline `CURRENT (1808)`. Source was restored and final
  full verify passed; do not repeat this z7 multiply-order spelling. Another
  sibling x8 multiply-order probe (`xPositions[8] = -scaledXCos +
  (scaledXSin * 2.0f)`) missed in the same no-movement family: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy` stayed at promoted baseline
  `CURRENT (1808)`. Source was restored and final full verify passed; do not
  repeat this x8 multiply-order spelling. Earlier
  x7/z6/z5/x5
  multiply-order, vertex pointer-loop, color fallback initialization-order,
  final global pointer store-order, final triangle postincrement, and center
  position store-order probes also missed; do not repeat them.
  `func_80059208` also remains active after a 2026-05-24 alternate-route
  sentinel operand-order probe (`if (-1 == temp_v0_4->altRouteID)` at both
  early alternate-route checks) missed: promoted full verify failed with
  calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The final object-dot/checkpoint-dot plus
  vertical FPR drift was unchanged. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this alternate-route
  sentinel operand-order spelling. A 2026-05-24 positive checkpoint-dot
  numerator probe (`pad2 = (tempZ * diffZ) + (diffX * tempX);
  diffX = (pad2 - pad) / divisor`) missed: promoted full verify failed with
  calculated CRCs `0xC7D996EA/0xC6D1DFDE`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1300)`. The diff preserved
  more of the target pre-swap store family than the prior swap-through-`pad`
  miss, but removed the target post-divide `neg.s`, shifted the object-dot FPR
  allocation, and broadened final vertical correction drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` remained 97.30%; do not repeat this positive
  checkpoint-dot numerator spelling. A 2026-05-24 final swap-temp
  spelling (`pad = diffX; diffX = diffZ; diffZ = -pad`) missed: full verify
  failed with calculated CRCs `0x0A689858/0x4CFBB1F6`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1798)`. The diff moved the
  final swap/tail away from the target pre-swap `0x50(sp)` store, shifted the
  object-dot FPR schedule, and broadened final vertical correction register
  drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this final swap through
  `pad` spelling. A 2026-05-24 checkpoint-scale
  divisor lerp probe (`divisor = (scale * splinePos) + (distance * (1.0f -
  splinePos))`) missed: full verify failed with calculated CRCs
  `0x8227660E/0xF9723FA3`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (2955)`. The diff disrupted
  the checkpoint-scale interpolation block and cascaded float-register drift
  through the five-node fill and final tail. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this checkpoint-scale divisor
  lerp spelling. A 2026-05-24 final vertical `pad` clamp-limit carrier probe
  (`pad = 100.0f; if (diffY > pad) ...; if (diffY < -pad) ...`) missed:
  full verify failed with calculated CRCs `0x4400230F/0x7B651F08`, and
  relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (870)` to `CURRENT (1995)`.
  The diff stayed in the bad final vertical clamp-limit carrier family,
  shifted constant/FPR scheduling, and broadened final object-dot/checkpoint-dot
  plus epilogue/global-offset drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this final vertical `pad`
  clamp-limit carrier. `func_80059208` also remains active after 2026-05-24 sibling
  probes around
  the wrong-way counter and final lateral cast carriers missed: spelling the
  wrong-way increment as an explicit byte wrap
  (`racer->wrongWayCounter = (u8) (racer->wrongWayCounter + updateRate)`) and
  routing the final lateral cast through the dead `updateRate` parameter
  (`updateRate = (s32) diffX; racer->unk1BA += updateRate`) both failed full
  verify with calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The final object-dot/checkpoint-dot plus
  vertical FPR drift was unchanged. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat these wrong-way byte-wrap or
  final lateral `updateRate` cast-carrier spellings. A 2026-05-24 final vertical
  `updateRate` cast-carrier probe (`updateRate = (s32) diffY;
  racer->unk1BC += updateRate`) missed: full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (870)`. The final lateral object/checkpoint-dot
  drift and final vertical FPR allocation mismatch were unchanged. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  final vertical `updateRate` cast-carrier spelling. A 2026-05-23 final
  lateral cast
  width probe (`racer->unk1BA += (s16) diffX` instead of `(s32) diffX`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x4EB921DF/0x33EF7BFD`, and relinked
  `./diff.sh func_80059208` worsened from promoted baseline `CURRENT (870)` to
  `CURRENT (935)` by adding a halfword cast/sign-extension family in the final
  lateral update while leaving the object-dot/checkpoint-dot tail drift. Source
  was restored and final full verify passed; do not repeat this final lateral
  `(s16) diffX` cast spelling. A sibling 2026-05-23 final vertical cast-width
  probe (`racer->unk1BC += (s16) diffY` instead of `(s32) diffY`) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x53C341DF/0x1D08B7B9`, and relinked
  `./diff.sh func_80059208` worsened from promoted baseline `CURRENT (870)` to
  `CURRENT (890)`. It added the same narrow-cast/sign-extension direction in
  the final vertical update while leaving the object-dot/checkpoint-dot plus
  vertical FPR drift unresolved. Source was restored and final full verify
  passed; do not repeat this final vertical `(s16) diffY` cast spelling. A
  2026-05-23 explicit final self-add assignment probe
  (`racer->unk1BA = racer->unk1BA + (s32) diffX` and
  `racer->unk1BC = racer->unk1BC + (s32) diffY`) also missed as a no-movement
  family: full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`,
  and relinked `./diff.sh func_80059208` stayed at promoted baseline
  `CURRENT (870)`. Source was restored and final full verify passed; do not
  repeat this explicit final self-add assignment spelling. A
  final vertical clamp-limit carrier through the now-dead `scale` local
  (`scale = 100.0f; if (diffY > scale) ...; if (diffY < -scale) ...`) also
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x4400230F/0x7B651F08`, and relinked
  `./diff.sh func_80059208` worsened from promoted baseline `CURRENT (870)` to
  `CURRENT (1995)`, matching the bad vertical clamp-limit carrier family.
  Source was restored and final full verify passed; do not repeat this final
  vertical `scale` clamp-limit carrier. A checkpoint-distance complement
  single-precision literal probe (`splinePos = 1.0f -
  racer->checkpoint_distance`) also missed: full verify failed with calculated
  CRCs `0xC0802A15/0xAB5B7DB7`, and relinked `./diff.sh func_80059208`
  regressed from promoted baseline `CURRENT (870)` to `CURRENT (3020)`. The
  diff changed the first complement from the target double subtract to a
  single-precision `sub.s`, shifted the early checkpoint-distance branches, and
  broadened downstream FPR/register scheduling. Source was restored and final
  full verify passed; do not repeat this checkpoint-distance `1.0f`
  complement spelling. A wrong-way velocity threshold single-precision literal
  probe (`racer->velocity <= -1.0f` instead of the current double literal)
  also missed: full verify failed with calculated CRCs
  `0x10768535/0x41CC0F5A`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (2130)`. The diff changed
  the wrong-way velocity compare away from the target double-compare family and
  broadened downstream labels/final-tail drift. Source was restored and final
  full verify passed; do not repeat this wrong-way velocity `-1.0f` spelling.
  A 2026-05-24 promotion-only check of the current C also failed the canonical
  gate: after removing the `NON_MATCHING` guard, uncompressed
  `./diff.sh func_80059208 --no-pager` reported `CURRENT (0)`, but
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` failed SHA with calculated CRCs
  `0x53D141DF/0xB9D4B481`. Object sections kept matching sizes and inspected
  `.rodata` bytes matched, but source was restored because acceptance requires
  full `Verify: OK`; do not promote `func_80059208` from focused `CURRENT (0)`
  alone.
  A nested wrong-way counter condition probe (`if (wrongWayCounter < 200) { if
  (velocity <= -1.0) ... }`) also missed: full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`, and relinked `./diff.sh func_80059208` stayed
  at promoted baseline `CURRENT (870)` with the same final lateral/vertical
  object-dot and tempY register drift. Source was restored and final full verify
  passed; do not repeat this nested wrong-way counter spelling.
  Earlier final vertical reciprocal-multiply,
  courseCheckpoint threshold, splineIndex comparison-direction, normalization
  reciprocal double-literal, normalization guard comparison-order, and
  magnitude sum-order probes also missed; do not repeat them.
  `func_8002B0F4` also remains active after a 2026-05-24 promoted
  coordinate-local type probe (`s32 XInInt`/`ZInInt` narrowed to `s16`)
  missed: full verify failed with calculated CRCs
  `0x93CE4D86/0x8EE561B4`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (4425)`. The narrowed locals inserted extra sign-extension
  scheduling, shifted `spB0` from target `0xb0(sp)` to current `0xb4(sp)`, and
  retained the unwanted pre-loop `gCurrentLevelModel` spill at `0x64(sp)` with
  broad segment/grid/tail drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this `XInInt`/`ZInInt`
  `s16` local-type spelling. A 2026-05-24 promoted
  collision-plane scalar-local probe (`Vec4f tempVec4f` replaced with
  `planeX`/`planeY`/`planeZ`/`planeW`) missed as a no-movement family: full
  verify failed with the promoted-baseline calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` plus broad segment/grid/tail register drift remained. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  collision-plane scalar-local spelling. A 2026-05-24 early `sp108`
  positive-range guard spelling (`if (!(sp108 != 0 && sp108 < 8))`) missed:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, and
  relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed
  at promoted baseline `CURRENT (2860)`. The unwanted pre-loop
  `gCurrentLevelModel` spill at `0x60(sp)` plus broad segment/grid/tail
  register drift remained. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this early `sp108`
  positive-range guard spelling. A 2026-05-24 dead `vert = NULL`
  lifetime-seed probe before the outer segment loop missed: full verify failed
  with calculated CRCs `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2860)`. The unwanted pre-loop
  `gCurrentLevelModel` load/spill at `0x60(sp)` and broad segment/grid/tail
  register drift were unchanged. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this dead `vert = NULL`
  lifetime-seed spelling. A 2026-05-24 pre-call coordinate conversion probe
  (`XInInt = xIn; ZInInt = zIn; sp108 = get_inside_segment_count_xz(XInInt,
  ZInInt, spB0)`, with the per-segment conversions removed) missed: full
  verify failed with the promoted-baseline calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2860)`. The diff still inserted the unwanted
  pre-loop `gCurrentLevelModel` spill at `0x60(sp)` with broad
  segment/grid/tail register drift. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this current-source pre-call
  `XInInt`/`ZInInt` conversion plus int-call spelling. `func_8002B0F4` remains
  active after a 2026-05-24
  triangle-inside boolean
  width probe (`s16 temp_ra_1`, `temp_ra_2`, `temp_ra_3` instead of `s32`)
  missed: full verify failed with calculated CRCs `0x987293C4/0xFED1F035`,
  and relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  worsened to `CURRENT (4658)`. The diff shifted `spB0` from target
  `0xb0(sp)` to `0xb4(sp)` and retained the unwanted early
  `gCurrentLevelModel` spill family with broad segment/grid/tail drift. Source
  was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  `temp_ra_*` `s16` boolean-width spelling. A 2026-05-23 Z-grid bitmask doubling
  probe (`var_a1 += var_a1` only in the second grid loop) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x77E6007A/0x78D4AD50`, and relinked
  `./diff.sh func_8002B0F4` regressed to `CURRENT (4130)` while still inserting
  the unwanted early `gCurrentLevelModel` spill at `0x60(sp)` with broad
  segment/grid/tail drift. Source was restored and final full verify passed; do
  not repeat this single Z-grid `var_a1 += var_a1` spelling. The sibling X-grid
  bitmask doubling probe (`var_a1 += var_a1` only in the first grid loop)
  missed with a more interesting relinked focused improvement to
  `CURRENT (1805)`, but still retained the same model-spill family; do not
  repeat that single X-grid spelling either. Combining the better pad3-removal
  stack-shape branch with that X-grid `var_a1 += var_a1` spelling also missed:
  full verify failed with calculated CRCs `0x78D4C01A/0xEA4191D0`, relinked
  `./diff.sh func_8002B0F4` reported `CURRENT (1813)`, and the unwanted early
  `gCurrentLevelModel` spill remained at `0x64(sp)` with broad
  segment/grid/tail drift. Source was restored and final full verify passed;
  do not repeat this combined pad3-removal plus X-grid doubling spelling. A
  sibling collision-plane index local type probe (`s32 temp` to `u16 temp`,
  matching `basePlaneIndex`) missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked `./diff.sh func_8002B0F4` stayed at
  promoted baseline `CURRENT (2860)`. It kept the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` with broad segment/grid/tail drift.
  Source was restored and final full verify passed; do not repeat this
  collision-plane index local type spelling. A sibling collision-plane
  nonzero literal-type probe (`if (tempVec4f.y != 0.0f)` instead of the
  current double literal) also missed: full verify failed with calculated CRCs
  `0xF03EAC35/0x346A795F`, and relinked `./diff.sh func_8002B0F4` regressed
  to `CURRENT (3815)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` and broadened segment/grid/tail
  drift. Source was restored and final full verify passed; do not repeat this
  collision-plane nonzero `0.0f` literal spelling. A current-source
  surface-skip branch inversion probe also missed: promoting the current C and
  changing only the water/hidden-collision guard to an inverted empty-if
  (`surface == SURFACE_WATER_CALM || surface == SURFACE_WATER_UNK_F ||
  !flags`) with `currentFaceOffset = nextFaceOffset` in `else` failed full
  verify with calculated CRCs `0x77D9E18A/0xB9F696E2`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` regressed from
  the promoted baseline `CURRENT (2780)` to `CURRENT (2995)`. The diff still
  inserted the unwanted early `gCurrentLevelModel` spill at `0x60(sp)`,
  broadened segment/grid register rotation, and shifted tail labels by 4
  bytes. Source was restored and final full verify passed; do not repeat this
  inverted empty-if surface-skip branch shape. A current-source bottom
  `func_800BB2F4` rot-output address spelling probe also missed: changing
  `&(yOutCount + D_8011D128)->rot` to `&D_8011D128[yOutCount].rot` failed full
  verify with calculated CRCs `0x7A567F98/0xC658B8F4`, and relinked
  `./diff.sh func_8002B0F4` regressed to `CURRENT (4298)`. The diff changed the
  bottom call address setup to `addiu a3,v1,4`, spilled `v1` at `0x68(sp)`, and
  widened the known unwanted early `gCurrentLevelModel` spill/tail register
  drift. Source was restored and final full verify passed; do not repeat this
  bottom rot-output address spelling. A 2026-05-24 current-source declaration
  probe adding `register` to `currentSegment` and `currentBoundingBox` also
  missed as a no-movement family: full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)` with the same unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` and broad segment/grid/tail drift. Source was restored and final
  full verify passed; do not repeat these segment-pointer register hints.
  A 2026-05-24 promoted current-source global-clear literal spelling
  (`D_8011D308 = FALSE` instead of `0`) also missed as a no-movement family:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2860)`. The diff retained the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` plus broad segment/grid/tail register drift. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` remained 97.30%; do not repeat this global-clear `FALSE`
  literal spelling.
  Earlier partial/default water store-order, explicit default-water height
  cast, bottom segment-range guard reorder, target default-water store-order,
  and bottom-water condition-order probes also missed; do not repeat them.
- Latest no-park routing note: `func_80049794` remains active and should not be
  parked solely because the current source-shape families are saturated. A
  2026-05-24 current-baseline `spA2` type probe (`s32 spA2` instead of the
  current byte local) missed: full verify failed with calculated CRCs
  `0x37DDDF63/0x9ECDB374`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed from
  promoted baseline `CURRENT (2760)` to `CURRENT (3417)`. It widened the frame
  to `0x100`, shifted saved-register slots, changed the expected byte-local
  traffic into word traffic around `0xa4(sp)`, still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  `spA2` `s32` type spelling. A
  2026-05-24 worker-tested saved wave-count/bound carrier
  (`var_v0 = gRacerWaveCount; var_v1 = var_v0 - 1; var_a0 = var_v1`, terminal
  compare against `var_v1`) missed: full verify failed with calculated CRCs
  `0xC79BC23F/0x82216C34`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (2760)` to `CURRENT (5580)`. The diff still
  lacked target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and moved the wave scan into an `a1/a0/v0` drift family
  instead of target `v0` count, `v1` saved bound, and `a0` loop index. Worker
  source was restored and active-surface check passed; do not repeat this
  saved wave-count/bound carrier without a separate proven saved-FPR source
  shape. A 2026-05-24 worker-tested manual first-load / loop-flag wave scan
  (`var_v1 = gRacerWaveCount - 1; var_a0 = var_v1`, first compare into
  `var_v0`, then `while (var_v0)` decrementing only `var_a0`) missed:
  full verify failed with calculated CRCs `0xF20C8121/0xFE69FF37`, and
  relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (2760)` to `CURRENT (10125)`.
  The diff allocated count/bound/index as current `a0`/`a3`/`v0` plus a
  loop-flag `v1`, not target `v0` count, `v1` saved bound, and `a0` loop
  index; it also inserted `spA2` stack-byte traffic, dropped target
  `$f20/$f21` prologue saves, and kept early zero in `$f16` instead of target
  `$f14`. Worker source was restored and active-surface check passed; do not
  repeat this manual first-load / loop-flag wave-scan spelling. A
  2026-05-24 worker-tested post-`sqrtf` `spCC` carrier
  (`spCC = sqrtf(...); var_f20 = spCC - 2.0`) missed: focused
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` worsened from the
  promoted baseline `CURRENT (2760)` to `CURRENT (3154)`. The diff still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave bound/index allocation reversed as current
  `a0`/`v1`, and broadened later first-speed/gravity scheduling. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` remained 97.30%; do not repeat this post-`sqrtf` `spCC`
  carrier. A 2026-05-24 worker-tested top-speed live-float carrier through
  `spCC` (`spCC = var_f14; var_f14 = (spCC *
  handle_racer_top_speed(obj, racer)) * 1.8`) optimized away against the
  promoted object: `NON_MATCHING=1` object compile plus
  `./diff.sh -o func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (0)`, so it produced no useful movement and is not matching
  progress. Source was restored and `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`; do not repeat this
  simple top-speed `spCC` live-float carrier or accept object-only
  `CURRENT (0)` as progress. A 2026-05-24 worker-tested current-baseline
  wave pointer-cache probe (`lastWaveIndex = gRacerWaveCount - 1; wave =
  &gRacerCurrentWave[var_a0]; if (var_a0 == lastWaveIndex) { var_a0--;
  wave--; }`, then use `wave[1]`) missed: compressed focused diff first
  printed stale `CURRENT (0)`, promoted full verify failed with calculated CRCs
  `0x9CF1F322/0x005EC88D`, and uncompressed `./diff.sh func_80049794
  --no-pager` showed `CURRENT (5700)`. The probe widened the frame to `0x100`,
  dropped target `$f20/$f21` prologue saves, kept early zero in `$f16`, and
  moved wave scan registers into a `v1/a0/v0` drift family. Source was
  restored; do not repeat this current-baseline wave pointer-cache spelling or
  trust compressed `CURRENT (0)` on this function without uncompressed/full-gate
  evidence. A
  2026-05-24 current-baseline wave-gate positive-count probe
  (`... && gRacerWaveCount > 0` instead of `gRacerWaveCount != 0`) missed:
  full verify failed with calculated CRCs `0x2FDDE03F/0xA529100F`, and
  relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (2760)` to `CURRENT (2960)`. It
  changed the gate to `blez`, still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop. Source was
  restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  and `./score.sh -s` remained 97.30%; do not repeat this positive-count
  wave-gate spelling. A 2026-05-24 current-baseline course-height trick-type
  guard reorder (`racer->trickType >= -1 && racer->trickType < 2 && var_f2 <
  0`) also missed: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEE2BD2FC`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3170)`. It changed the local branch family but still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this course-height
  trick-type guard order. A 2026-05-24 current-baseline zap sound null spelling
  (`sound_play(SOUND_ZAP4, 0)` instead of `NULL`) also missed as a no-movement
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and
  relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  at promoted baseline `CURRENT (2760)`. It still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave bound/index allocation reversed as current `a0`-bound/`v1`-loop.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  `SOUND_ZAP4` `0` null-argument spelling. A
  2026-05-23 current-baseline `spA3` type probe (`s32 spA3` instead of the
  current byte local) missed: full verify failed with calculated CRCs
  `0x8FDDDF9D/0x16677070`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (4010)`. It widened the frame to `0x100`, changed the target
  byte-local traffic around `0xa3(sp)` into word traffic around `0xa8(sp)`,
  still lacked target `$f20/$f21` prologue saves, kept early zero in `$f16`
  instead of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify passed;
  do not repeat this `spA3` `s32` type spelling. A sibling current-baseline
  `spA1` type probe (`s32 spA1` instead of the current byte local) also missed:
  full verify failed with calculated CRCs `0x8FDDDF73/0x95ACB78A`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (3225)`. It widened the frame
  to `0x100`, shifted the target byte-local traffic around `0xa3(sp)` to
  `0xab(sp)`, still lacked target `$f20/$f21` prologue saves, kept early zero in
  `$f16` instead of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify passed;
  do not repeat this `spA1` `s32` type spelling. A sibling current-baseline
  `spA2` type probe (`s32 spA2` instead of the current byte local) also
  missed: full verify failed with calculated CRCs `0x37DDDF63/0x9ECDB374`,
  and relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  regressed to `CURRENT (3417)`. It widened the frame to `0x100`, shifted
  saved-register slots, changed the expected byte-local traffic into word
  traffic around `0xa4(sp)`, still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan in
  the current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this `spA2` `s32` type spelling. A sibling
  current-baseline `newSpinoutTimer` type probe (`s32 newSpinoutTimer`
  instead of the current dead byte local) also missed: full verify failed with
  calculated CRCs
  `0x5FDDDF2F/0xDBEDB019`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (3245)`. It widened the frame to `0x100`, shifted the target
  byte-local traffic around `0xa3(sp)` to `0xab(sp)`, still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target `$f14`,
  and left the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this `newSpinoutTimer`
  `s32` type spelling. A current-baseline zipper rumble enum spelling probe
  (`rumble_set(racer->playerIndex, RUMBLE_TYPE_8)` instead of the current
  literal `8`) also missed as a no-movement family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target `$f14`,
  and left the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this zipper rumble
  `RUMBLE_TYPE_8` spelling. A current-baseline zipper success range-order probe
  (`steerVisualRotationOffset > -0x400 && steerVisualRotationOffset < 0x400`
  instead of the current upper-bound-first spelling) also missed: full verify
  failed with calculated CRCs `0x27DDE03F/0x4EBA4D1F`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (3170)`. The focused diff
  inverted the local branch polarity/order against the target, which tests
  `< 0x400` first and then `> -0x400`; it still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was restored
  and final full verify passed; do not repeat this zipper success range-order
  spelling. A
  2026-05-23 current-baseline independent drift-reset check probe
  (`if (racerVelocity < 8.0) { reset } if (gCurrentStickY < -10) { reset }`
  instead of the current `||` guard) missed: full verify failed with
  calculated CRCs `0xEAC7CF58/0x7D4B28D3`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (3590)`. It still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and changed the drift-reset branch shape away from the target.
  Source was restored and final full verify passed; do not repeat this
  independent drift-reset check spelling. A
  2026-05-23 current-baseline grounded-wheel surface-scan condition-order
  probe (`i < racer->wheel_surfaces[var_t0] &&
  racer->wheel_surfaces[var_t0] != SURFACE_NONE` instead of the current
  `SURFACE_NONE`-first guard) missed: full verify failed with calculated CRCs
  `0x5FDDE2A9/0xD5199208`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (3160)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and broadened later gravity/surface
  scheduling. Source was restored and final full verify passed; do not repeat
  this grounded-wheel surface-scan condition-order spelling. A sibling
  grounded-wheel brake-particle viewport condition-order probe
  (`gNumViewports < 3 && (gCurrentRacerInput & B_BUTTON)` instead of the
  current input-first guard) also missed: full verify failed with calculated
  CRCs `0x60DFE03F/0x93188AD7`, and relinked `./diff.sh func_80049794`
  regressed to `CURRENT (3195)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  scan in the current `a0`-bound/`v1`-loop family, and broadened later
  gravity/particle scheduling. Source was restored and final full verify
  passed; do not repeat this brake-particle viewport condition-order spelling.
  A sibling grounded-wheel zip-pad boost condition-order probe
  (`i == SURFACE_ZIP_PAD && racer->boostTimer == 0` instead of the current
  boost-timer-first guard) also missed: full verify failed with calculated CRCs
  `0x67DFE437/0xF7295BC5`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (3505)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and broadened later
  gravity/zip-pad/sound scheduling. Source was restored and final full verify
  passed; do not repeat this zip-pad boost condition-order spelling. A sibling
  grounded-wheel Taj-pad condition-order probe (`i == SURFACE_TAJ_PAD &&
  racer->playerIndex == PLAYER_ONE && gCurrentButtonsPressed & Z_TRIG` instead
  of the current player-first guard) also missed: full verify failed with
  calculated CRCs `0x5FDDE03B/0x1C5F94A8`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (3145)`. It still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and broadened later gravity/Taj-pad scheduling. Source was restored
  and final full verify passed; do not repeat this Taj-pad condition-order
  spelling. A sibling grounded-wheel brake-drag condition-order probe
  (`gCurrentStickY >= -40 && (gCurrentRacerInput & B_BUTTON) &&
  racer->velocity >= -0.5` instead of the current input-first guard) also
  missed: full verify failed with calculated CRCs `0xE653A2AA/0x3FD8E10F`,
  and relinked `./diff.sh func_80049794` regressed to `CURRENT (6085)`. It
  still lacked target `$f20/$f21` prologue saves, kept early zero in `$f16`
  instead of target `$f14`, left the wave scan in the current
  `a0`-bound/`v1`-loop family, and greatly broadened later
  gravity/brake/sound scheduling. Source was restored and final full verify
  passed; do not repeat this brake-drag condition-order spelling. A
  sibling grounded-wheel `spD8` multiplier literal probe (`spD8 *= 8.0f`
  instead of `spD8 *= 8`) also missed: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and kept the later `$f14`/`$f20`
  save-family register drift. Source was restored and final full verify
  passed; do not repeat this grounded-wheel `spD8` multiplier literal spelling.
  A
  2026-05-23 current-baseline early `spA1` initialization probe (moving
  `spA1 = FALSE` next to `playerObjectMoved = FALSE` and removing the later
  assignment inside the normal flight branch) missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x9935B12E/0xC848F044`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (4735)`. It widened local stack-byte traffic, removed the target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and pushed the wave block back into broad register drift. Source was
  restored and final full verify passed; do not repeat this early `spA1`
  initialization placement. A
  2026-05-23 close save-family selected-wave index carrier probe
  (`var_t9 = var_a0 + 1`, then using `gRacerCurrentWave[var_t9]` for the
  post-scan `waveHeight` and `rot.y` accesses on top of the x/z/y
  pre-`sqrtf`, chained-zero, no-trailing-pad shape) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x1457E419/0x21494B92`, and the relinked focused diff
  regressed to `CURRENT (6025)`. It kept the target `0xf8` frame and
  `$f20/$f21` saves but broadened the wave block into `a0`/`v1`/`t*` register
  churn, left early zero in `$f16` instead of target `$f14`, and disturbed
  later call-adjacent scheduling. Source was restored and final full verify
  passed; do not repeat this close-branch selected-wave index carrier. A
  2026-05-23 current-baseline wave-height threshold commute
  (`gRacerCurrentWave[var_a0]->waveHeight < 5 + obj->trans.y_position`
  instead of `obj->trans.y_position + 5`) missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FE1E03F/0x88CC2028`, and the relinked focused diff worsened to
  `CURRENT (2770)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this current-baseline wave-height threshold
  commute. A
  2026-05-23 current-baseline attach-point model-index postincrement probe
  (`temp_v0_obj->modelIndex++` instead of `temp_v0_obj->modelIndex += 1` for
  the first attach-point model advance) missed as a no-movement
  promoted-baseline family: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in
  the current `a0`-bound/`v1`-loop family, and only shifted constants and
  later call targets in the promoted current-baseline family. Source was
  restored and final full verify passed; do not repeat this attach-point
  model-index postincrement spelling. A sibling attach-point store-order probe
  (moving the first third-attach-object `modelIndex += 1` before
  `trans.rotation.y_rotation = 0x4000`) also missed as a no-movement
  promoted-baseline family: full verify failed with calculated CRCs
  `0x5CF5E03F/0x566478E3`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this attach-point model-index/rotation
  store-order spelling. A sibling final `unk201` particle-reset condition
  inversion probe (`if (racer->unk201 != 0) { } else { ... }` instead of
  `if (racer->unk201 == 0)`) also missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  relinked `./diff.sh func_80049794` stayed `CURRENT (2760)`, and focused
  object disassembly still showed the local target tail
  `lb 0x201(s0)`/`bnez`/`sw zero,0x74(s1)` pattern at
  `func_80049794+0x289c`. It still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family. Source was restored and final
  full verify passed; do not repeat this final `unk201` condition-inversion
  spelling. A sibling attach-point count-threshold spelling probe (changing
  both late `obj->attachPoints->count >= 3` guards to `count > 2`) also missed
  as a no-movement promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly still emitted the same `slti at,count,3`/`bnez` guard family at
  both attach-point checks. It still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family. Source was restored and final
  full verify passed; do not repeat this attach-point `count > 2` spelling. A
  sibling attach-point lowering compound-assignment probe (changing both
  `trans.y_position = trans.y_position - 2.0` stores to
  `trans.y_position -= 2.0`) also missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  relinked `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted
  object disassembly still emitted the same local double-subtract/cvt.s block
  for both attach-point lowering paths. It still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this attach-point
  `-= 2.0` lowering spelling. A sibling attach-point raising
  compound-assignment probe (changing both
  `trans.y_position = trans.y_position + 1.0f` stores to
  `trans.y_position += 1.0f`) also missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  relinked `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted
  object disassembly still emitted the same local `add.s`/store sequence for
  both attach-point raising paths. It still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this attach-point
  `+= 1.0f` raising spelling. A
  2026-05-23 current-baseline attach-point grounded-wheel branch-order probe
  (`if (spA2 != FALSE || racer->groundedWheels != 0)` instead of the existing
  grounded-wheels-first guard) missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0x16726463`,
  and the relinked focused diff stayed `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and only shifted constants and later call targets in the promoted
  current-baseline family. Source was restored and final full verify passed;
  do not repeat this attach-point grounded-wheel branch-order spelling. A
  2026-05-23 current-baseline late boost-emitter branch-order probe
  (`if (var_t0 < 10) { low boost object tests } else { high boost object
  tests }` instead of the existing `var_t0 >= 10` split) missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x631891D7/0xA31290E5`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in
  the current `a0`-bound/`v1`-loop family, and only shifted constants and
  later call targets in the promoted current-baseline family. Source was
  restored and final full verify passed; do not repeat this late
  boost-emitter branch-order spelling. A 2026-05-23 current-baseline late
  boost-emitter nonzero compare probe (`boostObj->unk70 != 0` instead of
  `boostObj->unk70 > 0` in the high boost object test) missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x5FDDE03F/0xB46C45DD`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family. Source was restored and final
  full verify passed; do not repeat this late boost-emitter nonzero compare
  spelling. A worker-tested sibling late boost-emitter high-boost
  condition-order probe (`boostObj->unk74 > 0.0 || boostObj->unk70 > 0`
  instead of the current `unk70`-first guard) also missed as a no-movement
  promoted-baseline family: probe verify failed with calculated CRCs
  `0x5FE1E03F/0xA0AF4D76`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Worker source was restored and verified;
  do not repeat this high-boost `unk74 || unk70` operand-order spelling. A
  sibling late boost-emitter pointer-index spelling probe
  (`boostObj += racer->racerIndex` instead of
  `boostObj = &boostObj[racer->racerIndex]`) missed: full verify failed with
  calculated CRCs `0x5A11E03F/0x019B7EA6`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly changed the local pointer add to `addu v1,v0,t9` instead of the
  target/current `addu v1,t9,v0`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored and
  final full verify passed; do not repeat this late boost-emitter pointer
  `+= racerIndex` spelling. A 2026-05-23 current-baseline race-start
  y-velocity double-literal
  probe (`obj->y_velocity = -5.0` instead of `-5.0f` in the
  `gRaceStartTimer == 100` path) missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  and the relinked focused diff stayed `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and only shifted constants and later call targets in the promoted
  current-baseline family. Source was restored and final full verify passed;
  do not repeat this race-start y-velocity double-literal spelling. A
  2026-05-23 current-baseline late position-delta reciprocal double-literal
  probe (`var_f0 = 1.0 / updateRateF` instead of `1.0f / updateRateF`) missed:
  full verify failed with calculated CRCs `0x916D4F5C/0xD6E2A760`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (6207)`. It widened the frame
  to `0x100`, dropped target `$f20/$f21` prologue saves, kept early zero in
  `$f16` instead of target `$f14`, shifted late rodata/global offsets, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was restored
  and final full verify passed; do not repeat this late position-delta
  reciprocal double-literal spelling. A
  2026-05-23 current-baseline first transform `x_rotation` store-order probe
  (move `gCurrentRacerTransform.rotation.x_rotation =
  obj->trans.rotation.x_rotation` after the zero position stores, before
  `scale`) missed: full verify failed with calculated CRCs
  `0xDBDDE1B6/0x5C94BA6C`, and relinked `./diff.sh func_80049794` reported
  `CURRENT (3350)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, shifted late rodata/global
  offsets, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this first
  transform `x_rotation` store-order spelling. A
  2026-05-23 current-baseline first transform `sp60` call-site cast probe
  (use `(MtxF *) &sp60` for the three first `mtxf_transform_point` calls while
  leaving `sp60` as `f32 sp60[4]`) missed: it compiled with incompatible
  pointer-type warnings, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, shifted late
  rodata/global offsets, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify
  passed; do not repeat this first transform `sp60` call-site cast spelling. A
  2026-05-23 current-baseline first transform scale-before-position store-order
  probe (move `gCurrentRacerTransform.scale = 1.0f` before the zero position
  stores) also missed as a no-movement promoted-baseline family: full verify
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this first
  transform scale-before-position store-order spelling. A
  movement-block approach-target pointer-test spelling probe
  (`if (!racer->approachTarget)` instead of `== NULL`) also missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x5FDDE03F/0xEF7A0514`, and relinked `./diff.sh func_80049794`
  stayed `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored and
  final full verify passed; do not repeat this movement-block approach-target
  pointer-test spelling. A
  2026-05-23 current-baseline brake lower-clamp zero literal probe
  (`if (racer->brake < 0) { racer->brake = 0; }` instead of the `0.0f`
  compare/store) missed: full verify failed with calculated CRCs
  `0xDDB58EAF/0x090C564F`, and the relinked focused diff regressed to
  `CURRENT (4835)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and widened later gravity/buoyancy
  float-register scheduling. Source was restored and final full verify passed;
  do not repeat this brake lower-clamp zero literal spelling. A
  2026-05-23 current-baseline A-button throttle clamp literal probe
  (`racer->throttle = 1.0f` and `racer->throttle < 0.0f` instead of
  `racer->throttle = 1` and `racer->throttle < 0`) missed as a no-movement
  promoted-baseline family: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and only shifted constants and later
  call targets in the promoted current-baseline family. Source was restored and
  final full verify passed; do not repeat this A-button throttle clamp literal
  spelling. A
  2026-05-23 current-baseline A-button throttle upper-store single-precision
  probe (`racer->throttle = 1.0f` only, leaving the surrounding compare and
  lower clamp unchanged) also missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  and relinked `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not
  recover target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify
  passed; do not repeat this A-button throttle upper-store `1.0f` spelling. A
  2026-05-23 current-baseline A-button throttle upper-compare single-precision
  probe (`if (racer->throttle > 1.0f)`) also missed: full verify failed with
  calculated CRCs `0x60AF757D/0x32C9B3B0`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (4400)`. It dropped the
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and widened later gravity/particle FPR scheduling. Source was
  restored and final full verify passed; do not repeat this A-button throttle
  upper-compare `1.0f` spelling. A sibling current-baseline A-button throttle
  lower-compare single-precision probe (`if (racer->throttle < 0.0f)`,
  leaving the upper compare/store unchanged) also missed: full verify failed
  with calculated CRCs `0xA746C795/0x4D4908D0`, and relinked
  `./diff.sh func_80049794 --max-size 900 --compress-matching 2 --no-pager`
  reported `CURRENT (2430)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  scan in the current `a0`-bound/`v1`-loop family, and widened later
  throttle/gravity/boost FPR drift. Source was restored and final full verify
  passed; do not repeat this A-button throttle lower-compare `0.0f` spelling.
  A
  2026-05-23 current-baseline low-speed drag multiply grouping probe
  (`racer->velocity * (spD8 * 8.0f)` instead of
  `racer->velocity * spD8 * 8.0f`) missed: full verify failed with calculated
  CRCs `0x5FD5CB40/0x334EF099`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and only shifted constants and later
  call targets in the promoted current-baseline family. Source was restored and
  final full verify passed; do not repeat this low-speed drag multiply
  grouping spelling. A
  2026-05-23 current-baseline low-speed drag condition-order probe
  (`!(gCurrentRacerInput & A_BUTTON) && spEC < 1.0f` instead of
  `spEC < 1.0f && !(gCurrentRacerInput & A_BUTTON)`) missed: full verify
  failed with calculated CRCs `0x5FDDE03B/0xCF4A45EB`, and the relinked
  focused diff stayed `CURRENT (2760)`. It did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and only shifted
  constants and later call targets in the promoted current-baseline family.
  Source was restored and final full verify passed; do not repeat this
  low-speed drag condition-order spelling. A
  2026-05-23 current-baseline vertical drag scale grouping probe
  (`racer->unk34 * (spD0 * 4.0f)` instead of
  `4.0f * (racer->unk34 * spD0)`) missed: full verify failed with calculated
  CRCs `0x5FF4CBE3/0xAB5E4543`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and only shifted constants and later
  call targets in the promoted current-baseline family. Source was restored and
  final full verify passed; do not repeat this vertical drag scale grouping
  spelling. A
  2026-05-23 current-baseline lateral drag scale grouping probe
  (`racer->lateral_velocity * (spD4 * 4.0f)` instead of
  `racer->lateral_velocity * spD4 * 4.0f`) missed: full verify failed with
  calculated CRCs `0x6001A43F/0x2E622A7C`, and the relinked focused diff
  stayed `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  scan in the current `a0`-bound/`v1`-loop family, and only shifted constants
  and later call targets in the promoted current-baseline family. Source was
  restored and final full verify passed; do not repeat this lateral drag scale
  grouping spelling. A
  2026-05-23 current-baseline trick lift scale constant-grouping probe
  (`racer->velocity * (0.058823529411764705 * 1.5)` instead of
  `racer->velocity * 0.058823529411764705 * 1.5`) missed: full verify failed
  with calculated CRCs `0x57E6973B/0x9F5650FC`, and the relinked focused diff
  stayed `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  scan in the current `a0`-bound/`v1`-loop family, and only shifted constants
  and later call targets in the promoted current-baseline family. Source was
  restored and final full verify passed; do not repeat this trick lift scale
  constant-grouping spelling. A
  2026-05-23 current-baseline brake negative-velocity double-zero probe
  (`racer->velocity < 0.0` instead of `racer->velocity < 0.0f` in the
  B-button brake condition) missed: full verify failed with calculated CRCs
  `0x334AD7AC/0x83F55E31`, and the relinked focused diff regressed to
  `CURRENT (5125)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, left the wave scan in the
  current `a0`-bound/`v1`-loop family, and added broad double-conversion
  scheduling around the later brake/gravity path. Source was restored and
  final full verify passed; do not repeat this brake negative-velocity
  double-zero spelling. A
  2026-05-23 current-baseline forwardVel damping sum-order probe
  (`((racer->velocity * 0.05) + racer->forwardVel)` instead of
  `(racer->forwardVel + (racer->velocity * 0.05))`) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x5FDD003F/0x3118A39C`, and the relinked focused diff
  stayed `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family while later gravity remained
  in the wrong `$f14` family. Source was restored and final full verify passed;
  do not repeat this forwardVel damping sum-order spelling. A
  2026-05-23 current-baseline grounded stick-scale operand-order probe
  (`gCurrentStickY = ((f32) gCurrentStickY) * (1.0 - var_f20)`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x6036E63F/0x817F988F`, and the relinked
  focused diff regressed to `CURRENT (2795)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family
  while shifting later gravity registers toward the `$f14` family. Source was
  restored and final full verify passed; do not repeat this grounded
  stick-scale operand-order spelling. A
  2026-05-23 current-baseline boost non-positive-first branch-order probe
  (`if (racer->boostTimer <= 0) { reset } else if (gRaceStartTimer == 0)`)
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x27DDE041/0xF6868CFC`, and the relinked
  focused diff stayed `CURRENT (2760)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this boost
  non-positive-first branch-order spelling. A
  2026-05-23 current-baseline boost-active assignment-order probe also missed:
  promoting the current C and moving `racer->boostTimer -= updateRate` before
  `racer->throttle = 1` failed full verify with calculated CRCs
  `0xF1E91063/0x5815ED91`, and the relinked focused diff improved from
  promoted baseline `CURRENT (2760)` to `CURRENT (2430)` but still missed
  target `$f20/$f21` prologue saves, kept the early zero in `$f16`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. A sibling order
  (`racer->throttle = 1; racer->boostTimer -= updateRate; var_f14 = 2.0f`)
  also stayed `CURRENT (2430)` but failed with baseline CRCs
  `0x5FDDE03F/0xEF7A0514`. Source was restored and final full verify passed;
  do not repeat these boost-active assignment-order spellings. Next
  `func_80049794` work should pivot away from boost assignment ordering unless
  paired with a broader saved-FPR or wave bound/index allocation hypothesis. A
  2026-05-23 current-baseline implicit wave-count gate probe
  (`... && gRacerWaveCount` instead of `... && gRacerWaveCount != 0`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this implicit wave-count gate spelling. A
  2026-05-23 current-baseline terminal wave-bound inverted empty-if probe
  (`if (var_a0 != gRacerWaveCount - 1) { } else { var_a0--; }`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this terminal wave-bound inverted empty-if
  spelling. A
  2026-05-23 current-baseline `spA2` declaration-initialization probe
  (`s8 spA2 = FALSE;` with the later standalone assignment removed) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0xC22DF330/0x3B2BA987`, and the relinked focused
  diff regressed to `CURRENT (4869)`. It inserted an early `sb zero,0xa2(sp)`,
  lost target `$f20/$f21` prologue saves after relink, kept early zero in
  `$f16`, and widened the wave-scan register/order drift. Source was restored
  and final full verify passed; do not repeat this `spA2`
  declaration-initialization spelling. A
  2026-05-23 current-baseline first-speed grouped z/y add probe
  (`sqrtf(x*x + (z*z + y*y)) - 2.0`) missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x6025B63F/0xF5C950EA`, and the relinked focused diff regressed to
  `CURRENT (2980)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of `$f14`, and left the wave loop reversed
  as current `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop.
  Source was restored and final full verify passed; do not repeat this
  first-speed grouped z/y add spelling. A
  2026-05-23 current-baseline R-trigger grounded-wheel stash guard probe
  (`racer->groundedWheels > 0`) missed: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x2FDDE03F/0x495E14B9`, and the relinked focused diff stayed in the
  promoted current-baseline family at `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  `$f14`, and left the wave loop reversed as current `a0`-bound/`v1`-loop
  instead of target `v1`-bound/`a0`-loop. Source was restored and final full
  verify passed; do not repeat this R-trigger grounded-wheel stash guard
  spelling. A 2026-05-23 current-baseline normal-flight side-force guard
  condition-order probe (`racer->groundedWheels == 0 ||
  !(gCurrentRacerInput & R_TRIG) || racer->zipperDirCorrection != 0`) missed:
  full verify failed with calculated CRCs `0x605DE9ED/0x38B1F9D8`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of `$f14`, and
  left the wave loop reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this normal-flight side-force guard condition-order spelling. A
  2026-05-23 current-baseline normal-flight pitch damping factor probe (hoist
  the shared `obj->trans.rotation.x_rotation -=
  (obj->trans.rotation.x_rotation * updateRate) >> 4` before the R-trigger
  `19`/`30` multiplier branch) missed: full verify failed with calculated CRCs
  `0x81BCA331/0x35054A7B`, and relinked `./diff.sh func_80049794` reported
  `CURRENT (2480)`. It did not recover target `$f20/$f21` prologue saves, used
  the smaller saved-register stack slots, kept early zero in `$f16` instead of
  `$f14`, and left the wave loop reversed as current `a0`-bound/`v1`-loop
  instead of target `v1`-bound/`a0`-loop. Source was restored and final full
  verify passed; do not repeat this normal-flight pitch damping factor
  spelling. A
  2026-05-23 current-baseline grounded boss throttle/brake condition-order
  probe (`racer->velocity > -6.0 && racer->vehicleID >= VEHICLE_BOSSES`)
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x5FDDE03F/0xC5DC283B`, and the relinked
  focused diff regressed to `CURRENT (3555)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of `$f14`, and
  left the wave loop reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this grounded boss throttle/brake condition-order
  spelling. A
  2026-05-23 current-baseline course-height guard operand-order probe
  (`0.0f > var_f2`) missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0xA7DACB8B/0x793F4084`, and the relinked focused diff regressed to
  `CURRENT (3575)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of `$f14`, and left the wave loop reversed as
  current `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source
  was restored and final full verify passed; do not repeat this course-height
  compare operand-order spelling. A
  2026-05-23 current-baseline `spA3` course-height placement probe (moving
  `spA3 = FALSE` after the course-height subtraction and immediately before
  the range guard) missed: full verify failed with calculated CRCs
  `0x5FDDE03F/0xAA1C31A9`, and the relinked focused diff regressed to
  `CURRENT (3000)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this `spA3` course-height placement spelling. A
  2026-05-23 current-baseline course-height buoyancy subtract spelling
  (`var_f20 -= var_f2 / 25.0` instead of `var_f20 += -var_f2 / 25.0`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FE112BA/0x09397095`, and the relinked
  focused diff regressed to `CURRENT (3305)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop family, and
  shifted later buoyancy/gravity scheduling away from the target `$f20`
  family. Source was restored and final full verify passed; do not repeat this
  course-height buoyancy subtract spelling. A
  2026-05-23 current-baseline course-height upper-cap compare-order spelling
  (`if (2.5 < var_f20)`) missed as a no-movement promoted-baseline family:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored and
  final full verify passed; do not repeat this course-height upper-cap
  compare-order spelling. A 2026-05-23 current-baseline explicit
  first-compare/do-loop wave-scan spelling missed by collapsing into the known
  split-bound CRC family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5790053C/0x1C8C0179`, and the relinked focused diff regressed to
  `CURRENT (5755)`. It split the saved wave bound into `a3` and the loop index
  into `v0` instead of target `v1` bound plus `a0` loop, inserted `spA2`
  stack-byte traffic, still lacked target `$f20/$f21` prologue saves, and kept
  early zero in `$f16` instead of target `$f14`. Source was restored and final
  full verify passed; do not repeat this current-baseline explicit
  first-compare/do-loop wave-scan spelling. A 2026-05-23 current-baseline
  trailing-pad removal probe (removing only unused `pad3`/`pad4`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FDDE55F/0x6EE6C1E0`, and the relinked
  focused diff regressed to `CURRENT (3261)`. It shrank the frame to `0xf0`,
  shifted saved-register and parameter stack slots down by 8 bytes, still
  lacked target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and left the wave scan with the current bound/index order.
  Source was restored and final full verify passed; do not repeat this
  current-baseline trailing `pad3`/`pad4` removal. A
  2026-05-23 current-baseline first-speed boss-adjustment divide-before-subtract
  probe (`var_f20 = (var_f20 / 2.0) - 1.0`) missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0xCF9C57E6/0xCC0EF4F1`, and the relinked focused diff regressed to
  `CURRENT (4030)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and broadened the same
  first-speed/course-height plus wave-scan drift family. Source was restored
  and final full verify passed; do not repeat this first-speed
  boss-adjustment divide-before-subtract spelling. A 2026-05-23
  current-baseline first-speed boss guard operand-order probe
  (`if (VEHICLE_BOSSES <= racer->vehicleID)`) missed as a no-movement family:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  and the relinked focused diff stayed `CURRENT (2760)`. It still did not
  recover target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and left the wave scan in the current `a0`-bound/
  `v1`-loop family. Source was restored and final full verify passed; do not
  repeat this first-speed boss guard operand-order spelling. A 2026-05-23
  current-baseline later vehicleID upper-guard operand-order probe
  (`if (VEHICLE_BOSSES < racer->vehicleID)`) also missed as a no-movement
  family: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan in
  the current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this later vehicleID upper-guard operand-order
  spelling. A 2026-05-23 current-baseline trick divisor branch-polarity probe
  (`if (racer->trickType == 0) { var_f2 = 8.0; } else { var_f2 = 4.0; }`)
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x97DCE260/0x7D421449`, and the relinked
  focused diff regressed to `CURRENT (3815)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop family, and
  shifted later call-adjacent scheduling. Source was restored and final full
  verify passed; do not repeat this trick divisor branch-polarity spelling. A
  2026-05-23 current-baseline explicit `exitObj` pointer-test probe
  (`if (racer->exitObj != NULL)`) missed as a no-movement family: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with the
  promoted-baseline calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked
  focused diff stayed `CURRENT (2760)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this
  explicit `exitObj` pointer-test spelling. A 2026-05-23 current-baseline
  exit-throttle single-precision literal probe (`racer->throttle = 0.5f`)
  missed as the same no-movement family: full verify failed with the
  promoted-baseline calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked
  focused diff stayed `CURRENT (2760)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this
  exit-throttle single-precision literal spelling. A 2026-05-23
  current-baseline exit-throttle direct dataflow probe
  (`if (racer->exitObj) { racerThrottle = racer->throttle = 0.5; } else {
  racerThrottle = racer->throttle; }`) missed badly: full verify failed with
  calculated CRCs `0x37836355/0x67E5A883`, and the relinked focused diff
  regressed to `CURRENT (4665)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and disturbed later
  call-adjacent/sound scheduling. Source was restored and final full verify
  passed; do not repeat this exit-throttle direct dataflow spelling. A
  2026-05-23 current-baseline brake direct dataflow probe (moving
  `racerBrake = racer->brake` into both brake update arms) missed: full verify
  failed with calculated CRCs `0x6017B63F/0xECA9D437`, and the relinked focused
  diff regressed to `CURRENT (3350)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop family, and
  widened later gravity/call-adjacent scheduling drift. Source was restored
  and final full verify passed; do not repeat this brake direct dataflow
  spelling. A 2026-05-23 current-baseline vertical stick-rate grouping probe
  (`var_v1 = var_v0 * (updateRateF * 0.0625)` for the `unk1E8` update)
  missed badly: full verify failed with calculated CRCs
  `0x4B47F76E/0xEC3D5C69`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (7755)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, moved the vertical stick-rate
  multiply away from the target double-literal shape, and broadened downstream
  wave/gravity/call-adjacent scheduling. Source was restored and final full
  verify passed; do not repeat this vertical stick-rate grouping spelling. A
  2026-05-23 current-baseline horizontal steer-rate operand-order probe
  (`var_v1 = updateRateF * var_v0 / var_f2` for the `steerAngle` update)
  missed as a no-movement family: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this horizontal steer-rate operand-order
  spelling. A
  2026-05-23 current-baseline horizontal steer-rate divide-before-multiply
  probe (`var_v1 = (var_v0 / var_f2) * updateRateF` for the `steerAngle`
  update) missed: full verify failed with calculated CRCs
  `0x5FF1E13F/0xB7D0947C`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (2975)`. It moved the horizontal steer-rate math away from the
  target multiply-then-divide schedule, still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this
  horizontal steer-rate divide-before-multiply spelling. A
  2026-05-23 current-baseline `spA3` boolean guard spelling probe
  (`if (!spA3)` before `apply_vehicle_rotation_offset` instead of
  `if (spA3 == FALSE)`) missed as a no-movement family: full verify failed
  with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this `spA3`
  boolean guard spelling. A
  2026-05-23 current-baseline zipper fallback damping single-precision literal
  probe (changing the three `0.75` velocity dampers to `0.75f`) missed: full
  verify failed with calculated CRCs `0xCF769843/0x5618CD3F`, and relinked
  `./diff.sh func_80049794` reported `CURRENT (2555)`. The numeric score
  improved, but the diff moved the zipper fallback damping block away from the
  target double-literal shape into a single-precision literal family, shifted
  nearby labels/call targets, and still did not recover target `$f20/$f21`
  prologue saves or the early `$f14` zero family. Source was restored and final
  full verify passed; do not repeat this zipper fallback damping
  single-precision literal spelling. A
  2026-05-23 current-baseline throttle-rate single-precision
  literal probe (`racer->throttle += updateRateF * 0.01f` and
  `racer->throttle -= updateRateF * 0.01f`) missed badly: full verify failed
  with calculated CRCs `0xE2FEB7C7/0xB4368A76`, and the relinked focused diff
  regressed to `CURRENT (6518)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and disturbed later
  gravity/call-adjacent/sound scheduling. Source was restored and final full
  verify passed; do not repeat this throttle-rate single-precision literal
  spelling. A sibling throttle-rate operand-order probe
  (`racer->throttle += 0.01 * updateRateF` and
  `racer->throttle -= 0.01 * updateRateF`) missed: full verify failed with
  calculated CRCs `0x5FE5403F/0x70F0D8DF`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (2780)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and slightly shifted later gravity/call-adjacent scheduling. Source
  was restored and final full verify passed; do not repeat this throttle-rate
  operand-order spelling. A 2026-05-23 current-baseline brake-rate
  single-precision literal probe (`racer->brake += updateRateF * 0.016f` and
  `racer->brake -= updateRateF * 0.016f`) missed: guarded object-only focused
  diff first printed stale `CURRENT (0)`, promoted full verify failed with
  calculated CRCs `0x37F64CDD/0xCFC86BFD`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (5463)`. It still did not
  recover target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and widened the wave-scan/register-offset drift. Source
  was restored and final full verify passed; do not repeat this brake-rate
  single-precision literal spelling. A sibling brake-rate operand-order probe
  (`racer->brake += 0.016 * updateRateF` and
  `racer->brake -= 0.016 * updateRateF`) missed: full verify failed with
  calculated CRCs `0x5FCD003F/0x88486FB6`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (2780)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop
  family, and slightly shifted later gravity/call-adjacent scheduling. Source
  was restored and final full verify passed; do not repeat this brake-rate
  operand-order spelling. A 2026-05-23 current-baseline brake
  upper-clamp comparison-width probe (`if (racer->brake > 1.2f)` instead of
  the double literal compare) missed: guarded object-only focused diff first
  printed stale `CURRENT (0)`, promoted full verify failed with calculated
  CRCs `0xDE864D08/0x30E77DF1`, and relinked `./diff.sh func_80049794`
  regressed to `CURRENT (4195)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and widened later
  gravity/call-adjacent scheduling drift. Source was restored and final full
  verify passed; do not repeat this brake upper-clamp single-precision compare
  spelling. A sibling brake upper-clamp store-width probe (`racer->brake =
  1.2` instead of `1.2f` while keeping the double compare) missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this brake
  upper-clamp double store-width spelling. A 2026-05-23 current-baseline brake
  rumble-threshold
  single-precision compare probe (`racer->velocity < -2.0f` instead of the
  double literal compare) missed: promoted full verify failed with calculated
  CRCs `0xD0FF913E/0xB80E8394`, and relinked `./diff.sh func_80049794`
  regressed to `CURRENT (3965)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and widened later
  gravity/call-adjacent scheduling drift. Source was restored and final full
  verify passed; do not repeat this brake rumble-threshold single-precision
  compare spelling. A 2026-05-23 current-baseline brake rumble guard
  operand-order probe (`racer->groundedWheels >= 2 && racer->velocity < -2.0`)
  missed: promoted full verify failed with calculated CRCs
  `0x5FDDE425/0x05855E51`, and relinked `./diff.sh func_80049794` regressed
  to `CURRENT (3525)`. It still did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  scan in the current `a0`-bound/`v1`-loop family, and widened later
  gravity/call-adjacent scheduling drift. Source was restored and final full
  verify passed; do not repeat this brake rumble guard operand-order spelling.
  A 2026-05-23 current-baseline spinout brake single-precision literal probe
  (`racer->brake = 1.0f` instead of `1` in the spinout path) missed:
  promoted full verify failed with calculated CRCs `0xA746C795/0x4D4908D0`,
  and relinked `./diff.sh func_80049794` regressed to `CURRENT (3355)`. It
  did not recover target `$f20/$f21` prologue saves, kept early zero in
  `$f16` instead of target `$f14`, left the wave scan in the current
  `a0`-bound/`v1`-loop family, and widened/shifted later
  spinout/gravity/call-adjacent scheduling. Source was restored and final full
  verify passed; do not repeat this spinout brake single-precision literal
  spelling. A 2026-05-23 current-baseline pitch-flip rotation mask
  simplification probe (`racer->trickType * 0x180` instead of the current
  nested `0x180 & 0xFFFFFFFF` mask expression) missed as a no-movement
  promoted-baseline family: full verify failed with calculated CRCs
  `0x5FDDE03F/0x25C10EDA`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family. Source was restored and final
  full verify passed; do not repeat this pitch-flip `0x180` mask
  simplification spelling. A 2026-05-23 current-baseline trick-input
  horizontal `else if` probe (`if (gCurrentStickX > 40) { ... } else if
  (gCurrentStickX < -40) { ... }`) missed: full verify failed with calculated
  CRCs `0xE9D841B7/0xEEDBB8BB`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop
  family. Source was restored and final full verify passed; do not repeat this
  trick-input horizontal `else if` spelling. A 2026-05-23 current-baseline
  pitch-flip boost-duration decimal spelling (`normalise_time(10)` instead of
  `normalise_time(0xA)` in the `trickType == 2` completion path) missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop
  family. Source was restored and final full verify passed; do not repeat this
  pitch-flip boost-duration decimal spelling. A sibling pitch-flip
  boost-duration hex spelling (`normalise_time(0xA)` instead of
  `normalise_time(10)` in the `trickType == -2` completion path) also missed
  as a no-movement promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`. It did not recover
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop
  family. Source was restored and final full verify passed; do not repeat this
  pitch-flip boost-duration hex spelling. A 2026-05-23 current-baseline
  explicit wave-drift float-threshold
  probe (`var_f2 < 35.0f` and `var_f2 < 38.0f` instead of integer literals)
  missed as a no-movement promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this explicit wave-drift float-threshold
  spelling. A 2026-05-23 current-baseline drift-start speed-threshold
  single-precision probe (`racerVelocity >= 8.0f` in only the
  `drift_direction == 0` start branch) also missed: full verify failed with
  calculated CRCs `0x601FC875/0x0F7B5827`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (5670)`. It changed the
  start-branch compare into a single-precision family, shifted late-rodata
  references, still lacked target `$f20/$f21` prologue saves, kept early zero
  in `$f16` instead of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify
  passed; do not repeat this drift-start `racerVelocity >= 8.0f` spelling. A
  2026-05-23 current-baseline `spA2` speed-threshold single-precision probe
  (`racerVelocity < 8.0f` only in the `spA2 = TRUE` guard) also missed: full
  verify failed with calculated CRCs `0x602FD375/0x8F5948D3`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (5940)`. It shifted that
  compare into a single-precision family, still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this `spA2`
  `racerVelocity < 8.0f` spelling. A
  2026-05-23 current-baseline grouped x/y first-speed expression probe
  (`sqrtf(((x*x) + (y*y)) + (z*z)) - 2.0`) missed: full verify failed
  with calculated CRCs `0x5FDDE03F/0xA73DFC7C`, and the relinked focused diff
  reported `CURRENT (2770)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was restored
  and final full verify passed; do not repeat this grouped x/y first-speed
  expression. A 2026-05-23 current-baseline first-speed suffix
  single-precision probe (`sqrtf(...) - 2.0f` instead of the current `- 2.0`)
  missed: full verify failed with calculated CRCs `0x12F152B3/0x7EB3E947`, and
  relinked `./diff.sh func_80049794` regressed to `CURRENT (4560)`. It still
  did not recover target `$f20/$f21` prologue saves, kept early zero in `$f16`
  instead of target `$f14`, left the wave scan in the current
  `a0`-bound/`v1`-loop family, and widened later gravity/buoyancy scheduling.
  Source was restored and final full verify passed; do not repeat this
  first-speed `- 2.0f` suffix spelling. A 2026-05-23 current-baseline
  `OBJ_EMIT_9` store-before-`5.5`
  gravity assignment probe (moving `obj->particleEmittersEnabled |=
  OBJ_EMIT_9` before `var_f20 = 5.5`) missed: full verify failed with
  calculated CRCs `0x5FDDE03F/0x2087AB13`, and the relinked focused diff
  regressed to `CURRENT (2820)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and inserted an
  extra/reordered `unk1FE` reload around the `5.5` assignment rather than
  matching the target local schedule. Source was restored and final full
  verify passed; do not repeat this `OBJ_EMIT_9` store-before-`5.5` spelling.
  A 2026-05-23 current-baseline `5.5f` gravity literal probe (`var_f20 =
  5.5f` in the `unk1FE == 0` block) missed as a no-movement promoted-baseline
  family: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  and the relinked focused diff stayed `CURRENT (2760)`. It still did not
  recover target `$f20/$f21` prologue saves, kept early zero in `$f16` instead
  of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify
  passed; do not repeat this `5.5f` gravity literal spelling. A 2026-05-23
  current-baseline `unk1FE == 1` gravity `else if` probe (changing the second
  post-rotation `if (racer->unk1FE == 1)` into `else if`) missed: full verify
  failed with calculated CRCs `0x5FDDE812/0x3B1FD959`, and the relinked
  focused diff regressed to `CURRENT (3215)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, left the wave scan in the current `a0`-bound/`v1`-loop family, and
  removed the target-like `unk1FE` reload after the `5.5` gravity/`OBJ_EMIT_9`
  path while shifting later gravity work through `$f14` instead of target
  `$f20`. Source was restored and final full verify passed; do not repeat
  this current-baseline gravity `else if` spelling. A 2026-05-23
  current-baseline buoyancy single-precision nonzero guard probe
  (`if (racer->buoyancy != 0.0f)` after the post-rotation `unk1FE` gravity
  assignments) missed: full verify failed with calculated CRCs
  `0xA7264CF3/0x20C04378`, and the relinked focused diff regressed to
  `CURRENT (3790)`. It changed the target buoyancy zero test from the
  double-compare sequence (`cvt.d.s`/`c.eq.d`) into `c.eq.s`, still did not
  recover target `$f20/$f21` prologue saves, kept early zero in `$f16`
  instead of target `$f14`, left the wave scan in the current
  `a0`-bound/`v1`-loop family, and kept the later buoyancy/gravity path on
  `$f14` instead of target `$f20`. Source was restored and final full verify
  passed; do not repeat this current-baseline buoyancy single-precision
  nonzero guard spelling. A 2026-05-23 current-baseline direct selected-wave
  height subtraction probe (`var_f2 = (obj->trans.y_position -
  gRacerCurrentWave[var_a0 + 1]->waveHeight) - 10`) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x602A473F/0x3E5DF743`, and the relinked focused diff
  regressed to `CURRENT (4055)`. It still did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave scan in the current `a0`-bound/`v1`-loop family, and shifted the local
  selected-wave height subtraction into `$f18`/`$f4`/`$f6`/`$f8` scheduling
  rather than target `$f2`/`$f18`/`$f4`/`$f6`. Source was restored and final
  full verify passed; do not repeat this direct selected-wave height
  subtraction spelling. A 2026-05-23 current-baseline wave-height upper-reset
  constant-left compare probe (`if (100.0f < var_f2)`) missed as a no-movement
  promoted-baseline family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored and
  final full verify passed; do not repeat this wave-height upper-reset
  constant-left compare spelling. A
  2026-05-23
  current-baseline opening update-rate single-precision multiplier probe
  (`updateRateF *= 1.09f`) missed badly: full verify failed with calculated
  CRCs `0x9A37265B/0xDC30F32A`, and the relinked focused diff regressed to
  `CURRENT (4943)`. It changed the opening multiply from target-like
  double-literal `mul.d`/`cvt.s.d` to `mul.s`, still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave scan in the current `a0`-bound/`v1`-loop family.
  Source was restored and final full verify passed; do not repeat this opening
  update-rate single-precision multiplier spelling. A
  2026-05-23 current-baseline nested `spA2` wave-drift boolean probe
  (`if (var_f2 < 35) { if (racerVelocity < 8.0) spA2 = TRUE; }`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  and the relinked focused diff stayed in the promoted current-baseline family
  at `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this nested `spA2` wave-drift boolean spelling. A
  2026-05-23 current-baseline explicit wave-height subtract constant probe
  (`var_f2 = (obj->trans.y_position - var_f2) - 10.0f`) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with the
  promoted-baseline calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked
  focused diff stayed in the promoted current-baseline family at
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this explicit wave-height subtract `10.0f` spelling. A
  2026-05-23 current-baseline wave-drift single-precision normalization
  constants probe (`racerVelocity -= 8.0f; ... = 4.0f; ... /= 4.0f`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5B9A8D6D/0x2117429E`, and the relinked
  focused diff regressed to `CURRENT (6330)`. This source shape did align the
  early zero allocation with target `$f14`, but still did not recover target
  `$f20/$f21` prologue saves, left the wave scan in the current
  `a0`-bound/`v1`-loop family instead of target `v1`-bound/`a0`-loop, and
  broadened drift/inverse-gravity float-register churn. Source was restored
  and final full verify passed; do not repeat this wave-drift
  single-precision normalization-constant spelling. A
  2026-05-23 current-baseline wave-drift subtract-only suffix probe
  (`racerVelocity -= 8.0f` with the clamp/divide spelling unchanged) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x6006EA9D/0x93E5B79C`, and the relinked
  focused diff regressed to `CURRENT (4900)`. It still did not recover target
  `$f20/$f21` prologue saves, kept the wave scan as current `a0`-bound/
  `v1`-loop instead of target `v1`-bound/`a0`-loop, and broadened later
  `$f14`/`$f20` gravity scheduling drift. Source was restored and final full
  verify passed; do not repeat this current-baseline wave-drift subtract-only
  suffix spelling. A
  2026-05-23 current-baseline wave-drift clamp-assignment suffix probe
  (`racerVelocity = 4.0f` with the subtract/compare/divide spelling unchanged)
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0xA72E8795/0xE7316761`, and the relinked
  focused diff regressed to `CURRENT (3355)`. It still did not recover target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, kept the wave scan as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop, and broadened later `$f14`/`$f20` gravity
  scheduling drift. Source was restored and final full verify passed; do not
  repeat this current-baseline wave-drift clamp-assignment suffix spelling. A
  2026-05-23 close save-family plus wave-drift subtract-suffix probe
  (promoted close chained-zero/x/z/y/no-trailing-pad shape with only
  `racerVelocity -= 8.0f` changed) missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0xA8F39A57/0xC08781AF`, and the relinked focused diff regressed to
  `CURRENT (7769)`. It preserved the target `0xf8` frame, `$f20/$f21` saves,
  and early `$f14` zero family, but left/widened the wave scan as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop and disturbed
  later float-register scheduling. Source was restored and final full verify
  passed; do not repeat this close save-family plus wave-drift subtract-suffix
  combination. A
  2026-05-23 current-baseline wave-lift single-precision literal probe
  (`((38.0f - var_f2) * updateRateF * racerVelocity) / 8.0f`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x6006EA9F/0x791FEBA1`, and the relinked
  focused diff regressed to `CURRENT (5085)`. It kept the full `0xf8` frame
  and aligned the early zero allocation with target `$f14`, but still missed
  target `$f20/$f21` prologue saves, shifted saved GPR slots down by 8 bytes,
  left the wave scan as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and broadened later `$f14`/`$f20` gravity scheduling
  drift. Source was restored and final full verify passed; do not repeat this
  current-baseline wave-lift single-precision literal spelling. A
  2026-05-23 current-baseline wave-lift divided-speed grouping probe
  (`((38 - var_f2) * updateRateF) * (racerVelocity / 8)`) missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FED69B7/0xD53B5C00`, and the relinked
  focused diff regressed to `CURRENT (3025)`. It kept the full `0xf8` frame,
  but still missed target `$f20/$f21` prologue saves, shifted saved GPR slots
  down by 8 bytes, put early zero back in `$f16` instead of target `$f14`, left
  the wave scan as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and broadened later `$f14`/`$f20` gravity scheduling
  drift. Source was restored and final full verify passed; do not repeat this
  current-baseline wave-lift divided-speed grouping. A
  2026-05-23 current-baseline wave-lift positive-stick half-division probe
  (`gCurrentStickY = gCurrentStickY / 2` instead of `gCurrentStickY >>= 1`)
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x581EE800/0x4D6819EC`, and the relinked
  focused diff regressed to `CURRENT (3560)`. It still missed target
  `$f20/$f21` prologue saves, shifted saved GPR slots down by 8 bytes, kept
  early zero in `$f16` instead of target `$f14`, left the wave scan as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop, and broadened
  later `$f14`/`$f20` gravity scheduling drift. Source was restored and final
  full verify passed; do not repeat this current-baseline wave-lift
  positive-stick half-division spelling. A
  2026-05-23 current-baseline split drift-reset condition probe
  (`if (racerVelocity < 8.0) { reset } else if (gCurrentStickY < -10) {
  reset }`) missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0x7CB10841/0x43C4193E`, and the
  relinked focused diff regressed to `CURRENT (5300)`. It still missed target
  `$f20/$f21` prologue saves, shifted saved GPR slots down by 8 bytes, kept
  early zero in `$f16` instead of target `$f14`, left the wave scan as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop, and broadened
  player/wave plus later `$f14`/`$f20` temporary-register scheduling drift.
  Source was restored and final full verify passed; do not repeat this
  current-baseline split drift-reset condition spelling. A
  2026-05-23 current-baseline independent drift-reset check spelling
  (`if (racerVelocity < 8.0) { reset } if (gCurrentStickY < -10) { reset }`)
  also missed: full verify failed with calculated CRCs
  `0xEAC7CF58/0x7D4B28D3`, and relinked `./diff.sh func_80049794` regressed
  to `CURRENT (3590)`. It still missed target `$f20/$f21` prologue saves,
  shifted saved GPR slots down by 8 bytes, kept early zero in `$f16` instead
  of target `$f14`, left the wave scan as current `a0`-bound/`v1`-loop
  instead of target `v1`-bound/`a0`-loop, and changed the drift-reset branch
  shape away from the target. Source was restored and final full verify
  passed; do not repeat this independent drift-reset check spelling. A
  2026-05-23 current-baseline drift-direction nonzero spelling probe
  (`if (racer->drift_direction)` instead of `!= 0`) missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  at `CURRENT (2760)`. It still missed target `$f20/$f21` prologue saves,
  shifted saved GPR slots down by 8 bytes, kept early zero in `$f16` instead
  of target `$f14`, and left the wave scan as current `a0`-bound/`v1`-loop
  instead of target `v1`-bound/`a0`-loop. Source was restored and final full
  verify passed; do not repeat this current-baseline drift-direction nonzero
  spelling. A
  2026-05-17 current-baseline reversed chained-zero probe
  (`racer->unk84 = (racer->unk88 = 0.0f)`) compiled, but missed: full verify
  failed with calculated CRCs `0x5FDDE03F/0x127A8488`, the relinked focused
  diff worsened to `CURRENT (3000)`, and it reversed the two early zero stores
  while still using `$f16` and still lacking target `$f20/$f21` prologue saves.
  Source was restored and final full verify passed; do not repeat this
  reversed chained-zero current-baseline spelling. The
  2026-05-17 save-family wave-bound probe recreated the close x/z/y
  pre-`sqrtf` branch with chained grounded-wheel zero, removed trailing
  `pad3`/`pad4`, and steer-vel no-op, then spelled the wave loop bound as
  `var_a0 = (var_v1 = gRacerWaveCount - 1)` plus `if (var_a0 == var_v1)`.
  It compiled and kept the target `0xf8` frame and `$f20/$f21` saves, but
  regressed the relinked full focused score to `CURRENT (6100)`, widened the
  wave integer-register churn, and failed full verify with calculated CRCs
  `0x2E4A9A41/0xD04D4E64`; source was restored and final full verify passed.
  A split-assignment spelling of the same wave-bound idea
  (`var_v1 = gRacerWaveCount - 1; for (var_a0 = var_v1; ...); if (var_a0 ==
  var_v1)`) on the same save-family branch compiled to the same bad CRC family
  and relinked `CURRENT (6100)`, so treat it as equivalent to the comma
  assignment and do not repeat either wave-bound spelling on the save-family
  branch. Making only the wave-height threshold explicit `5.0f` on the close
  save-family branch was a no-op, producing the same failed CRCs
  `0xB8DD79CD/0xE47454ED` and preserving the wave `a0`/`v1` swap; do not
  repeat that threshold spelling. Commuting the threshold to
  `5 + obj->trans.y_position` on the same branch also missed with calculated
  CRCs `0xB8CD59CD/0xDE963C8F` and relinked focused `CURRENT (2142)`, keeping
  the same `a0`/`v1` wave-register mismatch; do not repeat that commuted
  threshold spelling either. A later bound-local copy spelling on the same
  close save-family branch (`var_a0 = gRacerWaveCount - 1; var_v1 = var_a0;
  while (...) { var_a0--; } if (var_a0 == var_v1)`) also missed: it kept the
  target frame/save family but widened the relinked focused score to
  `CURRENT (4252)`, failed full verify with calculated CRCs
  `0x527F28C9/0xA7E04D93`, and introduced extra `spA2` stack-byte traffic plus
  broader wave-block register churn. Close save-family `register s32 var_v0`
  and `register s32 var_v1` hints also missed: both kept the target `0xf8`
  frame and `$f20/$f21` saves, but full verify failed with the known
  close-branch CRCs `0xB8DD79CD/0xE47454ED`, the relinked focused score
  worsened to `CURRENT (4365)`, and the wave bound/index allocation remained
  reversed with current `a0` as bound and `v1` as loop index instead of target
  `v1` bound and `a0` loop. Do not repeat these close-branch register hints
  (`var_v0`/`var_v1`) or this local-copy while-loop wave-bound spelling. A
  close save-family `racerTrickType` wave-reset cache also missed: it failed
  full verify with calculated CRCs `0xB14B79CD/0x12BCEA0A`, worsened relinked
  focused score to `CURRENT (4375)`, and flipped the `trickType == -1`
  compare from target `beq t1,v0` to current `beq v0,t1` while leaving the
  bound/index allocation reversed. The
  2026-05-17 branch operand-order spelling
  (`PLAYER_COMPUTER == var_v0`) compiled but produced no object change from the
  promoted baseline and stayed `CURRENT (2550)`. Moving `spA3 = FALSE` before
  the first speed-magnitude block compiled but worsened the focused score to
  `CURRENT (2760)` and still did not introduce the target `$f20/$f21` prologue
  saves. Staging the inverse-gravity divide through the existing `var_f0`
  (`var_f0 = var_f20 / 4.0; var_f20 = 1.0 - var_f0`) compiled but worsened the
  focused score to `CURRENT (3445)` and still did not introduce the target
  `$f20/$f21` prologue saves. A later x-component `var_f2` carrier on the
  x/z/y save-family plus steer-noop/buoyancy-carrier branch compiled but
  regressed the relinked focused score to `CURRENT (4665)`. A standalone
  `register f32 racerVelocity` allocation hint compiled but produced no
  relinked compressed focused change from the promoted baseline
  (`CURRENT (759)` under `--max-size 520`) and failed full verify with the same
  calculated CRCs `0x5FDDE03F/0xEF7A0514`. Reusing the existing `var_f0` local
  for the wave-block speed carrier instead of the named `racerVelocity` local
  compiled but worsened the relinked focused score to `CURRENT (3364)` and
  failed full verify with calculated CRCs `0xF40AF157/0xCBAF4125`. A nested
  spelling of the computer-player handling branch
  (`if (var_v0 == PLAYER_COMPUTER) { if (gCurrentPlayerIndex !=
  PLAYER_COMPUTER) ... }`) compiled but produced the same promoted-baseline
  CRC family `0x5FDDE03F/0xEF7A0514`, stayed `CURRENT (759)` under
  `--max-size 520`, and still lacked the target `$f20/$f21` prologue saves.
  Routing the initial grounded-wheel zero stores through the existing `var_f2`
  local (`var_f2 = 0.0f; racer->unk84 = var_f2; racer->unk88 = var_f2`)
  likewise compiled but stayed at `CURRENT (759)` under `--max-size 520`,
  failed full verify with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and still
  allocated the early zero in `$f16` instead of target `$f14`. A dedicated
  early-zero carrier family also missed: plain `f32 zero` and `register f32
  zero` variants widened the frame to `0x100`, kept the early zero in `$f16`,
  failed full verify with calculated CRCs `0x5FDDDEDF/0x01A99146`, and still
  did not introduce target `$f20/$f21` prologue saves. Routing the early zero
  stores through existing `var_f14` (`var_f14 = 0.0f; racer->unk84 = var_f14;
  racer->unk88 = var_f14`) while promoting the current C was also a no-op:
  focused score stayed `CURRENT (2430)`, full verify failed with the same
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the early zero still allocated
  in `$f16` instead of target `$f14`. Do not repeat this existing-`var_f14`
  early-zero carrier. A later current-baseline chained zero spelling
  (`racer->unk88 = (racer->unk84 = 0.0f)`) also produced no useful movement:
  relinked focused score `CURRENT (2430)`, same failed full-verify CRCs
  `0x5FDDE03F/0xEF7A0514`, still missing target `$f20/$f21` prologue saves,
  and still allocating the early zero in `$f16` instead of `$f14`. Do not
  repeat this standalone current-baseline chained-zero probe. A pre-spinout
  zero-timing probe that inserted `var_f14 = 0.0f` after the grounded-wheel
  `unk84`/`unk88` zero stores and before the `unk1FE`/spinout check also
  missed in the same family: focused score stayed `CURRENT (2430)`, full verify
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, the target `$f20/$f21`
  prologue saves were still absent, and the early zero still allocated in
  `$f16` rather than target `$f14`. Do not repeat this pre-spinout
  `var_f14 = 0.0f` timing probe. Promoting the
  existing C in the current checkout and
  relinking shows the uncompressed focused baseline at `CURRENT (1926)` with
  the known calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; the first visible drift remains the missing
  `$f20/$f21` prologue saves, shifted saved `$ra/$s1/$s0` stack slots, and early
  zero allocation in `$f16` instead of target `$f14`. Adding `register` to
  `racerThrottle` compiled but produced no object movement: same uncompressed
  `CURRENT (1926)`, same CRC family, and still no target `$f20/$f21` saves.
  Adding `register` to `racerBrake` also compiled but did not change the
  failed CRC family (`0x5FDDE03F/0xEF7A0514`) and stayed in the same compressed
  focused family (`CURRENT (859)` under `--max-size 620`), with the same
  missing `$f20/$f21` prologue saves and early `$f16` zero allocation. Adding
  `register` to the long-lived `updateRateF` parameter likewise missed in the
  same family: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, focused diff stayed `CURRENT (859)` under
  `--max-size 620`, and the target `$f20/$f21` prologue saves plus early
  `$f14` zero allocation were still absent. Do not repeat this
  parameter-register hint. Adding `register` to the integer `updateRate`
  parameter was another no-op in the same promoted-baseline family: full verify
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, focused diff stayed
  `CURRENT (859)` under `--max-size 620`, and the target `$f20/$f21` prologue
  saves plus early `$f14` zero allocation were still absent. Do not repeat this
  integer-parameter register hint. A later retained-pad `var_f2` z/y
  component-staging branch with the inverse-gravity expression changed to
  multiply form (`var_f20 = 1.0 - (var_f20 * 0.25)`) also missed: full verify
  failed with calculated CRCs `0x5FEF1D9D/0x4258C5C1`, relinked focused diff
  reported `CURRENT (3620)`, and the function still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16`, and kept the wave `a0`/`v1` swap.
  Source was restored and final full verify passed; do not repeat this
  retained-pad `var_f2`/inverse-multiply hybrid. A later
  save-family wave-threshold local probe on the close chained-zero/x/z/y/
  steer-noop branch (`var_f0 = obj->trans.y_position + 5.0f` before the wave
  scan) kept the target `0xf8` frame and `$f20/$f21` saves but regressed the
  relinked focused score to `CURRENT (7555)`, introduced broad wave-block
  float/register churn, and failed full verify with calculated CRCs
  `0x2B7A77D5/0x5B507890`. A later explicit decrementing
  `WaterProperties **wavePtr` walk on top of the close chained-zero/x/z/y/
  steer-noop branch failed worse: it widened the frame to `0x100`, regressed
  the relinked focused score to `CURRENT (7232)`, failed full verify with
  calculated CRCs `0xC51623A2/0xD2F96DC4`, and used `v0/a1/v1` for the scan
  instead of the target `v1/a0/v0` family. A later explicit first-compare plus
  `do`-loop wave scan on the close chained-zero/x/z/y/steer-noop branch
  compiled but produced no object movement from that close CRC family: full
  verify failed with the same calculated CRCs `0xB8DD79CD/0xE47454ED`, the
  relinked focused diff reported `CURRENT (3260)` under `--max-size 900`, and
  the wave scan still used current `a0`/`v1` opposite the target order. Keep
  `func_80049794` active rather than parked, but do not repeat this explicit
  `wavePtr` pointer-walk or first-compare `do`-loop wave-scan spelling. A
  promotion-only 2026-05-17 acceptance probe showed why the full gate is
  mandatory: an object-only focused diff printed stale `CURRENT (0)`, but
  promoting the existing C failed full verify with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; after relink, the focused diff reported
  `CURRENT (2990)` with the same missing target `$f20/$f21` prologue saves,
  shifted saved-register stack slots, early `$f16` zero, and wave `a0`/`v1`
  drift. Do not accept `func_80049794` from object-only `CURRENT (0)` evidence.
  A 2026-05-17 current-checkout reconfirmation of the already-recorded
  early-`var_f20` zero carrier (`var_f20 = 0.0f; racer->unk84 = var_f20;
  racer->unk88 = var_f20`) produced no useful movement: full verify failed
  with calculated CRCs `0x5FDDE03F/0xEF7A0514`, the relinked focused diff
  stayed in the same compressed `CURRENT (2430)` family, the target
  `$f20/$f21` prologue saves were still absent, and the early zero still used
  `$f16` instead of target `$f14`. Source was restored and final full verify
  passed; do not repeat this early-`var_f20` zero-carrier spelling.
  Splitting the wave bound on the current baseline
  (`var_v1 = gRacerWaveCount - 1; for (var_a0 = var_v1; ...); if (var_a0 ==
  var_v1)`) worsened the focused score from promoted-baseline `CURRENT (2430)`
  to `CURRENT (4920)`, failed full verify with calculated CRCs
  `0x5790053C/0x1C8C0179`, introduced `spA2` stack-byte traffic, and widened
  wave-scan register churn. Do not repeat this current-baseline split
  wave-bound spelling. A current-baseline predecrement loop spelling
  (`for (var_a0 = gRacerWaveCount; --var_a0 >= 0 && ...;)`) also missed:
  relinked focused score worsened to `CURRENT (3680)`, full verify failed with
  calculated CRCs `0x77882035/0x6FF367A8`, and the scan shifted into a broader
  integer-register family instead of matching the target `v1/a0/v0` order. Do
  not repeat this current-baseline predecrement wave-scan loop. A later
  current-baseline wave-height threshold-local probe
  (`var_f0 = obj->trans.y_position + 5.0f` before the wave scan) compiled but
  widened the relinked focused score to `CURRENT (5590)`, failed full verify
  with calculated CRCs `0x5F811F98/0x9CE14139`, and still lacked the target
  `$f20`/`$f21` prologue saves plus early `$f14` zero. Do not repeat this
  current-baseline threshold-local spelling. A current-baseline wave-height
  threshold commute
  (`gRacerCurrentWave[var_a0]->waveHeight < 5 + obj->trans.y_position`)
  also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0x5FE1E03F/0x88CC2028`, and the
  relinked focused diff worsened to `CURRENT (2770)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16`, left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop, and shifted the current-baseline family rather
  than improving it. Source was restored and final full verify passed; do not
  repeat this current-baseline threshold-commute spelling. A close save-family
  continuation with x/z/y pre-`sqrtf` accumulation, chained grounded-wheel
  zero, steer-vel no-op, and removed trailing `pad3`/`pad4` tested an existing-`var_t0`
  wave-bound carrier (`var_t0 = gRacerWaveCount - 1; for (var_a0 = var_t0;
  ...); if (var_a0 == var_t0)`). It kept the target `0xf8` frame and
  `$f20/$f21` prologue saves, but worsened the relinked focused score to
  `CURRENT (5115)`, failed full verify with calculated CRCs
  `0x2364AB01/0x1E30A2A8`, and shifted the wave block into a broader
  `t0/v0/t2` register family rather than target `v1/a0/v0`. Source was
  restored and final full verify passed; do not repeat this close-branch
  existing-`var_t0` wave-bound carrier. A current-baseline existing-`var_t9`
  wave-bound carrier (`var_t9 = gRacerWaveCount - 1; for (var_a0 = var_t9;
  ...); if (var_a0 == var_t9)`) also missed: full verify failed with
  calculated CRCs `0x1ED9F907/0x570DED85`, the relinked focused score worsened
  from promoted-baseline `CURRENT (2430)` to `CURRENT (4460)`, and the wave
  block shifted into broader integer-register churn rather than target
  `v1/a0/v0`. Source was restored and final full verify passed; do not repeat
  this current-baseline existing-`var_t9` wave-bound carrier. A 2026-05-17
  save-family in-place inverse-gravity split (`var_f20 /= 4.0; var_f20 = 1.0
  - var_f20`) on top of the close chained-zero/x/z/y/steer-noop branch kept
  the target `0xf8` frame and `$f20/$f21` saves, but regressed: full verify
  failed with calculated CRCs `0x772B05DA/0x0C3D3274`, relinked focused diff
  reported `CURRENT (4075)`, call-adjacent `$f14` save/reload and sound
  scheduling were disturbed, and the wave `a0`/`v1` drift remained. Source was
  restored and final full verify passed; do not repeat this save-family
  in-place inverse-gravity split. A 2026-05-17 save-family double-multiply
  inverse spelling (`var_f20 = 1.0 - (var_f20 * 0.25)`) on the same close
  chained-zero/x/z/y/steer-noop branch kept the target `0xf8` frame and
  `$f20/$f21` saves, but stayed in the known close-branch CRC family: full
  verify failed with calculated CRCs `0xB8DD79CD/0xE47454ED`, relinked focused
  diff reported `CURRENT (3260)`, the wave `a0`/`v1` drift remained, and the
  target `$f14` reload after `apply_vehicle_rotation_offset` was still absent.
  Source was restored and final full verify passed; do not repeat this
  save-family double-multiply inverse spelling. A 2026-05-17 close
  save-family existing-`var_t9` wave-bound carrier (`var_t9 =
  gRacerWaveCount - 1; for (var_a0 = var_t9; ...); if (var_a0 == var_t9)`)
  kept the target `0xf8` frame and `$f20/$f21` saves, but regressed the
  relinked focused score to `CURRENT (5430)` and failed full verify with
  calculated CRCs `0xEA44B192/0x165715AD`. It broadened the wave block into
  `v1/v0/t*` register churn rather than target `v1/a0/v0`. Source was
  restored and final full verify passed; do not repeat this close-branch
  existing-`var_t9` wave-bound carrier. A 2026-05-17 close save-family
  predecrement wave-loop spelling (`for (var_a0 = gRacerWaveCount; --var_a0
  >= 0 && ...;)`) kept the target `0xf8` frame and `$f20/$f21` saves, but
  failed full verify with calculated CRCs `0xCE58DA51/0x62A7B089` and regressed
  the relinked focused score to `CURRENT (4660)`. It shifted the wave scan into
  an `a0/v0/v1` register/order family with extra post-loop compare math instead
  of target `v1/a0/v0`. Source was restored and final full verify passed; do
  not repeat this close-branch predecrement wave-loop spelling. A
  current-baseline early `spA2 = FALSE` timing probe that moved the stack-byte
  initialization before the grounded-wheel zeroing also missed: full verify
  failed with calculated CRCs `0xC22DF330/0xE8574E6D`, the relinked focused
  score worsened to `CURRENT (4660)`, and the diff inserted an extra early
  `0xa2(sp)` byte store while the early zero still used `$f16` and the
  `$f20/$f21` prologue saves were still absent. Source was restored and final
  full verify passed; do not repeat this early `spA2` timing spelling. A
  current-baseline `spA2` declaration-initialization spelling
  (`s8 spA2 = FALSE;` with the later standalone `spA2 = FALSE;` removed) also
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0xC22DF330/0x3B2BA987`, and the relinked
  focused score worsened to `CURRENT (4869)`. The relinked diff inserted an
  early `sb zero,0xa2(sp)`, still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16`, and broadened the wave-scan register/order drift.
  Source was restored and final full verify passed; do not repeat this `spA2`
  declaration-initialization spelling.
  Rewriting the current-baseline drift flag test from the guarded assignment to
  direct boolean assignment (`spA2 = var_f2 < 35 && racerVelocity < 8.0`)
  widened the frame to `0x100`, introduced stack-byte traffic for the drift
  flag, failed full verify with calculated CRCs `0xAD0C80F7/0xC3551BE0`, and
  regressed the relinked focused score to `CURRENT (5226)`. Source was
  restored and final full verify passed; do not repeat this drift-flag boolean
  assignment spelling.
- `func_80059208` is also active, not parked. A 2026-05-17 `register f32
  divisor` allocation hint compiled but produced no relinked object movement:
  full verify failed with the same calculated CRC family
  `0x53D141DF/0xB9D4B481`, focused diff stayed `CURRENT (870)`, and the final
  lateral tail still used the baseline object-dot/checkpoint-dot register
  schedule. Source was restored and final full verify passed; do not repeat
  this divisor register hint. The 2026-05-17 final-offset
  no-movement family also includes reusing the already-loaded `distance` local
  in the early checkpoint-scale divisor expression (`(scale - distance) *
  splinePos + distance`): full verify failed with the same calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused stayed `CURRENT (870)`, and the
  final object-dot/checkpoint-dot drift was unchanged. Do not repeat this
  divisor-distance reuse spelling. A later final vertical clamp-limit carrier
  through the existing dead `pad3` local (`pad3 = 100.0f; if (diffY > pad3)
  ...; if (diffY < -pad3) ...`) also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x4400230F/0x7B651F08`, and the relinked focused score worsened to
  `CURRENT (1995)` by inserting extra vertical-clamp float traffic and
  broadening the final object-dot/checkpoint-dot plus epilogue drift. Source
  was restored and final full verify passed; do not repeat this final vertical
  `pad3` clamp-limit carrier.
  The 2026-05-17 final-offset
  probes compiled, but checkpoint-dot-before-object-dot stayed `CURRENT (870)`,
  direct `pad2 + object-dot` fold regressed to `CURRENT (1445)`, and empty
  `if (pad2) {}` lifetime hint regressed to `CURRENT (2645)`. A later final
  vertical `diffX` cast-carrier probe
  (`diffX = diffY; racer->unk1BC += (s32) diffX`) worsened to `CURRENT (1030)`
  by adding a final-block stack store before the conversion. A term-negated
  checkpoint-dot probe (`pad2 = ((-tempZ) * diffZ) - (diffX * tempX)`) worsened
  to `CURRENT (1192)` with broader final-block register drift. Computing the
  negated checkpoint dot before loading both final object-position locals
  compiled but left the focused score unchanged at `CURRENT (870)`, with the
  same final object-load/arithmetic drift. Adding `register` to `splinePos`
  compiled but produced no object change and also stayed `CURRENT (870)`. A
  later final object-dot product carrier through the existing `distance` local
  (`distance *= diffZ; pad = (splinePos * diffX) + distance`) worsened the
  relinked focused score to `CURRENT (2043)`. A final object-pointer lifetime
  probe (`Object *obj2; obj2 = obj; splinePos = obj2->trans.x_position;
  distance = obj2->trans.z_position`) worsened the relinked focused score from
  baseline `CURRENT (870)` to `CURRENT (878)` and failed full verify with
  calculated CRCs `0x53D141D7/0xAA087F2A`, leaving the same final
  arithmetic/register drift. The sibling term-negation spelling
  (`pad2 = (tempZ * -diffZ) - (diffX * tempX)`) worsened the relinked focused
  score from `CURRENT (870)` to `CURRENT (1165)` and failed full verify with
  calculated CRCs `0x53AB58B5/0xBC82B0CE`. Loading the final object x/z
  locals first, then computing the negated checkpoint dot before the final
  object dot (`splinePos = obj->trans.x_position; distance =
  obj->trans.z_position; pad2 = -(...); pad = ...`) also produced no object
  movement from the promoted baseline, stayed `CURRENT (870)`, and failed full
  verify in the same CRC family `0x53D141DF/0xB9D4B481`; source was restored.
  Splitting the negated checkpoint dot into `pad2 = -(tempZ * diffZ); pad2 -=
  diffX * tempX` compiled but worsened the relinked focused score to
  `CURRENT (1405)` and failed full verify with calculated CRCs
  `0x53C0A2B5/0x47AA3C12`; keep active, but do not repeat this split-negated
  checkpoint-dot spelling. Reversing the split-negated term order
  (`pad2 = -(diffX * tempX); pad2 -= tempZ * diffZ`) worsened further to
  `CURRENT (1736)` and failed full verify with calculated CRCs
  `0x53B3FDB5/0x46D415EE`; do not repeat either split-negated
  checkpoint-dot order. Removing the misleading `UNUSED` marker from the used
  `pad`/`pad2` locals while promoting the current C compiled but produced no
  focused movement from the baseline (`CURRENT (870)` under `--max-size 620`)
  and failed full verify with calculated CRCs `0x53D141DF/0xB9D4B481`; do not
  repeat this declaration-only cleanup. Removing only the dead `pad3` local
  while promoting the current C compiled but shrank the frame from target
  `0xc0` to `0xb8`, worsened the relinked focused score to `CURRENT (1218)`,
  and failed full verify with calculated CRCs `0x53D13F77/0x21BEEE76`; source
  was restored and final full verify passed. Keep active, but do not repeat
  this declaration-only stack-shape probe. Recasting `pad2` as a positive
  checkpoint-dot carrier and subtracting it in the final numerator
  (`pad2 = checkpointDot; diffX = -((pad - pad2) / divisor)`) compiled but
  produced no movement from the promoted baseline: relinked focused diff stayed
  `CURRENT (870)` and full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; source was restored and final full verify passed.
  Do not repeat this positive-`pad2` subtract spelling. Directly commuting the
  final negated sum to `diffX = -((pad2 + pad) / divisor)` also compiled but
  produced no object movement from the promoted baseline: relinked focused
  diff stayed `CURRENT (870)` and full verify failed with the same calculated
  CRCs `0x53D141DF/0xB9D4B481`; source was restored and final full verify
  passed. Do not repeat this direct `pad2 + pad` spelling. A later final
  `tempZ`/`tempX` mutating checkpoint-dot carrier
  (`tempZ *= diffZ; tempX *= diffX; pad2 = -(tempZ + tempX)`) compiled but
  broadened register allocation from the early spline block, worsened the
  relinked focused score to `CURRENT (2173)`, and failed full verify with
  calculated CRCs `0x5CBA1A12/0x20830C42`; source was restored and final full
  verify passed. A later positive checkpoint-minus-object numerator carrier
  (`pad = checkpointDot; pad2 = objectDot; pad -= pad2; diffX = pad /
  divisor`) compiled but worsened the relinked focused score to
  `CURRENT (1300)` and failed full verify with calculated CRCs
  `0xC7D996EA/0xC6D1DFDE`; source was restored and final full verify passed.
  A `pad2`-carrier variant of the same positive numerator
  (`pad2 = checkpointDot; pad = objectDot; pad2 -= pad; diffX = pad2 /
  divisor`) reproduced the same miss: relinked focused score `CURRENT (1300)`
  and failed full-verify CRCs `0xC7D996EA/0xC6D1DFDE`. Do not repeat this
  temp-mutating checkpoint-dot carrier or either positive numerator carrier.
  Rewriting the final lateral offset update as
  `racer->unk1BA = (s32) diffX + racer->unk1BA` compiled but worsened the
  relinked focused score to `CURRENT (900)` and failed full verify with
  calculated CRCs `0x53CD41DF/0x4CAF790B`; source was restored and final full
  verify passed. Rewriting the sibling final vertical offset update as
  `racer->unk1BC = (s32) diffY + racer->unk1BC` also worsened the relinked
  focused score to `CURRENT (900)` and failed full verify with calculated CRCs
  `0x53CD41DF/0x291D30F4`; source was restored and final full verify passed.
  A 2026-05-23 final offset compound-assignment implicit-cast spelling
  (`racer->unk1BA += diffX` and `racer->unk1BC += diffY`, removing the explicit
  `(s32)` casts) also missed badly: full verify failed with calculated CRCs
  `0xC76F5A8F/0x277FF7CB`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (4195)` by changing the
  final adds into float-add-before-convert traffic, shifting the
  lateral/vertical update schedule, and moving downstream labels/global
  offsets. Source was restored and final full verify passed. Do not repeat
  either final `unk1BA`/`unk1BC` add-order spelling or this implicit-cast
  compound-assignment spelling. An
  explicit-zero axis-negation spelling
  (`diffZ = 0.0f - diffY`) compiled but regressed the relinked focused score to
  `CURRENT (1626)` and failed full verify with calculated CRCs
  `0x53B93C23/0x99E6EAF5`; source was restored and final full verify passed.
  Commuting only the final object-dot x product from `splinePos * diffX` to
  `diffX * splinePos` compiled but regressed the relinked focused score from
  baseline `CURRENT (870)` to `CURRENT (875)` and failed full verify with
  calculated CRCs `0x53D0C1DF/0xC593C532`; source was restored and final full
  verify passed. A later split final vertical carrier
  (`diffY = obj->trans.y_position; diffY -= tempY; diffY /= divisor`) compiled
  but widened the relinked focused score to `CURRENT (1922)` and failed full
  verify with calculated CRCs `0xDACE25C4/0x70185CA9`. A negative object-dot
  plus positive checkpoint-dot numerator spelling
  (`pad = -objectDot; pad2 = checkpointDot; diffX = (pad2 + pad) / divisor`)
  reproduced the bad positive-numerator family: relinked focused score
  `CURRENT (1300)` and failed full-verify CRCs
  `0xC7D996EA/0xC6D1DFDE`. Keep active, but do not repeat this
  axis-negation spelling, final object-dot x-multiply commute, split final
  vertical carrier, or negative-object/positive-checkpoint numerator spelling.
  A later `register f32 diffZ` allocation hint inside `func_80059208` is
  invalid because `diffZ` is passed by address to
  `cubic_spline_interpolation`; the compile failed with
  `address of register variable requested`. A `register f32 scale` allocation
  hint compiled but produced no movement from the promoted baseline: full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked focused
  score stayed `CURRENT (870)`, and the same final object-dot plus
  negated-checkpoint-dot load/register drift remained. Source was restored and
  final full verify passed. Keep active, but do not repeat either of these
  register-hint probes. A later axis-swap lifetime probe staged old `diffZ`
  through existing `pad` (`diffY = diffX; pad = diffZ; diffZ = -diffY; diffX
  = pad`) but missed badly: full verify failed with calculated CRCs
  `0x53ACBBF7/0x0E5DD078`, relinked focused score worsened from baseline
  `CURRENT (870)` to `CURRENT (2016)`, and the final tail shifted earlier into
  a broader object-dot/checkpoint-dot register family. Staging old `diffZ`
  through the now-dead `distance` local instead (`distance = diffZ; diffY =
  diffX; diffX = distance`) also missed with no focused movement: promoted full
  verify failed in the baseline CRC family `0x53D141DF/0xB9D4B481`, relinked
  focused diff stayed `CURRENT (870)`, and the final offset drift was
  unchanged. Source was restored and final full verify passed. Keep active, but
  do not repeat either old-`diffZ` axis-swap carrier. A later final-sum carrier
  through the
  now-dead `diffX` local (`diffX = pad; diffX += pad2; diffX = -(diffX /
  divisor)`) also missed: full verify failed with calculated CRCs
  `0x63E46DB5/0x591D1D44`, the relinked focused score worsened to
  `CURRENT (1165)`, and the final tail added stack traffic/register drift
  instead of matching the target `pad + pad2` schedule. Source was restored
  and final full verify passed. Keep active, but do not repeat this
  `diffX` final-sum carrier. Adding `register` to the long-lived `tempZ`
  spline result compiled but produced no object movement from the promoted
  baseline: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused score stayed `CURRENT (870)`,
  and the same final object-dot plus negated-checkpoint-dot schedule drift
  remained. Source was restored and final full verify passed. Do not repeat
  this `tempZ` register-hint probe. Adding `register` to the sibling
  long-lived `tempX` spline result produced the same no-movement family: full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked focused
  score stayed `CURRENT (870)`, and the same final tail object-dot plus
  negated-checkpoint schedule drift remained. Source was restored and final
  full verify passed. Do not repeat this `tempX` register-hint probe. Adding
  `register` to the final vertical `tempY` spline result likewise produced no
  object movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused score stayed `CURRENT (870)`,
  and the same final tail object-dot plus vertical FPR drift remained. Source
  was restored and final full verify passed. Do not repeat this `tempY`
  register-hint probe. Rewriting the negated checkpoint dot as a multiply by
  negative one (`pad2 = ((tempZ * diffZ) + (diffX * tempX)) * -1.0f`) missed:
  full verify failed with calculated CRCs `0x8247080C/0xE00CF805`, the relinked
  focused score worsened from baseline `CURRENT (870)` to `CURRENT (2085)`,
  and the diff shifted late rodata/global offsets while broadening the final
  tail. Source was restored and final full verify passed. Do not repeat this
  `pad2` negative-one multiply spelling.
- `func_8002B0F4` is also active, not parked. A 2026-05-17 declaration-only
  `register s32 XInInt` / `register s32 ZInInt` hint compiled, but missed:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, the
  relinked focused diff worsened to `CURRENT (2860)`, and the diff introduced
  the known early `gCurrentLevelModel` spill at `0x60(sp)` plus broad
  integer-register rotation through the grid loops. Source was restored and
  final full verify passed; do not repeat this X/Z integer register-hint
  spelling. The 2026-05-17 explicit
  `gTrackWaves` remainder plus unrolled-by-four pointer-copy spelling compiled
  but only produced the known stale object-only `CURRENT (0)` before relink;
  after relink it worsened to `CURRENT (4623)` and failed full verify before
  the source guard was restored. A later early `XInInt`/`ZInInt` conversion
  probe, keeping the original `xIn`/`zIn` call arguments to
  `get_inside_segment_count_xz`, compiled but left the relinked focused score
  unchanged at `CURRENT (2780)`. A later pad-stack-slot probe found that
  removing the dead `pad3` local improved the relinked focused score to
  `CURRENT (1998)`, but still hoisted `gCurrentLevelModel` to `0x64(sp)`;
  moving `pad3` after `tempVec4f` returned to the promoted-baseline CRC family
  and did not solve the hoist. Combining the `pad3`-removed branch with a
  pointer-increment `gTrackWaves` population loop (`for (..., wave =
  D_8011D128; ...; wave++)`) compiled but worsened the relinked focused score
  to `CURRENT (6366)` and failed full verify with calculated CRCs
  `0x47E07C97/0x7D45A79C`. Combining the better plain `pad3`-removed stack
  layout with early `XInInt`/`ZInInt` conversions before
  `get_inside_segment_count_xz` and passing those integer locals compiled but
  regressed the relinked focused score to `CURRENT (2868)` and failed full
  verify with the same calculated CRCs as plain `pad3` removal,
  `0x785671AA/0x0D6F6A4A`. A scalar plane-carrier variant on the
  pad3-removed promoted branch (`planeX`/`planeY`/`planeZ`/`planeW` replacing
  `Vec4f tempVec4f`) also compiled but regressed from the better plain
  pad3-removal score to relinked focused `CURRENT (2868)`, failed full verify
  with calculated CRCs `0x785671AA/0x0D6F6A4A`, and still showed the unwanted
  pre-loop `gCurrentLevelModel` spill to `0x64(sp)`. A later declaration-only
  probe removed the unused `WaterProperties *wave2` while promoting the current
  C; it compiled but collapsed into the same failed CRC family as plain
  `pad3` removal (`0x785671AA/0x0D6F6A4A`), regressed the relinked focused
  score to `CURRENT (2868)`, and still showed the early `gCurrentLevelModel`
  spill. A later pad3-removed three-level water-surface guard split
  (`surface != SURFACE_WATER_CALM`, then `surface != SURFACE_WATER_UNK_F`,
  then flags) improved the relinked focused score to `CURRENT (1720)`, but it
  still failed full verify with the plain pad3-removal CRC family
  `0x785671AA/0x0D6F6A4A` and preserved the unwanted early
  `gCurrentLevelModel` spill at `0x64(sp)`. Combining that pad3-removed
  three-level guard branch with direct volatile `gCurrentLevelModel` reloads at
  the initial segment/bounding-box setup also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x785671AA/0xB93C9C08`, the relinked focused score was `CURRENT (1920)`,
  and the unwanted early model-pointer spill still landed at `0x64(sp)`.
  Routing only `currentBatch->textureIndex` through the existing `temp` local
  before reading `surfaceType` on the same pad3-removed three-level guard
  branch improved the relinked focused score to `CURRENT (1520)`, but still
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x7C4CE1AA/0x7C1438D3`, and the unwanted
  early `gCurrentLevelModel` spill still appeared at `0x64(sp)`.
  Moving the batch offset loads (`facesOffset`, `verticesOffset`, and next
  `facesOffset`) before that texture-index `temp` surface read produced no
  movement from the texture-index carrier: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7C4CE1AA/0x7C1438D3`, relinked focused score stayed `CURRENT (1520)`,
  and the unwanted early `gCurrentLevelModel` spill still appeared at
  `0x64(sp)`.
  Adding an existing-`faceNum` carrier for `currentBatch->flags` on top of
  that same texture-index branch also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7B7E11AA/0x52CD4FC5`, the relinked focused score regressed to
  `CURRENT (1635)`, and the unwanted early `gCurrentLevelModel` spill still
  appeared at `0x64(sp)`.
  Keeping `pad3` intact but
  moving `XInInt = xIn; ZInInt = zIn;` before `get_inside_segment_count_xz` and
  passing those integer locals matched the target prologue conversion/call
  shape, but still inserted the unwanted pre-loop `gCurrentLevelModel` spill,
  regressed the relinked focused score to `CURRENT (2860)`, and failed full
  verify with calculated CRCs `0x7856718A/0x66208CAA`; source was restored and
  final full verify passed. Removing only unused `pad2` while promoting the
  current C also missed: relinked focused `CURRENT (2878)`, failed full verify
  with calculated CRCs `0x78567132/0xCBE53596`, shifted `spB0` from target
  `0xb0(sp)` to `0xb4(sp)`, and preserved the early `gCurrentLevelModel` spill
  at `0x64(sp)`. Removing both unused `pad2` and dead `pad3` together while
  promoting the current C also missed: frame shrank from target `0x128` to
  `0x120`, relinked focused score `CURRENT (2928)`, failed full verify with
  calculated CRCs `0x78566FC2/0xC14E0CEA`, and preserved the unwanted early
  `gCurrentLevelModel` spill family. A later first-dead-`pad` removal while
  promoting the current C also missed: full verify failed with calculated CRCs
  `0x7856713A/0x0D9BD727`, the relinked focused score worsened to
  `CURRENT (2886)`, `spB0` shifted from target `0xb0(sp)` to `0xb4(sp)`,
  `sp108` shifted to `0x10c(sp)`, and the unwanted early
  `gCurrentLevelModel` spill stayed at `0x64(sp)`. Source was restored and
  final full verify passed. A later statement-order variant moved the existing
  `XInInt = xIn` / `ZInInt = zIn` conversions immediately after
  `D_8011D308 = 0`, then stored `*arg3 = NULL`, passed the integer locals into
  `get_inside_segment_count_xz`, and removed the per-segment reassignments; it
  recreated the same early-conversion call-shape miss with relinked focused
  `CURRENT (2860)`, failed full verify with calculated CRCs
  `0x7856718A/0x66208CAA`, and still inserted the unwanted pre-loop
  `gCurrentLevelModel` spill to `0x60(sp)`. A later segment-index carrier
  through the existing `i` local (`i = spB0[var_fp]`, then indexing both
  segment arrays with `i`) also missed: relinked focused score worsened to
  `CURRENT (2925)`, full verify failed with calculated CRCs
  `0x78BF118A/0x21FC9F7D`, the early `gCurrentLevelModel` spill at `0x60(sp)`
  remained, and the segment-index register family drifted from the
  target/baseline `t1` toward `a3`/`t1`. Rewriting both grid bitmask doublings
  from `var_a1 *= 2` to `var_a1 += var_a1` also missed: object-only focused
  diff first printed stale `CURRENT (0)`, full verify failed with calculated
  CRCs `0x79235F02/0xA15ADC5A`, and the relinked focused score worsened to
  `CURRENT (3375)`. The diff inserted the known early `gCurrentLevelModel`
  spill at `0x60(sp)` and shifted the X/Z grid bitmask register family from
  target `a1` toward `v1`. Source was restored and final full verify passed.
  Rewriting only the X-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 <<= 1` also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with the known promoted CRC family
  `0x7856718A/0x66208CAA`, and the relinked focused score was `CURRENT (2860)`.
  The diff kept the known early `gCurrentLevelModel` spill at `0x60(sp)` plus
  broad grid/tail register drift. Source was restored and final full verify
  passed. Rewriting only the Z-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 <<= 1` produced no relinked movement from the promoted baseline:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, the focused
  score stayed `CURRENT (2860)`, and the same early `gCurrentLevelModel` spill
  at `0x60(sp)` plus grid/tail register drift remained. Source was restored
  and final full verify passed; do not repeat this Z-grid shift spelling.
  Rewriting only the X-grid loop condition from `i < 8` to `i != 8`
  also missed in the same family as the Z-grid condition probe: full verify
  failed with calculated CRCs `0x6818718A/0x890290E9`, the relinked focused
  score worsened to `CURRENT (3320)`, and the diff changed the X-grid loop
  exit to `li at,8`/`bne a3,at` while preserving the early
  `gCurrentLevelModel` spill at `0x60(sp)` plus broad grid/tail drift. Source
  was restored and final full verify passed; do not repeat this X-grid
  loop-condition spelling.
  Rewriting only the Z-grid loop condition from `i < 8` to `i != 8`
  also missed: full verify failed with calculated CRCs
  `0x6818718A/0x890290E9`, the relinked focused score worsened to
  `CURRENT (3320)`, and the diff inserted the known early
  `gCurrentLevelModel` spill at `0x60(sp)` while broadly rotating the grid
  register family. Source was restored and final full verify passed.
  A standalone current-source texture-index carrier
  (`temp = currentBatch->textureIndex; surface =
  gCurrentLevelModel->textures[temp].surfaceType`) also missed: full verify
  failed with calculated CRCs `0x7C4CE18A/0x3A298210`, and the relinked focused
  score improved from promoted-baseline `CURRENT (2780)` to `CURRENT (2435)`
  but still inserted the unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` with broad segment/grid/tail register drift. Source was restored
  and final full verify passed; do not repeat this standalone texture-index
  `temp` carrier without a separate model-spill fix.
  Keep active; do not repeat the simple moved `pad3` variant,
  the pointer-increment population spelling, either early-conversion call
  shape, the direct-cast `get_inside_segment_count_xz` call shape, this
  `D_8011D308`-first conversion/order variant, this segment-index `i` carrier,
  the grid bitmask `var_a1 += var_a1` spelling, the X-grid
  `var_a1 <<= 1` spelling, either X-grid or Z-grid `i != 8` loop-condition
  spelling, the scalar plane-carrier replacement, the
  unused-wave2 removal, or the declaration-only `pad2` removal or
  first-dead-`pad` removal.
- `trackbg_render_flashy` is also active, not parked. The 2026-05-17
  first-ring `xCos * 1280.0f + scaledXSin`, minimal `xPositions[3]` before
  `xPositions[2]` reorder, and `register f32 var_f16` allocation-hint probes
  all compiled but produced no object movement from the promoted baseline:
  uncompressed focused diff stayed `CURRENT (1808)`, still starting at the
  early position-array `$f16/$f18` split and `0x30(sp)` reload/add scheduling.
  A later single-site spelling of `zPositions[0]` as `-scaledXCos +
  scaledXSin` compiled but shrank the frame to `0x150`, worsened the relinked
  focused score to `CURRENT (13376)`, and failed full verify with calculated
  CRCs `0x218F9FFA/0x18F4A6D6`. Source was restored and full matching verify
  passed. A follow-up existing-`var_f16` first-ring carrier for the duplicated
  `-scaledXCos - (xSin * 1280.0f)` value (`xPositions[0] = var_f16`;
  `zPositions[1] = var_f16`) collapsed into the same bad family: frame `0x150`,
  focused score `CURRENT (13376)`, and full-verify CRCs
  `0x218F9FFA/0x18F4A6D6`. A later outer-ring assignment-order probe moved
  `xPositions[5]` before `zPositions[5]`, `zPositions[6]` before
  `xPositions[6]`, and `zPositions[7]` before `xPositions[7]` to mimic the
  target store order; it compiled but worsened the relinked focused score to
  `CURRENT (2786)` and failed full verify with calculated CRCs
  `0xDC7DB491/0xB2CAADCB`. A narrower single-site outer-ring reorder that only
  moved `zPositions[6]` before `xPositions[6]` also missed: relinked focused
  score worsened to `CURRENT (3860)` and full verify failed with calculated
  CRCs `0x93D338FF/0xB8A243D7`; source was restored and final full verify
  passed. A later paired first-ring
  `scaledXCos - (xSin * 1280.0f)` carrier through the existing `pad_sp108`
  local for `xPositions[1]` and `zPositions[2]` compiled but collapsed into
  the same bad frame-shrink family: frame `0x150`, focused score
  `CURRENT (13376)`, and full-verify CRCs `0x218F9FFA/0x18F4A6D6`.
  Routing only the doubled outer-ring cosine term through existing `pad_sp108`
  (`pad_sp108 = scaledXCos + scaledXCos`, then using it for `zPositions[5-8]`)
  compiled but produced no focused improvement from the promoted baseline:
  relinked focused diff stayed `CURRENT (1808)` and full verify failed with
  the same additive-double CRC family `0x93D338FF/0x03D9C8FE`. A combined
  first-ring plus outer-ring target-store-order probe also missed, failing
  full verify with calculated CRCs `0x8EAD21EA/0x274096CC` and worsening the
  relinked focused score to `CURRENT (3810)` while shrinking the frame from
  target `0x158` to `0x150`. Source was restored and final full verify passed;
  do not repeat this combined first/outer target-store-order probe. A paired
  first-ring `pad_sp108` carrier for the duplicated `-scaledXCos +
  scaledXSin` value (`zPositions[0] = pad_sp108; xPositions[3] = pad_sp108`)
  also collapsed into the bad frame-shrink family: frame `0x150`, relinked
  focused `CURRENT (13471)`, and full-verify CRCs
  `0x218F9FFA/0x18F4A6D6`. A later unused-`pad_sp100` carrier for the
  duplicated `-scaledXCos - (xSin * 1280.0f)` value (`xPositions[0]` and
  `zPositions[1]`) also collapsed into that bad family: frame `0x150`,
  relinked focused `CURRENT (13706)`, and full-verify CRCs
  `0x218F9FFA/0x18F4A6D6`. Rewriting only `xPositions[7]` from
  `scaledXCos + (2.0f * scaledXSin)` to
  `scaledXCos - -(2.0f * scaledXSin)` also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x1FBBB527/0xBCB1313B`, and the relinked focused score worsened to
  `CURRENT (2503)`. The diff kept the `0x158` frame but shifted the early
  negative-cosine register family plus first/outer position-array and later
  UV/vertex scheduling. Source was restored and final full verify passed; do
  not repeat this single-site x7 minus-negative spelling. Keep active and
  avoid repeating those no-op, single-site scaled-sine, first-ring
  existing-`var_f16` carrier,
  first-ring `pad_sp108`/unused-`pad_sp100` carrier, outer-ring
  assignment-order, single-site `zPositions[6]`/`xPositions[6]` reorder,
  exact outer-ring `x5/z5/z6/x6` store-order, `scaledXCos`-first assignment
  order, first-ring store-order grouping, single-site `zPositions[5]`
  subtract-chain, single-site x7 minus-negative spelling, or `pad_sp108`
  x1/z2/double-cosine carrier shapes. A later
  all-first-ring `scaledXSin` spelling replaced every remaining first-ring
  `(xSin * 1280.0f)` term in `xPositions[0..3]` and `zPositions[0..2]` with
  the existing `scaledXSin` carrier; it compiled but widened the frame to
  `0x168`, worsened the relinked focused score to `CURRENT (13466)`, and
  failed full verify with calculated CRCs `0x8310DF9D/0x3EA48C03`. Source was
  restored and final full verify passed. Do not repeat this all-first-ring
  `scaledXSin` rewrite.
- The baserom lives at `baseroms/baserom.us.v77.z64`, has SHA1
  `0cb115d8716dbbc2922fda38e533b9fe63bb9670`, and should remain untracked.
- This checkout needs repo-local binutils for the matching gate. Plain
  `gmake -j4` selects Homebrew `mips-linux-gnu-ld` and fails linking
  `build/src/objects.c.o` with an invalid `.strtab` offset.

## Matching Lessons

- `NON_MATCHING=1` builds are useful for behavior experiments but are not the
  acceptance gate for matching packets.
- Matching mode uses IDO and `std=gnu90`; keep source compatible with the
  existing compiler path.
- Prefer exact type width, signedness, volatile use, expression order, early
  return shape, and local variable lifetime before broad rewrites.
- If a source probe does not improve the focused diff, record the source-shape
  family in the handoff instead of retrying it blindly.
- `func_8008FF1C` has exhausted probe notes in `research/tasks/PARKED.md`:
  matching-mode
  promotion currently fails on a `v1` vs `t2` selected-track halfword
  load/branch after `level_name`, while broader local-order/branch probes
  cascade register allocation. A 2026-05-17 default-skipped revisit with
  `register s16 temp` also missed: full verify failed with calculated CRCs
  `0x55C240E7/0x18E4F9B4`, focused diff stayed `CURRENT (10)`, and the
  selected-track load/branch still used `v1`. Later `selectedTrack` allocation
  probes also missed: `s16 selectedTrack` worsened to `CURRENT (1355)` with
  calculated CRCs `0x5B5E4609/0x72935A6E`, while `register s32 selectedTrack`
  stayed `CURRENT (10)` with calculated CRCs `0x55C240E7/0x18E4F9B4`. Do not
  retry those same probes as the next packet. A later plain `s32 temp`
  selected-track carrier removed the unsequenced-assignment warning but
  worsened the focused score to `CURRENT (935)`, failed full verify with
  calculated CRCs `0x553930E7/0x227AD4A3`, still used `v1` for the
  selected-track branch, and broadened downstream register drift; do not retry
  that carrier. A 2026-05-17 direct table-branch spelling moved the selected
  track load/branch into the target `t2` register family, but missed because
  the hub-name store hoisted before the `lh`: full verify failed with
  calculated CRCs `0x53D440E3/0x6E70641F` and focused diff widened to
  `CURRENT (125)`. Duplicating the hub-name store inside both branch arms also
  missed with calculated CRCs `0xAED257D4/0xAE31DFED` and focused
  `CURRENT (500)`, adding a `move v1,v0` / duplicate-store family. A later
  compare-carrier spelling (`temp = -1; if (selectedTrack != temp)`) produced
  no object movement from the baseline: full verify failed with calculated
  CRCs `0x55C240E7/0x18E4F9B4`, focused diff stayed `CURRENT (10)`, and the
  selected-track branch still used `v1`. Moving the `selectedTrack`
  declaration after `temp` widened the focused diff to `CURRENT (58)`, failed
  full verify with calculated CRCs `0x55C24297/0x59444A08`, shifted stack
  slots, and still used `v1`; do not retry these compare-carrier or
  declaration-order probes. A 2026-05-17 no-temp selectedTrack-only probe
  removed the `s16 temp` carrier and unsequenced temp assignment while
  promoting the function. It matched the known plain-temp bad family rather
  than improving the target register: full verify failed with calculated CRCs
  `0x553930E7/0x227AD4A3`, focused diff was `CURRENT (935)`, and the
  selected-track load/branch still used `v1` instead of target `t2` while
  preserving the `sw v0,0(s0)` delay slot. Source restored and final verify
  passed; do not repeat this no-temp cleanup shape. A later 2026-05-17
  comma-store dependency probe (`cur->hubName = (selectedTrack = ..., levelName)`)
  compiled but was a no-op from the baseline: full verify failed with
  calculated CRCs `0x55C240E7/0x18E4F9B4`, focused diff stayed
  `CURRENT (10)`, and the selected-track load/branch still used `v1` instead
  of target `t2`. A `register s16 selectedTrack` probe collapsed into the
  known bad `s16 selectedTrack` family: full verify failed with calculated
  CRCs `0x5B5E4609/0x72935A6E`, focused diff widened to `CURRENT (1340)`,
  added sign-extension/register churn, and still used `v1`; source restored
  and final verify passed. A 2026-05-22 post-if common-store revisit that kept
  the current `temp`/`selectedTrack` assignments but used a direct table branch
  and moved `cur->hubName = levelName` after the if/else also missed: full
  verify failed with calculated CRCs `0xD60A52B7/0xA389682F`, focused diff
  widened to `CURRENT (985)`, and the branch still used `v1` rather than
  target `t2`. Removing the two selected-track temporary assignments from that
  post-if common-store shape moved the load/branch into the target `t2` family,
  but still missed: full verify failed with calculated CRCs
  `0xDC0852B7/0x5580AC19`, focused diff was `CURRENT (975)`, and the common
  hub-name store stayed after the join (`sw s4,0(s0)`) instead of the target
  delay-slot `sw v0,0(s0)`. Source restored and final verify passed; do not
  repeat either post-if common-store variant. If intentionally revisiting this
  no-park function, use a new source shape that preserves the direct-table
  `t2` load and restores the target delay-slot `sw v0, 0(s0)`.
- `func_80017A18` has exhausted probe notes in `research/tasks/PARKED.md`:
  existing C compiles when promoted, but diff evidence points at frame size,
  saved-register allocation, and float-temp lifetime mismatches. Do not retry
  the recorded dead-local, edge-plane-inline, or `register var_s6` probes as the
  next packet.
- `init_particle_buffers` has exhausted probe notes in
  `research/tasks/PARKED.md`: existing C compiles when promoted, but diff
  evidence points at saved-register allocation for the particle counts and
  allocator colour tag. A 2026-05-24 fresh promotion recheck failed full verify
  with CRCs `0xC451FA61/0xDA992566` and relinked focused diff score `2098`;
  adding a named allocator `colourTag` local made no object-code movement and
  stayed score `2098`. Source was restored and final verify passed. Do not
  retry the recorded `register` parameter, local count alias, pointer-to-global,
  plain-promotion, or allocator-tag-local probes as the next packet.
- `func_80049794` is active, not parked. Current focused evidence points at
  target `$f20/$f21` saves and broad `$f20` float-temp allocation across the
  plane physics function. Tested probes that did not solve it: `register f32
  var_f20`, moving `var_f20` declaration, explicit `f64 var_f20_d`, inline
  casts around the clamp expression, replacing `/ 2.0` and `/ 4.0` with
  multiply forms, splitting the initial `sqrtf` result into a new named local,
  `register f32 var_f14`, moving `var_f14` into the early local group,
  `register f32 segmentZVelocity`, direct assignment of the misc-asset
  interpolation into `var_f14`, delaying the `segmentZVelocity` copy until
  `handle_racer_top_speed`, `register` hints on `spEC`/`spD8`/`spD4`/`spD0`,
  naming `gRacerWaveCount - 1` in `var_v1` before the wave scan, and
  explicitly materializing the early zero through `var_f14` before the grounded
  wheel reset. The wave-scan probe matched the intended `v1/a0` idea locally
  but worsened the focused score to `CURRENT (5445)` by increasing register
  pressure and spilling/reshaping `spA2`. A related wave-count carrier probe
  (`var_v1 = gRacerWaveCount; var_a0 = var_v1 - 1`) compiled but worsened to
  `CURRENT (5540)`, causing broad integer-register churn through the wave scan
  and later scheduling. The early-zero `var_f14` probe
  compiled but left the focused score unchanged at `CURRENT (2550)` and did not
  move the `$f14/$f16` allocation split. Moving `spA3 = FALSE` after the
  `var_f20 = 1.0 - (var_f20 / 4.0)` inverse-gravity calculation also compiled
  but left the focused score unchanged at `CURRENT (2550)`. A later
  current-baseline `spA3` course-height placement probe that moved
  `spA3 = FALSE` after `var_f2 = (gCurrentCourseHeight - 50.0) -
  obj->trans.y_position` and immediately before the range guard missed: full
  verify failed with calculated CRCs `0x5FDDE03F/0xAA1C31A9`, and the relinked
  focused diff worsened to `CURRENT (3000)` while preserving the missing
  `$f20/$f21` saves, early `$f16` zero, and current `a0`-bound/`v1`-loop wave
  family. Source was restored and final full verify passed; do not repeat this
  `spA3` course-height placement spelling. Combining
  `register f32 var_f20` with `register f32 var_f14` also compiled but left the
  focused score unchanged at `CURRENT (2550)` and did not force the target
  `$f20/$f21` save pair. Routing the early grounded-wheel zero through the
  existing `spCC` float local before assigning `racer->unk84`/`unk88` also
  compiled but left the focused score unchanged at `CURRENT (2550)` and did not
  move the early `$f14` versus `$f16` zero split. Splitting the first `sqrtf`
  assignment into `var_f20 = sqrtf(...); var_f20 -= 2.0;` also compiled but left
  the focused score unchanged at `CURRENT (2550)`. Reusing
  `racerMiscAssetIdx` for the fractional `var_f14` calculation
  (`var_f0 = var_f14 - racerMiscAssetIdx`) likewise compiled but left the score
  unchanged at `CURRENT (2550)`. Reordering the misc-asset interpolation to
  spell the target-looking `current * (1.0 - frac) + next * frac` shape compiled
  but worsened the focused score to `CURRENT (2585)`. Loading `racer->velocity`
  once into `var_f14` and deriving `var_f0` from `var_f14` also compiled but
  worsened the focused score to `CURRENT (3095)`. Making the nearby velocity
  clamp constants explicitly single-precision (`4.0f`/`3.0f`) also compiled but
  worsened the focused score to `CURRENT (3045)`. Making the buoyancy gravity
  expression constants explicitly single-precision
  (`var_f20 = -1.0f - (var_f2 / 10.0f)`) compiled but left the focused score
  unchanged at `CURRENT (2550)`. Starting the `var_f20` lifetime at the first
  grounded-wheel zeroing (`var_f20 = 0.0f; racer->unk84 = var_f20;
  racer->unk88 = var_f20;`) also compiled but left the focused score unchanged
  at `CURRENT (2550)` and still did not introduce the target `$f20/$f21`
  prologue saves. A 2026-05-17 current-checkout reconfirmation of the same
  early-`var_f20` zero carrier failed full verify with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, stayed in the relinked focused compressed
  `CURRENT (2430)` family, and still used `$f16` for the early zero instead of
  target `$f14`; source was restored and final full verify passed. Combining
  `register f32 var_f20` with
  `register f32 racerVelocity` compiled but left the linked focused score
  unchanged at `CURRENT (2760)` in the current checkout and still did not
  introduce the target `$f20/$f21` prologue saves. Testing
  `register f32 racerVelocity` by itself on the promoted baseline also produced
  no relinked compressed focused change (`CURRENT (759)` under
  `--max-size 520`), failed full verify with the same calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and still lacked the target `$f20/$f21` prologue
  saves; do not repeat this standalone `racerVelocity` register hint. Reusing
  the existing `var_f0` local for the wave-block speed carrier instead of the
  named `racerVelocity` local worsened the relinked focused score to
  `CURRENT (3364)`, kept the target `$f20/$f21` prologue saves absent, and
  failed full verify with calculated CRCs `0xF40AF157/0xCBAF4125`; do not
  repeat this simple wave-speed `var_f0` carrier. Nesting the
  computer-player handling branch instead of using the short-circuit `&&`
  spelling also missed: it stayed at promoted-baseline `--max-size 520`
  `CURRENT (759)`, failed full verify with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and did not introduce target `$f20/$f21` saves; do
  not repeat this nested branch spelling. Routing the initial grounded-wheel
  zero through the existing `var_f2` local also produced no useful movement:
  it stayed at `--max-size 520` `CURRENT (759)`, failed full verify with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and kept the early zero in `$f16`;
  do not repeat this simple `var_f2` early-zero carrier. A dedicated early-zero
  carrier family also missed in the current checkout: plain `f32 zero` and
  `register f32 zero` locals used for the grounded-wheel stores and
  `racerVelocity` clamp widened the frame to `0x100`, failed full verify with
  calculated CRCs `0x5FDDDEDF/0x01A99146`, and still kept the early zero in
  `$f16` instead of target `$f14`; do not repeat this zero-carrier family.
  Moving the late normal-flight `spA1 = FALSE` initialization up next to
  `playerObjectMoved = FALSE` also missed in the current checkout:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x9935B12E/0xC848F044`, and the relinked focused
  score regressed to `CURRENT (4735)`. The diff inserted extra local byte
  stack traffic, dropped the target `$f20/$f21` prologue saves, kept the early
  zero in `$f16`, and widened the wave/register family; source was restored
  and final full verify passed. Do not repeat this early `spA1`
  initialization placement.
  Adding `register` to `racerThrottle` compiled but produced no object movement
  from the current promoted baseline: uncompressed focused diff stayed
  `CURRENT (1926)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the missing `$f20/$f21` prologue saves plus
  early `$f16` zero allocation remained unchanged; do not repeat this standalone
  `racerThrottle` register hint. Adding `register` to the `updateRateF`
  parameter was also a no-op against the promoted baseline: full verify failed
  with calculated CRCs `0x5FDDE03F/0xEF7A0514`, focused diff stayed
  `CURRENT (859)` under `--max-size 620`, and the target `$f20/$f21` prologue
  saves plus early `$f14` zero allocation remained absent. Source was restored
  and final full verify passed; do not repeat this `updateRateF` parameter
  register hint. Adding `register` to the integer `updateRate` parameter was
  also a no-op against the promoted baseline: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, focused diff stayed
  `CURRENT (859)` under `--max-size 620`, and the target `$f20/$f21` prologue
  saves plus early `$f14` zero allocation remained absent. Source was restored
  and final full verify passed; do not repeat this `updateRate` parameter
  register hint.
  Combining `register f32 var_f20` with `register f32 segmentZVelocity`
  compiled but produced no object change from the promoted baseline, stayed
  focused `CURRENT (2550)`, and still did not introduce the target `$f20/$f21`
  prologue saves. Splitting the first speed-magnitude operands into dedicated
  `xVelocity`/`zVelocity`/`yVelocity` locals before `sqrtf` compiled but widened
  the frame to `0x108`, worsened the focused object score to `CURRENT (3163)`,
  and still did not introduce the target `$f20/$f21` prologue saves. Splitting
  the first speed magnitude into the existing `var_f2` temp
  (`var_f2 = sqrtf(...) - 2.0; var_f20 = var_f2;` and using `var_f2` for the
  boss adjustment) compiled but left the focused object score unchanged at
  `CURRENT (2550)` and still did not introduce the target `$f20/$f21` prologue
  saves. Making the shared `var_f2` temp a `register f32` also compiled but
  left the focused object score unchanged at `CURRENT (2550)`. Splitting the
  buoyancy expression so `var_f20 = -1.0f` materializes before the
  `gCurrentStickY = -60` store matched that local target direction but worsened
  the focused object score to `CURRENT (2590)`. Removing the empty
  `if ((!racerSteerAngle)) {}` lifetime hint in the wave drift branch compiled
  but left the focused object score unchanged at `CURRENT (2550)`. Splitting
  the top-speed multiply into two assignments (`var_f14 *=
  handle_racer_top_speed(...); var_f14 *= 1.8;`) compiled but widened the
  frame to `0x100` and worsened the focused object score to `CURRENT (5977)`.
  A promoted current-baseline top-speed multiply regrouping
  (`var_f14 = var_f14 * (handle_racer_top_speed(obj, racer) * 1.8)`) also
  missed: full verify failed with calculated CRCs `0xAC61AD1B/0xFE0F8158`,
  relinked `./diff.sh func_80049794` stayed at `CURRENT (2760)`, and the
  function still lacked target `$f20/$f21` prologue saves while keeping the
  early zero in `$f16` and the wave scan in the known `a0`/`v1` drift family.
  Source was restored and final full verify passed; do not repeat this
  top-speed multiply regrouping. A worker-tested top-speed live-float carrier
  through existing `spCC` (`spCC = var_f14; var_f14 = (spCC *
  handle_racer_top_speed(obj, racer)) * 1.8`) compiled back to the same
  promoted object shape: `NON_MATCHING=1` object compile plus
  `./diff.sh -o func_80049794 --compress-matching 2 --no-pager` reported
  `CURRENT (0)`. It produced no saved `$f20/$f21` prologue-save movement, no
  early-zero allocation movement, and no wave bound/index movement. Source was
  restored and final full verify passed; do not repeat simple top-speed
  `spCC` live-float carrier spelling.
  Initializing `var_f20` at declaration (`f32 var_f20 = 0.0f`) compiled but
  left the focused object score unchanged at `CURRENT (2550)` and still did not
  introduce the target `$f20/$f21` prologue saves. Reusing `var_f20` for the
  early wave velocity magnitude instead of the separate `racerVelocity` local
  compiled but worsened the focused object score to `CURRENT (2704)` by
  perturbing the early wave block float-register family. Changing `sp60` from
  the existing `f32 sp60[4]` to `MtxF sp60` compiled with pointer-type warnings
  but widened the frame to `0x128` and worsened the focused object score to
  `CURRENT (4567)`. Moving `spA3 = FALSE` after the inverse-gravity assignment
  and before the course-height subtraction compiled but worsened the focused
  object score to `CURRENT (2790)`. Splitting the course-height expression into
  `var_f2 = gCurrentCourseHeight - 50.0; var_f2 -= obj->trans.y_position;`
  compiled but worsened the focused object score to `CURRENT (3530)`. Rewriting
  the inverse-gravity expression as `var_f20 = (4.0 - var_f20) / 4.0` compiled
  but worsened the focused object score to `CURRENT (4250)`. Splitting the
  early gravity value into a dedicated `f32 gravity` local from the initial
  speed magnitude through the `obj->y_velocity -= gravity` store compiled but
  widened the frame to `0x100` and worsened the focused object score to
  `CURRENT (2959)`. Staging `racerTrickType = racer->trickType` before the
  course-height expression and using that local in the range test compiled but
  left the focused object score unchanged at `CURRENT (2550)` and still did not
  introduce target `$f20/$f21` saves. Adding an empty `if (var_f20) {}`
  immediately after `apply_vehicle_rotation_offset` compiled but worsened the
  focused object score to `CURRENT (3045)` and still did not introduce target
  `$f20/$f21` saves. Rewriting the first speed-derived `var_f20` zero clamp as
  `0.0f` comparisons/assignments compiled but worsened the focused object score
  to `CURRENT (3355)` and still did not introduce target `$f20/$f21` saves.
  Extending the `var_f14` velocity lifetime before the first `sqrtf` block
  compiled but worsened the relinked focused score to `CURRENT (5000)` by
  moving the absolute-velocity path into `$f16` and still did not introduce
  target `$f20/$f21` saves. Staging the inverse-gravity fraction through the
  existing `var_f2` (`var_f2 = var_f20 / 4.0; var_f20 = 1.0 - var_f2`) compiled
  but worsened the relinked focused score to `CURRENT (3850)` and still did not
  introduce target `$f20/$f21` saves. Casting the misc-asset index assignment
  explicitly (`racerMiscAssetIdx = (s32) var_f14`) compiled but left the focused
  object score unchanged at `CURRENT (2550)` and still did not introduce target
  `$f20/$f21` saves. Reordering the default constant setup to assign `spD0`
  before `spD4` (`spD0 = 0.02; spD4 = 0.01; spD8 = 0.004`) compiled but left
  the focused object score unchanged at `CURRENT (2550)` and still did not
  introduce target `$f20/$f21` saves. Splitting the early gravity path into a
  `register f32 gravity` local from the first speed magnitude through the
  `obj->y_velocity -= gravity` store compiled but widened the frame to `0x100`,
  worsened the focused object score to `CURRENT (2959)`, and still did not
  introduce target `$f20/$f21` saves. Making the shared `var_f20` local
  volatile compiled but worsened the focused object score to `CURRENT (6441)`
  by forcing broad stack traffic and still did not introduce target
  `$f20/$f21` prologue saves. Changing the shared `var_f20` local itself to
  `f64` compiled but widened the frame to `0x108`, worsened the focused object
  score to `CURRENT (10417)`, and still did not introduce the target
  `$f20/$f21` prologue saves. Splitting the first speed magnitude through a
  separate `f64 speedMagnitude` local before assigning `var_f20 =
  speedMagnitude - 2.0` compiled but widened the frame to `0x108`, worsened
  the focused object score from `CURRENT (2550)` to `CURRENT (3163)`, and still
  did not introduce the target `$f20/$f21` prologue saves. Repeating that
  staging as `register f64 speedMagnitude` compiled but widened the frame to
  `0x100`, worsened the focused object score from `CURRENT (2550)` to
  `CURRENT (3007)`, and still did not introduce the target `$f20/$f21`
  prologue saves. Rewriting the boss
  adjustment from `var_f20 = ((var_f20 - 2.0) / 2.0)` to
  `var_f20 = (var_f20 * 0.5) - 1.0` compiled but worsened the focused object
  score from `CURRENT (2550)` to `CURRENT (3520)` and still did not introduce
  target `$f20/$f21` prologue saves. Splitting the same boss adjustment into
  two mutating assignments (`var_f20 -= 2.0; var_f20 /= 2.0`) compiled but
  worsened the focused object score from `CURRENT (2550)` to `CURRENT (3235)`
  by broadening first-speed/gravity float-register drift and still did not
  introduce target `$f20/$f21` prologue saves. A current-baseline
  divide-before-subtract boss-adjustment spelling
  (`var_f20 = (var_f20 / 2.0) - 1.0`) also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0xCF9C57E6/0xCC0EF4F1`, and the relinked focused diff worsened to
  `CURRENT (4030)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16`, and broadened the same first-speed/course-height plus
  wave-scan drift family. Source was restored and final full verify passed; do
  not repeat this first-speed boss-adjustment divide-before-subtract spelling.
  Reordering only the promoted
  current-baseline first speed-magnitude expression from `x*x + z*z + y*y` to
  `z*z + x*x + y*y` also missed: full verify failed with calculated CRCs
  `0x5FDDE03F/0x6CE3B8C9`, relinked focused diff worsened to `CURRENT (2770)`,
  and the function still lacked target `$f20/$f21` prologue saves and kept the
  early zero in `$f16` instead of target `$f14`. Source was restored and final
  full verify passed; do not repeat this current-baseline z-first speed
  magnitude expression-order spelling. A sibling promoted current-baseline
  expression-order probe from `x*x + z*z + y*y` to `x*x + y*y + z*z` collapsed
  into the same miss: full verify failed with calculated CRCs
  `0x5FDDE03F/0x6CE3B8C9`, relinked focused diff stayed `CURRENT (2770)`,
  target `$f20/$f21` prologue saves were still absent, and the early zero still
  used `$f16` instead of target `$f14`. Source was restored and final full
  verify passed; do not repeat this current-baseline x/y/z speed magnitude
  expression-order spelling. Rewriting the first
  speed-derived upper
  clamp as explicit single-precision
  (`if (var_f20 > 4.0f) { var_f20 = 4.0f; }`) compiled but worsened the
  focused object score from `CURRENT (2550)` to `CURRENT (4975)` and still did
  not introduce target `$f20/$f21` prologue saves. Rewriting the
  inverse-gravity expression as `var_f20 = 1.0 - (var_f20 * 0.25)` compiled but
  left the focused object score unchanged at `CURRENT (2550)` and still did not
  introduce target `$f20/$f21` prologue saves. Introducing a dedicated early
  `f32 zero` local for the grounded-wheel zeroing and early `racerVelocity`
  clamp compiled but widened the frame to `0x100`, worsened the focused object
  score from `CURRENT (2550)` to `CURRENT (3035)`, and still did not introduce
  target `$f20/$f21` prologue saves. Initializing `var_f14` at declaration
  (`f32 var_f14 = 0.0f`) compiled but left the focused object score unchanged at
  `CURRENT (2550)`, kept the early zero in `$f16`, and still did not introduce
  target `$f20/$f21` prologue saves. Carrying the interpolated misc-asset speed
  factor through the existing `segmentZVelocity` local into
  `handle_racer_top_speed`, boost override, throttle, and brake uses compiled
  but worsened the focused object score from `CURRENT (2550)` to
  `CURRENT (2800)`; it moved the key speed/gravity float family from `$f14` to
  `$f16` but still did not introduce target `$f20/$f21` prologue saves.
  Changing the long-lived misc-speed/top-speed carrier `var_f14` itself from
  `f32` to `f64` compiled but widened the frame to `0x100`, worsened the
  focused object score from `CURRENT (2550)` to `CURRENT (10933)`, and still
  did not introduce target `$f20/$f21` prologue saves. Rewriting the
  grounded-wheel zeroing as a chained assignment
  (`racer->unk88 = (racer->unk84 = 0.0f)`) compiled but produced no object
  change from the promoted baseline and left the focused object score unchanged
  at `CURRENT (2550)`, with the early zero still allocated as `$f16` instead of
  target `$f14`. Routing the same grounded-wheel zeroing through the existing
  `var_f0` local (`var_f0 = 0.0f; racer->unk84 = var_f0; racer->unk88 =
  var_f0`) also compiled but produced no object change from the promoted
  baseline and left the focused object score unchanged at `CURRENT (2550)`,
  with early zero still allocated as `$f16` instead of target `$f14`. Routing
  the same grounded-wheel zeroing through the existing `spEC` local
  (`spEC = 0.0f; racer->unk84 = spEC; racer->unk88 = spEC`) compiled and moved
  the early zero into target-like `$f14`, improving the relinked focused score
  from `CURRENT (2760)` to `CURRENT (2635)` and the compressed `--max-size 340`
  window from `CURRENT (664)` to `CURRENT (519)`, but it inserted an unwanted
  `swc1 $f14,0xec(sp)` before the stores and still failed full verify with
  calculated CRCs `0x191B2144/0x410B379B`; do not repeat this simple `spEC`
  early-zero carrier. Routing the same grounded-wheel zeroing through
  `segmentZVelocity` (`segmentZVelocity = 0.0f; racer->unk84 =
  segmentZVelocity; racer->unk88 = segmentZVelocity`) compiled but produced no
  relinked object change from the promoted baseline, staying `CURRENT (2760)`
  and `--max-size 340` `CURRENT (664)` with the same calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; do not repeat this segmentZVelocity early-zero
  carrier. Replacing
  the `gCurrentCarSteerVel = 0` store with an
  initialized no-op comparison (`gCurrentCarSteerVel = (updateRateF > 0.0f) *
  0`) compiled and improved the focused object score to `CURRENT (2490)`, same
  as the older `FAKEMATCH` no-op family, but remained nonmatching and still did
  not introduce target `$f20/$f21` prologue saves. Splitting the first
  horizontal/vertical speed magnitude into pre-`sqrtf` accumulation in
  `var_f20` (`var_f20 = x*x + z*z; var_f20 += y*y; var_f20 = sqrtf(var_f20) -
  2.0`) did introduce the target `$f20/$f21` prologue saves but widened the
  frame to `0x100` and worsened the focused score to `CURRENT (4049)`.
  Removing the two leading unused `pad5`/`pad7` locals with that same
  pre-`sqrtf` accumulation restored the target `0xf8` frame and kept
  `$f20/$f21` saves, but still worsened the focused score to `CURRENT (3932)`
  by shifting local stack slots and later scheduling. Routing the same
  pre-`sqrtf` speed-magnitude sum through the existing `spEC` local instead of
  `var_f20` (`spEC = x*x + z*z; spEC += y*y; var_f20 = sqrtf(spEC) - 2.0`)
  widened the local scheduling around the first `sqrtf`, worsened the focused
  score to `CURRENT (3300)`, and still did not introduce target `$f20/$f21`
  prologue saves. Removing only one leading unused pad at a time (`pad5` only
  or `pad7` only retained) with the same pre-`sqrtf` `var_f20` accumulation
  still introduced target `$f20/$f21` saves, but kept the frame widened to
  `0x100` and worsened the focused score to `CURRENT (4125)` for both
  variants. Combining the two leading unused pads into `UNUSED s32 pad[2]`
  compiled but produced no object change from the promoted baseline and left
  the focused score unchanged at `CURRENT (2550)`. Rewriting the grounded-wheel
  zero stores as double literals (`racer->unk84 = 0.0; racer->unk88 = 0.0`)
  changed the early zero allocation shape but cascaded register drift, worsened
  the focused score to `CURRENT (4685)`, and still did not introduce target
  `$f20/$f21` prologue saves. Spelling those stores as integer zero literals
  (`racer->unk84 = 0; racer->unk88 = 0`) produced the same bad focused score
  `CURRENT (4685)` and split the two stores across `$f4`/`$f6`, so do not
  retry that literal spelling either. Removing both trailing unused pads
  (`pad3`/`pad4`) with the same pre-`sqrtf` `var_f20` accumulation kept the
  target `0xf8` frame and target `$f20/$f21` prologue saves, improving on the
  leading-pad removal variant to `CURRENT (3620)`, but still left broad
  zero/wave/scheduling drift and did not match. Retaining exactly one trailing
  pad (`pad4` only or `pad3` only) with that same pre-`sqrtf` accumulation
  widened the frame back to `0x100` and regressed to `CURRENT (4049)` in both
  cases. Do not repeat these simple trailing-pad toggles; if continuing this
  family, inspect the remaining local-slot/scheduling drift from the
  both-trailing-pads-removed candidate instead. Staging that same
  both-trailing-pads-removed pre-`sqrtf` x/z partial sum through an existing
  float local (`spCC` or `spD8`) kept the target `0xf8` frame and
  `$f20/$f21` saves and nudged the score from `CURRENT (3620)` to
  `CURRENT (3615)`, but still left the early `$f14/$f16`, wave-register, and
  later scheduling drift. Do not repeat simple existing-float scratch aliases
  for this partial sum unless there is a new reason from target scheduling.
  Combining the both-trailing-pads-removed pre-`sqrtf` accumulation with an
  explicit early-zero carrier through `var_f14`
  (`var_f14 = 0.0f; racer->unk84 = var_f14; racer->unk88 = var_f14`) compiled,
  kept the target `0xf8` frame and `$f20/$f21` saves, but left the focused
  score unchanged at `CURRENT (3620)` and still allocated the early zero in
  `$f16` instead of target `$f14`. Do not repeat that combined source shape.
  Keeping the both-trailing-pads-removed pre-`sqrtf` accumulation but routing
  the post-`sqrtf` result through the existing `var_f2` local
  (`var_f2 = sqrtf(var_f20) - 2.0; var_f20 = var_f2`) compiled and left the
  focused score unchanged at `CURRENT (3620)`. Separating the `sqrtf` result
  from the subtraction through `var_f2`
  (`var_f2 = sqrtf(var_f20); var_f20 = var_f2 - 2.0`) also compiled and left
  the focused score unchanged at `CURRENT (3620)`. Reordering only that
  pre-`sqrtf` accumulation to start with the y component
  (`var_f20 = y*y; var_f20 += x*x + z*z`) compiled but worsened the focused
  score to `CURRENT (3640)` and disturbed the first speed-magnitude velocity
  load/register order. Do not repeat these two dataflow/operand-order variants.
  A later narrow buoyancy carrier spelling
  (`var_f0 = -1.0f; ... var_f20 = var_f0 - (var_f2 / 10)`) compiled but left
  the focused score unchanged at `CURRENT (2550)` and did not move the
  `$f14/$f20` allocation. Commuting the nearby player-index condition
  (`PLAYER_COMPUTER == var_v0`) and spelling it as an explicit inverted empty
  branch (`if (PLAYER_COMPUTER != var_v0) {} else if (...)`) also compiled but
  left the focused score unchanged at `CURRENT (2550)` and did not swap the
  target/current `bne v1,v0` versus `bne v0,v1` branch operands. Do not repeat
  these simple local source spellings. Staging `PLAYER_COMPUTER` through the
  existing `var_v1` local
  (`var_v1 = PLAYER_COMPUTER; if ((var_v0 == var_v1) &&
  (gCurrentPlayerIndex != var_v1))`) also compiled but left the focused score
  unchanged at `CURRENT (2550)`, did not swap the target/current branch
  operands, and did not move the `$f14/$f20` allocation. Do not repeat that
  staged-constant branch spelling either.
  Moving `spA2 = FALSE` inside the wave gate with an explicit non-wave `else`
  compiled but worsened the focused score to `CURRENT (7820)` by forcing
  stack-byte traffic for the drift flag and cascading broad integer/float
  register allocation. Do not repeat this wave-flag scheduling shape.
  Removing both leading pads and
  both trailing pads together with the same pre-`sqrtf` accumulation retained
  `$f20/$f21` saves but shrank the frame to `0xf0` and scored `CURRENT
  (3737)`, worse than the both-trailing-pads-only variant. Do not repeat the
  combined leading/trailing pad removal shape. Splitting the inverse-gravity
  assignment in place (`var_f20 /= 4.0; var_f20 = 1.0 - var_f20`) compiled but
  worsened the focused score from baseline `CURRENT (2550)` to `CURRENT
  (3435)` and still did not introduce the target `$f20/$f21` prologue saves.
  Do not repeat this in-place inverse-gravity spelling. Staging the same
  inverse-gravity divide through the existing `var_f0` local
  (`var_f0 = var_f20 / 4.0; var_f20 = 1.0 - var_f0`) compiled but worsened the
  focused score to `CURRENT (3445)` and still did not introduce the target
  `$f20/$f21` prologue saves. Do not repeat this `var_f0` staging spelling.
  Regrouping the nearby
  course-height expression as `var_f2 = gCurrentCourseHeight -
  obj->trans.y_position; var_f2 -= 50.0` compiled but worsened the focused
  score from baseline `CURRENT (2550)` to `CURRENT (3755)` and still did not
  introduce target `$f20/$f21` saves. Do not repeat this course-height grouping
  shape. Staging the misc-asset interpolation inverse fraction through the
  existing `var_f2` local
  (`var_f2 = 1.0 - var_f0; ... gCurrentRacerMiscAssetPtr[racerMiscAssetIdx] *
  var_f2`) compiled but worsened the focused score from baseline
  `CURRENT (2550)` to `CURRENT (3983)` and still did not introduce target
  `$f20/$f21` saves. Do not repeat this misc inverse-fraction staging shape.
  Adding an otherwise-dead `var_f14 = 0.0f` immediately after the zap/spinout
  sound block compiled but produced the same focused score as baseline,
  `CURRENT (2550)`, kept the early zero in `$f16`, and still did not introduce
  target `$f20/$f21` saves. Do not repeat this post-zap early-zero lifetime
  hint. Combining that post-zap `var_f14 = 0.0f` hint with the
  both-trailing-pads-removed pre-`sqrtf` `var_f20` accumulation compiled, kept
  the target `0xf8` frame and `$f20/$f21` saves, but left the focused score
  unchanged at `CURRENT (3620)` and still allocated the early zero in `$f16`.
  Do not repeat this combined post-zap-zero / trailing-pad-removal shape.
  Combining the both-trailing-pads-removed pre-`sqrtf` `var_f20` accumulation
  with the existing `gCurrentCarSteerVel = (var_f0 > 0.0f) * 0` no-op store
  compiled, kept the target `0xf8` frame and `$f20/$f21` saves, and improved
  the focused score from `CURRENT (3620)` to `CURRENT (3560)`, but remained
  nonmatching with the same wave-register mismatch family and later scheduling
  drift. Combining that same both-trailing-pads-removed pre-`sqrtf`
  accumulation and steer-vel no-op with the early grounded-wheel zero routed
  through `spEC` also missed: it kept the target `0xf8` frame and `$f20/$f21`
  saves, but failed full verify with calculated CRCs
  `0x3256B05A/0x4244923C` and lowered the relinked focused diff to
  `CURRENT (3480)`, but inserted the known unwanted `swc1 $f14,0xec(sp)`
  before the early zero stores and still kept wave-scan register/order drift.
  Do not repeat this weaker sibling of the later x/z/y `spEC` save-family
  probe. If continuing this family, inspect the x/z/y split or a way to keep
  the `$f14` zero without the `spEC` stack spill rather than the weaker plain
  trailing-pad-removal shape. Combining that same steer-vel
  no-op store with an existing-`spCC` pre-`sqrtf` partial-sum carrier lowered
  the numeric focused score to `CURRENT (3451)`, but did so by shrinking the
  frame to `0xf0` and dropping target `$f20/$f21` saves, so do not treat it as
  the preferred continuation of the save-family path. Combining the same
  steer-vel no-op store with the sibling existing-`spD8` pre-`sqrtf`
  partial-sum carrier produced the same result: `CURRENT (3451)`, frame shrunk
  to `0xf0`, and target `$f20/$f21` saves dropped. Do not treat either
  existing-float scratch/no-op side branch as the preferred continuation of the
  save-family path. Adding an empty `if (var_f14) {}` immediately after
  `apply_vehicle_rotation_offset` on the best save-family branch compiled but
  regressed from `CURRENT (3560)` to `CURRENT (3980)` and did not create the
  target call-adjacent `$f14` save/reload shape. Do not repeat this post-apply
  `var_f14` lifetime no-op. Staging the fifth
  `apply_vehicle_rotation_offset` argument through `pad2 = 0` on the same
  branch compiled but produced no object change from the save-family candidate,
  staying `CURRENT (3560)` with the same target/current call-adjacent `sw zero`
  versus `$f14` save mismatch. Do not repeat this argument-staging spelling.
  Splitting that same first speed-magnitude sum as x-first accumulation
  (`var_f20 = x*x; var_f20 += z*z; var_f20 += y*y; var_f20 = sqrtf(var_f20) -
  2.0`) compiled and improved the best save-family focused score from
  `CURRENT (3560)` to `CURRENT (3550)` while preserving the target `0xf8`
  frame family; if continuing this branch, inspect from this x-first split
  candidate rather than the weaker two-step x/z sum spelling. Combining that
  x/z/y save-family branch with the `spEC` early-zero carrier
  (`spEC = 0.0f; racer->unk84 = spEC; racer->unk88 = spEC`) improved the
  focused score further to `CURRENT (3415)`, preserved the target `0xf8` frame
  and `$f20/$f21` saves, but still failed full verify with calculated CRCs
  `0x32EE7D5A/0x1DE43B81`; it retained the unwanted `swc1 $f14,0xec(sp)`
  before the stores plus the wave-register drift. Source was restored and
  final full verify passed. Do not repeat this exact combined `spEC`
  early-zero / x/z/y save-family probe; if continuing this family, inspect how
  to keep the `$f14` zero without the `spEC` stack spill. The sibling
  x/y/z split spelling
  (`var_f20 = x*x; var_f20 += y*y; var_f20 += z*z; var_f20 = sqrtf(var_f20) -
  2.0`) compiled but regressed back to `CURRENT (3560)`, so do not continue
  from x/y/z unless new target scheduling evidence demands it. Adding a
  post-zap `var_f14 = 0.0f` carrier immediately after the zap sound call on
  the x/z/y best branch compiled but produced no object change and stayed
  `CURRENT (3550)`, so do not repeat that early `$f14` zero hint on this
  branch. Replacing the best branch's `var_f0` steer no-op with the initialized
  `updateRateF` spelling
  (`gCurrentCarSteerVel = (updateRateF > 0.0f) * 0`) also compiled but
  produced no object improvement and stayed `CURRENT (3550)`, so do not repeat
  that no-op source spelling on this branch. Keeping the save-family x/z/y
  setup but staging only the y component through `var_f2`
  (`var_f20 += z*z; var_f2 = y; var_f20 += var_f2 * var_f2`) kept the target
  `0xf8` frame and `$f20/$f21` saves, but worsened the focused score to
  `CURRENT (3765)` and disrupted the later `sound_play_spatial` scheduling; do
  not repeat this y-only `var_f2` staging shape. Staging only the z component
  through `var_f2` on that same save-family setup
  (`var_f2 = z; var_f20 += var_f2 * var_f2; var_f20 += y*y`) kept the target
  `0xf8` frame and `$f20/$f21` saves, but regressed to `CURRENT (3560)` and did
  not create the target-like `$f14` call-adjacent save/reload shape; do not
  repeat this z-only `var_f2` staging shape. Routing the first speed-magnitude
  accumulation through existing `var_f14` instead of `var_f20`
  (`var_f14 = x*x; var_f14 += z*z; var_f14 += y*y; var_f20 = sqrtf(var_f14) -
  2.0`) improved the numeric focused score to `CURRENT (3441)` with trailing
  pads removed, but shrank the frame to `0xf0` and dropped target
  `$f20/$f21` saves. Retaining trailing `pad3`/`pad4` with that same `var_f14`
  accumulator improved to `CURRENT (2940)` and restored the target `0xf8`
  frame, but still dropped `$f20/$f21` and carried gravity in `$f14`; adding
  `register f32 var_f20` to that retained-pad variant produced no object
  change. Adding an existing-`spCC` preserve of the post-clamp gravity carrier
  across `apply_vehicle_rotation_offset` on this retained-pad `var_f14`
  accumulator branch regressed to `CURRENT (3216)` and still did not recover
  target `$f20/$f21`; moving existing `spCC` after `spE0` shifted the
  call-adjacent spill/reload to `0xdc(sp)` but regressed further to
  `CURRENT (3236)`. Do not repeat these `var_f14` first-speed accumulator or
  `spCC` preserve shapes unless new evidence for recovering `$f20/$f21`
  appears. Reordering the save-family first-speed pre-`sqrtf` accumulation to
  z-first (`var_f20 = z*z; var_f20 += x*x; var_f20 += y*y`) kept the target
  `0xf8` frame and `$f20/$f21` saves, but regressed to `CURRENT (3560)`, worse
  than the x/z/y save-family best at `CURRENT (3550)`; do not repeat z-first
  pre-`sqrtf` accumulation unless new scheduling evidence specifically points
  there. Routing the first speed-magnitude accumulation through existing
  `var_f6` (`var_f6 = x*x; var_f6 += z*z; var_f6 += y*y; var_f20 =
  sqrtf(var_f6) - 2.0`) improved the numeric focused score to `CURRENT (3441)`
  with trailing pads removed, but shrank the frame to `0xf0` and dropped target
  `$f20/$f21` saves, matching the side-branch pattern of caller-saved
  accumulators; do not repeat simple `var_f6` accumulator staging without new
  save-pressure evidence. On the x/z/y save-family plus steer no-op branch,
  materializing the buoyancy `-1.0f` carrier through `var_f20` before
  `gCurrentStickY = -60` compiled and improved the focused score from
  `CURRENT (3550)` to `CURRENT (3520)`, but remained nonmatching with the
  broader call-adjacent and later scheduling drift. Combining that buoyancy
  carrier with the existing `spCC` preserve regressed to `CURRENT (3556)` and
  still did not recover the target `$f14` reload. Using `var_f0` as the
  `-1.0f` carrier instead produced no object improvement and stayed
  `CURRENT (3550)`. Combining the same buoyancy `var_f20 = -1.0f` carrier
  with the moved-`spCC` preserve slot also missed: it used `0xdc(sp)` but
  regressed to `CURRENT (3696)` and still spilled `$f4` instead of the target
  `$f14`. Do not repeat simple buoyancy `-1.0f` carrier spellings or
  moved-`spCC` combinations on this branch unless new evidence ties them to a
  separate scheduling fix. Combining the x/z/y save-family plus steer-noop plus
  `var_f20 = -1.0f` buoyancy carrier with a direct `racer->playerIndex ==
  PLAYER_COMPUTER` condition compiled and kept the early target frame/save
  family (`--max-size 520`: `CURRENT (270)`), but worsened the full focused
  score to `CURRENT (5155)` and failed full verify with calculated CRCs
  `0xCB45C241/0x9A5E2B4C`; do not repeat this direct-player-index combination
  on the save-family branch. Reordering the default handling constants on the
  same x/z/y save-family branch also produced no object improvement: assigning
  `spD0` before `spD4` stayed `CURRENT (3550)`, and assigning `spD8` before
  `spD0`/`spD4` also stayed `CURRENT (3550)`. Do not repeat simple
  save-family handling-constant order swaps.
  Preserving the long-lived `var_f14` across
  `apply_vehicle_rotation_offset` on the x/z/y save-family branch is useful
  evidence for the target call-adjacent `$f14` save/reload. A new `spDC` local
  widened the frame to `0x100` and worsened to `CURRENT (3883)`, so do not add
  that new stack slot. Reusing existing `spCC` for the preserve kept the target
  `0xf8` frame and improved the focused score to `CURRENT (3526)`, but spilled
  at `0xcc(sp)` instead of target `0xdc(sp)`. Reusing existing `spEC` kept
  `0xf8` but spilled at `0xec(sp)` and regressed to `CURRENT (3733)`. Reusing
  `racerVelocity` kept `0xf8` but worsened to `CURRENT (4114)` by perturbing
  the early wave float register family. Reusing existing `spD4` for the
  preserve on the promoted x/z/y pre-`sqrtf` branch widened the frame to
  `0x100`, worsened the focused score to `CURRENT (4335)`, and spilled `$f4`
  at `0xdc(sp)` instead of the target `$f14`; do not repeat this `spD4`
  preserve spelling. Reusing existing `spD0` for the same preserve also widened
  the frame to `0x100`, worsened to `CURRENT (4343)`, and spilled `$f4` at
  `0xd8(sp)` instead of target `$f14` at `0xdc(sp)`; do not repeat this `spD0`
  preserve spelling. Reusing existing `spD8` for the same preserve widened the
  frame to `0x100`, worsened to `CURRENT (7052)`, spilled at `0xe0(sp)`, and
  caused broad downstream scheduling churn; do not repeat this `spD8` preserve
  spelling. If continuing this preserve-across-call branch, start from the
  `spCC` result and solve the stack-slot/register drift without adding a new
  local or disturbing the wave block. Moving the existing
  `spCC` declaration after `spE0` targeted the desired stack slot: it kept the
  `0xf8` frame and made the call delay-slot spill use `0xdc(sp)`, but regressed
  to `CURRENT (3666)` because the spill used `$f4` and the target-like `$f14`
  reload was still missing. Making that moved `spCC` volatile forced reload
  traffic but shrank the frame to `0xf0`, dropped target `$f20/$f21` saves, and
  worsened to `CURRENT (4284)`. Do not repeat moved or volatile `spCC`
  declaration variants unless new evidence shows how to keep `$f20/$f21` and
  target `$f14` allocation together. A 2026-05-23 close save-family moved-`spCC`
  identity-preserve probe (`spCC = var_f14 + 0.0f` before
  `apply_vehicle_rotation_offset`, then `var_f14 = spCC` after, on top of the
  x/z/y pre-`sqrtf`, chained-zero, steer-noop, no-trailing-pad branch) also
  missed: full verify failed with calculated CRCs `0xF40EFA11/0x4DD27B9B`, and
  relinked `./diff.sh func_80049794` regressed to `CURRENT (4336)`. It kept
  the `0xdc(sp)` call-delay spill slot but still spilled `$f4` instead of
  target `$f14`, omitted the target `$f14` reload, kept the wave `a0`/`v1`
  drift, and broadened downstream scheduling. Source was restored and final
  full verify passed; do not repeat this moved-`spCC` identity-preserve
  spelling. Adding `register f32 var_f14` to this
  x/z/y save-family `spCC` preserve branch produced no improvement: original
  `spCC` stayed `CURRENT (3526)`, moved `spCC` stayed `CURRENT (3666)`, and
  the moved slot still spilled the wrong source FPR at `0xdc(sp)` instead of
  creating the target-like `$f14` reload. Reusing the existing otherwise-dead
  `segmentXVelocity` local as the preserve carrier on the x/z/y save-family
  plus chained-zero/steer-noop branch (`segmentXVelocity = var_f14` before
  `apply_vehicle_rotation_offset`; `var_f14 = segmentXVelocity` after) lowered
  the relinked focused score to `CURRENT (3318)`, but still failed full verify
  with calculated CRCs `0xF40EF8B9/0x958BDCC8`. The diff loaded from
  `0x9c(sp)` and spilled/reloaded through `0x70(sp)` rather than creating the
  target `$f14` save/reload at `0xdc(sp)`, while the wave `a0`/`v1` drift
  remained. Do not repeat this exact `segmentXVelocity` preserve spelling;
  if continuing this preserve family, solve the stack-slot/register placement
  rather than adding another preserve carrier. Reusing existing `var_f6` as
  the same preserve carrier on the x/z/y save-family plus chained-zero/
  steer-noop branch (`var_f6 = var_f14` before
  `apply_vehicle_rotation_offset`; `var_f14 = var_f6` after) was a near sibling
  miss: full verify failed with calculated CRCs `0xF40EF8A9/0xF04AE6F7`,
  relinked focused diff lowered to `CURRENT (3310)`, but it loaded from
  `0x9c(sp)` and spilled through `0x78(sp)` instead of target `$f14` at
  `0xdc(sp)`, with the wave `a0`/`v1` drift still present. Do not repeat this
  exact `var_f6` preserve carrier. Do not repeat register-`var_f14` / `spCC`
  preserve combinations. A narrow `segmentZVelocity` carrier
  spelling on the x/z/y save-family branch also missed: assigning
  `var_f14 = segmentZVelocity` immediately after
  `apply_vehicle_rotation_offset` compiled but produced no focused
  improvement, staying `CURRENT (3550)`, and using `segmentZVelocity` directly
  in the later `handle_racer_top_speed` multiply also stayed `CURRENT (3550)`.
  Do not repeat simple `segmentZVelocity` top-speed carrier spellings on this
  branch unless new target scheduling evidence points there. Moving the
  `spA3 = FALSE` initialization before the first speed-magnitude block compiled
  but worsened the promoted baseline from `CURRENT (2550)` to `CURRENT (2760)`;
  it inserted an early stack-byte store before the `sqrtf` family and still
  did not create the target `$f20/$f21` prologue saves. Do not repeat this
  early-`spA3` scheduling shape. Staging the z/y
  velocity
  component loads through the existing `var_f2` local before the first `sqrtf`
  (`var_f2 = z; var_f20 += var_f2 * var_f2; var_f2 = y; ...`) compiled and
  created the target-like call-adjacent `$f14` save/reload shape, but it
  regressed to `CURRENT (3751)` by shrinking the frame to `0xf0` and dropping
  the target `$f20/$f21` prologue saves; this is useful evidence for the call
  schedule, but not the preferred save-family continuation by itself. Retaining
  the trailing `pad3`/`pad4` locals with that same `var_f2` z/y component
  staging kept the target `0xf8` frame and improved the focused score to
  `CURRENT (3250)`, but still dropped the target `$f20/$f21` prologue saves and
  shifted the broad gravity carrier into `$f14`; if continuing this branch,
  inspect how to regain `$f20/$f21` save pressure without losing the
  call-adjacent `$f14` save/reload shape. Preserving that retained-pad branch's
  post-clamp gravity carrier through existing `spCC` across
  `apply_vehicle_rotation_offset` compiled and scored `CURRENT (3526)`, but it
  still dropped target `$f20/$f21` prologue saves and spilled/reloaded at
  `0xcc(sp)`. Moving existing `spCC` after `spE0` on the same retained-pad
  preserve branch shifted the call-adjacent spill/reload to `0xdc(sp)`, but
  regressed to `CURRENT (3546)` and still lacked target `$f20/$f21` saves. Do
  not repeat these retained-pad `spCC` preserve/slot variants unless new
  evidence shows how to recover the save family. Adding `register f32 var_f20`
  to that
  retained-pad `var_f2` component-staging branch compiled but produced the same
  focused score, `CURRENT (3250)`: the target `0xf8` frame and `$f14`
  call-adjacent shape stayed, but the target `$f20/$f21` prologue saves were
  still absent, so do not repeat this register hint on that branch. Adding
  `register f32 var_f14` to the same retained-pad `var_f2` z/y
  component-staging branch also missed: full verify failed with calculated CRCs
  `0x5FEF1D9D/0x4258C5C1`, and the relinked focused diff reported
  `CURRENT (3280)`. It preserved the target-like `$f14` save/reload at
  `0xdc(sp)`, but still dropped the target `$f20/$f21` prologue saves, shifted
  saved `ra`/`s1`/`s0` stack slots, kept early zero in `$f16`, and left the wave
  `a0`/`v1` drift. Do not repeat this `register var_f14` allocation hint on the
  retained-pad `var_f2` branch. Adding `register f32 var_f2` to that same
  retained-pad z/y component-staging branch also missed: full verify failed
  with calculated CRCs `0x5FEF1D9D/0x4258C5C1`, and the relinked focused diff
  reported `CURRENT (3620)`. It kept the target `0xf8` frame and the
  target-like call-adjacent `$f14` save/reload at `0xdc(sp)`, but still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16`, and left the
  wave `a0`/`v1` register/order swap. Source was restored and final full verify
  passed; do not repeat this `register var_f2` allocation hint on the
  retained-pad `var_f2` branch. Changing the inverse-gravity expression to
  multiply form (`var_f20 = 1.0 - (var_f20 * 0.25)`) on a promoted
  retained-pad `var_f2` z/y component-staging branch also missed: full verify
  failed with calculated CRCs `0x5FEF1D9D/0x4258C5C1`, the relinked focused
  diff reported `CURRENT (3620)`, target `$f20/$f21` prologue saves remained
  absent, early zero still allocated in `$f16`, and the wave scan still had
  the `a0`/`v1` swap. Source was restored and final full verify passed; do not
  repeat this retained-pad `var_f2`/inverse-multiply hybrid. Removing
  the two leading unused pads (`pad5`/`pad7`) while retaining trailing
  `pad3`/`pad4` on that same `var_f2` component-staging branch compiled but
  shrank the frame to `0xf0`, worsened the focused score to `CURRENT (3367)`,
  and still did not introduce the target `$f20/$f21` saves, so do not continue
  from this leading-pad removal shape. Removing only `pad5` while retaining
  `pad7` and trailing `pad3`/`pad4` kept the target `0xf8` frame but worsened
  the focused score to `CURRENT (3514)`, shifted several local stack slots, and
  still did not introduce target `$f20/$f21` saves. Removing only `pad7` while
  retaining `pad5` and trailing `pad3`/`pad4` produced the same focused score,
  `CURRENT (3514)`, with the same target `0xf8` frame, stack-slot shift, and
  missing target `$f20/$f21` saves; do not repeat these single-leading-pad
  removal shapes. Staging only the x component through `var_f2` on the
  x/z/y save-family plus steer-noop/buoyancy-carrier branch (`var_f2 = x;
  var_f20 = var_f2 * var_f2; ...`) compiled, kept the target `0xf8` frame, but
  regressed the relinked focused score to `CURRENT (4665)` with broad early
  wave and later scheduling drift; do not repeat this x-only `var_f2` carrier
  shape. A 2026-05-17 x/z/y pre-`sqrtf` save-family variant that removed
  trailing `pad3`/`pad4` and split the post-`sqrtf` subtraction as
  `var_f20 = sqrtf(var_f20); var_f20 -= 2.0` compiled and kept the target
  `0xf8` frame plus `$f20/$f21` prologue saves in the early diff, but worsened
  the relinked focused score to `CURRENT (4425)` (`--max-size 260`:
  `CURRENT (195)`) and failed full verify with calculated CRCs
  `0xB8B259CD/0xD730D2DE`; do not repeat this mutating post-`sqrtf`
  subtraction split. Combining the x/z/y save-family plus steer-noop branch
  with an early grounded-wheel zero carrier through existing `spEC`
  (`spEC = 0.0f; racer->unk84 = spEC; racer->unk88 = spEC`) compiled, kept the
  target `0xf8` frame and `$f20/$f21` saves, and improved the relinked
  compressed `--max-size 620` score from promoted baseline `CURRENT (859)` to
  `CURRENT (820)`, but it inserted an unwanted `swc1 $f14,0xec(sp)` before the
  two zero stores and still failed full verify with calculated CRCs
  `0x32EE7D5A/0x1DE43B81`; do not repeat this combined `spEC` early-zero spill
  shape unless a new source change removes the spill while preserving the save
  family. Combining the x/z/y save-family plus steer-noop branch with chained
  early grounded-wheel zero (`racer->unk88 = (racer->unk84 = 0.0f)`) and
  removed trailing `pad3`/`pad4` kept the target `0xf8` frame and `$f20/$f21`
  saves, removed the previous `spEC` zero-spill, and improved the relinked
  compressed `--max-size 620` score to `CURRENT (620)`, but full verify still
  failed with calculated CRCs `0xB8DD79CD/0xE47454ED`. Remaining focused drift
  was the wave-scan `a0`/`v1` register/order swap plus first-speed arithmetic
  register-family drift. A 2026-05-23 close save-family explicit-subtract
  wave-speed probe on that same x/z/y/chained-zero/steer-noop/no-trailing-pad
  branch (`racerVelocity = 0.0f - racer->velocity`) also missed: full verify
  failed with calculated CRCs `0xB8278BD1/0xEE8E0068`, and relinked
  `./diff.sh func_80049794` regressed to `CURRENT (5440)`. It kept the target
  `0xf8` frame and `$f20/$f21` prologue saves, but changed the wave-speed
  negate into a subtract family, broadened wave FPR/register scheduling,
  preserved the wave `a0`/`v1` drift, and still omitted the target
  call-adjacent `$f14` save/reload. Source was restored and final full verify
  passed; do not repeat this close save-family explicit-subtract wave-speed
  spelling. Reversing only the wave count comparison spelling to
  `(gRacerWaveCount - 1) == var_a0` was a no-op: full verify produced the same
  CRCs and the relinked focused diff stayed `CURRENT (620)` with the same
  `a0`/`v1` swap. Making only the wave-height threshold explicit single
  precision (`obj->trans.y_position + 5.0f`) on the same branch also produced
  no object movement: full verify failed with the same calculated CRCs
  `0xB8DD79CD/0xE47454ED`, and the relinked focused diff reported `CURRENT
  (2132)` under the uncompressed `--max-size 760` window with the same
  `a0`/`v1` wave swap. Commuting that threshold to
  `5 + obj->trans.y_position` on the same branch also missed: it kept the
  target `0xf8` frame and `$f20/$f21` saves, failed full verify with calculated
  CRCs `0xB8CD59CD/0xDE963C8F`, and relinked focused diff reported
  `CURRENT (2142)` with the same `a0`/`v1` wave-register mismatch family. Do
  not repeat this exact chained-zero save-family shape, the comparison-only
  wave operand spelling, or the explicit/commuted wave-threshold spellings.
  Combining that close chained-zero x/z/y save-family branch with an
  existing-`spCC` preserve across `apply_vehicle_rotation_offset`
  (`spCC = var_f14; ...; var_f14 = spCC`) also missed badly: it kept the
  target `0xf8` frame but regressed the relinked focused score to
  `CURRENT (5976)`, failed full verify with calculated CRCs
  `0xF40EFA01/0x5672460E`, and inserted broad `$f14` save/reload traffic
  through the spinout and voice/sound scheduling path. Do not repeat this
  close-branch `spCC` preserve combination.
  Rewriting the wave scan as a bound-local copy while-loop
  (`var_a0 = gRacerWaveCount - 1; var_v1 = var_a0; while (...) { var_a0--; };
  if (var_a0 == var_v1)`) also missed: full verify failed with calculated CRCs
  `0x527F28C9/0xA7E04D93`, the relinked focused score widened to `CURRENT
  (4252)`, and the diff showed extra `spA2` stack-byte traffic plus broader
  wave-block register churn rather than the target `a0`/`v1` allocation. Do
  not repeat this local-copy while-loop wave-bound spelling; keep the function
  active and continue by solving the wave register/order or first-speed
  arithmetic drift without losing the frame/save family. An explicit-break
  loop on the close chained-zero/x/z/y/steer-noop save-family branch
  (`var_v1 = gRacerWaveCount - 1; for (var_a0 = var_v1; var_a0 >= 0; var_a0--) {
  if (!(...)) break; } if (var_a0 == var_v1)`) also missed worse: full verify
  failed with calculated CRCs `0xE5832189/0x7F0FCADC`, relinked focused diff
  widened to `CURRENT (8805)`, and the wave block shifted into `a3/v1` plus
  early `spA2` stack-byte traffic rather than target `v1/a0`. Source was
  restored and final full verify passed; do not repeat this explicit-break
  close-branch wave-scan spelling. Two first-speed carrier variants on
  that same branch both regressed by losing the target frame/save family: using
  existing `var_f6` for the pre-`sqrtf` sum failed full verify with calculated
  CRCs `0x6035EC5F/0x4C26F14E` and relinked focused `CURRENT (2326)`, while
  keeping only the x/z sum in `var_f20` and adding the y component in the
  `sqrtf` argument failed with calculated CRCs `0x5F84A15F/0x79820DF5` and
  relinked focused `CURRENT (2311)`. Both shrank the frame to `0xf0` and
  dropped `$f20/$f21` saves, so do not repeat existing-temp or call-argument
  y-component first-speed carriers unless new evidence shows how to retain the
  save family. A close save-family z-product carrier variant (`var_f2 =
  obj->z_velocity * obj->z_velocity; var_f20 += var_f2`) also missed: full
  verify failed with calculated CRCs `0xB8DECACD/0x023D0D27`, the relinked
  focused diff worsened to `CURRENT (4640)`, and the early zero allocation
  shifted away from the target `$f14` family while the wave `a0`/`v1` drift
  remained. Source was restored and final full verify passed; do not repeat
  this first-speed `var_f2` z-product carrier. A close save-family
  `segmentXVelocity` first-speed carrier (`segmentXVelocity = x*x; var_f20 =
  segmentXVelocity; var_f20 += z*z; var_f20 += y*y`) also missed: full verify
  failed with calculated CRCs `0xB8DD79CD/0xCD5971FB`, relinked focused diff
  worsened to `CURRENT (4365)`, and although the target `0xf8` frame and
  `$f20/$f21` prologue saves remained, the wave `a0`/`v1` swap and later
  scheduling drift were unchanged. Source was restored and final full verify
  passed; do not repeat this first-speed `segmentXVelocity` carrier. A close
  save-family `racerVelocity` first-speed carrier (`racerVelocity = x*x;
  var_f20 = racerVelocity; var_f20 += z*z; var_f20 += y*y`) also missed: full
  verify failed with calculated CRCs `0xB8B409CD/0xBE8F170B`, relinked focused
  diff widened to `CURRENT (4555)`, early zero shifted from target `$f14` to
  `$f12`, and the wave `a0`/`v1` swap remained. Source was restored and final
  full verify passed; do not repeat this first-speed `racerVelocity` carrier.
  A sibling close save-family `segmentZVelocity` first-speed carrier
  (`segmentZVelocity = x*x; var_f20 = segmentZVelocity; var_f20 += z*z;
  var_f20 += y*y`) collapsed into the `segmentXVelocity` miss family: full
  verify failed with calculated CRCs `0xB8DD79CD/0xCD5971FB`, relinked focused
  diff stayed `CURRENT (4365)`, and the target `0xf8` frame plus `$f20/$f21`
  prologue saves remained while the wave `a0`/`v1` swap and later scheduling
  drift were unchanged. Source was restored and final full verify passed; do
  not repeat this first-speed `segmentZVelocity` carrier. A current-baseline
  in-place `var_f20` first-speed magnitude spelling (`var_f20 = x; var_f20 *=
  var_f20; var_f20 += z*z; var_f20 += y*y; var_f20 = sqrtf(var_f20) - 2.0`)
  also missed: full verify failed with calculated CRCs
  `0x5FF65B3F/0xBF0023C8`, relinked focused diff reported `CURRENT (3255)`,
  the frame stayed `0xf8` but `$f20/$f21` prologue saves were still absent,
  early zero stayed in `$f16`, and the wave bound/index allocation remained
  reversed as current `a0` bound plus `v1` loop index instead of target
  `v1`/`a0`. Source was restored and final full verify passed; do not repeat
  this current-baseline in-place `var_f20` first-speed spelling. A sibling
  current-baseline named-component first-speed spelling (`segmentXVelocity =
  x*x; segmentZVelocity = z*z; var_f20 = sqrtf(segmentXVelocity +
  segmentZVelocity + y*y) - 2.0`) also missed: full verify failed with
  calculated CRCs `0xCBBC5B5C/0x66C212B9`, relinked focused diff regressed to
  `CURRENT (5950)`, the frame stayed `0xf8` but `$f20/$f21` prologue saves
  were still absent, early zero stayed in `$f16`, and the wave bound/index
  allocation remained reversed with extra float-register churn. Source was
  restored and final full verify passed; do not repeat this current-baseline
  `segmentXVelocity`/`segmentZVelocity` first-speed component-carrier spelling.
  A current-baseline y-first speed magnitude expression order
  (`sqrtf(y*y + x*x + z*z) - 2.0`) also missed: full verify failed with
  calculated CRCs `0x5FDDE03F/0x8DEA1B78`, relinked focused diff reported
  `CURRENT (2775)`, the frame stayed `0xf8` but `$f20/$f21` prologue saves
  were still absent, early zero stayed in `$f16`, and the wave bound/index
  allocation remained reversed as current `a0`/`v1` instead of target
  `v1`/`a0`. Source was restored and final full verify passed; do not repeat
  this current-baseline y-first speed magnitude expression order.
  A current-baseline positive-break wave scan (`for (...; var_a0 >= 0;
  var_a0--) { if (gRacerCurrentWave[var_a0]->waveHeight >=
  obj->trans.y_position + 5) break; }`) also missed: full verify failed with
  calculated CRCs `0xB9C0DBCD/0xB65AA559`, relinked focused diff regressed to
  `CURRENT (8035)`, the frame stayed `0xf8` but `$f20/$f21` prologue saves
  were still absent, early zero stayed in `$f16`, and the wave scan shifted
  into a broader `v0/v1` pointer/index family with `c.le.s`/`bgez` flow.
  Source was restored and final full verify passed; do not repeat this
  current-baseline positive-break wave-scan spelling. A
  2026-05-17 save-family
  wave-bound comma-assignment probe
  (`var_a0 = (var_v1 = gRacerWaveCount - 1)` and `if (var_a0 == var_v1)`) on
  top of the close chained-zero/x/z/y/steer-noop branch kept the target `0xf8`
  frame and `$f20/$f21` saves, but regressed the relinked focused score to
  `CURRENT (6100)` and failed full verify with calculated CRCs
  `0x2E4A9A41/0xD04D4E64`; it widened wave-block integer-register churn and
  disturbed later scheduling, so do not repeat this comma-assignment
  wave-bound source shape. Splitting the same wave-bound spelling into two
  assignments (`var_v1 = gRacerWaveCount - 1; for (var_a0 = var_v1; ...); if
  (var_a0 == var_v1)`) on the same close save-family branch produced the same
  failed full-verify CRCs `0x2E4A9A41/0xD04D4E64` and relinked focused
  `CURRENT (6100)`, with the same widened wave integer-register churn and
  later scheduling drift. Treat this split-`var_v1` form as the same bad
  wave-bound family, not a new continuation point. A follow-up existing-`var_v0`
  wave-count carrier on the same close save-family branch (`var_v0 =
  gRacerWaveCount`; loop from `var_v0 - 1`; compare against `var_v0 - 1`)
  also missed: it kept the target `0xf8` frame and `$f20/$f21` saves, but
  regressed the relinked focused score to `CURRENT (4557)`, failed full verify
  with calculated CRCs `0xA637D7C4/0x633471A3`, and widened wave-register churn
  by introducing `a0/a1/v0/v1` drift through the scan. Do not repeat this
  `var_v0` wave-count carrier spelling on the close save-family branch.
  A fresh-local `var_t1` wave-bound carrier on the same close save-family
  branch (`var_t1 = gRacerWaveCount - 1; for (var_a0 = var_t1; ...);
  if (var_a0 == var_t1)`) also missed: full verify failed with calculated CRCs
  `0xEA44ADF2/0x9E975CE5`, the relinked focused diff regressed to
  `CURRENT (7242)`, and the function frame widened from target `0xf8` to
  `0x100` while the wave scan shifted into broader `a0/v0/v1` churn. Source
  was restored and final full verify passed; do not repeat this close-branch
  fresh-`var_t1` wave-bound carrier.
  A close save-family continuation that carried the wave-height threshold
  through existing `var_f6` (`var_f6 = obj->trans.y_position + 5.0f`, then the
  scan compares wave height against `var_f6`) also missed: it kept the target
  `0xf8` frame and `$f20/$f21` saves, but regressed the relinked focused score
  to `CURRENT (6580)`, failed full verify with calculated CRCs
  `0xB523523E/0x7EEBEC55`, and shifted the wave scan into a worse register
  schedule with the `a0`/`v1` allocation still wrong. Source was restored and
  final full verify passed; do not repeat this existing-`var_f6`
  wave-threshold carrier. A sibling close save-family continuation carrying
  the threshold through existing `spEC` (`spEC = obj->trans.y_position + 5.0f`)
  was worse: full verify failed with calculated CRCs
  `0xC65CFFD3/0xC660208A`, the relinked focused score regressed to
  `CURRENT (8620)`, early zero allocation fell back to `$f16`, and the wave
  path inserted a `0xec(sp)` spill while the bound/index registers remained
  wrong. Source was restored and final full verify passed; do not repeat this
  `spEC` wave-threshold carrier.
  A 2026-05-17 current-baseline split wave-bound probe also missed:
  promoting the current C and spelling `var_v1 = gRacerWaveCount - 1; for
  (var_a0 = var_v1; ...); if (var_a0 == var_v1)` worsened the relinked focused
  score from promoted-baseline `CURRENT (2430)` to `CURRENT (4920)`, failed
  full verify with calculated CRCs `0x5790053C/0x1C8C0179`, introduced `spA2`
  stack-byte traffic, and widened wave-scan register churn instead of matching
  target `v1` bound plus `a0` loop-index allocation. Source was restored and
  final full verify passed; do not repeat this current-baseline split
  wave-bound spelling. A current-baseline existing-`var_t9` wave-bound carrier
  (`var_t9 = gRacerWaveCount - 1; for (var_a0 = var_t9; ...); if (var_a0 ==
  var_t9)`) also missed: full verify failed with calculated CRCs
  `0x1ED9F907/0x570DED85`, the relinked focused score worsened from
  promoted-baseline `CURRENT (2430)` to `CURRENT (4460)`, and the wave block
  shifted into broad integer-register churn with `spA2` stack-byte traffic
  rather than target `v1/a0/v0`. Source was restored and final full verify
  passed; do not repeat this current-baseline existing-`var_t9` wave-bound
  carrier. A current-baseline sibling using existing `temp_t7` as the
  wave-bound carrier (`temp_t7 = gRacerWaveCount - 1; for (var_a0 =
  temp_t7; ...); if (var_a0 == temp_t7)`) collapsed into the same CRC family:
  full verify failed with calculated CRCs `0x1ED9F907/0x570DED85`, and the
  relinked focused diff worsened to `CURRENT (5080)`. The diff still lacked
  target `$f20/$f21` prologue saves, kept the early zero in `$f16`, and shifted
  the wave scan into broad integer-register churn rather than target `v1`
  bound plus `a0` loop-index allocation. Source was restored and final full
  verify passed; do not repeat this current-baseline existing-`temp_t7`
  wave-bound carrier. A current-baseline sibling using existing `var_t0` as
  the wave-bound carrier (`var_t0 = gRacerWaveCount - 1; for (var_a0 =
  var_t0; ...); if (var_a0 == var_t0)`) also missed: full verify failed with
  calculated CRCs `0x9AF972E0/0xD531DD3C`, and the relinked focused diff
  worsened to `CURRENT (4970)`. The diff still lacked target `$f20/$f21`
  prologue saves, kept the early zero in `$f16`, and shifted the wave scan
  into `t0/v0/v1` register churn rather than target `v1` bound plus `a0`
  loop-index allocation. Source was restored and final full verify passed; do
  not repeat this current-baseline existing-`var_t0` wave-bound carrier. A
  current-baseline existing-`i` wave-bound carrier
  (`i = gRacerWaveCount - 1; for (var_a0 = i; ...); if (var_a0 == i)`) also
  missed: full verify failed with calculated CRCs `0x1E560907/0x082E5A2F`,
  the relinked focused score worsened from current promoted baseline
  `CURRENT (2760)` to `CURRENT (5110)`, and the wave block widened into broad
  register churn plus `spA2` stack-byte traffic instead of solving the target
  `v1/a0/v0` allocation. Source was restored and final full verify passed; do
  not repeat this current-baseline existing-`i` wave-bound carrier. A
  current-baseline existing-`var_v0` wave-bound carrier (`var_v0 =
  gRacerWaveCount - 1; for (var_a0 = var_v0; ...); if (var_a0 == var_v0)`)
  also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0x422CAA9F/0x6001E375`, and the
  relinked focused score worsened to `CURRENT (4660)`. The diff still lacked
  the target `$f20/$f21` prologue saves, kept the early zero in `$f16` instead
  of target `$f14`, and shifted the wave block into a broader `v1/a0/v0`
  register family rather than target `v1` bound plus `a0` loop index. Source
  was restored and final full verify passed; do not repeat this
  current-baseline existing-`var_v0` wave-bound carrier. A
  current-baseline explicit `var_t1 = PLAYER_COMPUTER` allocation
  probe reused that local for the early `gCurrentPlayerIndex` wave gate and
  `trickType == -1` check. It did create the target-like early `li t1,-1`
  shape, but full verify failed with calculated CRCs
  `0x5FDDDF87/0x4196D76A`, the relinked focused diff reported
  `CURRENT (2879)`, the frame widened to `0x100`, target `$f20/$f21` prologue
  saves were still absent, early zero still used `$f16`, and the wave loop
  still kept `a0`/`v1` opposite the target. Source was restored and final full
  verify passed; do not repeat this standalone `var_t1` `PLAYER_COMPUTER`
  allocation probe. A current-baseline `register s32 var_a0` allocation hint
  also produced no useful movement: full verify failed with the promoted
  baseline CRC family `0x5FDDE03F/0xEF7A0514`, the relinked focused diff
  reported `CURRENT (2430)`, and the function still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16`, and kept the wave loop `a0`/`v1`
  allocation opposite the target. Source was restored and final full verify
  passed; do not repeat this standalone `var_a0` register hint. A sibling
  current-baseline `register s32 var_v1` allocation hint was also a no-op:
  full verify failed with the same promoted baseline CRC family
  `0x5FDDE03F/0xEF7A0514`, the relinked focused diff stayed
  `CURRENT (2430)`, and the target `$f20/$f21` saves, early `$f14` zero, and
  wave `v1` bound / `a0` loop-index order were still missing. Source was
  restored and final full verify passed; do not repeat this standalone
  `var_v1` register hint. A current-baseline pointer-parameter allocation hint
  (`register Object *obj, register Object_Racer *racer`) also compiled but
  produced no useful movement: full verify failed with the same promoted
  baseline CRC family `0x5FDDE03F/0xEF7A0514`, the relinked focused diff
  stayed `CURRENT (2430)`, and the target `$f20/$f21` prologue saves, early
  `$f14` zero, and wave `v1`/`a0` allocation were still missing. Source was
  restored and final full verify passed; do not repeat this pointer-parameter
  register hint. A current-baseline explicit decrementing
  `WaterProperties **wavePtr` walk
  (`for (var_a0 = gRacerWaveCount - 1, wavePtr =
  &gRacerCurrentWave[var_a0]; ...; var_a0--, wavePtr--)`) also missed badly:
  full verify failed with calculated CRCs `0x791E2110/0x2A523649`, the
  relinked focused score worsened from current promoted baseline
  `CURRENT (2760)` to `CURRENT (5680)`, widened the frame to `0x100`, kept the
  early zero in `$f16`, and broadened the wave scan into `a*/v1` register
  churn instead of solving target `v1/a0/v0` allocation. Source was restored
  and final full verify passed; do not repeat this current-baseline
  `wavePtr` pointer-walk spelling. A bounded worker sibling that combined the
  split `var_v1 = gRacerWaveCount - 1; var_a0 = var_v1` bound/index shape with
  a `WaterProperties **wave = &gRacerCurrentWave[var_a0]` pointer-carry also
  missed: full verify failed with calculated CRCs
  `0x0F72E671/0xB9F156E0`, relinked focused diff regressed to
  `CURRENT (7197)`, the frame widened to `0x100`, stack locals shifted, target
  `$f20/$f21` prologue saves and early `$f14` zero were still absent, and the
  target `v1` bound plus `a0` loop-index allocation was still missing. Worker
  source was restored and verified; do not repeat this split-bound
  pointer-carry sibling. A current-baseline local
  `WaterProperties *wave` element carrier with an explicit `for`/`break` scan
  and later `wave->rot.y` reuse missed even worse: full verify failed with
  calculated CRCs `0x1EB8E425/0x5BFDC8B4`, the relinked focused score
  worsened from current promoted baseline `CURRENT (2760)` to
  `CURRENT (9650)`, widened the frame to `0x100`, kept the early zero in
  `$f16`, and reshaped the wave scan into broad `v*/a*` churn. Source was
  restored and final full verify passed; do not repeat this current-baseline
  `wave` element-carrier scan spelling.
  Carrying the wave-height threshold through existing `var_f0` on the same
  close save-family branch (`var_f0 = obj->trans.y_position + 5.0f`, then the
  scan compares wave height against `var_f0`) also missed: it kept the target
  `0xf8` frame and `$f20/$f21` saves, but regressed the relinked focused score
  to `CURRENT (7555)`, failed full verify with calculated CRCs
  `0x2B7A77D5/0x5B507890`, and shifted the wave block into a worse
  `a0/v1/f12/f14` register family with extra stack traffic. Do not repeat this
  explicit `var_f0` wave-threshold carrier. A 2026-05-17 explicit decrementing
  `WaterProperties **wavePtr` spelling on top of the close chained-zero/x/z/y/
  steer-noop branch also missed badly: it widened the frame from target `0xf8`
  to `0x100`, regressed the relinked focused score to `CURRENT (7232)`, failed
  full verify with calculated CRCs `0xC51623A2/0xD2F96DC4`, and shifted the scan
  into a `v0/a1/v1` family rather than solving the target `v1/a0/v0` order.
  Source was restored and final full verify passed. Do not repeat this explicit
  `wavePtr` pointer-walk shape. A 2026-05-17 explicit first-compare plus
  `do`-loop wave scan on the close chained-zero/x/z/y/steer-noop branch also
  missed as a no-op against that close CRC family: full verify failed with
  calculated CRCs `0xB8DD79CD/0xE47454ED`, relinked focused diff reported
  `CURRENT (3260)` under `--max-size 900`, and the wave scan still showed the
  current `a0`/`v1` register order opposite the target. Source was restored and
  final full verify passed. Do not repeat this explicit first-compare
  `do`-loop wave-scan spelling. A close save-family continuation that kept the
  x/z/y pre-`sqrtf` accumulation, steer-vel no-op, chained grounded-wheel zero,
  and removed trailing `pad3`/`pad4`, but rewrote the wave scan as
  `var_v1 = gRacerWaveCount - 1; var_a0 = var_v1; while (var_a0 >= 0) { if
  (waveHeight >= obj->trans.y_position + 5) break; var_a0--; }`, also missed
  badly: it kept the target `0xf8` frame and `$f20/$f21` saves, but relinked
  focused score worsened to `CURRENT (11495)`, full verify failed with
  calculated CRCs `0xE586A191/0x17A5E745`, and the wave block shifted into a
  broad `a3/v1/a0` register family with downstream scheduling churn. Source
  was restored and final full verify passed. Do not repeat this close-branch
  `while`/break wave-scan spelling. A close save-family continuation using an
  existing-`var_t0` wave-bound carrier (`var_t0 = gRacerWaveCount - 1; for
  (var_a0 = var_t0; ...); if (var_a0 == var_t0)`) also missed: it kept the
  target `0xf8` frame and `$f20/$f21` prologue saves, but worsened the
  relinked focused score to `CURRENT (5115)`, failed full verify with
  calculated CRCs `0x2364AB01/0x1E30A2A8`, and shifted the wave block into a
  broader `t0/v0/t2` register family instead of target `v1/a0/v0`. Source was
  restored and final full verify passed. Do not repeat this close-branch
  existing-`var_t0` wave-bound carrier. A 2026-05-17 save-family in-place
  inverse-gravity split on top of the close chained-zero/x/z/y/steer-noop
  branch (`var_f20 /= 4.0; var_f20 = 1.0 - var_f20`) kept the target `0xf8`
  frame and `$f20/$f21` prologue saves, but worsened the relinked focused
  score to `CURRENT (4075)` and failed full verify with calculated CRCs
  `0x772B05DA/0x0C3D3274`. The diff showed the call-adjacent `$f14`
  save/reload around `apply_vehicle_rotation_offset` and later sound
  scheduling were disturbed, while the wave scan still had the current
  `a0`/`v1` register order opposite the target. Source was restored and final
  full verify passed. Do not repeat this save-family in-place inverse-gravity
  split. A 2026-05-17 save-family double-multiply inverse spelling on that
  same close branch (`var_f20 = 1.0 - (var_f20 * 0.25)`) kept the target `0xf8`
  frame and `$f20/$f21` prologue saves, but produced the same close-branch
  failed full-verify CRCs `0xB8DD79CD/0xE47454ED` and relinked focused
  `CURRENT (3260)` under `--max-size 900`. The wave `a0`/`v1` register drift
  remained, and the target call-adjacent `$f14` reload after
  `apply_vehicle_rotation_offset` was still missing. Source was restored and
  final full verify passed. Do not repeat this save-family double-multiply
  inverse spelling. A 2026-05-17 close save-family existing-`var_t9`
  wave-bound carrier (`var_t9 = gRacerWaveCount - 1; for (var_a0 = var_t9;
  ...); if (var_a0 == var_t9)`) kept the target `0xf8` frame and `$f20/$f21`
  prologue saves, but worsened the relinked focused score to `CURRENT (5430)`
  and failed full verify with calculated CRCs `0xEA44B192/0x165715AD`. The
  wave block shifted into broader `v1/v0/t*` register churn rather than target
  `v1/a0/v0`, with downstream scheduling drift. Source was restored and final
  full verify passed. A close save-family sibling using the existing
  `temp_t7` local as the same wave-bound carrier (`temp_t7 =
  gRacerWaveCount - 1; for (var_a0 = temp_t7; ...); if (var_a0 == temp_t7)`)
  also missed: full verify failed with the same calculated CRCs
  `0xEA44B192/0x165715AD`, the relinked focused diff regressed to
  `CURRENT (6825)`, and the diff kept the target `0xf8` frame plus
  `$f20/$f21` saves but widened wave-register churn instead of solving the
  target `v1/a0/v0` allocation. Source was restored and final full verify
  passed. Do not repeat this close-branch existing-`var_t9` or `temp_t7`
  wave-bound carrier. A 2026-05-17 close save-family predecrement wave-loop
  spelling (`for (var_a0 = gRacerWaveCount; --var_a0 >= 0 && ...;)`) kept the
  target `0xf8` frame and `$f20/$f21` prologue saves, but failed full verify
  with calculated CRCs `0xCE58DA51/0x62A7B089` and worsened the relinked
  focused score to `CURRENT (4660)`. The wave scan shifted into an
  `a0/v0/v1` register/order family with extra post-loop compare math rather
  than target `v1/a0/v0`; downstream scheduling drift remained. Source was
  restored and final full verify passed. Do not repeat this close-branch
  predecrement wave-loop spelling. A
  linked compressed focused diff printed stale `CURRENT (0)` after object-only
  rebuild during the 2026-05-15 packet, and the 2026-05-17 promotion repeated
  the trap: object-only diff printed `CURRENT (0)`, but relink/full gate
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused
  diff reported `CURRENT (2990)` with the same missing target `$f20/$f21`
  prologue saves, shifted saved-register stack slots, early `$f16` zero, and
  wave `a0`/`v1` drift; do not accept this function without relink/full gate
  evidence. A later current-baseline chained grounded-wheel zero spelling
  (`racer->unk88 = (racer->unk84 = 0.0f)`) compiled but stayed in the same
  failed CRC family `0x5FDDE03F/0xEF7A0514`, relinked focused score
  `CURRENT (2430)`, still lacked target `$f20/$f21` prologue saves, and still
  used `$f16` for the early zero instead of target `$f14`; source was restored
  and final full verify passed. Do not repeat this standalone chained-zero
  current-baseline probe. A 2026-05-17 current-baseline reversed chained-zero
  spelling (`racer->unk84 = (racer->unk88 = 0.0f)`) also missed: it failed
  full verify with calculated CRCs `0x5FDDE03F/0x127A8488`, worsened the
  relinked focused score to `CURRENT (3000)`, reversed the early `unk84`/`unk88`
  zero-store order, still used `$f16` for zero, and still lacked target
  `$f20/$f21` prologue saves. Source was restored and final full verify passed;
  do not repeat this reversed chained-zero current-baseline probe. A later
  promotion-only acceptance check after `d988f300` reconfirmed the stale
  object-only diff trap: object-only focused diff printed `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the
  relinked focused diff returned to `CURRENT (2430)` with the same missing
  `$f20/$f21` saves, shifted saved-register slots, early `$f16` zero, and
  wave `a0`/`v1` swap. Source was restored and final full verify passed; do
  not accept or retry promotion-only `func_80049794` from object-only
  `CURRENT (0)` evidence. A close save-family continuation using x/z/y
  pre-`sqrtf` accumulation, steer-vel no-op, chained grounded-wheel zero, and
  removed trailing `pad3`/`pad4`, but rewriting the wave scan as an explicit
  `for` loop with `if (waveHeight >= obj->trans.y_position + 5) break`, also
  missed: it kept the target `0xf8` frame and `$f20/$f21` prologue saves, but
  full verify failed with calculated CRCs `0xC46E9FFB/0x5EC5EF90` and the
  relinked focused score worsened to `CURRENT (8075)`. The diff showed the
  wave scan moving into a broader `v1/a0/v0` drift family instead of fixing
  target `v1` bound plus `a0` loop-index allocation. Source was restored and
  final full verify passed; do not repeat this close-branch explicit
  `for`/`break` wave-scan spelling. A close save-family compare-only
  bound-cache variant (`var_v1 = gRacerWaveCount - 1; for (var_a0 =
  gRacerWaveCount - 1; ...); if (var_a0 == var_v1)`) also missed: it kept the
  target `0xf8` frame and `$f20/$f21` prologue saves, but full verify failed
  with calculated CRCs `0x52412037/0x63D27627` and the relinked focused score
  worsened to `CURRENT (5795)`. The diff moved the loop-index family from
  target `a0` toward `v1/a3` and inserted stack-byte drift for the drift flag,
  so it did not fix the target bound/index allocation. Source was restored and
  final full verify passed; do not repeat this close-branch compare-only
  wave-bound cache. A current-baseline wave pointer-cache probe
  (`lastWaveIndex = gRacerWaveCount - 1; wave =
  &gRacerCurrentWave[var_a0]; if (var_a0 == lastWaveIndex) { var_a0--;
  wave--; }`, then use `wave[1]` for wave-height and `rot.y`) also missed:
  compressed focused diff first printed stale `CURRENT (0)`, but promoted full
  verify failed with calculated CRCs `0x9CF1F322/0x005EC88D`, and uncompressed
  `./diff.sh func_80049794 --no-pager` showed `CURRENT (5700)`. It widened
  the frame to `0x100`, dropped the target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of `$f14`, and moved the wave scan into a
  `v1/a0/v0` drift family rather than target `v0` count, `v1` bound, and `a0`
  loop index. Source was restored; do not repeat this current-baseline wave
  pointer-cache spelling. A baseline
  current-checkout drift-flag boolean assignment probe
  (`spA2 = var_f2 < 35 && racerVelocity < 8.0`) also missed: object-only diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0xAD0C80F7/0xC3551BE0`, and the relinked focused score regressed to
  `CURRENT (5226)`. The probe widened the frame to `0x100`, stored the
  transient boolean through `0xaa(sp)`, still lacked target `$f20/$f21`
  prologue saves, and kept the early zero in `$f16` instead of target `$f14`.
  Source was restored and final full verify passed; do not repeat this
  drift-flag boolean assignment spelling. A baseline current-checkout nested
  wave drift-start branch (`if (racer->drift_direction == 0) { if (var_f2 <
  38 && racerVelocity >= 8.0) ... }`) also missed: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused score was
  `CURRENT (2760)`. It stayed in the missing `$f20/$f21` prologue-save,
  early `$f16` zero, and wave `a0`/`v1` drift family. Source was restored and
  final full verify passed; do not repeat this nested drift-start branch
  spelling. A baseline current-checkout comma-gate drift-flag initialization
  (`if ((spA2 = FALSE, gCurrentPlayerIndex != PLAYER_COMPUTER) && ...)`) also
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and
  the relinked focused score was `CURRENT (2760)`. The diff still lacked
  target `$f20/$f21` prologue saves, kept the early zero in `$f16` instead of
  target `$f14`, and left the wave bound/index allocation as current
  `a0`/`v1` opposite target `v1`/`a0`. Source was restored and final full
  verify passed; do not repeat this comma-gate `spA2` initialization spelling.
  A baseline current-checkout nested early wave-gate spelling
  (`if (gCurrentPlayerIndex != PLAYER_COMPUTER) { if (racer->vehicleIDPrev !=
  VEHICLE_WIZPIG) { if (gRacerWaveCount != 0) ... } }`) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked
  focused score was `CURRENT (2760)`. It produced no useful movement from the
  promoted baseline: target `$f20/$f21` prologue saves were still absent, the
  early zero still used `$f16` instead of `$f14`, and the wave bound/index
  allocation still had `a0`/`v1` opposite the target. Source was restored and
  final full verify passed; do not repeat this baseline nested early
  wave-gate spelling. A baseline current-checkout nested wave-reset condition
  spelling (`if (trickType == 1) { reset } else if (trickType == -1) { reset
  } else if (wave->rot.y < 0.4) { reset }`) also missed badly: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0xFF986DDD/0x8281F72F`, and the relinked focused score
  worsened to `CURRENT (6055)`. The diff duplicated reset-branch control flow,
  inserted `spA2` stack-byte traffic, still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16`, and moved the wave block into broader
  register churn rather than target `v1/a0/v0`. Source was restored and final
  full verify passed; do not repeat this baseline nested wave-reset condition.
  A 2026-05-23 baseline current-checkout early-zero carrier through the
  existing `spE8` local (`spE8 = 0.0f; racer->unk84 = spE8; racer->unk88 =
  spE8`) also produced no object movement: full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, the relinked focused diff
  stayed `CURRENT (2760)`, target `$f20/$f21` prologue saves were still
  absent, and the early zero still allocated in `$f16` instead of target
  `$f14`. Source was restored and final full verify passed; do not repeat this
  baseline `spE8` early-zero carrier. A sibling baseline current-checkout
  early-zero carrier through existing `spE4` (`spE4 = 0.0f; racer->unk84 =
  spE4; racer->unk88 = spE4`) also missed in the same no-movement family: full
  verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, target `$f20/$f21`
  prologue saves were still absent, and the early zero still allocated in
  `$f16` instead of target `$f14`. Source was restored and final full verify
  passed; do not repeat this baseline `spE4` early-zero carrier.
  A sibling baseline current-checkout early-zero carrier through existing
  `spE0` (`spE0 = 0.0f; racer->unk84 = spE0; racer->unk88 = spE0`) also
  produced no object movement: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`, target `$f20/$f21` prologue saves were still absent, and
  the early zero still allocated in `$f16` instead of target `$f14`. Source
  was restored and final full verify passed; do not repeat this baseline
  `spE0` early-zero carrier.
  A sibling baseline current-checkout early-zero carrier through existing
  `spD8` (`spD8 = 0.0f; racer->unk84 = spD8; racer->unk88 = spD8`) also
  produced no object movement: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`, target `$f20/$f21` prologue saves were still absent, and
  the early zero still allocated in `$f16` instead of target `$f14`. Source
  was restored and final full verify passed; do not repeat this baseline
  `spD8` early-zero carrier.
  A sibling baseline current-checkout early-zero carrier through existing
  `spD4` (`spD4 = 0.0f; racer->unk84 = spD4; racer->unk88 = spD4`) also
  produced no object movement: full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`, target `$f20/$f21` prologue saves were still absent, and
  the early zero still allocated in `$f16` instead of target `$f14`. Source
  was restored and final full verify passed; do not repeat this baseline
  `spD4` early-zero carrier. A sibling baseline current-checkout early-zero
  carrier through existing `spD0` (`spD0 = 0.0f; racer->unk84 = spD0;
  racer->unk88 = spD0`) also collapsed into the same no-movement family: full
  verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked focused
  diff stayed `CURRENT (2760)`, target `$f20/$f21` prologue saves were still
  absent, and the early zero still allocated in `$f16` instead of target
  `$f14`. Source was restored and final full verify passed; do not repeat this
  baseline `spD0` early-zero carrier.
  A close save-family continuation
  using x/z/y pre-`sqrtf` accumulation, steer-vel no-op, chained
  grounded-wheel zero, and removed trailing `pad3`/`pad4`, but commuting the
  early wave-gate player check to `PLAYER_COMPUTER != gCurrentPlayerIndex`,
  also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0xB95979CD/0xA04AD574`, and the
  relinked focused score was `CURRENT (3270)`. The diff kept the target
  `0xf8` frame and `$f20/$f21` saves plus target `$f14` early zero, but the
  player branch became current `beq t3,t1` opposite target `beq t1,t3`, and
  the wave bound/index allocation still had `a0`/`v1` opposite the target.
  Source was restored and final full verify passed; do not repeat this
  close-branch commuted wave-gate player-check spelling. A close save-family
  continuation using the same x/z/y pre-`sqrtf` accumulation, steer-vel no-op,
  chained grounded-wheel zero, and removed trailing `pad3`/`pad4`, but adding a
  `register s32 var_a0` hint, also missed as a no-op against that close
  branch: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0xB8DD79CD/0xE47454ED`, and the relinked
  focused score stayed `CURRENT (3260)` under `--max-size 900`. The target
  `0xf8` frame, `$f20/$f21` saves, and target `$f14` early zero remained, but
  the wave bound/index allocation still had `a0`/`v1` opposite the target.
  Source was restored and final full verify passed; do not repeat this
  close-branch `register var_a0` hint. Close save-family siblings with
  `register s32 var_v0` and `register s32 var_v1` also missed: full verify
  failed with calculated CRCs `0xB8DD79CD/0xE47454ED`, the relinked focused
  score worsened to `CURRENT (4365)`, and the diff kept the target `0xf8`
  frame plus `$f20/$f21` saves but moved the bound/index family further from
  target: the current code used `a0` as the wave bound and `v1` as the loop
  index, still opposite target `v1` bound and `a0` loop index. Source was
  restored and final full verify passed; do not repeat these close-branch
  `register var_v0` or `register var_v1` hints. A close save-family
  `register s32 var_t0` allocation hint on the same x/z/y/chained-zero/
  steer-noop branch also missed: full verify failed with the same close-family
  calculated CRCs `0xB8DD79CD/0xE47454ED`, and the relinked focused diff
  worsened to `CURRENT (4365)`. It preserved the target `0xf8` frame,
  `$f20/$f21` saves, and target `$f14` early zero, but the wave bound/index
  allocation remained reversed with current `a0` as bound and `v1` as loop
  index, and later scheduling drift increased. Source was restored and final
  full verify passed; do not repeat this close-branch `register var_t0` hint.
  A sibling close save-family `register s32 var_t9` allocation hint produced
  the same bad family: full verify failed with calculated CRCs
  `0xB8DD79CD/0xE47454ED`, and the relinked focused diff reported
  `CURRENT (4365)`. It preserved the target `0xf8` frame, `$f20/$f21` saves,
  and target `$f14` early zero, but kept the wave bound/index allocation
  reversed with current `a0` as bound and `v1` as loop index. Source was
  restored and final full verify passed; do not repeat this close-branch
  `register var_t9` hint.
  A close save-family nested spinout-zap condition split also missed: on top of
  the x/z/y pre-`sqrtf` accumulation, steer-vel no-op, chained grounded-wheel
  zero, and removed trailing `pad3`/`pad4`, splitting
  `racer->unk1FE == 4 && racer->spinout_timer == 0` into nested `if`
  statements preserved the close-family failed full-verify CRCs
  `0xB8DD79CD/0xE47454ED` and regressed the relinked focused diff to
  `CURRENT (4365)`. It kept the target `0xf8` frame and `$f20/$f21` saves, but
  the wave bound/index allocation remained reversed (`a0` bound / `v1` loop)
  and later scheduling drift increased. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this close-branch nested
  spinout-zap condition split.
  A close save-family nested course-height guard probe also missed: on top of
  the x/z/y pre-`sqrtf` accumulation, steer-vel no-op, chained grounded-wheel
  zero, and removed trailing `pad3`/`pad4`, keeping the trick-type range guard
  first and nesting only `if (var_f2 < 0)` preserved the close-family failed
  full-verify CRCs `0xB8DD79CD/0xE47454ED` and relinked focused diff reported
  `CURRENT (4365)`. It kept the target `0xf8` frame and `$f20/$f21` saves, but
  the wave bound/index allocation remained reversed (`a0` bound / `v1` loop)
  and later scheduling drift remained. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this close-branch nested
  course-height guard spelling.
  A worker close save-family explicit wave-bound local-count probe also missed:
  assigning `var_v1 = gRacerWaveCount - 1`, iterating `var_a0` from `var_v1`,
  and comparing `if (var_a0 == var_v1)` worsened the focused diff to
  `CURRENT (5755)` after full verify failed with calculated CRCs
  `0x5790053C/0x1C8C0179`. Instead of the target `v1` bound / `a0` loop-index
  family, the scan broadened into `a3`/`v0`/`v1` allocation with pointer
  recomputation. Source was restored, worker and main validation both reached
  `Verify: OK`, and `./score.sh -s` remained 97.30%; do not repeat this
  explicit surviving count-bound local shape.
  A close save-family decrementing `WaterProperties **wave` pointer-carrier
  probe also missed: adding the pointer local on top of the x/z/y pre-`sqrtf`,
  steer-noop, chained-zero, and no-trailing-pad branch widened the frame to
  `0x100`, full verify failed with calculated CRCs
  `0x9ED4C306/0xE6587C63`, and relinked focused diff worsened to
  `CURRENT (8081)`. The target `v1` bound / `a0` loop-index roles were still
  reversed, and the pointer update scheduled as `lw -4(v0)` followed by
  `addiu v0,-4` instead of target predecrement. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%; do not repeat this close-branch explicit
  decrementing pointer-carrier shape.
  A close save-family
  wave-reset condition probe that cached `racer->trickType` into the existing
  `racerTrickType` local before testing `racerTrickType == 1 ||
  racerTrickType == -1 || wave->rot.y < 0.4` also missed: full verify failed
  with calculated CRCs `0xB14B79CD/0x12BCEA0A`, relinked focused score worsened
  to `CURRENT (4375)`, and the diff flipped the `trickType == -1` compare from
  target `beq t1,v0` to current `beq v0,t1` while leaving the wave bound/index
  allocation reversed. Source was restored and final full verify passed; do
  not repeat this close-branch `racerTrickType` wave-reset cache.
  A close save-family selected-wave index carrier (`var_t9 = var_a0 + 1`, then
  using `gRacerCurrentWave[var_t9]` for both post-scan `waveHeight` and `rot.y`
  accesses on top of the x/z/y pre-`sqrtf`, chained-zero, no-trailing-pad
  branch) also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x1457E419/0x21494B92`, and the relinked focused score regressed to
  `CURRENT (6025)`. It kept the target `0xf8` frame and `$f20/$f21` prologue
  saves, but broadened the wave block into `a0`/`v1`/`t*` register churn, left
  early zero in `$f16` instead of target `$f14`, and disturbed later
  call-adjacent scheduling. Source was restored and final full verify passed;
  do not repeat this close-branch selected-wave index carrier.
  A baseline current-checkout spinout-zap
  condition split (`if (racer->unk1FE == 4) { if (racer->spinout_timer == 0)
  ... }`) matched the local target branch shape in the object-only focused
  view, but did not move the relinked object: full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, the relinked focused score
  stayed `CURRENT (2430)`, and the same missing `$f20/$f21` saves, shifted
  saved-register slots, early `$f16` zero, and wave `a0`/`v1` drift remained.
  Source was restored and final full verify passed; do not repeat this
  baseline nested spinout-zap condition spelling. Commuting only the same
  spinout-zap condition order (`if (racer->spinout_timer == 0 &&
  racer->unk1FE == 4)`) also missed: full verify failed with calculated CRCs
  `0x5FDDE03F/0x274DE960`, the relinked focused score worsened to
  `CURRENT (3830)`, and the early branch order changed without restoring the
  target `$f20/$f21` saves or `$f14` zero family. Source was restored and
  final full verify passed; do not repeat this commuted spinout-zap condition
  order. A baseline current-checkout spinout clear condition-order probe
  (`racer->groundedWheels >= 3 && racer->velocity > -2.0` instead of the
  current velocity-first guard) also missed as a no-movement family: full
  verify failed with calculated CRCs `0x5E20AA2C/0x0360F9F3`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this spinout clear condition-order spelling. A
  baseline current-checkout wave-gate condition reorder
  (`racer->vehicleIDPrev != VEHICLE_WIZPIG && gCurrentPlayerIndex !=
  PLAYER_COMPUTER && gRacerWaveCount != 0`) also missed: full verify failed
  with calculated CRCs `0x5EC30E74/0x34AE258F`, relinked focused diff
  regressed to `CURRENT (4880)`, the branch order moved the vehicle check
  before the current-player check instead of target player-first order,
  `$f20/$f21` prologue saves were still absent, early zero stayed in `$f16`,
  and the wave bound/index allocation remained current `a0`/`v1` instead of
  target `v1`/`a0`. Source was restored and final full verify passed; do not
  repeat this baseline wave-gate condition reorder. A current-baseline
  adjacent declaration-order swap of `var_a0` and `var_v1` also missed as a
  no-op: full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`,
  the relinked focused diff stayed `CURRENT (2760)`, `$f20/$f21` prologue
  saves were still absent, early zero stayed in `$f16`, and the wave
  bound/index allocation remained current `a0`/`v1` instead of target
  `v1`/`a0`. Source was restored and final full verify passed; do not repeat
  this current-baseline `var_a0`/`var_v1` declaration-order swap. A
  current-baseline roll-trick `x_rotation_vel` comma no-op removal probe
  (`racer->x_rotation_vel = var_v1 + ((racer->trickType * 0x600) *
  updateRate)`) also missed as a no-movement family: full verify failed with
  calculated CRCs `0x60E1E03F/0x46C688CD`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this roll-trick comma no-op removal spelling. A
  current-baseline drift reset integer spelling (`racer->drift_direction = 0`
  instead of `0.0f`) also missed as a no-op: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, the relinked focused diff stayed
  `CURRENT (2760)`, `$f20/$f21` prologue saves were still absent, early zero
  stayed in `$f16`, and the wave bound/index allocation remained current
  `a0`/`v1` instead of target `v1`/`a0`. Source was restored and final full
  verify passed; do not repeat this current-baseline `drift_direction = 0`
  spelling. A current-baseline drift flag type probe (`s32 spA2` instead of
  `s8 spA2`) also missed: full verify failed with calculated CRCs
  `0x37DDDF63/0x9ECDB374`, the relinked focused diff worsened to
  `CURRENT (3417)`, the frame widened to `0x100`, stack slots shifted,
  `$f20/$f21` prologue saves were still absent, early zero stayed in `$f16`,
  and the wave bound/index allocation remained current `a0`/`v1` instead of
  target `v1`/`a0`. Source was restored and final full verify passed; do not
  repeat this current-baseline `s32 spA2` drift-flag type probe. A baseline
  current-checkout nested `spA2` wave-drift boolean spelling
  (`if (var_f2 < 35) { if (racerVelocity < 8.0) spA2 = TRUE; }`) also missed
  as a no-movement promoted-baseline family: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and relinked focused diff stayed `CURRENT (2760)`.
  `$f20/$f21` prologue saves were still absent, early zero stayed in `$f16`,
  and the wave bound/index allocation remained current `a0`/`v1` instead of
  target `v1`/`a0`. Source was restored and final full verify passed; do not
  repeat this nested `spA2` wave-drift boolean spelling. A baseline
  current-checkout explicit wave-height subtract constant spelling
  (`var_f2 = (obj->trans.y_position - var_f2) - 10.0f`) also missed as a
  no-movement promoted-baseline family: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and relinked focused diff stayed `CURRENT (2760)`.
  `$f20/$f21` prologue saves were still absent, early zero stayed in `$f16`,
  and the wave bound/index allocation remained current `a0`/`v1` instead of
  target `v1`/`a0`. Source was restored and final full verify passed; do not
  repeat this explicit wave-height subtract `10.0f` spelling. A baseline
  current-checkout wave-drift single-precision normalization constants spelling
  (`racerVelocity -= 8.0f; if (racerVelocity > 4.0f) racerVelocity = 4.0f;
  racerVelocity /= 4.0f`) also missed: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5B9A8D6D/0x2117429E`, and relinked focused diff regressed to
  `CURRENT (6330)`. The early zero allocation moved into target `$f14`, but
  `$f20/$f21` prologue saves were still absent, the wave bound/index allocation
  remained current `a0`/`v1` instead of target `v1`/`a0`, and the drift/
  inverse-gravity float-register schedule broadened. Source was restored and
  final full verify passed; do not repeat this wave-drift single-precision
  normalization-constant spelling. A baseline current-checkout wave-drift
  subtract-only suffix spelling (`racerVelocity -= 8.0f` with the clamp/divide
  spelling unchanged) also missed: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x6006EA9D/0x93E5B79C`, and the relinked focused diff regressed to
  `CURRENT (4900)`. `$f20/$f21` prologue saves were still absent, the wave
  bound/index allocation remained current `a0`/`v1` instead of target
  `v1`/`a0`, and later `$f14`/`$f20` gravity scheduling drift broadened.
  Source was restored and final full verify passed; do not repeat this
  current-baseline wave-drift subtract-only suffix spelling. A baseline
  current-checkout wave-drift clamp-assignment suffix spelling
  (`racerVelocity = 4.0f` with the subtract/compare/divide spelling unchanged)
  also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0xA72E8795/0xE7316761`, and the
  relinked focused diff regressed to `CURRENT (3355)`. `$f20/$f21` prologue
  saves were still absent, early zero stayed in current `$f16` instead of
  target `$f14`, the wave bound/index allocation remained current `a0`/`v1`
  instead of target `v1`/`a0`, and later `$f14`/`$f20` gravity scheduling
  drift broadened. Source was restored and final full verify passed; do not
  repeat this current-baseline wave-drift clamp-assignment suffix spelling. A
  2026-05-23 close save-family plus wave-drift subtract-suffix probe
  (promoted close chained-zero/x/z/y/
  no-trailing-pad shape with `racerVelocity -= 8.0f` only) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0xA8F39A57/0xC08781AF`, and the relinked focused
  diff regressed to `CURRENT (7769)`. It preserved the target `0xf8` frame,
  `$f20/$f21` prologue saves, and early `$f14` zero family, but widened the
  wave block into current `a0`-bound/`v1`-loop allocation instead of target
  `v1`-bound/`a0`-loop and disturbed later float-register scheduling. Source
  was restored and final full verify passed; do not repeat this close
  save-family plus wave-drift subtract-suffix combination. A baseline
  current-checkout first-speed carrier family through existing float locals also
  missed: using `spEC` for the pre-`sqrtf` sum failed full verify with
  calculated CRCs `0x18B44436/0x9C5E8797` and worsened the relinked focused
  diff to `CURRENT (3320)`, while using `spCC` failed full verify with
  calculated CRCs `0x5FF63A3F/0x2631AADC` and relinked focused `CURRENT
  (3210)`. A sibling current-checkout `var_f6` carrier
  (`var_f6 = x*x; var_f6 += z*z; var_f6 += y*y; var_f20 = sqrtf(var_f6) -
  2.0`) collapsed into the same `spCC` miss family: full verify failed with
  calculated CRCs `0x5FF63A3F/0x2631AADC`, and relinked focused diff reported
  `CURRENT (3210)`. All kept `$f20/$f21` prologue saves absent, kept early zero
  in `$f16` instead of target `$f14`, and left the wave bound/index allocation
  as current `a0`/`v1` instead of target `v1`/`a0`. Source was restored and
  final full verify passed; do not repeat these current-baseline `spEC`/`spCC`/
  `var_f6` first-speed carrier probes. A baseline
  current-checkout wave speed spelling as an explicit zero subtract
  (`racerVelocity = 0.0f - racer->velocity`) also missed: full verify failed
  with calculated CRCs `0x6035C737/0x97D59D33`, and relinked focused diff
  worsened to `CURRENT (4160)`. It moved the early zero allocation into
  `$f14`, but still lacked target `$f20/$f21` prologue saves, kept the wave
  bound/index allocation as current `a0`/`v1` instead of target `v1`/`a0`, and
  broadened float-register drift through the wave/gravity path. Source was
  restored and final full verify passed; do not repeat this current-baseline
  explicit-subtract wave speed spelling. A baseline current-checkout
  post-scan wave-index increment spelling (`var_a0++` after the wave scan,
  then `gRacerCurrentWave[var_a0]` instead of repeated
  `gRacerCurrentWave[var_a0 + 1]`) also missed: full verify failed with
  calculated CRCs `0x6763F03F/0xAFC9BBAD`, and relinked focused diff was
  `CURRENT (3315)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, shifted the wave scan into an
  `a1`/`v1`/`a0`-style register family rather than target `v1`/`a0`
  bound/index allocation, and inserted post-scan pointer/index adjustment
  drift. Source was restored and final full verify passed; do not repeat this
  current-baseline post-scan wave-index increment spelling. A baseline
  current-checkout wave-count carrier
  (`var_v0 = gRacerWaveCount; var_v1 = var_v0 - 1; for (var_a0 = var_v1;
  ...); if (var_a0 == var_v1)`) also missed: full verify failed with
  calculated CRCs `0xC88B59B4/0xF77ED7E9`, and relinked focused diff worsened
  to `CURRENT (6185)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, inserted `spA2` stack-byte
  traffic, and shifted the wave scan into current `v1` count, `a0` bound,
  `v0` loop-index order instead of target `v0` count, `v1` bound, `a0`
  loop-index order. Source was restored and final full verify passed; do not
  repeat this current-baseline `var_v0` wave-count carrier. A baseline
  current-checkout selected-wave index carrier (`var_t9 = var_a0 + 1`, then
  using `gRacerCurrentWave[var_t9]` for both post-scan accesses) also missed:
  full verify failed with calculated CRCs `0x3B15743F/0x1E2ED6C8`, and
  relinked focused diff worsened to `CURRENT (4365)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, kept the wave loop reversed as current `a0` bound plus `v1`
  loop-index rather than target `v1` bound plus `a0` loop-index, and
  recomputed the selected-wave offset for the `rot.y` check instead of
  reusing the target post-scan offset. Source was restored and final full
  verify passed; do not repeat this current-baseline selected-wave index
  carrier. A baseline current-checkout attach-point store-order spelling
  (moving the first third-attach-object `modelIndex += 1` before
  `trans.rotation.y_rotation = 0x4000`) also missed as a no-movement
  promoted-baseline family: full verify failed with calculated CRCs
  `0x5CF5E03F/0x566478E3`, and relinked `./diff.sh func_80049794` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this attach-point model-index/rotation
  store-order spelling. A baseline current-checkout zap sound null-argument
  spelling (`sound_play(SOUND_ZAP4, 0)` instead of `NULL`) also missed as a
  no-movement promoted-baseline family: full verify failed with calculated
  CRCs `0x5FDDE03F/0xEF7A0514`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this `SOUND_ZAP4` `0` null-argument spelling.
  A baseline current-checkout final `unk201`
  particle-reset condition inversion (empty `if (racer->unk201 != 0)` with the
  reset in `else`) also missed as a no-movement promoted-baseline family: full
  verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and focused object
  disassembly still emitted the target local tail branch at
  `func_80049794+0x289c`. It did not recover target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored and
  final full verify passed; do not repeat this final `unk201`
  condition-inversion spelling. A baseline current-checkout attach-point
  count-threshold spelling (`obj->attachPoints->count > 2` for both late
  attach blocks) also missed as a no-movement promoted-baseline family: full
  verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly still emitted `slti at,count,3` before the same attach branches.
  It did not recover target `$f20/$f21` prologue saves, kept early zero in
  `$f16` instead of target `$f14`, and left the wave scan in the current
  `a0`-bound/`v1`-loop family. Source was restored and final full verify
  passed; do not repeat this attach-point `count > 2` threshold spelling. A
  baseline current-checkout attach-point lowering compound assignment
  (`temp_v0_obj->trans.y_position -= 2.0` for both lowered objects) also
  missed as a no-movement promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly still emitted the same local double-subtract/cvt.s sequence for
  both lowering paths. It did not recover target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave scan
  in the current `a0`-bound/`v1`-loop family. Source was restored and final
  full verify passed; do not repeat this attach-point `-= 2.0` lowering
  spelling. A baseline current-checkout attach-point raising compound
  assignment (`temp_v0_obj->trans.y_position += 1.0f` for both raised objects)
  also missed as a no-movement promoted-baseline family: full verify failed
  with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly still emitted the same local `add.s`/store sequence for both
  raising paths. It did not recover target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored and final full
  verify passed; do not repeat this attach-point `+= 1.0f` raising spelling.
  A baseline current-checkout late boost-emitter pointer-index spelling
  (`boostObj += racer->racerIndex` instead of
  `boostObj = &boostObj[racer->racerIndex]`) also missed: full verify failed
  with calculated CRCs `0x5A11E03F/0x019B7EA6`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and promoted object
  disassembly changed the local pointer add to `addu v1,v0,t9` instead of the
  target/current `addu v1,t9,v0`. It did not recover target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, and left
  the wave scan in the current `a0`-bound/`v1`-loop family. Source was
  restored and final full verify passed; do not repeat this late boost-emitter
  pointer `+= racerIndex` spelling. A worker-tested late boost-emitter
  high-boost condition-order probe (`boostObj->unk74 > 0.0 ||
  boostObj->unk70 > 0`) produced no relinked movement: probe verify failed with
  calculated CRCs `0x5FE1E03F/0xA0AF4D76`, and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. The same missing `$f20/$f21` prologue saves, early
  `$f16` zero, and current `a0`-bound/`v1` wave scan remained. Worker source
  was restored and verified; do not repeat this high-boost condition operand
  order. A baseline current-checkout movement-block
  approach-target pointer-test spelling (`if (!racer->approachTarget)` instead
  of `== NULL`) also missed as a no-movement promoted-baseline family: full
  verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, relinked
  `./diff.sh func_80049794` stayed `CURRENT (2760)`, and the same missing
  `$f20/$f21` prologue saves, early `$f16` zero, and current `a0`-bound/`v1`
  wave-scan family remained. Source was restored and final full verify passed;
  do not repeat this movement-block approach-target pointer-test spelling. A
  baseline current-checkout grouped z/y first-speed
  expression
  (`sqrtf(x*x + (z*z + y*y)) - 2.0`) also missed: full verify failed with
  calculated CRCs `0x6025B63F/0xF5C950EA`, and relinked focused diff reported
  `CURRENT (2980)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave loop
  reversed as current `a0` bound plus `v1` loop-index rather than target `v1`
  bound plus `a0` loop-index. Source was restored and final full verify
  passed; do not repeat this current-baseline grouped z/y first-speed
  expression. A baseline current-checkout grouped x/y first-speed expression
  (`sqrtf(((x*x) + (y*y)) + (z*z)) - 2.0`) also missed: full verify failed
  with calculated CRCs `0x5FDDE03F/0xA73DFC7C`, and the relinked focused diff
  reported `CURRENT (2770)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  loop reversed as current `a0` bound plus `v1` loop-index rather than target
  `v1` bound plus `a0` loop-index. Source was restored and final full verify
  passed; do not repeat this current-baseline grouped x/y first-speed
  expression. A baseline current-checkout `OBJ_EMIT_9` store-before-`5.5`
  gravity assignment spelling (moving `obj->particleEmittersEnabled |=
  OBJ_EMIT_9` before `var_f20 = 5.5`) also missed: full verify failed with
  calculated CRCs `0x5FDDE03F/0x2087AB13`, and the relinked focused diff
  regressed to `CURRENT (2820)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave loop
  reversed as current `a0` bound plus `v1` loop-index rather than target `v1`
  bound plus `a0` loop-index, and inserted an extra/reordered `unk1FE` reload
  around the `5.5` assignment rather than matching the target local schedule.
  Source was restored and final full verify passed; do not repeat this
  current-baseline `OBJ_EMIT_9` store-before-`5.5` spelling. A baseline
  current-checkout `5.5f` gravity literal spelling (`var_f20 = 5.5f` in the
  `unk1FE == 0` block) also missed as a no-movement promoted-baseline family:
  full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the
  relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave loop reversed as current `a0` bound plus `v1`
  loop-index rather than target `v1` bound plus `a0` loop-index. Source was
  restored and final full verify passed; do not repeat this current-baseline
  `5.5f` gravity literal spelling. A baseline current-checkout `unk1FE == 1`
  gravity `else if` spelling (changing the second post-rotation
  `if (racer->unk1FE == 1)` into `else if`) also missed: full verify failed
  with calculated CRCs `0x5FDDE812/0x3B1FD959`, and the relinked focused diff
  regressed to `CURRENT (3215)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  loop reversed as current `a0` bound plus `v1` loop-index rather than target
  `v1` bound plus `a0` loop-index, removed the target-like `unk1FE` reload
  after the `5.5` gravity/`OBJ_EMIT_9` path, and shifted later gravity work
  through `$f14` instead of target `$f20`. Source was restored and final full
  verify passed; do not repeat this current-baseline gravity `else if`
  spelling. A baseline current-checkout buoyancy single-precision nonzero
  guard spelling (`if (racer->buoyancy != 0.0f)` after the post-rotation
  `unk1FE` gravity assignments) also missed: full verify failed with
  calculated CRCs `0xA7264CF3/0x20C04378`, and the relinked focused diff
  regressed to `CURRENT (3790)`. It changed the target buoyancy zero test from
  the double-compare sequence (`cvt.d.s`/`c.eq.d`) into `c.eq.s`, still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, left the wave loop reversed as current `a0` bound plus `v1`
  loop-index rather than target `v1` bound plus `a0` loop-index, and kept the
  later buoyancy/gravity path on `$f14` instead of target `$f20`. Source was
  restored and final full verify passed; do not repeat this current-baseline
  buoyancy single-precision nonzero guard spelling. A baseline
  current-checkout first-speed single-precision
  subtract spelling (`sqrtf(...) - 2.0f` for the first speed magnitude only)
  also missed: full verify failed with calculated CRCs
  `0x12F152B3/0x7EB3E947`, and relinked focused diff worsened to `CURRENT
  (4560)`. It still lacked target `$f20/$f21` prologue saves, kept early zero
  in `$f16` instead of target `$f14`, and left the wave loop reversed as
  current `a0` bound plus `v1` loop-index rather than target `v1` bound plus
  `a0` loop-index. Source was restored and final full verify passed; do not
  repeat this first-speed `2.0f` subtract spelling. A baseline
  current-checkout wave-speed lower-clamp operand-order spelling
  (`if (0.0f > racerVelocity)`) also missed in the promoted-baseline family:
  full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the
  relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave loop reversed as current `a0` bound plus `v1`
  loop-index rather than target `v1` bound plus `a0` loop-index. Source was
  restored and final full verify passed; do not repeat this wave-speed
  lower-clamp operand-order spelling. A baseline current-checkout boss branch
  polarity spelling (`if (racer->vehicleID < VEHICLE_BOSSES) { } else { ... }`)
  also missed in the promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave loop
  reversed as current `a0` bound plus `v1` loop-index rather than target `v1`
  bound plus `a0` loop-index. Source was restored and final full verify
  passed; do not repeat this boss-branch polarity spelling. A baseline
  current-checkout upper-clamp operand-order spelling (`if (4.0 < var_f20)`)
  also missed in the promoted-baseline family: full verify failed with
  calculated CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave loop
  reversed as current `a0` bound plus `v1` loop-index rather than target `v1`
  bound plus `a0` loop-index. Source was restored and final full verify
  passed; do not repeat this first-speed upper-clamp operand-order spelling. A
  baseline current-checkout grouped course-height subtraction
  (`var_f2 = gCurrentCourseHeight - (50.0 + obj->trans.y_position)`) also
  missed: full verify failed with calculated CRCs `0x601C493F/0x8CFF7E1F`,
  and the relinked focused diff worsened to `CURRENT (3905)`. It still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, and left the wave loop reversed as current `a0` bound plus
  `v1` loop-index rather than target `v1` bound plus `a0` loop-index. Source
  was restored and final full verify passed; do not repeat this grouped
  course-height subtraction spelling. A baseline current-checkout
  course-height range-guard reorder (`if (var_f2 < 0 && racer->trickType < 2 &&
  racer->trickType >= -1)`) also missed: full verify failed with calculated
  CRCs `0x5FDDD6C1/0xA30A4934`, and the relinked focused diff worsened to
  `CURRENT (3770)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave loop
  reversed as current `a0` bound plus `v1` loop-index rather than target `v1`
  bound plus `a0` loop-index. Source was restored and final full verify passed;
  do not repeat this course-height range-guard order. A baseline
  current-checkout course-height trick-type guard reorder
  (`racer->trickType >= -1 && racer->trickType < 2 && var_f2 < 0`) also
  missed: full verify failed with calculated CRCs `0x5FDDE03F/0xEE2BD2FC`,
  and relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (3170)`. It changed the local branch family but still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this course-height trick-type guard order. A
  baseline
  current-checkout selected-wave pointer cache (`WaterProperties *wave =
  gRacerCurrentWave[var_a0 + 1]`, reused for both `waveHeight` and `rot.y`)
  also missed: full verify failed with calculated CRCs
  `0x6DFA65AE/0x7EEB0391`, and the relinked focused diff worsened to
  `CURRENT (5395)`. It widened the frame to `0x100`, still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this selected-wave
  pointer cache. A baseline current-checkout direct selected-wave height
  subtraction spelling (`var_f2 = (obj->trans.y_position -
  gRacerCurrentWave[var_a0 + 1]->waveHeight) - 10`) also missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x602A473F/0x3E5DF743`, and the relinked focused diff
  regressed to `CURRENT (4055)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop, and shifted the selected-wave height
  subtraction into `$f18`/`$f4`/`$f6`/`$f8` scheduling rather than target
  `$f2`/`$f18`/`$f4`/`$f6`. Source was restored and final full verify passed;
  do not repeat this direct selected-wave height subtraction spelling. A
  baseline current-checkout terminal wave-bound inverted empty-if spelling
  (`if (var_a0 != gRacerWaveCount - 1) { } else { var_a0--; }`) also missed as
  a no-movement promoted-baseline family: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this terminal wave-bound inverted empty-if spelling. A
  baseline current-checkout grounded stick-scale operand-order spelling
  (`gCurrentStickY = ((f32) gCurrentStickY) * (1.0 - var_f20)`) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x6036E63F/0x817F988F`, and the relinked
  focused diff regressed to `CURRENT (2795)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop, and shifted
  later gravity work through `$f14` instead of the target `$f20` family.
  Source was restored and final full verify passed; do not repeat this
  grounded stick-scale operand-order spelling. A
  baseline current-checkout boost non-positive-first branch-order spelling
  (`if (racer->boostTimer <= 0) { racer->boostTimer = 0; } else if
  (gRaceStartTimer == 0) { ... }`) also missed as a no-movement
  promoted-baseline family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x27DDE041/0xF6868CFC`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this boost non-positive-first branch-order spelling. A
  baseline current-checkout implicit wave-count gate spelling
  (`... && gRacerWaveCount` instead of `... && gRacerWaveCount != 0`) also
  missed as a no-movement promoted-baseline family: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this implicit wave-count gate spelling. A
  baseline current-checkout wave-height upper-reset constant-left compare
  spelling (`if (100.0f < var_f2)`) also missed as a no-movement family:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this wave-height upper-reset constant-left compare spelling. A
  baseline current-checkout `register f32 var_f2` allocation hint also missed
  as a no-improvement family: full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused
  diff stayed `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this current-baseline `register var_f2` hint. A
  baseline current-checkout wave-reset constant-left condition
  (`if (1 == racer->trickType || -1 == racer->trickType || ... )`) also
  missed as a no-movement family: full verify failed with the promoted-baseline
  CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this constant-left wave-reset condition spelling. A baseline
  current-checkout existing-`var_f0` first-speed accumulator spelling
  (`var_f0 = x^2 + z^2; var_f0 += y^2; sqrtf(var_f0) - 2.0`) also missed:
  full verify failed with calculated CRCs `0xF436DADF/0x9C800F7B`, and the
  relinked focused diff worsened to `CURRENT (3550)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this existing-`var_f0`
  first-speed accumulator spelling. A baseline current-checkout nested
  course-height guard spelling that kept the trick-type range first but nested
  `if (var_f2 < 0)` inside it also missed as a no-movement family: full verify
  failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the
  relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this nested
  course-height guard spelling. A baseline current-checkout course-height
  buoyancy subtract spelling (`var_f20 -= var_f2 / 25.0` instead of
  `var_f20 += -var_f2 / 25.0`) also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FE112BA/0x09397095`, and the relinked focused diff regressed to
  `CURRENT (3305)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and shifted the later buoyancy/gravity block into
  `$f14`/`$f18`/`$f10` scheduling rather than the target `$f20` family. Source
  was restored and final full verify passed; do not repeat this
  course-height buoyancy subtract spelling. A baseline current-checkout
  course-height upper-cap compare-order spelling (`if (2.5 < var_f20)`) also
  missed as a no-movement family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with the promoted-baseline calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this course-height upper-cap compare-order spelling. A baseline
  current-checkout explicit first-compare plus decrementing `do`-loop wave
  scan (`var_v1 = gRacerWaveCount - 1; var_a0 = var_v1; if (...) do {
  var_a0--; } while (...)`) also missed by reproducing the known split-bound
  CRC family: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x5790053C/0x1C8C0179`, and the relinked
  focused diff regressed to `CURRENT (5755)`. It allocated the saved bound in
  `a3` and the walking index in `v0` rather than target `v1`/`a0`, inserted
  `spA2` stack-byte traffic, still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and broadened wave-block
  register churn. Source was restored and final full verify passed; do not
  repeat this current-baseline explicit first-compare/do-loop wave-scan
  spelling. A baseline current-checkout trailing-pad removal probe (removing
  only unused `pad3`/`pad4` while promoting the current source) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FDDE55F/0x6EE6C1E0`, and the relinked
  focused diff regressed to `CURRENT (3261)`. It shrank the frame from target
  `0xf8` to `0xf0`, moved saved-register and parameter stack slots down by 8
  bytes, still lacked target `$f20/$f21` prologue saves, kept early zero in
  `$f16` instead of target `$f14`, and left the wave scan in current
  bound/index order. Source was restored and final full verify passed; do not
  repeat this current-baseline trailing `pad3`/`pad4` removal. A baseline
  current-checkout `ABSF` spelling
  for both absolute-velocity temporaries (`var_f14 = ABSF(racer->velocity);
  var_f0 = ABSF(racer->velocity)`) also missed: full verify failed with
  calculated CRCs `0x40ED9F86/0xDE608AA0`, and the relinked focused diff
  worsened to `CURRENT (4250)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this `ABSF` absolute-velocity spelling. A baseline
  current-checkout logical-not spinout-zap zero test
  (`racer->unk1FE == 4 && !racer->spinout_timer`) also missed as a
  no-movement family: full verify failed with the promoted-baseline CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this logical-not spinout-zap zero-test spelling. A baseline
  current-checkout `newSpinoutTimer` spinout assignment carrier
  (`newSpinoutTimer = 20; racer->spinout_timer = newSpinoutTimer`) also
  missed as a no-movement family: full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused
  diff stayed `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this `newSpinoutTimer` spinout assignment carrier. A
  baseline current-checkout first-speed boss-adjustment multiply spelling
  (`var_f20 = (var_f20 - 2.0) * 0.5`) also missed as a no-movement family:
  full verify failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`,
  and the relinked focused diff stayed `CURRENT (2760)`. It still lacked
  target `$f20/$f21` prologue saves, kept early zero in `$f16` instead of
  target `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this first-speed
  boss-adjustment multiply spelling. A baseline current-checkout first-speed
  boss guard operand-order spelling (`if (VEHICLE_BOSSES <=
  racer->vehicleID)`) also missed as a no-movement family: object-only focused
  diff first printed stale `CURRENT (0)`, full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused
  diff stayed `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this first-speed boss guard operand-order spelling. A
  baseline current-checkout later vehicleID upper-guard operand-order spelling
  (`if (VEHICLE_BOSSES < racer->vehicleID)`) also missed as a no-movement
  family: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and
  the relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this later vehicleID
  upper-guard operand-order spelling. A baseline current-checkout trick
  divisor branch-polarity spelling (`if (racer->trickType == 0) { var_f2 =
  8.0; } else { var_f2 = 4.0; }`) also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x97DCE260/0x7D421449`, and the relinked focused diff regressed to
  `CURRENT (3815)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and shifted later call-adjacent scheduling. Source was
  restored and final full verify passed; do not repeat this trick divisor
  branch-polarity spelling. A baseline current-checkout explicit `exitObj`
  pointer-test spelling (`if (racer->exitObj != NULL)`) also missed as a
  no-movement family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with the promoted-baseline CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this explicit `exitObj` pointer-test spelling. A baseline
  current-checkout exit-throttle single-precision literal spelling
  (`racer->throttle = 0.5f`) also missed as a no-movement family: full verify
  failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the
  relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this exit-throttle
  single-precision literal spelling. A baseline current-checkout exit-throttle
  direct dataflow spelling (`if (racer->exitObj) { racerThrottle =
  racer->throttle = 0.5; } else { racerThrottle = racer->throttle; }`) also
  missed badly: full verify failed with calculated CRCs
  `0x37836355/0x67E5A883`, and the relinked focused diff regressed to
  `CURRENT (4665)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and disturbed later call-adjacent/sound scheduling.
  Source was restored and final full verify passed; do not repeat this
  exit-throttle direct dataflow spelling. A baseline current-checkout brake
  direct dataflow spelling (moving `racerBrake = racer->brake` into both brake
  update arms) also missed: full verify failed with calculated CRCs
  `0x6017B63F/0xECA9D437`, and the relinked focused diff regressed to
  `CURRENT (3350)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and widened later gravity/call-adjacent scheduling
  drift. Source was restored and final full verify passed; do not repeat this
  brake direct dataflow spelling. A baseline current-checkout throttle-rate
  single-precision literal spelling (`racer->throttle += updateRateF * 0.01f`
  and `racer->throttle -= updateRateF * 0.01f`) also missed badly: full verify
  failed with calculated CRCs `0xE2FEB7C7/0xB4368A76`, and the relinked focused
  diff regressed to `CURRENT (6518)`. It still lacked target `$f20/$f21`
  prologue saves, kept early zero in `$f16` instead of target `$f14`, left the
  wave bound/index allocation reversed as current `a0`-bound/`v1`-loop instead
  of target `v1`-bound/`a0`-loop, and disturbed later
  gravity/call-adjacent/sound scheduling. Source was restored and final full
  verify passed; do not repeat this throttle-rate single-precision literal
  spelling. A baseline current-checkout brake upper-clamp double store-width
  spelling (`racer->brake = 1.2` instead of `1.2f` while keeping the double
  compare) also missed as a no-movement family: full verify failed with the
  promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and the relinked focused
  diff stayed `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this brake upper-clamp double store-width
  spelling. A baseline current-checkout opening
  update-rate single-precision multiplier spelling (`updateRateF *= 1.09f`)
  also missed badly: full verify failed with calculated CRCs
  `0x9A37265B/0xDC30F32A`, and the relinked focused diff regressed to
  `CURRENT (4943)`. It changed the opening multiply from target-like
  double-literal `mul.d`/`cvt.s.d` to `mul.s`, still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this opening
  update-rate single-precision multiplier spelling. A
  baseline current-checkout first-speed
  upper-clamp zero-threshold spelling (`if (var_f20 > 0.0) { var_f20 = 4; }`)
  also missed: full verify failed with calculated CRCs
  `0x67440D57/0x26427635`, and the relinked focused diff worsened to
  `CURRENT (3570)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this first-speed upper-clamp zero-threshold spelling. A
  baseline current-checkout negative inverse-gravity spelling
  (`var_f20 = -(var_f20 / 4.0)`) also missed: full verify failed with
  calculated CRCs `0xF1FCA843/0x71D137FF`, and the relinked focused diff
  worsened to `CURRENT (4340)`. It still lacked target `$f20/$f21` prologue
  saves, kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this negative inverse-gravity spelling. A
  baseline current-checkout first-speed sqrt-result split through existing
  `var_f0` (`var_f0 = sqrtf(...); var_f20 = var_f0 - 2.0`) also missed as a
  no-movement family: an object-only focused diff first printed stale
  `CURRENT (0)`, but full verify failed with the promoted-baseline CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff reported
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop. Source was restored and final full verify passed; do
  not repeat this existing-`var_f0` first-speed sqrt-result split. A baseline
  current-checkout late Wizpig animation guard branch-polarity spelling
  (`if (obj->animationID >= 3) { var_f20 = 0.0f; } else { var_f20 = 4.0f; }`)
  also missed: full verify failed with calculated CRCs
  `0x55404BDB/0xC3B5A8D9`, and relinked `./diff.sh func_80049794` regressed to
  `CURRENT (3765)`. The local Wizpig block changed from target `beqz` after
  `slti` to `bnez`, still lacked target `$f20/$f21` prologue saves, kept early
  zero in `$f16` instead of target `$f14`, and widened the usual wave-bound/FPR
  drift. Source was restored and final full verify passed; do not repeat this
  late Wizpig branch-polarity spelling. A close
  save-family x/z/y pre-`sqrtf` branch with chained grounded-wheel zero,
  steer-vel no-op, removed trailing `pad3`/`pad4`, and the target-looking
  first-speed zero-threshold upper clamp (`if (var_f20 > 0.0) { var_f20 = 4;
  }`) also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0xF07192B5/0xD69ABBCC`, and the
  relinked focused diff regressed to `CURRENT (5315)`. It kept the target
  `0xf8` frame, `$f20/$f21` prologue saves, and early `$f14` zero stores, but
  left the wave bound/index allocation reversed as current `a0`-bound/
  `v1`-loop instead of target `v1`-bound/`a0`-loop and disturbed later
  call-adjacent/sound scheduling. Source was restored and final full verify
  passed; do not repeat this close save-family zero-threshold clamp
  combination. A baseline current-checkout wave-lift single-precision literal
  spelling (`((38.0f - var_f2) * updateRateF * racerVelocity) / 8.0f`) also
  missed: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x6006EA9F/0x791FEBA1`, and the relinked
  focused diff regressed to `CURRENT (5085)`. It kept the target `0xf8` frame
  and early `$f14` zero stores, but still lacked target `$f20/$f21` prologue
  saves, moved saved GPR slots down by 8 bytes, left the wave bound/index
  allocation reversed as current `a0`-bound/`v1`-loop instead of target
  `v1`-bound/`a0`-loop, and disturbed later `$f14`/`$f20` gravity scheduling.
  Source was restored and final full verify passed; do not repeat this
  wave-lift single-precision literal spelling. A baseline current-checkout
  wave-lift divided-speed grouping
  (`((38 - var_f2) * updateRateF) * (racerVelocity / 8)`) also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x5FED69B7/0xD53B5C00`, and the relinked
  focused diff regressed to `CURRENT (3025)`. It kept the target `0xf8` frame,
  but still lacked target `$f20/$f21` prologue saves, moved saved GPR slots down
  by 8 bytes, put early zero back in `$f16` instead of target `$f14`, left the
  wave bound/index allocation reversed as current `a0`-bound/`v1`-loop instead
  of target `v1`-bound/`a0`-loop, and disturbed later `$f14`/`$f20` gravity
  scheduling. Source was restored and final full verify passed; do not repeat
  this wave-lift divided-speed grouping. A baseline current-checkout wave-lift
  positive-stick half-division spelling (`gCurrentStickY = gCurrentStickY / 2`
  instead of `gCurrentStickY >>= 1`) also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x581EE800/0x4D6819EC`, and the relinked focused diff regressed to
  `CURRENT (3560)`. It still lacked target `$f20/$f21` prologue saves, moved
  saved GPR slots down by 8 bytes, kept early zero in `$f16` instead of target
  `$f14`, left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop, and disturbed
  later `$f14`/`$f20` gravity scheduling. Source was restored and final full
  verify passed; do not repeat this wave-lift positive-stick half-division
  spelling. A baseline current-checkout split
  drift-reset condition
  (`if (racerVelocity < 8.0) { reset } else if (gCurrentStickY < -10) {
  reset }`) also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7CB10841/0x43C4193E`, and the relinked focused diff regressed to
  `CURRENT (5300)`. It still lacked target `$f20/$f21` prologue saves, moved
  saved GPR slots down by 8 bytes, kept early zero in `$f16` instead of target
  `$f14`, left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop, and disturbed
  player/wave plus later `$f14`/`$f20` temporary-register scheduling. Source
  was restored and final full verify passed; do not repeat this split
  drift-reset condition spelling. A worker current-checkout early wave
  magnitude carrier probe (`spEC = -racer->velocity`, then clamp/compare/use
  `spEC` in place of `racerVelocity` only in the early wave block) also missed:
  relinked `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, kept
  early zero in `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`/`v1` register-family drift. Worker source was restored, parent
  source guard was restored, and final full verify passed; do not repeat this
  `spEC` early wave magnitude carrier. A baseline current-checkout
  drift-direction nonzero spelling (`if (racer->drift_direction)` instead of
  `!= 0`) also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the relinked focused diff stayed at
  `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves, moved
  saved GPR slots down by 8 bytes, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this drift-direction
  nonzero spelling. A baseline current-checkout pitch-flip rotation mask
  simplification spelling (`racer->trickType * 0x180` instead of the nested
  `0x180 & 0xFFFFFFFF` mask expression) also missed as a no-movement family:
  full verify failed with calculated CRCs `0x5FDDE03F/0x25C10EDA`, and the
  relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this pitch-flip
  `0x180` mask simplification spelling. A baseline current-checkout
  trick-input horizontal `else if` spelling (`if (gCurrentStickX > 40) { ... }
  else if (gCurrentStickX < -40) { ... }`) also missed: full verify failed
  with calculated CRCs `0xE9D841B7/0xEEDBB8BB`, and the relinked focused diff
  stayed `CURRENT (2760)`. It still lacked target `$f20/$f21` prologue saves,
  kept early zero in `$f16` instead of target `$f14`, and left the wave
  bound/index allocation reversed as current `a0`-bound/`v1`-loop instead of
  target `v1`-bound/`a0`-loop. Source was restored and final full verify
  passed; do not repeat this trick-input horizontal `else if` spelling. A
  baseline current-checkout pitch-flip boost-duration decimal spelling
  (`normalise_time(10)` instead of `normalise_time(0xA)` in the
  `trickType == 2` completion path) also missed as a no-movement family: full
  verify failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and
  the relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this pitch-flip
  boost-duration decimal spelling. A sibling baseline pitch-flip boost-duration
  hex spelling (`normalise_time(0xA)` instead of `normalise_time(10)` in the
  `trickType == -2` completion path) also missed as a no-movement family: full
  verify failed with the promoted-baseline CRCs `0x5FDDE03F/0xEF7A0514`, and
  the relinked focused diff stayed `CURRENT (2760)`. It still lacked target
  `$f20/$f21` prologue saves, kept early zero in `$f16` instead of target
  `$f14`, and left the wave bound/index allocation reversed as current
  `a0`-bound/`v1`-loop instead of target `v1`-bound/`a0`-loop. Source was
  restored and final full verify passed; do not repeat this pitch-flip
  boost-duration hex spelling. A
  baseline check of `func_80059208` was still
  `CURRENT (870)`, with the same final-offset expression/load-order drift; do
  not repeat its recorded rejected final-block source shapes as a fallback.
  Keep the function active; do not park it just because these
  allocation/scheduling probes missed.
- `func_80059208` is active, not parked. Promoting the existing C compiles and
  focused object diff scores `CURRENT (870)`. The remaining drift is localized
  near the final lateral/vertical offset math: target preserves the negated
  `pad2 = -((tempZ * diffZ) + (diffX * tempX))` temporary and adds it to `pad`,
  while current folds the equivalent math into a subtract. Rejected probes:
  a 2026-05-24 promotion-only recheck of the current C removed the
  `NON_MATCHING` guard and showed uncompressed `./diff.sh func_80059208
  --no-pager` at `CURRENT (0)`, but the full matching build failed SHA with
  calculated CRCs `0x53D141DF/0xB9D4B481`. Object section sizes matched the
  expected object and inspected `.rodata` bytes matched, but the source was
  restored because the canonical gate did not reach `Verify: OK`; do not accept
  focused `CURRENT (0)` promotion-only evidence for this function without a
  passing full build.
  commuting the wrong-way angle guard to negative-first order
  (`angle < -0x4000 || angle > 0x4000`) missed: full verify failed with
  calculated CRCs `0x5BD141DF/0x44652332`, and the relinked focused diff
  worsened from promoted baseline `CURRENT (870)` to `CURRENT (1280)`. It
  shifted the mid-function angle branch family and did not improve the final
  object-dot plus negated-checkpoint-dot tail. Source was restored and final
  full verify passed; do not repeat this wrong-way angle branch-order spelling.
  A wrong-way velocity threshold single-precision literal probe
  (`racer->velocity <= -1.0f` instead of the current double literal) also
  missed: full verify failed with calculated CRCs `0x10768535/0x41CC0F5A`,
  and relinked `./diff.sh func_80059208` worsened from promoted baseline
  `CURRENT (870)` to `CURRENT (2130)`. It changed the target double-compare
  family in the wrong-way velocity guard and broadened downstream
  labels/final-tail drift. Source was restored and final full verify passed;
  do not repeat this wrong-way velocity `-1.0f` spelling.
  A nested wrong-way counter condition spelling (`if (racer->wrongWayCounter <
  200) { if (racer->velocity <= -1.0) ... }`) produced no relinked object
  movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and relinked `./diff.sh func_80059208` stayed at
  promoted baseline `CURRENT (870)`. The key drift remained the final
  lateral/vertical object-dot and tempY register allocation, not the wrong-way
  counter branch shape. Source was restored and final full verify passed; do
  not repeat this nested wrong-way counter spelling.
  A 2026-05-24 alternate-route sentinel operand-order spelling
  (`if (-1 == temp_v0_4->altRouteID)` at both early alternate-route checks)
  produced no relinked object movement: promoted full verify failed with
  calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed at
  baseline `CURRENT (870)`. The early alternate-route branch family remained
  target-like, and the key drift stayed in the final object-dot/checkpoint-dot
  plus vertical FPR allocation tail. Source was restored, final full verify
  passed, and `./score.sh -s` remained 97.30%; do not repeat this
  alternate-route sentinel operand-order spelling.
  Routing the final `diffX`/`diffZ` swap through the existing `pad` float local
  (`pad = diffX; diffX = diffZ; diffZ = -pad`) also missed: full verify failed
  with calculated CRCs `0x0A689858/0x4CFBB1F6`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1798)`. It inserted an early
  `neg.s`/store to `0x4c(sp)`, failed to preserve the target pre-swap
  `0x50(sp)` store family, shifted object-dot FPR allocation, and broadened
  final vertical correction drift. Source was restored and final full verify
  passed; do not repeat this final swap-through-`pad` spelling.
  A positive checkpoint-dot numerator spelling (`pad2 = (tempZ * diffZ) +
  (diffX * tempX); diffX = (pad2 - pad) / divisor`) also missed: promoted
  full verify failed with calculated CRCs `0xC7D996EA/0xC6D1DFDE`, and
  relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  worsened from promoted baseline `CURRENT (870)` to `CURRENT (1300)`. It
  kept the target pre-swap store family closer than the swap-through-`pad`
  probe, but removed the target post-divide `neg.s`, shifted the object-dot
  FPR allocation (`$f16` to `$f12` family), and broadened final vertical
  correction drift. Source was restored and final full verify passed; do not
  repeat this positive checkpoint-dot numerator spelling.
  Reusing the already-loaded `distance` local in the early checkpoint-scale
  divisor expression (`divisor = ((scale - distance) * splinePos) + distance`)
  produced no relinked object movement: object-only focused diff first showed
  stale prior output, full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and the relinked focused score stayed
  `CURRENT (870)` with the same final object-dot plus negated-checkpoint-dot
  drift. Source was restored and final full verify passed; do not repeat this
  divisor-distance reuse spelling. A baseline current-checkout early lap-reset
  nested guard branch-shape probe (`if (level_id() == 0) { if
  (racer->nextCheckpoint >= temp_v0) ... }`) also missed with no useful
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208` stayed `CURRENT (870)`. The final
  object-dot/checkpoint-dot plus vertical FPR drift remained unchanged. Source
  was restored and final full verify passed; do not repeat this early
  lap-reset nested guard branch-shape spelling. Commuting only the
  normalization magnitude sum from `sqrtf((diffX * diffX) + (diffZ * diffZ))` to
  `sqrtf((diffZ * diffZ) + (diffX * diffX))` missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x53D141DF/0x1FD84747`, and the relinked focused diff regressed from
  baseline `CURRENT (870)` to `CURRENT (916)` without improving the final
  object-dot/checkpoint-dot tail. Source was restored and final full verify
  passed; do not repeat this normalization magnitude sum-order spelling.
  Commuting only the normalization guard comparison from
  `if (distance != 0.0f)` to `if (0.0f != distance)` produced no relinked
  object movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and the relinked focused score stayed
  `CURRENT (870)` with the same final object-dot plus negated-checkpoint-dot
  drift. Source was restored and final full verify passed; do not repeat this
  normalization guard comparison-order spelling. Changing only the
  normalization reciprocal literal from `scale = 1.0f / distance` to
  `scale = 1.0 / distance` also missed: full verify failed with calculated CRCs
  `0x9261C342/0x2708D89B`, and relinked `./diff.sh func_80059208` regressed
  from promoted baseline `CURRENT (870)` to `CURRENT (2610)` by adding broad
  double-conversion scheduling around the normalization path and shifting later
  labels. Source was restored and final full verify passed; do not repeat this
  normalization reciprocal double-literal spelling. Changing only the initial
  checkpoint-distance complement from `splinePos = 1.0 -
  racer->checkpoint_distance` to `splinePos = 1.0f -
  racer->checkpoint_distance` also missed: full verify failed with calculated
  CRCs `0xC0802A15/0xAB5B7DB7`, and relinked `./diff.sh func_80059208`
  regressed from promoted baseline `CURRENT (870)` to `CURRENT (3020)`. The
  diff replaced the target double subtract with a single-precision `sub.s`,
  shifted the early checkpoint-distance branch schedule, and broadened
  downstream FPR/register scheduling well before the final tail. Source was
  restored and final full verify passed; do not repeat this checkpoint-distance
  `1.0f` complement spelling. Other rejected probes:
  reordering `pad`/`pad2`, accumulating into `pad`, `register f32 pad2`,
  signed-zero `0.0f - (...)`, removing `UNUSED` from `pad`/`pad2`, two-step
  `pad2 = expr; pad2 = -pad2`, operand-order swaps, inline `pad2` use, and
  splitting the final `diffX` assignment into a temporary. Additional rejected
  probes: delaying the `obj->trans.z_position` load until after `pad2`,
  `register f32 pad`, an empty `if (1) {}` barrier near `pad2`, transiently
  storing the negated dot product through `distance`, `register f32 distance`,
  rewriting the final expression as `pad - (-pad2)`, and a target-dataflow
  order that computes the checkpoint dot product, then the object dot product,
  then negates the checkpoint term before adding. That target-dataflow order
  compiled but worsened the focused score to `CURRENT (1684)` by moving the
  `diffZ = -diffY` store/load shape earlier and cascading float-register
  allocation through the final vertical offset block. Additional rejected
  probes: using a positive `pad2` plus `diffX = -((pad - pad2) / divisor)`
  compiled but left the focused score unchanged at `CURRENT (870)`; inlining
  the object position loads in the dot product worsened the score to
  `CURRENT (1356)` and changed earlier `splinePos` float-register allocation.
  Inlining only `obj->trans.x_position` while keeping `z_position` in the
  existing `distance` temporary worsened the score to `CURRENT (1826)` and
  disturbed earlier `splinePos`/double-temp allocation. Routing the checkpoint
  dot product through the existing `pad3` local before negating into `pad2`
  compiled but left the focused score unchanged at `CURRENT (870)`. Reusing
  the now-dead `diffY` local for the checkpoint dot product before the lateral
  correction worsened the focused score to `CURRENT (1465)`. Rewriting the
  equivalent final expression as positive `pad2` with
  `diffX = (pad2 - pad) / divisor` worsened the focused score to
  `CURRENT (1200)`. Routing the axis-rotation swap through the existing `pad3`
  local (`pad3 = diffX; diffX = diffZ; diffZ = -pad3`) worsened the focused
  score to `CURRENT (1698)`. Computing the negated rotated axis first
  (`diffY = -diffX; diffX = diffZ; diffZ = diffY`) worsened the focused score
  to `CURRENT (1090)`. Moving `pad`/`pad2` into a nested final lateral-offset
  block compiled but worsened the focused score to `CURRENT (1336)` by shifting
  stack slots by 8 bytes. Accumulating into `pad2`
  (`pad2 += pad; diffX = -(pad2 / divisor)`) compiled but left the focused
  score unchanged at `CURRENT (870)`. Reusing the now-dead `scale` local for
  the final `5.0f` lateral clamp (`scale = 5.0f; if (diffX > scale) ...`) also
  compiled but worsened the focused object score to `CURRENT (1015)`. Tightening
  the final lateral clamp comparisons one side at a time also missed: changing
  the upper branch to `if (diffX >= 5.0f)` failed full verify with calculated
  CRCs `0x53D141DF/0x46AE3428` and worsened the relinked focused score to
  `CURRENT (1065)`, while changing only the lower branch to
  `if (diffX <= -5.0f)` failed with CRCs `0x53D141DF/0x19D259D9` and worsened
  to `CURRENT (1070)`. Source was restored and final full verify passed; do
  not repeat these lateral clamp strictness probes. Swapping only the lateral
  clamp order to test the lower bound before the upper bound also missed: full
  verify failed with calculated CRCs `0x53D8C1DF/0xDBE11CED`, the relinked
  focused score worsened from promoted baseline `CURRENT (870)` to
  `CURRENT (1030)`, and the tail stayed in the same object-dot plus
  negated-checkpoint arithmetic/register drift family. Source was restored and
  final full verify passed; do not repeat this lateral lower-first clamp order.
  Tightening the final
  vertical clamp comparisons one side at a time also missed: changing the
  upper branch to `if (diffY >= 100.0f)` failed full verify with calculated
  CRCs `0x53D141DF/0x8F101C3E` and worsened the relinked focused score to
  `CURRENT (1070)`, while changing only the lower branch to
  `if (diffY <= -100.0f)` failed with CRCs `0x53D141DF/0x5B9D4EFD` and
  worsened to `CURRENT (1070)`. Source was restored and final full verify
  passed; do not repeat these vertical clamp strictness probes. Swapping only
  the vertical clamp order to test the lower bound before the upper bound also
  missed: full verify failed with calculated CRCs `0x53D101DF/0xB0C39AEC`,
  the relinked focused score worsened from promoted baseline `CURRENT (870)`
  to `CURRENT (1035)`, and the tail shifted the final vertical clamp
  comparison/constant schedule. Source was restored and final full verify
  passed; do not repeat this vertical lower-first clamp order. Replacing
  the final manual `diffX`/`diffY` clamp pairs with the repo `CLAMP` macro
  compiled but left the focused object score unchanged at `CURRENT (870)`.
  Inlining only `obj->trans.z_position` into the final object dot product while
  keeping `splinePos = obj->trans.x_position` local compiled but worsened the
  focused object score to `CURRENT (1684)` by reshaping the final offset block.
  Routing only the final object dot product through the unused `pad3` local
  (`pad3 = objDot; diffX = -((pad3 + pad2) / divisor)`) compiled but left the
  focused object score unchanged at `CURRENT (870)`. Routing the final
  `pad + pad2` sum through `pad3` also compiled but left the focused score
  unchanged at `CURRENT (870)`. Computing the final sum as
  `pad = pad2 + objectDot; diffX = -(pad / divisor)` after materializing the
  negated `pad2` also compiled but left the focused object score unchanged at
  `CURRENT (870)`. Routing the final `5.0f` lateral clamp limit through the
  unused `pad3` local compiled but worsened the focused object score to
  `CURRENT (1015)`. Reusing the now-dead `distance` local as the final `5.0f`
  lateral clamp-limit carrier (`distance = 5.0f; if (diffX > distance) ...;
  if (diffX < -distance) ...`) also missed: full verify failed with calculated
  CRCs `0x440002C7/0xC48C782C`, and the relinked focused diff worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1445)`. The tail broadened
  versus the earlier `scale`/`pad3` clamp-limit carriers and shifted later
  epilogue/global offsets. Source was restored and final full verify passed;
  do not repeat this final lateral `distance` clamp-limit carrier. Reusing the
  now-dead `splinePos` local as the final `5.0f` lateral clamp-limit carrier
  (`splinePos = 5.0f; if (diffX > splinePos) ...; if (diffX < -splinePos)
  ...`) also missed in the same family: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x440002C7/0xC48C782C`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (1445)`. The tail matched
  the bad final lateral clamp-limit carrier family and shifted downstream
  labels/global offsets. Source was restored and final full verify passed; do
  not repeat this final lateral `splinePos` clamp-limit carrier. Reusing the
  now-dead `diffZ` local as the final `5.0f` lateral clamp-limit carrier
  (`diffZ = 5.0f; if (diffX > diffZ) ...; if (diffX < -diffZ) ...`) also
  missed in that clamp-limit family: object-only focused diff first printed
  stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x96CFE0BD/0xA581F36F`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (1215)`. Source was
  restored and final full verify passed; do not repeat this final lateral
  `diffZ` clamp-limit carrier. Making `pad2` volatile compiled but worsened
  the focused score to `CURRENT (955)` by forcing stack traffic and shifting
  final-block
  scheduling. Rewriting the final lateral correction as a
  relative-position dot product (`splinePos = obj->trans.x_position - tempX;
  distance = obj->trans.z_position - tempZ; pad = (splinePos * diffX) + (diffZ
  * distance); diffX = -(pad / divisor)`) compiled but worsened the focused
  object score to `CURRENT (1897)`. Folding a positive checkpoint dot through
  `pad2` (`pad2 = checkpointDot; pad = objectDot - pad2; diffX = -(pad /
  divisor)`) compiled but left the focused score unchanged at `CURRENT (870)`.
  Computing `pad = objectDot; pad -= checkpointDot; diffX = -(pad / divisor)`
  also compiled but left the focused score unchanged at `CURRENT (870)`.
  Staging axis negation as `diffY = diffX; diffX = diffZ; diffY = -diffY;
  diffZ = diffY` compiled but worsened the focused object score to
  `CURRENT (974)`. Adding `register` lifetime hints to the final-block
  `tempX`/`tempZ` locals compiled but produced no object change from the
  baseline promoted candidate and left the focused object score unchanged at
  `CURRENT (870)`. Making only `pad` volatile in the promoted function compiled
  but worsened the focused object score to `CURRENT (1695)` by forcing extra
  final-block stack traffic. Splitting the final object dot into a partial
  `pad = splinePos * diffX`, then computing `pad2`, then loading
  `distance = obj->trans.z_position` and accumulating `pad += diffZ * distance`
  compiled but produced no object change from the promoted baseline and left
  the focused score unchanged at `CURRENT (870)`. Routing only the final
  vertical numerator through `pad3`
  (`pad3 = obj->trans.y_position - tempY; diffY = pad3 / divisor`) compiled but
  worsened the focused object score from `CURRENT (870)` to `CURRENT (1680)` by
  shifting final clamp scheduling/register allocation. Reusing the now-dead
  `distance` local as the axis-swap temporary
  (`distance = diffX; diffX = diffZ; diffZ = -distance`) compiled but worsened
  the focused object score from `CURRENT (870)` to `CURRENT (1548)` by shifting
  final-offset register allocation and clamp scheduling. Reusing the now-dead
  `tempY` local for the final vertical numerator
  (`tempY = obj->trans.y_position - tempY; diffY = tempY / divisor`) compiled
  but worsened the focused object score from `CURRENT (870)` to
  `CURRENT (1650)` by shifting final vertical clamp scheduling/register
  allocation. Reusing the now-dead `scale` local as the axis-swap temporary
  (`scale = diffX; diffX = diffZ; diffZ = -scale`) compiled but worsened the
  focused object score from `CURRENT (870)` to `CURRENT (1698)` by reshaping the
  final offset register family. Reusing the now-dead `splinePos` local as the
  axis-swap temporary (`splinePos = diffX; diffX = diffZ; diffZ = -splinePos`)
  also compiled but worsened the focused object score from `CURRENT (870)` to
  `CURRENT (1698)`, matching the bad `pad3`/`scale` axis-swap family. Moving
  the final lateral-correction negation into the numerator (`diffX = (-(pad +
  pad2)) / divisor`) compiled but worsened the focused object score from
  `CURRENT (870)` to `CURRENT (1600)` by delaying the negation until after the
  folded object-dot subtraction and perturbing the final vertical temp register
  family. Splitting the final vertical numerator through `diffY`
  (`diffY = obj->trans.y_position; diffY -= tempY; diffY /= divisor`) compiled
  but worsened the focused object score from `CURRENT (870)` to focused score
  `CURRENT (1242)` by extending the final vertical clamp/register drift.
  Reusing the now-dead `pad` local for the same final vertical numerator
  (`pad = obj->trans.y_position - tempY; diffY = pad / divisor`) compiled but
  worsened the focused object score to `CURRENT (1680)`, matching the bad
  final-vertical carrier direction rather than improving the lateral miss.
  Reusing the now-dead `distance` local for that final vertical numerator
  (`distance = obj->trans.y_position - tempY; diffY = distance / divisor`)
  also compiled but worsened the focused object score to `CURRENT (1680)` by
  inserting extra final-vertical stack traffic and leaving the lateral drift
  unchanged. Reusing the now-dead `pad2` local for that final vertical
  numerator (`pad2 = obj->trans.y_position - tempY; diffY = pad2 / divisor`)
  also compiled but worsened the relinked focused score to `CURRENT (1680)` and
  shifted the epilogue labels by adding final-clamp stack traffic; do not
  repeat this final-vertical carrier either. Routing only the final vertical
  clamp limit through the existing dead `pad3` local (`pad3 = 100.0f; if
  (diffY > pad3) ...; if (diffY < -pad3) ...`) also missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x4400230F/0x7B651F08`, and the relinked focused score
  worsened from promoted-baseline `CURRENT (870)` to `CURRENT (1995)`. The
  diff inserted extra vertical-clamp float traffic, shifted the final
  object-dot/checkpoint-dot register family, and moved the epilogue labels.
  Source was restored and final full verify passed; do not repeat this final
  vertical `pad3` clamp-limit carrier. Reusing the now-dead `scale` local for
  the same final vertical clamp-limit carrier (`scale = 100.0f; if (diffY >
  scale) ...; if (diffY < -scale) ...`) also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x4400230F/0x7B651F08`, and the relinked focused score worsened from
  promoted-baseline `CURRENT (870)` to `CURRENT (1995)`. This matches the same
  bad vertical clamp-limit carrier family as the `pad3`/`distance` variants,
  adding final-clamp float traffic and shifting the tail schedule. Source was
  restored and final full verify passed; do not repeat this final vertical
  `scale` clamp-limit carrier. Rewriting the final lateral
  correction as a reciprocal multiply (`diffX = -((pad + pad2) * (1.0f /
  divisor))`) compiled but worsened the relinked focused score to
  `CURRENT (1420)`, failed full verify with calculated CRCs
  `0x4BBAD57F/0xE56B870D`, and shifted the final vertical block after adding a
  reciprocal division/multiply sequence; do not repeat this final reciprocal
  spelling. Spelling the same final lateral correction with a negative divisor
  (`diffX = (pad + pad2) / -divisor`) also missed: relinked focused score
  worsened to `CURRENT (1295)`, full verify failed with calculated CRCs
  `0x53B0B9DF/0x4E71FC94`, and the target post-division negation shifted into
  a divisor-negation family with broader final vertical register drift. Do not
  repeat this negative-divisor spelling. Reordering the final lateral-axis
  swap to stage old `diffZ` through `diffY`
  (`diffY = diffZ; diffZ = -diffX; diffX = diffY`) compiled but worsened the
  relinked focused score from the promoted baseline `CURRENT (870)` to
  `CURRENT (1209)` and failed full verify with calculated CRCs
  `0x53B935EF/0x19303D77`; it shifted the final-block register family rather
  than matching the target tail. Do not repeat this old-`diffZ` axis-swap
  staging shape.
  Reusing the final-block `pad` local as the axis-swap temporary
  (`pad = diffX; diffX = diffZ; diffZ = -pad`) compiled and produced a
  deceptively low compressed score (`--max-size 260`: `CURRENT (20)`), but
  relinked full focused score worsened to `CURRENT (1698)` and full verify
  failed with calculated CRCs `0x0A689858/0x4CFBB1F6` because the final
  block/epilogue shifted. Reusing `pad2` as that axis-swap temporary produced
  the same relinked score and CRC family; do not repeat either `pad`/`pad2`
  axis-swap carrier. Using `pad` as a post-swap final-axis carrier
  (`diffY = diffX; diffX = diffZ; pad = diffY; diffZ = -pad`) compiled but
  produced no relinked focused movement from the promoted baseline: compressed
  tail stayed `CURRENT (845)` and full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; do not repeat this post-swap `pad` carrier either.
  Staging old `diffZ` through the existing `pad` local
  (`diffY = diffX; pad = diffZ; diffZ = -diffY; diffX = pad`) also missed:
  full verify failed with calculated CRCs `0x53ACBBF7/0x0E5DD078`, relinked
  focused score worsened to `CURRENT (2016)`, and the final tail shifted
  earlier into a broader object-dot/checkpoint-dot register family instead of
  matching the target delayed old-`diffZ` assignment. Source was restored and
  final full verify passed; do not repeat this old-`diffZ` through-`pad`
  axis-swap carrier.
  Splitting the checkpoint dot product into accumulating `pad2` statements
  (`pad2 = tempZ * diffZ; pad2 += diffX * tempX; pad2 = -pad2`) before the
  object dot compiled but produced the same focused score, `CURRENT (870)`, and
  the same final object-load/arithmetic drift as baseline. Routing the final
  `pad + pad2` sum through the now-dead `scale` local
  (`scale = pad + pad2; diffX = -(scale / divisor)`) also compiled but left the
  focused score unchanged at `CURRENT (870)`, with the same final
  arithmetic/register-family drift. Routing only the negated checkpoint-dot
  carrier through the now-dead `scale` local (`pad = checkpointDot; scale =
  -pad; pad = objectDot; diffX = -((pad + scale) / divisor)`) also compiled
  but produced no relinked object movement: focused score stayed
  `CURRENT (870)` and full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; source was restored and final full verify passed.
  Directly commuting the final expression to
  `diffX = -((pad2 + pad) / divisor)` also produced no relinked movement:
  focused score stayed `CURRENT (870)` and full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`. Do not repeat this direct `pad2 + pad`
  expression-order spelling. Swapping the final temp roles so the negated
  checkpoint dot lives in `pad`, the object dot lives in `pad2`, and the final
  expression is `diffX = -((pad2 + pad) / divisor)` also compiled but produced
  no relinked object movement: focused score stayed `CURRENT (870)` and full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`; source was
  restored and final full verify passed. Do not repeat this `pad`/`pad2`
  role-swap spelling. A later staged positive-checkpoint/split-object-dot
  spelling (`pad2 = checkpointDot; pad = objX * diffX; pad2 = -pad2;
  distance = objZ; pad += diffZ * distance`) also compiled to the promoted
  baseline shape: focused score stayed `CURRENT (870)`, full verify failed
  with calculated CRCs `0x53D141DF/0xB9D4B481`, and the final tail still loaded
  both object-position terms before matching the target negated-checkpoint
  schedule. Do not repeat this split-object-dot-after-positive-checkpoint
  spelling. Routing the final clamped vertical value
  through the now-dead `diffX` before the `unk1BC` cast/add
  (`diffX = diffY; racer->unk1BC += (s32) diffX`) compiled but worsened to
  `CURRENT (1030)` by inserting an extra `swc1` before the final conversion
  while leaving the lateral drift unchanged. Rewriting the final lateral
  update as `racer->unk1BA = (s32) diffX + racer->unk1BA` compiled but
  worsened the relinked focused score to `CURRENT (900)`, failed full verify
  with calculated CRCs `0x53CD41DF/0x4CAF790B`, and shifted the final update
  schedule rather than matching the target tail; do not repeat this add-order
  spelling. The sibling final vertical add-order spelling
  (`racer->unk1BC = (s32) diffY + racer->unk1BC`) also missed with relinked
  focused `CURRENT (900)` and calculated CRCs `0x53CD41DF/0x291D30F4`; do not
  repeat either final add-order update. Spelling the negated checkpoint
  dot product term-by-term (`pad2 = ((-tempZ) * diffZ) - (diffX * tempX)`)
  compiled but worsened to `CURRENT (1192)`: it introduced explicit early
  negation, but cascaded final-block register drift and still missed the target
  lateral arithmetic. Spelling the same negated checkpoint dot as
  `pad2 = (tempZ * -diffZ) - (diffX * tempX)` compiled but worsened the
  relinked focused score from `CURRENT (870)` to `CURRENT (1165)` and failed
  full verify with calculated CRCs `0x53AB58B5/0xBC82B0CE`; it shifted the final
  block/epilogue labels while still missing the target object-dot plus
  negated-checkpoint-dot schedule, so do not repeat this sibling term-negation
  spelling. Computing the negated checkpoint dot first, then loading
  both object-position locals before building `pad` compiled but left the
  focused score unchanged at `CURRENT (870)` with the same final
  object-load/arithmetic drift as the promoted baseline. Routing the final
  object-position loads through a named `ObjectTransform *trans = &obj->trans`
  local compiled and produced the target-like `lw v0, 0xc0(sp)` timing in the
  tail, but worsened the focused score to `CURRENT (1096)` by shifting the
  spline/local stack slots down by 4 bytes. Replacing the dead `pad3` local
  with that `ObjectTransform *trans` restored the stack-slot layout and
  compiled back to baseline `CURRENT (870)`, but produced no focused
  improvement and left the same final arithmetic/register drift. A narrower
  final-only `Object *obj2` lifetime probe (`obj2 = obj` immediately before
  loading final x/z positions, then using `obj2->trans`) also missed: relinked
  focused score worsened from `CURRENT (870)` to `CURRENT (878)`, full verify
  failed with calculated CRCs `0x53D141D7/0xAA087F2A`, and the same object-dot
  plus negated-checkpoint-dot arithmetic drift remained. Do not repeat this
  final object-pointer lifetime probe. Adding
  `register` to
  the `splinePos` local also compiled but produced no object change from the
  promoted baseline and left the focused score unchanged at `CURRENT (870)`.
  Reusing the now-dead `splinePos` local as the negated checkpoint-dot carrier
  (`pad = checkpointDot; splinePos = -pad; pad2 = objectDot; diffX = -((pad2 +
  splinePos) / divisor)`) compiled but worsened the focused object score to
  `CURRENT (1356)` by perturbing earlier `splinePos`/double-temp allocation and
  expanding final-block register drift. Routing the final object-dot `diffZ *
  distance` product through the existing `distance` local (`distance *= diffZ;
  pad = (splinePos * diffX) + distance`) compiled but worsened the relinked
  focused score to `CURRENT (2043)` by pulling the object pointer load and
  z-position load too early and broadening final-block register drift; do not
  repeat this distance-product carrier shape. Promoting the existing C can
  appear as focused `CURRENT (0)` before relink, but full verify fails with
  calculated CRCs `0x53D141DF/0xB9D4B481`; after relink the focused score is
  again `CURRENT (870)`, so treat any zero object-only result here as stale
  unless full `gmake` verifies. Reusing the now-dead `splinePos` local as a
  positive checkpoint-dot carrier
  (`splinePos = checkpointDot; pad = objectDot; diffX = -((pad - splinePos) /
  divisor)`) also compiled but produced no object change from promoted baseline,
  left the relinked focused score at `CURRENT (870)`, and failed full verify in
  the same CRC family `0x53D141DF/0xB9D4B481`; do not repeat this positive
  `splinePos` carrier shape. A positive checkpoint-minus-object numerator that
  kept the checkpoint dot in `pad2` (`pad2 = checkpointDot; pad = objectDot;
  pad2 -= pad; diffX = pad2 / divisor`) compiled but matched the existing
  positive-numerator failure family: relinked focused score `CURRENT (1300)`
  and full-verify CRCs `0xC7D996EA/0xC6D1DFDE`; source was restored and final
  full verify passed. Do not repeat this `pad2` positive-numerator variant
  either. Computing the negated checkpoint dot before the
  object-position locals, then splitting the final object dot into
  `pad = splinePos * diffX; pad += diffZ * distance`, also compiled to the
  promoted baseline shape: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused diff stayed `CURRENT (870)`, and
  the same final object-load/arithmetic drift remained. Do not repeat this
  split-object-dot-after-checkpoint spelling. Commuting only the x-position
  multiply in the final object dot (`pad = (diffX * splinePos) + (diffZ *
  distance)`) compiled but regressed from baseline to relinked focused
  `CURRENT (875)` and failed full verify with calculated CRCs
  `0x53D0C1DF/0xC593C532`; do not repeat this x-multiply commute. Splitting
  the negated checkpoint dot into `pad2 = -(tempZ * diffZ); pad2 -= diffX *
  tempX` compiled but
  worsened the relinked focused score to `CURRENT (1405)`, failed full verify
  with calculated CRCs `0x53C0A2B5/0x47AA3C12`, and broadened final-block
  register/label drift instead of matching the target checkpoint-dot schedule;
  do not repeat this split-negated spelling. Reversing the split order
  (`pad2 = -(diffX * tempX); pad2 -= tempZ * diffZ`) compiled but worsened the
  relinked focused score to `CURRENT (1736)`, failed full verify with
  calculated CRCs `0x53B3FDB5/0x46D415EE`, and expanded the same final-block
  register/label drift; do not repeat the reverse split-negated spelling
  either. Delaying the `diffZ = -diffY`
  axis assignment until after a positive checkpoint-dot expression
  (`pad2 = (tempZ * -diffY) + (diffX * tempX); diffZ = -diffY; ... diffX =
  -((pad - pad2) / divisor)`) compiled but worsened the relinked focused score
  to `CURRENT (2365)`, failed full verify with calculated CRCs
  `0x538F82DF/0x50E88FA7`, and perturbed earlier float-register allocation
  around the `0x59fbc` region before still missing the final arithmetic
  schedule; do not repeat this delayed-`diffZ` positive-checkpoint-dot spelling.
  Loading both final object-position locals before the negated checkpoint dot,
  then computing `pad2` before `pad`, compiled but produced no object movement
  from the promoted baseline: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused diff stayed `CURRENT (870)`, and
  the same final object-load/arithmetic drift remained. Do not repeat this
  object-local-before-`pad2` ordering. Mutating the now-dead `tempZ` and
  `tempX` locals before forming the checkpoint-dot carrier
  (`tempZ *= diffZ; tempX *= diffX; pad2 = -(tempZ + tempX)`) also missed:
  full verify failed with calculated CRCs `0x5CBA1A12/0x20830C42`, the
  relinked focused score worsened to `CURRENT (2173)`, and the diff showed
  broad float-register churn from the earlier spline setup through the final
  lateral/vertical clamp block instead of preserving the baseline tail. Do not
  repeat this temp-mutating checkpoint-dot carrier. Computing the positive
  checkpoint dot into `pad`, the object dot into `pad2`, then reusing `pad` as
  `checkpointDot - objectDot` before `diffX = pad / divisor` also missed:
  relinked focused score worsened to `CURRENT (1300)`, full verify failed with
  calculated CRCs `0xC7D996EA/0xC6D1DFDE`, and the final block/epilogue shifted
  instead of matching the target object-dot plus negated-checkpoint schedule.
  Do not repeat this positive numerator carrier. Reusing the now-dead `diffY`
  local as the final object x-position carrier before it is reassigned for the
  vertical correction (`diffY = obj->trans.x_position; pad = (diffY * diffX) +
  (diffZ * distance)`) also missed: relinked focused score worsened to
  `CURRENT (2611)`, full verify failed with calculated CRCs
  `0x1AA9FDC4/0x11BA4E46`, and the diff disturbed earlier
  `splinePos`/stack-slot allocation before broadening final-block register
  drift. Source was restored and final full verify passed. Do not repeat this
  final object-x `diffY` carrier. A `register f32 divisor` allocation hint
  also produced no movement from the promoted baseline: full verify failed with
  calculated CRCs `0x53D141DF/0xB9D4B481`, the relinked focused diff stayed
  `CURRENT (870)`, and the same final object-dot plus negated-checkpoint-dot
  arithmetic/register drift remained. Source was restored and final full
  verify passed; do not repeat this divisor register hint. Routing only the
  final object-dot x product through the now-dead `scale` local
  (`scale = splinePos * diffX; pad = scale + (diffZ * distance)`) compiled but
  worsened the relinked focused score to `CURRENT (940)`, failed full verify
  with calculated CRCs `0x53A518DF/0x0DEFF06A`, loaded object z before x in
  the final dot product, and broadened the final vertical FPR drift. Source
  was restored and final full verify passed; do not repeat this final
  object-dot `scale` carrier. Commuting the final object-dot terms directly
  (`pad = (diffZ * distance) + (splinePos * diffX)`) reproduced that same bad
  family: relinked focused score worsened to `CURRENT (940)`, full verify
  failed with calculated CRCs `0x53A518DF/0x0DEFF06A`, object z loaded before x
  in the final dot product, and the final vertical FPR drift broadened. Source
  was restored and final full verify passed; do not repeat this final object
  dot term-order spelling. Adding `register` to the
  final-block `diffZ` local is invalid because `diffZ` is passed by address to
  `cubic_spline_interpolation`; the compile failed with
  `address of register variable requested`. A narrower `register f32 scale`
  allocation hint compiled but produced no relinked object movement: full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, the focused score
  stayed `CURRENT (870)`, and the same final object-dot plus
  negated-checkpoint-dot load/register drift remained. Source was restored and
  final full verify passed; do not repeat either register-hint probe.
  Routing the final `pad + pad2` sum through the now-dead `diffX` local
  (`diffX = pad; diffX += pad2; diffX = -(diffX / divisor)`) compiled but
  missed: full verify failed with calculated CRCs
  `0x63E46DB5/0x591D1D44`, the relinked focused score worsened from the
  promoted baseline `CURRENT (870)` to `CURRENT (1165)`, and the final tail
  introduced extra `swc1` stack traffic/register drift around the lateral
  clamp instead of matching the target object-dot plus negated-checkpoint-dot
  schedule. Source was restored and final full verify passed; do not repeat
  this `diffX` final-sum carrier.
  Accumulating the existing negated checkpoint-dot carrier directly into
  `pad` (`pad += pad2; diffX = -(pad / divisor)`) compiled but produced no
  relinked movement from the promoted baseline: full verify failed with
  calculated CRCs `0x53D141DF/0xB9D4B481`, the focused score stayed
  `CURRENT (870)`, and the final object-dot/checkpoint-dot register drift was
  unchanged. Source was restored and final full verify passed; do not repeat
  this direct `pad += pad2` final-sum spelling.
  Directly commuting the negated checkpoint-dot sum inside the existing
  `pad2` expression (`pad2 = -((diffX * tempX) + (tempZ * diffZ))`) also
  missed: full verify failed with calculated CRCs `0x53ABC0DF/0xA18C1BA8`,
  the relinked focused score worsened to `CURRENT (1450)`, and the final tail
  shifted the checkpoint-dot multiply order while broadening the object-dot and
  final vertical FPR drift. Source was restored and final full verify passed;
  do not repeat this direct checkpoint-dot sum-order spelling.
  Keeping the current axis-swap order but spelling the negated checkpoint dot
  through the still-live old-`diffX` carrier
  (`pad2 = -((tempZ * -diffY) + (diffX * tempX))`) also missed: full verify
  failed with calculated CRCs `0x53D161DF/0x6008CEF3`, the relinked focused
  score worsened from the promoted baseline `CURRENT (870)` to `CURRENT (880)`,
  and the tail only swapped the first checkpoint-dot multiply operand order
  while leaving the object-dot plus final vertical FPR drift. Source was
  restored and final full verify passed; do not repeat this post-swap
  old-`diffX` checkpoint-dot carrier. Commuting only the first multiply inside
  the existing checkpoint-dot expression
  (`pad2 = -((diffZ * tempZ) + (diffX * tempX))`) reproduced that same miss
  family: full verify failed with calculated CRCs `0x53D161DF/0x6008CEF3`,
  relinked focused score worsened to `CURRENT (880)`, and the diff only
  swapped the first checkpoint-dot multiply while broadening the final tail.
  Source was restored and final full verify passed; do not repeat this direct
  first checkpoint-dot multiply-order spelling. Commuting only the second
  multiply inside the existing checkpoint-dot expression
  (`pad2 = -((tempZ * diffZ) + (tempX * diffX))`) missed worse: full verify
  failed with calculated CRCs `0x53D13EDF/0x99CD5C6A`, the relinked focused
  score worsened to `CURRENT (980)`, and the diff moved the final-tail
  `0x54(sp)` store later while broadening object-dot and final vertical
  float-register drift. Source was restored and final full verify passed; do
  not repeat this direct second checkpoint-dot multiply-order spelling.
  Commuting both checkpoint-dot multiplies together
  (`pad2 = -((diffZ * tempZ) + (tempX * diffX))`) also missed: full verify
  failed with calculated CRCs `0x53D15EDF/0xD6D4ED5A`, the relinked focused
  score worsened to `CURRENT (990)`, and the final tail shifted the same
  checkpoint-dot multiply-order family while broadening object-dot and final
  vertical FPR drift. Source was restored and final full verify passed; do not
  repeat this combined checkpoint-dot multiply-order spelling.
  Computing the negated
  checkpoint dot before completing the axis swap (`diffY = diffX; pad2 = -((tempZ * -diffY)
  + (diffZ * tempX)); diffX = diffZ; diffZ = -diffY`) also missed: full verify
  failed with calculated CRCs `0xDF8F8E89/0x317A96FF`, the relinked focused
  score worsened to `CURRENT (2614)`, and the function tail shifted by eight
  bytes instead of matching the target object-dot plus negated-checkpoint-dot
  schedule. Source was restored and final full verify passed; do not repeat
  this pre-axis-swap checkpoint-dot spelling.
  Splitting the final checkpoint-dot calculation so the first term used old
  `diffX` after assigning `diffX = diffZ` (`pad2 = tempZ * -diffY; diffZ =
  -diffY; pad2 += diffX * tempX; pad2 = -pad2`) also missed: full verify
  failed with calculated CRCs `0x543A5FDF/0x5F70BBBB`, the relinked focused
  score regressed to `CURRENT (2165)`, and the diff showed broad early FPR
  allocation drift before returning to the same final object-dot/clamp
  mismatch family. Source was restored and final full verify passed; do not
  repeat this split old-`diffX` checkpoint-dot schedule.
  Routing the final lateral cast through the existing dead `angle` local
  (`angle = (s32) diffX; racer->unk1BA += angle`) compiled but produced no
  relinked focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and source
  was restored/final verify passed. Do not repeat this final lateral `angle`
  cast carrier.
  Routing the final lateral cast through the existing dead `counter` local
  (`counter = (s32) diffX; racer->unk1BA += counter`) also compiled but
  produced no relinked focused movement: full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and
  source was restored/final verify passed. Do not repeat this final lateral
  `counter` cast carrier.
  Routing the final vertical cast through the existing dead `angle` local
  (`angle = (s32) diffY; racer->unk1BC += angle`) compiled but also produced no
  relinked focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and source
  was restored/final verify passed. Do not repeat this final vertical `angle`
  cast carrier.
  Routing the final vertical cast through the existing dead `counter` local
  (`counter = (s32) diffY; racer->unk1BC += counter`) also produced no relinked
  focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and source was
  restored/final verify passed. Do not repeat this final vertical `counter`
  cast carrier.
  Routing the final lateral cast through the existing dead `splineIndex` local
  (`splineIndex = (s32) diffX; racer->unk1BA += splineIndex`) also produced no
  relinked focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and the same
  final object-dot/checkpoint-dot plus vertical FPR drift remained. Source was
  restored and final full verify passed; do not repeat this final lateral
  `splineIndex` cast carrier.
  Routing the final vertical cast through the existing dead `splineIndex` local
  (`splineIndex = (s32) diffY; racer->unk1BC += splineIndex`) likewise
  produced no relinked focused movement: full verify failed with calculated
  CRCs `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and the
  same final object-dot/checkpoint-dot plus vertical FPR drift remained. Source
  was restored and final full verify passed; do not repeat this final vertical
  `splineIndex` cast carrier.
  Replacing the negated checkpoint-dot expression with a post-axis-swap
  old-`diffX` positive carrier
  (`pad2 = (tempZ * diffY) - (diffX * tempX)`) also missed: full verify failed
  with calculated CRCs `0x53D0C1DF/0x02CA4607`, relinked focused score
  worsened to `CURRENT (980)`, and the final tail shifted into another
  object-dot/checkpoint-dot register family. Source was restored and final
  full verify passed; do not repeat this old-`diffX` positive checkpoint-dot
  spelling.
  Commuting only the final object-dot z product from
  `diffZ * distance` to `distance * diffZ` also missed: full verify failed
  with calculated CRCs `0x53F241DF/0xFF09E640`, relinked focused score
  worsened from the promoted baseline `CURRENT (870)` to `CURRENT (875)`, and
  the tail shifted into the same small object-dot multiply-order family as the
  earlier x-product commute while broadening the final vertical FPR drift.
  Source was restored and final full verify passed; do not repeat this
  final object-dot z-multiply commute.
  Commuting both final object-dot products while preserving term order
  (`pad = ((diffX * splinePos) + (distance * diffZ))`) also missed: full
  verify failed with calculated CRCs `0x53F1C1DF/0xFE149A6C`, relinked
  `./diff.sh func_80059208` worsened from promoted baseline `CURRENT (870)`
  to `CURRENT (880)`, and the tail stayed in the small object-dot
  multiply-order family while broadening final vertical FPR drift. Source was
  restored and final full verify passed; do not repeat this both-product
  object-dot commute.
  Rewriting the final vertical numerator as a negated reversed subtraction
  (`diffY = -((tempY - obj->trans.y_position) / divisor)`) also missed:
  full verify failed with calculated CRCs `0x53C55FB5/0x7A9D66B3`, relinked
  focused score worsened from promoted baseline `CURRENT (870)` to
  `CURRENT (1110)`, inserted an extra final-block `neg.s`, and shifted tail
  labels/final vertical FPR scheduling. Source was restored and final full
  verify passed; do not repeat this final-vertical reversed-subtraction
  spelling.
  A mid-axis-swap negated checkpoint-dot spelling
  (`diffY = diffX; diffX = diffZ; pad2 = -((tempZ * -diffY) + (diffX *
  tempX)); diffZ = -diffY`) also missed: full verify failed with calculated
  CRCs `0x4FA14EA0/0x0254255C`, relinked focused score worsened to
  `CURRENT (4296)`, and the probe perturbed float-register allocation before
  the final tail instead of matching the target delayed old-`diffZ` store.
  Source was restored and final full verify passed; do not repeat this
  mid-axis-swap negated checkpoint-dot spelling.
  Hoisting only the final object x/z position loads before the lateral-axis
  swap (`splinePos = obj->trans.x_position; distance =
  obj->trans.z_position;` before `diffY = diffX; diffX = diffZ; diffZ =
  -diffY`) also missed: full verify failed with calculated CRCs
  `0x53D141DF/0x612988AC`, relinked focused score worsened from baseline
  `CURRENT (870)` to `CURRENT (1681)`, and the diff pulled the object pointer
  plus x/z loads too early while broadening the final object-dot/checkpoint-dot
  register drift. Source was restored and final full verify passed; do not
  repeat this final object-load hoist.
  Routing the final lateral cast through the existing dead `temp_v0` local
  (`temp_v0 = (s32) diffX; racer->unk1BA += temp_v0`) also produced no relinked
  focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and the same
  final object-dot/checkpoint-dot plus vertical FPR drift remained. Source was
  restored and final full verify passed; do not repeat this final lateral
  `temp_v0` cast carrier.
  Routing the final lateral cast through the existing loop local `i`
  (`i = (s32) diffX; racer->unk1BA += i`) also produced no relinked focused
  movement: an object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked focused
  score stayed `CURRENT (870)`, and the same final object-dot/checkpoint-dot
  plus vertical FPR drift remained. Source was restored and final full verify
  passed; do not repeat this final lateral `i` cast carrier.
  Routing the final vertical cast through the existing dead `temp_v0` local
  (`temp_v0 = (s32) diffY; racer->unk1BC += temp_v0`) likewise produced no
  relinked focused movement: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, focused score stayed `CURRENT (870)`, and the same
  final object-dot/checkpoint-dot plus vertical FPR drift remained. Source was
  restored and final full verify passed; do not repeat this final vertical
  `temp_v0` cast carrier.
  Routing the final vertical cast through the existing loop local `i`
  (`i = (s32) diffY; racer->unk1BC += i`) also produced no relinked focused
  movement: object-only focused diff printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked focused score
  stayed `CURRENT (870)`, and the same final object-dot/checkpoint-dot plus
  vertical FPR drift remained. Source was restored and final full verify
  passed; do not repeat this final vertical `i` cast carrier.
  Reusing the now-dead `diffZ` local as the final vertical correction carrier
  (`diffZ = (obj->trans.y_position - tempY) / divisor`, clamp `diffZ`, then
  `racer->unk1BC += (s32) diffZ`) also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x53D135E7/0x934392FC`, and the relinked focused score worsened to
  `CURRENT (910)`. The tail moved the clamped vertical value to `0x4c(sp)`,
  changed the final conversion FPR family, and left the final
  object-dot/checkpoint-dot drift intact. Source was restored and final full
  verify passed; do not repeat this final vertical `diffZ` carrier.
  Computing the negated checkpoint dot first, then building the final object
  dot in-place through `pad` (`pad = obj->trans.x_position; pad *= diffX;
  distance = obj->trans.z_position; pad += diffZ * distance`) also missed:
  full verify failed with calculated CRCs `0x539CDEEF/0x8B5DB390`, and the
  relinked focused score worsened from promoted-baseline `CURRENT (870)` to
  `CURRENT (1951)`. The diff pulled the object pointer load earlier, broadened
  final-tail FPR allocation, and shifted tail labels. Source was restored and
  final full verify passed; do not repeat this in-place `pad` object-dot
  spelling. A node-sampling loop condition cleanup probe also missed:
  promoting `func_80059208` and changing the five-node fill loop from
  `(i < 5) ^ 0` to `i < 5` failed full verify with calculated CRCs
  `0x53905373/0x65198BEE`; the relinked focused diff worsened from the
  promoted baseline `CURRENT (870)` to `CURRENT (1515)`. The diff moved the
  sampling-loop pointer increments/limit test away from the target
  pointer-limit family (`a2`/`v1` updates and `bne v1,t8` vs target
  `sltu at,v1,t8`/`bnez at`), while later tail labels shifted by four bytes.
  Source was restored and final full verify passed. A 2026-05-24 sibling
  five-node loop condition spelling (`i != 5`) collapsed into the same miss:
  full verify failed with the same calculated CRCs `0x53905373/0x65198BEE`,
  and relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  worsened to `CURRENT (1515)` with the same sampling-loop pointer
  increment/limit-test drift. Source was restored and final full verify
  passed; do not repeat these loop condition cleanup variants.
  Spelling only the cubic-spline boolean carrier literals as
  `splineIndex = 0` and `splineIndex = 1` instead of `FALSE`/`TRUE` also
  missed: full verify failed with the baseline calculated CRCs
  `0x53D141DF/0xB9D4B481`, the relinked focused score stayed
  `CURRENT (870)`, and the same final object-dot/checkpoint-dot plus vertical
  FPR drift remained. Source was restored and final full verify passed; do not
  repeat this `splineIndex` literal boolean spelling.
  Reversing only the splineIndex threshold comparison to
  `if (1.0 <= splinePos)` also missed with no relinked focused movement: full
  verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, focused score
  stayed `CURRENT (870)`, and the same final object-dot/checkpoint-dot plus
  vertical FPR drift remained. Source was restored and final full verify
  passed; do not repeat this `splineIndex` comparison-direction spelling.
  Spelling the final lateral numerator as negated object-dot minus the existing
  negated checkpoint dot (`diffX = ((-pad) - pad2) / divisor`) also missed:
  full verify failed with calculated CRCs `0x53A8D1B5/0x58F0CEC9`, and the
  relinked focused score worsened from promoted-baseline `CURRENT (870)` to
  `CURRENT (2035)`. The tail pulled both object-position loads before the
  target `0x40a0` clamp constant, materialized a negative-object numerator
  family, shifted later labels by four bytes, and kept the final
  object-dot/checkpoint-dot plus vertical FPR drift. Source was restored and
  final full verify passed; do not repeat this negated-object numerator
  spelling.
  Splitting the final lateral correction into two independent divisions
  (`diffX = (-pad / divisor) - (pad2 / divisor)`) also missed: full verify
  failed with calculated CRCs `0x0B291618/0x580678D9`, and the relinked focused
  score worsened from promoted-baseline `CURRENT (870)` to `CURRENT (2415)`
  under `--max-size 520`. The final-tail schedule grew by 12 bytes, shifted
  later labels/global offsets, and broadened the final lateral/vertical FPR
  drift instead of matching the target single division plus post-division
  negation. Source was restored and final full verify passed; do not repeat
  this split-division final lateral spelling.
  Splitting only the final post-division negation
  (`diffX = (pad + pad2) / divisor; diffX = -diffX`) also missed: full verify
  failed with calculated CRCs `0xDAD5418A/0x1CDDCDF7`, and the relinked
  focused score worsened from promoted-baseline `CURRENT (870)` to
  `CURRENT (925)`. The tail still missed the object-dot/checkpoint-dot
  register schedule and broadened the final vertical FPR drift. Source was
  restored and final full verify passed; do not repeat this post-division
  negation split spelling.
  Splitting the final lateral correction into a pre-division numerator
  assignment (`diffX = -(pad + pad2); diffX /= divisor`) also missed: full
  verify failed with calculated CRCs `0xDAE4B7D2/0xC7074DD0`, and the relinked
  focused score worsened from promoted-baseline `CURRENT (870)` to
  `CURRENT (1610)`. The diff broadened the final-tail offset drift instead of
  matching the target single-expression division/negation schedule. Source was
  restored and final full verify passed; do not repeat this pre-division
  numerator split spelling.
  Keeping the current object-position load order but building the final object
  dot in-place through `pad` (`pad = splinePos; pad *= diffX; pad += diffZ *
  distance`) also produced no relinked object movement: full verify failed
  with calculated CRCs `0x53D141DF/0xB9D4B481`, the focused score stayed
  `CURRENT (870)`, and the same final object-dot/checkpoint-dot plus vertical
  FPR drift remained. Source was restored and final full verify passed; do not
  repeat this current-order in-place `pad` object-dot spelling.
  Reusing the now-dead `splinePos` local as the final vertical numerator
  carrier (`splinePos = obj->trans.y_position - tempY; diffY = splinePos /
  divisor`) also missed: full verify failed with calculated CRCs
  `0x0A7688A6/0x4502A514`, the relinked focused score worsened from promoted
  baseline `CURRENT (870)` to `CURRENT (1890)`, and the tail inserted extra
  final-vertical local traffic while leaving the object-dot/checkpoint-dot
  drift unresolved. Source was restored and final full verify passed; do not
  repeat this final-vertical `splinePos` numerator carrier.
  Reusing the now-dead `scale` local as the final vertical numerator carrier
  (`scale = obj->trans.y_position - tempY; diffY = scale / divisor`) also
  missed: full verify failed with calculated CRCs `0x0A76A8A6/0x783976A1`,
  the relinked focused score worsened from promoted baseline `CURRENT (870)`
  to `CURRENT (1875)`, and the tail inserted extra final-vertical local
  traffic while leaving the object-dot/checkpoint-dot drift unresolved. Source
  was restored and final full verify passed; do not repeat this final-vertical
  `scale` numerator carrier.
  Reusing the now-dead `distance` local only as the final vertical clamp-limit
  carrier (`distance = 100.0f; if (diffY > distance) ...; if (diffY <
  -distance) ...`) also missed: full verify failed with calculated CRCs
  `0x4400230F/0x7B651F08`, and the relinked focused diff worsened from
  promoted baseline `CURRENT (870)` to `CURRENT (1995)`. This collapsed into
  the same bad vertical clamp-limit family as the earlier `pad3` carrier,
  adding final-clamp float traffic and shifting the tail schedule. Source was
  restored and final full verify passed; do not repeat this final vertical
  `distance` clamp-limit carrier.
  A 2026-05-23 single-assignment unary first-product spelling of the negated
  checkpoint dot (`pad2 = -(tempZ * diffZ) - (diffX * tempX)`) also collapsed
  into the same split-negated checkpoint-dot family: full verify failed with
  calculated CRCs `0x53C0A2B5/0x47AA3C12`, the relinked focused diff worsened
  from promoted-baseline `CURRENT (870)` to `CURRENT (1445)`, and the tail
  moved the `0x54(sp)` store while broadening the lateral/vertical FPR
  schedule. Source was restored and final full verify passed; do not repeat
  this single-assignment unary first-product checkpoint-dot spelling.
  A sibling single-assignment unary second-product spelling of the negated
  checkpoint dot (`pad2 = (diffX * -tempX) - (tempZ * diffZ)`) also missed:
  full verify failed with calculated CRCs `0x53B8FDB5/0xDAD64A9D`, the
  relinked focused diff worsened from promoted-baseline `CURRENT (870)` to
  `CURRENT (1326)`, and the tail broadened the lateral/vertical FPR schedule
  instead of matching the target object-dot/checkpoint-dot order. Source was
  restored and final full verify passed; do not repeat this
  unary-second-product checkpoint-dot spelling.
  A later checkpoint-dot sum-order/product-order variant
  (`pad2 = -((diffX * tempX) + (diffZ * tempZ))`) also missed: full verify
  failed with calculated CRCs `0x53BCC0DF/0xB8771E78`, the relinked focused
  diff worsened from promoted baseline `CURRENT (870)` to `CURRENT (1445)`,
  and the tail stayed in the broadened checkpoint-dot FPR schedule instead of
  matching the target object-dot/checkpoint-dot order. Source was restored and
  final full verify passed; do not repeat this checkpoint-dot sum/product-order
  spelling.
  A 2026-05-23 courseCheckpoint threshold spelling that changed
  `racer->courseCheckpoint > -0x7D00` to
  `racer->courseCheckpoint >= -0x7CFF` also missed as a no-movement family:
  full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked
  `./diff.sh func_80059208` stayed `CURRENT (870)`, and the early
  courseCheckpoint guard still compiled to the same target-like `slti
  -0x7cff` block while the final object-dot/checkpoint-dot tail drift remained.
  Source was restored and final full verify passed; do not repeat this
  courseCheckpoint threshold spelling.
  A 2026-05-23 final vertical reciprocal-multiply spelling that changed
  `diffY = (obj->trans.y_position - tempY) / divisor` to
  `diffY = (obj->trans.y_position - tempY) * (1.0f / divisor)` also missed:
  full verify failed with calculated CRCs `0x4BE5F47F/0x9BA27DDB`, and
  relinked `./diff.sh func_80059208` worsened from promoted baseline
  `CURRENT (870)` to `CURRENT (1782)`. The probe inserted reciprocal
  divide/multiply traffic in the final vertical correction path and shifted
  downstream tail labels while leaving the object-dot/checkpoint-dot drift
  unresolved. Source was restored and final full verify passed; do not repeat
  this final vertical reciprocal-multiply spelling. A 2026-05-23 final lateral
  cast-width spelling that changed only `racer->unk1BA += (s32) diffX` to
  `racer->unk1BA += (s16) diffX` also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x4EB921DF/0x33EF7BFD`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (935)`. The diff added a
  halfword cast/sign-extension family in the final lateral update and left the
  object-dot/checkpoint-dot plus vertical FPR drift unresolved. Source was
  restored and final full verify passed; do not repeat this final lateral
  `(s16) diffX` cast spelling. A sibling final vertical cast-width spelling
  that changed only `racer->unk1BC += (s32) diffY` to
  `racer->unk1BC += (s16) diffY` also missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x53C341DF/0x1D08B7B9`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (890)`. The diff added
  a narrow-cast/sign-extension direction in the final vertical update and left
  the object-dot/checkpoint-dot plus vertical FPR drift unresolved. Source was
  restored and final full verify passed; do not repeat this final vertical
  `(s16) diffY` cast spelling. A 2026-05-23 explicit final self-add assignment
  probe (`racer->unk1BA = racer->unk1BA + (s32) diffX` and
  `racer->unk1BC = racer->unk1BC + (s32) diffY`) also missed: full verify
  failed with calculated CRCs `0x53D141DF/0xB9D4B481`, relinked
  `./diff.sh func_80059208` stayed at promoted baseline `CURRENT (870)`, and
  the same final object-dot/checkpoint-dot plus vertical FPR drift remained.
  Source was restored and final full verify passed; do not repeat this
  explicit final self-add assignment spelling. A final object-dot distance
  accumulation spelling (`distance *= diffZ; pad = (splinePos * diffX) +
  distance`) also missed: full verify failed with calculated CRCs
  `0x53C1B1DF/0xF7700159`, and relinked `./diff.sh func_80059208` worsened
  from promoted baseline `CURRENT (870)` to `CURRENT (2043)`. The probe pulled
  the object pointer/z load earlier, broadened the final object-dot FPR
  schedule, and shifted final vertical/clamp register allocation. Source was
  restored and final full verify passed; do not repeat this final object-dot
  distance accumulation spelling. A 2026-05-24 final vertical plus-negated
  numerator spelling (`diffY = (obj->trans.y_position + -tempY) / divisor`)
  also missed as a no-movement family: full verify failed with the
  promoted-baseline CRCs `0x53D141DF/0xB9D4B481`, and relinked
  `./diff.sh func_80059208 --compress-matching 2 --no-pager` stayed
  `CURRENT (870)` with the same final object-dot/checkpoint-dot plus vertical
  FPR drift. Source was restored and final full verify passed; do not repeat
  this final vertical plus-negated numerator spelling.
  Keep this function active; do not park it just because these final-offset
  probes missed.
- `trackbg_render_flashy` is active, not parked. Promoting the existing C
  compiles, but the uncompressed linked focused diff currently scores
  `CURRENT (1808)` and starts early in the position-array setup: the target
  keeps the negative scaled cosine in `$f18`, loads `0x30(sp)` before computing
  `scaledXCos + scaledXSin`, and then diverges through the outer-ring
  position-array schedule.
  Rejected probes: replacing the repeated `(xSin * 1280.0f)` terms in the first
  four x/z position assignments with `scaledXSin` widened the frame to `0x168`
  and worsened the focused score to `CURRENT (12121)`; reordering the index
  5-8 x/z position stores to match the apparent target store sequence worsened
  the focused score to `CURRENT (2551)` and shifted later scheduling. Replacing
  only `xPositions[0] = -scaledXCos - (xSin * 1280.0f)` with
  `xPositions[0] = -scaledXCos - scaledXSin` also collapsed into the bad
  frame-shrink family: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`, and the relinked focused score worsened to
  `CURRENT (13821)`. The frame shrank from target `0x158` to `0x150`, the
  early position-array schedule broadened, and global offsets/tail labels
  shifted. Source was restored and final full verify passed; do not repeat
  this single-site `xPositions[0]` scaledXSin replacement. A
  narrower single-site outer-ring reorder that moved only `zPositions[6]`
  before `xPositions[6]` compiled but worsened the relinked focused score to
  `CURRENT (3860)`, failed full verify with calculated CRCs
  `0x93D338FF/0xB8A243D7`, and shifted the early position-array schedule; do
  not repeat this single-site z6/x6 reorder. A later exact outer-ring
  `xPositions[5]`, `zPositions[5]`, `zPositions[6]`, `xPositions[6]`
  store-order spelling compiled but also missed: relinked focused score
  `CURRENT (3043)`, failed full verify with calculated CRCs
  `0xDC7DFA91/0xC168DB3D`, and shifted the early position-array
  float-register schedule instead of matching the target; source was restored
  and final full verify passed. Do not repeat this exact outer-ring
  x5/z5/z6/x6 store-order spelling. Computing `scaledXCos` before
  `scaledXSin` while leaving declarations and store expressions unchanged also
  missed: relinked focused score stayed `CURRENT (1808)`, full verify failed
  with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the early position-array
  float-register family stayed in the known baseline/additive-double miss
  shape. Do not repeat this `scaledXCos`-first assignment-order spelling.
  Commuting both initial scaled-sine/cosine multiply assignments to literal
  first (`scaledXSin = 1280.0f * xSin; scaledXCos = 1280.0f * xCos`) also
  missed: full verify failed with calculated CRCs `0x93A783FF/0x60886348`,
  and the relinked focused score worsened from baseline `CURRENT (1808)` to
  `CURRENT (2138)`. The diff moved the first multiply/register family from
  target `$f18` toward `$f16` and broadened early position-array scheduling.
  Source was restored and final full verify passed; do not repeat this
  initial scaled multiply operand-order spelling. Reordering only the center
  position stores from `xPositions[4] = 0.0f; zPositions[4] = 0.0f;` to
  `zPositions[4] = 0.0f; xPositions[4] = 0.0f;` also missed: object-only focused
  diff first printed stale `CURRENT (0)`, full verify failed with calculated
  CRCs `0x93D338FF/0xC989AC94`, and the relinked focused score worsened from
  baseline `CURRENT (1808)` to `CURRENT (1880)`. The diff moved the early
  negative-cosine carrier/register family and broadened the position-array
  schedule rather than recovering target ordering. Source was restored and
  final full verify passed; do not repeat this center position store-order
  spelling. A 2026-05-24 center position chained-zero assignment probe
  (`xPositions[4] = zPositions[4] = 0.0f`) also missed: full verify failed with
  calculated CRCs `0x96E81A7F/0x02FF87C9`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` worsened
  from promoted baseline `CURRENT (1808)` to `CURRENT (1992)`. It shifted the
  center/outer position stack schedule while keeping the early negative-cosine
  `$f18`/`$f16` register drift. Source was restored and final full verify passed;
  do not repeat this center chained-zero assignment spelling.
  Rewriting only the final vertex alpha ternary from
  `(i <= 4) ? 255 : 0` to the equivalent `(i < 5) ? 255 : 0` also produced no
  focused movement: full verify failed with the known calculated CRCs
  `0x93D338FF/0x03D9C8FE`, the relinked focused score stayed
  `CURRENT (1808)`, and the diff remained in the same early position-array
  register/order family. Source was restored and final full verify passed.
  Do not repeat this final vertex alpha ternary spelling.
  Rewriting the whole final vertex population from the index loop to an
  `xPositions`/`zPositions` pointer walk also missed: full verify failed with
  calculated CRCs `0x93853BFF/0xB63372C5`, relinked
  `./diff.sh trackbg_render_flashy` worsened from promoted baseline
  `CURRENT (1808)` to `CURRENT (2278)`, and the frame grew from target `0x158`
  to `0x160` while stack offsets and the early position-array schedule shifted.
  Source was restored and final full verify passed. Do not repeat this vertex
  pointer-loop spelling.
  Reordering only the `uCoords[7]` UV expression to put `pos.z` first
  (`uCoords[7] = (s16) (pos.z + (2.0f * xCos)) + var_v0`) compiled but did not
  move the function: focused diff stayed `CURRENT (1808)`, full verify failed
  with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the visible drift remained
  in the earlier position-array schedule. Do not repeat this `uCoords[7]`
  pos.z-first UV expression-order probe. Rewriting only `uCoords[7]` from
  `((2.0f * xCos) + pos.z)` to `((xCos + xCos) + pos.z)` also produced no
  relinked focused movement: full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, focused score stayed `CURRENT (1808)`, and the diff
  remained in the same early position-array register/order family. Source was
  restored and final full verify passed. Do not repeat this `uCoords[7]`
  additive-double UV spelling. Rewriting only `vCoords[7]` from
  `((2.0f * pos.x) - var_f16)` to `((pos.x + pos.x) - var_f16)` compiled but
  also did not move the function: focused diff stayed `CURRENT (1808)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the visible
  drift remained in the earlier position-array schedule. Do not repeat this
  `vCoords[7]` additive-double UV spelling. Rewriting only `vCoords[7]` from
  `((2.0f * pos.x) - var_f16)` to `(-var_f16 + (2.0f * pos.x))` also produced
  no useful movement: full verify failed with the known calculated CRCs
  `0x93D338FF/0x03D9C8FE`, the relinked focused score stayed
  `CURRENT (1808)`, and the diff remained in the same early position-array
  register/order family. Source was restored and final full verify passed. Do
  not repeat this `vCoords[7]` operand-order UV spelling. Rewriting only
  `uCoords[8]` from
  `((2.0f * xCos) - pos.z)` to `((xCos + xCos) - pos.z)` likewise compiled
  but did not move the function: focused diff stayed `CURRENT (1808)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the visible
  drift remained in the earlier position-array schedule. Do not repeat this
  `uCoords[8]` additive-double UV spelling. Rewriting only `uCoords[8]` from
  `((2.0f * xCos) - pos.z)` to `(-pos.z + (2.0f * xCos))` also produced no
  useful movement: full verify failed with the known calculated CRCs
  `0x93D338FF/0x03D9C8FE`, the relinked focused score stayed
  `CURRENT (1808)`, and the diff remained in the same early position-array
  register/order family. Source was restored and final full verify passed. Do
  not repeat this `uCoords[8]` operand-order UV spelling.
  Rewriting only `uCoords[8]` from `((2.0f * xCos) - pos.z)` to
  `-(pos.z - (2.0f * xCos))` also missed: full verify failed with calculated
  CRCs `0x1FBC3A27/0x76D68348`, the relinked focused score worsened from
  baseline `CURRENT (1808)` to `CURRENT (2173)`, and the diff shifted the
  early negative-cosine carrier from target `$f18` to `$f16` while broadening
  the outer position-array and UV scheduling. Source was restored and final
  full verify passed. Do not repeat this `uCoords[8]` grouped-negated-
  difference UV spelling.
  Rewriting only `vCoords[8]` from `((2.0f * pos.x) + var_f16)` to
  `((pos.x + pos.x) + var_f16)` also produced no relinked focused movement:
  full verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, focused
  score stayed `CURRENT (1808)`, and the diff remained in the same early
  position-array register/order family. Source was restored and final full
  verify passed. Do not repeat this `vCoords[8]` additive-double UV spelling.
  Commuting only `vCoords[8]` from `((2.0f * pos.x) + var_f16)` to
  `(var_f16 + (2.0f * pos.x))` likewise produced no useful movement: full
  verify failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in
  the same early position-array register/order family. Source was restored
  and final full verify passed. Do not repeat this `vCoords[8]` operand-order
  UV spelling. Rewriting only `vCoords[8]` from
  `((2.0f * pos.x) + var_f16)` to `-((-2.0f * pos.x) - var_f16)` missed:
  full verify failed with calculated CRCs `0x0E197333/0x8457D082`, the
  relinked focused score worsened from baseline `CURRENT (1808)` to
  `CURRENT (3523)`, and the diff shifted global offsets/tail labels while
  leaving the early negative-cosine carrier drifted from target `$f18` to
  current `$f16`. Source was restored and final full verify passed. Do not
  repeat this `vCoords[8]` grouped-negated-sum UV spelling. Rewriting only
  `vCoords[8]` from `((2.0f * pos.x) + var_f16)` to
  `((2.0f * pos.x) - -var_f16)` also missed: full verify failed with
  calculated CRCs `0x1FC35A27/0x9CAAD958`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (2358)`, and the diff kept the
  early negative-cosine register drift while shifting later UV/global
  scheduling. Source was restored and final full verify passed. Do not repeat
  this `vCoords[8]` plus-negative UV spelling. Rewriting only
  `uCoords[5]` from
  `(-var_f14 - (2.0f * xCos))` to `(-var_f14 - (xCos + xCos))` also produced
  no relinked focused movement: full verify failed with the known calculated
  CRCs `0x93D338FF/0x03D9C8FE`, focused score stayed `CURRENT (1808)`, and the
  visible drift remained in the same early position-array register/order
  family. Source was restored and final full verify passed. Do not repeat this
  `uCoords[5]` additive-double UV spelling.
  Rewriting only `vCoords[0]` from `(var_f16 - var_f14)` to
  `(-var_f14 + var_f16)` missed badly: full verify failed with calculated CRCs
  `0x511B5709/0x02A6A46F`, the relinked focused score widened to
  `CURRENT (8605)`, and the diff shifted first-ring UV float-register
  allocation plus later global offsets instead of improving the early
  position-array schedule. Source was restored and final full verify passed.
  Do not repeat this `vCoords[0]` operand-order UV spelling. Rewriting only
  `vCoords[0]` from `(var_f16 - var_f14)` to `(var_f16 + -var_f14)` collapsed
  into the same bad family: full verify failed with calculated CRCs
  `0x511B5709/0x02A6A46F`, the relinked focused score worsened to
  `CURRENT (8605)`, and the diff shifted first-ring UV float-register
  allocation plus later global offsets. Source was restored and final full
  verify passed. Do not repeat this `vCoords[0]` plus-negative UV spelling.
  Rewriting only `uCoords[0]` from `(-var_f14 - xCos)` to
  `(-xCos - var_f14)` also missed: full verify failed with calculated CRCs
  `0x1FE45A27/0x304C5843`, the relinked focused score worsened to
  `CURRENT (2901)`, and the diff shifted first-ring UV float-register
  allocation plus later vertex/triangle scheduling instead of improving the
  early position-array schedule. Source was restored and final full verify
  passed. Do not repeat this `uCoords[0]` operand-order UV spelling. Rewriting
  only `uCoords[0]` from `(-var_f14 - xCos)` to `-(var_f14 + xCos)` also
  missed: full verify failed with calculated CRCs `0x1FD43A21/0x8649CFBF`,
  the relinked focused score worsened to `CURRENT (3086)`, and the diff moved
  the early negative-cosine carrier from target `$f18` to `$f16` while
  broadening first-ring UV/position-array scheduling drift. Source was
  restored and final full verify passed. Do not repeat this `uCoords[0]`
  negated-sum UV spelling.
  Rewriting only `vCoords[1]` from `(-var_f14 - var_f16)` to
  `(-var_f16 - var_f14)` also missed: full verify failed with calculated CRCs
  `0x1FE45A27/0x91F59B93`, the relinked focused score worsened to
  `CURRENT (2378)`, and the diff broadened first-ring UV/position-array
  register drift plus later vertex/triangle scheduling. Source was restored
  and final full verify passed. Do not repeat this `vCoords[1]` operand-order
  UV spelling. Rewriting only `vCoords[1]` from `(-var_f14 - var_f16)` to
  `-(var_f14 + var_f16)` also missed: full verify failed with calculated CRCs
  `0x93C3400B/0x33BE38AF`, the relinked focused score worsened to
  `CURRENT (2668)`, and the diff inserted an explicit add-then-negate in the
  first-ring UV path while broadening first-ring UV/position-array and later
  vertex scheduling drift. Source was restored and final full verify passed.
  Do not repeat this `vCoords[1]` negated-sum UV spelling.
  Rewriting only `uCoords[1]` from `(var_f14 - xCos)` to
  `(-xCos + var_f14)` also produced no useful movement: full verify failed
  with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array/UV register-order family. Source was restored and
  final full verify passed. Do not repeat this `uCoords[1]` operand-order UV
  spelling. Rewriting only `uCoords[1]` from `(var_f14 - xCos)` to
  `(var_f14 + -xCos)` also produced no useful movement: full verify failed
  with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array/UV register-order family. Source was restored and
  final full verify passed. Do not repeat this `uCoords[1]` plus-negative UV
  spelling.
  Rewriting only `vCoords[2]` from `(var_f14 - var_f16)` to
  `(-var_f16 + var_f14)` also produced no useful movement: full verify failed
  with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array/UV register-order family. Source was restored and
  final full verify passed. Do not repeat this `vCoords[2]` operand-order UV
  spelling. Rewriting only `vCoords[2]` from `(var_f14 - var_f16)` to
  `(var_f14 + -var_f16)` also produced no useful movement: full verify failed
  with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array/UV register-order family. Source was restored and
  final full verify passed. Do not repeat this `vCoords[2]` plus-negative UV
  spelling.
  Rewriting only `uCoords[2]` from `(var_f14 + var_f16)` to
  `(var_f16 + var_f14)` also missed: full verify failed with calculated CRCs
  `0x93E7D8FF/0x2762B6F5`, the relinked focused score worsened from
  `CURRENT (1808)` to `CURRENT (1818)`, and the diff remained in the early
  position-array/UV register-order family with later UV/register drift. Source
  was restored and final full verify passed. Do not repeat this `uCoords[2]`
  sum-order UV spelling. Rewriting only `uCoords[2]` as a subtract-negative
  expression (`var_f14 - -var_f16`) also missed badly: object-only focused diff
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x58EB09ED/0x9176C3B4`, and the relinked focused score worsened to
  `CURRENT (8613)`. The diff moved the early negative-cosine carrier from
  target `$f18` to `$f16`, shifted first/outer position-array scheduling, and
  moved global offsets/tail labels. Source was restored and final full verify
  passed; do not repeat this `uCoords[2]` subtract-negative UV spelling.
  Rewriting only `vCoords[3]` from `(var_f14 + var_f16)` to
  `(var_f16 + var_f14)` also produced no useful movement: full verify failed
  with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array/UV register-order family. Source was restored and
  final full verify passed. Do not repeat this `vCoords[3]` sum-order UV
  spelling.
  Rewriting only `uCoords[3]` from `(var_f16 - var_f14)` to
  `(-var_f14 + var_f16)` missed badly: full verify failed with calculated
  CRCs `0x511B5709/0xE130E098`, the relinked focused score widened to
  `CURRENT (8410)`, and the diff shifted first-ring UV float-register
  allocation plus later global offsets instead of improving the early
  position-array schedule. Source was restored and final full verify passed.
  Do not repeat this `uCoords[3]` operand-order UV spelling. Rewriting only
  `uCoords[3]` from `(var_f16 - var_f14)` to `(var_f16 + -var_f14)` collapsed
  into the same bad family: full verify failed with calculated CRCs
  `0x511B5709/0xE130E098`, the relinked focused score widened to
  `CURRENT (8410)`, and the diff shifted first-ring UV float-register
  allocation plus later global offsets. Source was restored and final full
  verify passed. Do not repeat this `uCoords[3]` plus-negative UV spelling.
  Making the center
  UV assignments explicit casts (`uCoords[4] = (s16) var_v0; vCoords[4] =
  (s16) var_v1`) produced no relinked movement: full verify failed with the
  known calculated CRCs `0x93D338FF/0x03D9C8FE`, focused score stayed
  `CURRENT (1808)`, and the diff remained in the same early negative-cosine
  plus position-array register-order family. Source was restored and final
  full verify passed. Do not repeat this center UV cast spelling.
  Rewriting only `vCoords[6]` from
  `((-(2.0f * var_f14)) - var_f16)` to
  `(-var_f16 - (2.0f * var_f14))` missed: full verify failed with calculated
  CRCs `0x93C818FF/0x5CB67605`, the relinked focused score worsened from
  `CURRENT (1808)` to `CURRENT (1818)`, and the diff remained in the early
  position-array register/order family with later UV/register drift. Source
  was restored and final full verify passed. Do not repeat this `vCoords[6]`
  operand-order UV spelling. Rewriting only `vCoords[6]` from
  `((-(2.0f * var_f14)) - var_f16)` to
  `((-(var_f14 + var_f14)) - var_f16)` also produced no useful movement: full
  verify failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in the
  same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this `vCoords[6]` additive-double UV
  spelling. Rewriting only `uCoords[5]` from
  `(-var_f14 - (2.0f * xCos))` to `(-(2.0f * xCos) - var_f14)` also missed:
  full verify failed with calculated CRCs `0x1FD484FD/0x7F2AE5E8`, the
  relinked focused score worsened from `CURRENT (1808)` to `CURRENT (4488)`,
  and the diff broadened the early position-array float-register/store
  schedule plus later vertex/triangle tail. Source was restored and final full
  verify passed. Do not repeat this `uCoords[5]` operand-order UV spelling.
  Rewriting only `uCoords[5]` from `(-var_f14 - (2.0f * xCos))` to
  `(-var_f14 - (xCos + xCos))` also produced no relinked focused movement:
  full verify failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`,
  focused score stayed `CURRENT (1808)`, and the diff stayed in the same early
  position-array register/order family. Source was restored and final full
  verify passed. Do not repeat this `uCoords[5]` additive-double UV spelling.
  Rewriting only `uCoords[5]` from `(-var_f14 - (2.0f * xCos))` to
  `(-var_f14 + -(2.0f * xCos))` also produced no relinked focused movement:
  full verify failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`,
  focused score stayed `CURRENT (1808)`, and the diff stayed in the same early
  position-array register/order family. Source was restored and final full
  verify passed. Do not repeat this `uCoords[5]` plus-negative UV spelling.
  Rewriting only `uCoords[5]` from `(-var_f14 - (2.0f * xCos))` to
  `-(var_f14 + (2.0f * xCos))` also missed: full verify failed with
  calculated CRCs `0x1FD484FF/0x9EF16F5D`, the relinked focused score worsened
  to `CURRENT (4588)`, and the diff kept the early negative-cosine register
  drift while broadening first/outer position-array and UV scheduling. Source
  was restored and final full verify passed. Do not repeat this `uCoords[5]`
  negated-sum UV spelling.
  Rewriting only `vCoords[5]` from `(var_f16 - (2.0f * var_f14))` to
  `(-(2.0f * var_f14) + var_f16)` also missed: full verify failed with
  calculated CRCs `0x93BFBAFF/0xBB8CD176`, the relinked focused score worsened
  to `CURRENT (2433)`, and the diff stayed in the early position-array
  register/order family with broader UV/register drift. Source was restored
  and final full verify passed. Do not repeat this `vCoords[5]` operand-order
  UV spelling. Rewriting only `vCoords[5]` from
  `(var_f16 - (2.0f * var_f14))` to `(var_f16 + -(2.0f * var_f14))` collapsed
  into the same miss: full verify failed with calculated CRCs
  `0x93BFBAFF/0xBB8CD176`, the relinked focused score stayed widened at
  `CURRENT (2433)`, and the diff inserted the same explicit negation/add
  sequence while leaving the early position-array register drift. Source was
  restored and final full verify passed. Do not repeat this `vCoords[5]`
  plus-negative UV spelling.
  Rewriting only `vCoords[5]` from `(var_f16 - (2.0f * var_f14))` to
  `-((2.0f * var_f14) - var_f16)` also missed: full verify failed with
  calculated CRCs `0x1FCF7A27/0x04B06374`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (2478)`, and the diff shifted the
  early position-array float-register/store schedule plus later UV/register
  drift. Source was restored and final full verify passed. Do not repeat this
  `vCoords[5]` grouped-negated-difference UV spelling.
  Rewriting only `vCoords[5]` from `(var_f16 - (2.0f * var_f14))` to
  `(var_f16 - (var_f14 + var_f14))` also produced no relinked focused
  movement: full verify failed with the known calculated CRCs
  `0x93D338FF/0x03D9C8FE`, focused score stayed `CURRENT (1808)`, and the diff
  stayed in the same early position-array register/order family. Source was
  restored and final full verify passed. Do not repeat this `vCoords[5]`
  additive-double UV spelling.
  Rewriting only `uCoords[6]` from `(var_f14 - (2.0f * xCos))` to
  `(-(2.0f * xCos) + var_f14)` also produced no useful movement: full verify
  failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array register/order family. Source was restored and final
  full verify passed. Do not repeat this `uCoords[6]` operand-order UV
  spelling.
  Rewriting only `uCoords[6]` from `(var_f14 - (2.0f * xCos))` to
  `(var_f14 - (xCos + xCos))` also produced no useful movement: full verify
  failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array register/order family. Source was restored and final
  full verify passed. Do not repeat this `uCoords[6]` additive-double UV
  spelling. Rewriting only `uCoords[6]` from `(var_f14 - (2.0f * xCos))` to
  `(var_f14 + -(2.0f * xCos))` also produced no useful movement: full verify
  failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the relinked
  focused score stayed `CURRENT (1808)`, and the diff remained in the same
  early position-array register/order family. Source was restored and final
  full verify passed. Do not repeat this `uCoords[6]` plus-negative UV
  spelling.
  Rewriting only `uCoords[6]` from `(var_f14 - (2.0f * xCos))` to
  `-((2.0f * xCos) - var_f14)` also missed: full verify failed with
  calculated CRCs `0x1FC45A27/0x507B3763`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (2273)`, and the diff shifted the
  early position-array float-register/store schedule plus later UV/register
  drift. Source was restored and final full verify passed. Do not repeat this
  `uCoords[6]` grouped-negated-difference UV spelling.
  Rewriting the final triangle population loop as a two-triangle unroll
  (`for (i = 0; i < 8; i += 2)` with six `D_800DC92C` index reads per
  iteration) also missed: full verify failed with calculated CRCs
  `0x938938FF/0x32389065`, the relinked focused score worsened from baseline
  `CURRENT (1808)` to `CURRENT (1873)`, and the diff still began in the same
  early position-array register/order family before reaching the tail-loop
  scheduling. Source was restored and final full verify passed. Do not repeat
  this final triangle two-at-a-time unroll spelling.
  Rewriting only the final triangle index advances from `var_v0_3 += 1` to
  `var_v0_3++` also missed: full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, the relinked focused score stayed
  `CURRENT (1808)`, and the diff remained in the same early
  negative-cosine/position-array register schedule. Source was restored and
  final full verify passed. Do not repeat this final triangle postincrement
  spelling.
  Reordering only the final global pointer stores from `gTrackVtxPtr = verts;
  gTrackTriPtr = tris;` to `gTrackTriPtr = tris; gTrackVtxPtr = verts;` also
  missed: full verify failed with calculated CRCs `0x93D338FF/0x3EBCCB8F`, and
  relinked `./diff.sh trackbg_render_flashy` worsened from promoted baseline
  `CURRENT (1808)` to `CURRENT (1846)`. Source was restored and final full
  verify passed. Do not repeat this final global pointer store-order spelling.
  Moving the fallback color initialization to set `var_a3 = -0x100` before
  `var_a2 = -1` also missed: full verify failed with calculated CRCs
  `0x93D338FF/0xBC40711E`, and relinked `./diff.sh trackbg_render_flashy`
  worsened from promoted baseline `CURRENT (1808)` to `CURRENT (2088)`.
  Source was restored and final full verify passed. Do not repeat this color
  fallback initialization-order spelling.
  Rewriting only the fallback color mask literal from `var_a3 = -0x100` to
  `var_a3 = ~0xFF` also missed as a no-movement family: full verify failed
  with calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed
  at promoted baseline `CURRENT (1808)` with the same early negative-cosine
  register drift and position/UV scheduling mismatch. Source was restored,
  final full verify passed, and `./score.sh -s` remained 97.30%; do not repeat
  this color fallback `~0xFF` mask literal spelling.
  Flipping
  only `xPositions[2]` to `(xSin * 1280.0f) + scaledXCos` compiled but left the
  linked focused score unchanged at `CURRENT (1808)`. Replacing only
  `xPositions[2]` with `scaledXCos + scaledXSin` compiled but worsened the
  focused score to `CURRENT (12021)` and changed the frame to `0x150`.
  Replacing only `zPositions[0]` with `-scaledXCos + scaledXSin` also missed:
  full verify failed with calculated CRCs `0x218F9FFA/0x18F4A6D6`, the
  relinked focused score worsened to `CURRENT (13471)`, and the frame shrank
  to `0x150` with broad early position-array schedule drift. Source was
  restored and final full verify passed; do not repeat this single-site z0
  scaled-sine spelling. Replacing only `xPositions[0]` with
  `-scaledXCos - scaledXSin` reproduced the same miss: full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`, relinked focused score
  `CURRENT (13471)`, and the same `0x150` frame plus early position-array
  reshuffle. Source was restored and final full verify passed; do not repeat
  this single-site x0 scaled-sine spelling.
  Replacing the outer-ring `2.0f * scaledXCos/scaledXSin` terms with additive
  doubles (`scaledXCos + scaledXCos`, `scaledXSin + scaledXSin`) compiled but
  left the uncompressed linked diff at `CURRENT (1808)` and a promoted full
  build failed verify with CRC `0x93D338FF/0x03D9C8FE`. Routing only the
  doubled cosine term through existing `pad_sp108`
  (`pad_sp108 = scaledXCos + scaledXCos`, then using it for the outer
  `zPositions[5-8]`) also produced no focused movement from the promoted
  baseline: relinked focused diff stayed `CURRENT (1808)` and full verify
  failed with the same calculated CRCs `0x93D338FF/0x03D9C8FE`; source was
  restored and final full verify passed. Treat this as the same additive-double
  family and do not repeat it. Rewriting only `zPositions[5]` as a
  left-associative subtract chain (`scaledXSin - scaledXCos - scaledXCos`)
  also missed badly: relinked focused score worsened from `CURRENT (1808)` to
  `CURRENT (4558)`, full verify failed with calculated CRCs
  `0xD68DF16F/0x5A429915`, and the outer-ring position store schedule shifted
  much earlier. Do not repeat this single-site z5 subtract-chain spelling.
  Rewriting only `zPositions[5]` as a plus-after-negated-double expression
  (`-(2.0f * scaledXCos) + scaledXSin`) also missed: full verify failed with
  calculated CRCs `0x53DC5E0F/0x8B102C25`, the relinked focused score worsened
  to `CURRENT (2831)`, and the early position-array schedule shifted instead
  of matching target. The equivalent plus-negative spelling
  (`scaledXSin + -(2.0f * scaledXCos)`) compiled into the same miss family:
  object-only focused diff printed stale `CURRENT (0)`, full verify failed
  with the same calculated CRCs `0x53DC5E0F/0x8B102C25`, and the relinked
  focused score again worsened to `CURRENT (2831)`. Source was restored and
  final full verify passed. Do not repeat either single-site z5
  plus-negated-double spelling. Rewriting only
  `zPositions[5]` as a grouped negated-difference expression
  (`-((2.0f * scaledXCos) - scaledXSin)`) also missed: full verify failed with
  calculated CRCs `0x9C75F625/0x32EDAC40`, the relinked focused score worsened
  to `CURRENT (5055)`, and the diff shifted the early negative-cosine family
  plus first/outer position-array scheduling into broader global-offset churn.
  Source was restored and final full verify passed. Do not repeat this
  single-site z5 grouped negated-difference spelling.
  Adding a named
  `negScaledXCos` temporary for the first/outer position expressions also
  compiled but left the uncompressed linked diff at `CURRENT (1808)`. Swapping
  the `scaledXSin`/`scaledXCos` declaration order produced no object change,
  and `register f32 scaledXSin` / `register f32 scaledXCos` hints also produced
  no object change. Rewriting only `zPositions[3]` as
  `scaledXCos + (xSin * 1280.0f)` compiled but inserted an extra
  `swc1 $f0, 0x110(sp)`, shifted later scheduling/global offsets, worsened the
  linked score to `CURRENT (5579)`, and failed promoted full verify with CRC
  `0xF82B92BE/0x5DCC04AE`. Moving only
  `zPositions[3] = scaledXSin + scaledXCos` also produced no relinked
  movement: full verify failed with the promoted-baseline CRCs
  `0x93D338FF/0x03D9C8FE`, focused score stayed `CURRENT (1808)`, and the
  early negative-cosine carrier remained current `$f16` instead of target
  `$f18`. Source was restored and final full verify passed; do not repeat this
  single-site z3 positive-sum operand-order spelling. Moving only
  `xPositions[5] = -scaledXCos - (2.0f * scaledXSin)` before `zPositions[5]`
  compiled but worsened the uncompressed linked diff to `CURRENT (2408)`.
  Adding `register f32 negScaledXCos` and using it for the first/outer negative
  cosine expressions compiled but worsened the uncompressed linked diff to
  `CURRENT (2769)` and changed the promoted full-verify CRC to
  `0xDC79FC91/0xA51F89F4`. A first-four position-store order probe that grouped
  equivalent target temps compiled and initially printed a misleading
  object-only `CURRENT (0)`, but the promoted full build failed verify with CRC
  `0x8E7F39EA/0xD7399E4A` and the relinked uncompressed focused diff worsened
  to `CURRENT (4390)` with a smaller `0x150` frame and shifted early
  position-array stack slots. Replacing only `xPositions[3]` with
  `-scaledXCos + scaledXSin` compiled, but the promoted full build failed
  verify and the relinked focused diff worsened to `CURRENT (9344)` /
  `CURRENT (12161)`, reshuffling the first-four position stores and shrinking
  the frame to `0x150`; do not repeat this single-site scaled-sine rewrite.
  Replacing only `zPositions[0]` with `-scaledXCos + scaledXSin` also compiled
  into the bad single-site scaled-sine family: the frame shrank to `0x150`,
  relinked focused diff worsened to `CURRENT (13376)`, and full verify failed
  with calculated CRCs `0x218F9FFA/0x18F4A6D6`; do not repeat this z0 spelling.
  Routing the duplicated first-ring `-scaledXCos - (xSin * 1280.0f)` value
  through the existing `var_f16` local for `xPositions[0]` and `zPositions[1]`
  also compiled into the same bad family: frame `0x150`, relinked focused diff
  `CURRENT (13376)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and the final full verify
  passed, so keep the function active but do not repeat this first-ring
  existing-`var_f16` carrier.
  A
  compressed `-s --compress-matching` focused diff can misleadingly print
  `CURRENT (0)` for this function; rely on the uncompressed linked diff and the
  full verify gate before accepting anything. Later no-object-movement probes:
  spelling only `xPositions[2]` as `(xCos * 1280.0f) + scaledXSin`, moving only
  `xPositions[3]` before `xPositions[2]`, and adding `register` to the existing
  `var_f16` local all compiled but left the uncompressed focused diff unchanged
  at `CURRENT (1808)`; do not repeat those simple first-ring spelling/allocation
  hints. After restoring the guard, `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  returned `Verify: OK`. Routing only the doubled outer-ring sine term through
  the existing `var_f16` local (`var_f16 = scaledXSin + scaledXSin`, then using
  `var_f16` for the `xPositions[5-8]` sine offsets) compiled but worsened the
  relinked focused score to `CURRENT (4506)`, shifted the early position-array
  schedule, and failed full verify with calculated CRCs
  `0xDC65D929/0xA0527CE0`; do not repeat this existing-`var_f16`
  double-sine carrier. Routing only the duplicated first-ring positive
  `scaledXCos + scaledXSin` value through existing `pad_sp108` for
  `xPositions[2]` and `zPositions[3]` also collapsed into the bad frame-shrink
  family: frame `0x150`, relinked focused score `CURRENT (13456)`, and full
  verify failed with calculated CRCs `0x218EDFFA/0xDD1EF586`. Do not repeat
  this first-ring existing-`pad_sp108` positive-sum carrier. Rewriting the
  paired first-ring `-scaledXCos + scaledXSin` sites together
  (`zPositions[0]` and `xPositions[3]`) also fell into the same bad
  single-site scaled-sine family: frame `0x150`, relinked focused score
  `CURRENT (13596)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and final full verify passed.
  Do not repeat this paired first-ring scaled-sine rewrite. Routing that same
  paired `-scaledXCos + (xSin * 1280.0f)` value through the existing
  `pad_sp108` local for `zPositions[0]` and `xPositions[3]` also collapsed
  into the same bad first-ring family: frame `0x150`, relinked focused score
  `CURRENT (13376)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and final full verify passed.
  Do not repeat this `pad_sp108` z0/x3 carrier either.
  Rewriting only `xPositions[0]` from
  `-scaledXCos - (xSin * 1280.0f)` to `-scaledXCos - scaledXSin` also
  collapsed into the same bad first-ring scaled-sine family: frame `0x150`,
  relinked focused score `CURRENT (13471)`, and full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`; source was restored and final full
  verify passed. Do not repeat this single-site x0 scaled-sine rewrite.
  Rewriting only `zPositions[1]` from
  `-scaledXCos - (xSin * 1280.0f)` to `-scaledXCos - scaledXSin` also
  collapsed into the same bad first-ring scaled-sine family: frame `0x150`,
  relinked focused score `CURRENT (13821)`, and full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`; source was restored and final full
  verify passed. Do not repeat this single-site z1 scaled-sine rewrite.
  Rewriting only `xPositions[1]` from
  `scaledXCos - (xSin * 1280.0f)` to `scaledXCos - scaledXSin` also collapsed
  into the same bad first-ring scaled-sine family: frame `0x150`, relinked
  focused score `CURRENT (13471)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and final full verify passed.
  Do not repeat this single-site x1 scaled-sine rewrite.
  Rewriting only `zPositions[2]` from
  `scaledXCos - (xSin * 1280.0f)` to `scaledXCos - scaledXSin` also collapsed
  into the same bad first-ring scaled-sine family: frame `0x150`, relinked
  focused score `CURRENT (13471)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and final full verify passed.
  Do not repeat this single-site z2 scaled-sine rewrite.
  Routing the paired `scaledXCos - (xSin * 1280.0f)` value through existing
  `pad_sp108` for `xPositions[1]` and `zPositions[2]` likewise compiled but
  collapsed into the same bad first-ring frame-shrink family: frame `0x150`,
  relinked focused score `CURRENT (13376)`, and full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`; source was restored and final full
  verify passed. Do not repeat this `pad_sp108` x1/z2 carrier. Reordering the
  first four position assignments to pair target-equivalent values
  (`xPositions[0]` with `zPositions[1]`, `zPositions[0]` with `xPositions[1]`,
  `xPositions[2]` with `zPositions[3]`, and `zPositions[2]` with
  `xPositions[3]`) compiled but regressed the relinked focused score to
  `CURRENT (4034)`, failed full verify with calculated CRCs
  `0x93E03BFF/0x3B5D2DFE`, and shifted the early position-array float-register
  family. Do not repeat this first-ring store-order grouping. Routing the
  duplicated first-ring `-scaledXCos - (xSin * 1280.0f)` value through the
  unused existing `pad_sp100` local for `xPositions[0]` and `zPositions[1]`
  also compiled into the bad frame-shrink family: frame `0x150`, relinked
  focused score `CURRENT (13706)`, and full verify failed with calculated CRCs
  `0x218F9FFA/0x18F4A6D6`; source was restored and final full verify passed.
  Do not repeat this unused-`pad_sp100` x0/z1 carrier. Moving only
  `zPositions[1] = -scaledXCos - (xSin * 1280.0f)` immediately after
  `xPositions[0]` to pair the duplicated first-ring negative sum also missed:
  the frame stayed `0x158`, but relinked focused score worsened to
  `CURRENT (2938)`, full verify failed with calculated CRCs
  `0x93D342FF/0x71E01805`, and the diff shifted the early position-array
  float-register/store schedule instead of matching the target. Source was
  restored and final full verify passed. Do not repeat this single-pair
  x0/z1 store-order probe. Replacing every remaining first-ring
  `(xSin * 1280.0f)` term in `xPositions[0..3]` and `zPositions[0..2]` with
  the existing `scaledXSin` carrier also missed: it widened the frame to
  `0x168`, relinked focused score worsened to `CURRENT (13466)`, and full
  verify failed with calculated CRCs `0x8310DF9D/0x3EA48C03`. Source was
  restored and final full verify passed. Do not repeat this all-first-ring
  `scaledXSin` rewrite. Routing the paired first-ring
  `-scaledXCos + (xSin * 1280.0f)` value through the existing `var_f16` local
  for `zPositions[0]` and `xPositions[3]` likewise missed: it shrank the frame
  to `0x150`, relinked focused score worsened to `CURRENT (13471)`, and full
  verify failed with calculated CRCs `0x218F9FFA/0x18F4A6D6`. Source was
  restored and final full verify passed. Do not repeat this existing-`var_f16`
  z0/x3 carrier. Routing the paired first-ring positive
  `scaledXCos + (xSin * 1280.0f)` value through the existing `var_f16` local
  for `xPositions[2]` and `zPositions[3]` also missed: relinked focused score
  stayed `CURRENT (1808)`, full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and the diff stayed in the known additive-double
  register-order family. Source was restored and final full verify passed. Do
  not repeat this existing-`var_f16` positive x2/z3 carrier. Routing the same
  paired first-ring positive `scaledXCos + (xSin * 1280.0f)` value through the
  unused existing `pad_sp100` local for `xPositions[2]` and `zPositions[3]`
  also produced no useful movement: relinked focused score stayed
  `CURRENT (1808)`, full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and the diff stayed in the same additive-double
  register-order family. Source was restored and final full verify passed. Do
  not repeat this unused-`pad_sp100` positive x2/z3 carrier. Moving only
  `zPositions[3] = scaledXCos + scaledXSin` immediately after `xPositions[2]`
  to pair the duplicated first-ring positive value also missed: the frame
  stayed `0x158`, but relinked focused score worsened to `CURRENT (4433)`,
  full verify failed with calculated CRCs `0xDC9ABB91/0xDA2977C2`, and the diff
  shifted the early first-ring/outer-ring float schedule. Source was restored
  and final full verify passed. Do not repeat this single-pair x2/z3
  store-order probe. An exact first-ring target-store-order probe
  (`x0`, `z1`, `x1`, `z2`, `z0`, `x3`, `x2`, `z3`) without replacing the
  repeated `(xSin * 1280.0f)` terms also missed: the frame shrank to `0x150`,
  relinked focused score worsened to `CURRENT (4432)`, full verify failed with
  calculated CRCs `0x8E7C21EA/0x33457650`, and the diff shifted the early
  position-array schedule into a different `$f16`/`$f18` and stack-slot family.
  Source was restored and final full verify passed. Do not repeat this exact
  first-ring target-order probe. Rewriting only `xPositions[8]` from
  `-scaledXCos + (2.0f * scaledXSin)` to
  `(2.0f * scaledXSin) - scaledXCos` also missed: it widened the frame from
  target `0x158` to `0x160`, failed full verify with calculated CRCs
  `0xC59A4971/0x72BB7708`, and the relinked focused score worsened to
  `CURRENT (7441)` with broad first/outer position-array stack-slot/register
  churn. Source was restored and final full verify passed. Do not repeat this
  single-site x8 operand-order spelling. Rewriting only `xPositions[8]` from
  `-scaledXCos + (2.0f * scaledXSin)` to
  `-(scaledXCos - (2.0f * scaledXSin))` also missed: full verify failed with
  calculated CRCs `0x9C5E326B/0x55A97A82`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (3074)`, and the grouped
  negated-difference shape broadened first/outer position-array scheduling plus
  global-offset drift while preserving the target-sized `0x158` frame. Source
  was restored and final full verify passed. Do not repeat this single-site x8
  grouped-negated-difference spelling. Rewriting only `xPositions[8]` from
  `-scaledXCos + (2.0f * scaledXSin)` to
  `-scaledXCos + (scaledXSin * 2.0f)` also produced no useful movement:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, and the
  relinked focused score stayed `CURRENT (1808)` with the same early
  position-array register/order family. Source was restored and final full
  verify passed. Do not repeat this single-site x8 multiply-order spelling.
  Commuting only `zPositions[8]` from
  `(2.0f * scaledXCos) + scaledXSin` to
  `scaledXSin + (2.0f * scaledXCos)` produced no useful movement: full verify
  failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in the
  same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site z8 operand-order
  spelling. Rewriting only `zPositions[8]` from
  `(2.0f * scaledXCos) + scaledXSin` to
  `(2.0f * scaledXCos) - -scaledXSin` also missed: full verify failed with
  calculated CRCs `0x1FCC9227/0x382130AA`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (2651)`, and the diff inserted a
  negated-sine subtraction into the outer-ring schedule while preserving the
  target-sized `0x158` frame. Source was restored and final full verify passed.
  Do not repeat this single-site z8 minus-negative spelling. Rewriting only
  `zPositions[8]` from
  `(2.0f * scaledXCos) + scaledXSin` to
  `(scaledXCos * 2.0f) + scaledXSin` also produced no useful movement: full
  verify failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in the
  same early negative-cosine/outer-ring register-order family. Source was
  restored and final full verify passed. Do not repeat this single-site z8
  multiply-order spelling. Rewriting only
  `zPositions[7]` from
  `(2.0f * scaledXCos) - scaledXSin` to
  `(2.0f * scaledXCos) + -scaledXSin` also produced no movement: full verify
  failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in the
  same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site z7 plus-negative
  spelling. Rewriting only `zPositions[7]` from
  `(2.0f * scaledXCos) - scaledXSin` to
  `-scaledXSin + (2.0f * scaledXCos)` also produced no useful movement: full
  verify failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`,
  the relinked focused score stayed `CURRENT (1808)`, and the diff remained in
  the same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site z7 operand-order
  spelling. Rewriting only `zPositions[7]` as a grouped negated difference
  (`-((scaledXSin) - (2.0f * scaledXCos))`) also missed: object-only focused
  diff printed stale `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x9C72948D/0x12AA7789`, the relinked focused score worsened to
  `CURRENT (4289)`, and the diff shifted the early first/outer
  position-array register schedule while preserving the target-sized frame.
  Source was restored and final full verify passed. Do not repeat this
  single-site z7 grouped-negated-difference spelling. Rewriting only
  `zPositions[7]` from
  `(2.0f * scaledXCos) - scaledXSin` to
  `(scaledXCos * 2.0f) - scaledXSin` also produced no relinked focused
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, relinked
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/outer-ring register-order family.
  Source was restored and final full verify passed; do not repeat this
  single-site z7 multiply-order spelling. Commuting only
  `xPositions[7]` from
  `scaledXCos + (2.0f * scaledXSin)` to
  `(2.0f * scaledXSin) + scaledXCos` also produced no movement: full verify
  failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`, the
  relinked focused score stayed `CURRENT (1808)`, and the diff remained in the
  same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site x7 operand-order
  spelling. Rewriting only `xPositions[7]` from
  `scaledXCos + (2.0f * scaledXSin)` to
  `scaledXCos - -(2.0f * scaledXSin)` also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x1FBBB527/0xBCB1313B`, and the relinked focused score worsened to
  `CURRENT (2503)`. The diff kept the `0x158` frame but shifted the early
  negative-cosine register family plus first/outer position-array and later
  UV/vertex scheduling. Source was restored and final full verify passed. Do
  not repeat this single-site x7 minus-negative spelling. Rewriting only
  `xPositions[7]` from
  `scaledXCos + (2.0f * scaledXSin)` to
  `scaledXCos + (scaledXSin * 2.0f)` also produced no relinked focused
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, relinked
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/outer-ring register-order family.
  Source was restored and final full verify passed; do not repeat this
  single-site x7 multiply-order spelling. Rewriting only
  `xPositions[5]` from
  `-scaledXCos - (2.0f * scaledXSin)` to
  `-(2.0f * scaledXSin) - scaledXCos` also missed: it widened the frame from
  target `0x158` to `0x160`, failed full verify with calculated CRCs
  `0x499D7E20/0x23306384`, and the relinked focused score worsened to
  `CURRENT (8018)` with broad first/outer position-array stack-slot/register
  churn. Source was restored and final full verify passed. Do not repeat this
  single-site x5 operand-order spelling.
  Rewriting only `xPositions[5]` from
  `-scaledXCos - (2.0f * scaledXSin)` to
  `-(scaledXCos + (2.0f * scaledXSin))` also missed: full verify failed with
  calculated CRCs `0x9C863875/0xD9AD96ED`, the relinked focused score worsened
  from baseline `CURRENT (1808)` to `CURRENT (3503)`, and the grouped negated
  sum shifted the early first/outer position-array schedule while preserving
  the target-sized `0x158` frame. Source was restored and final full verify
  passed. Do not repeat this single-site x5 grouped-negated-sum spelling.
  Rewriting only `xPositions[5]` from
  `-scaledXCos - (2.0f * scaledXSin)` to
  `-scaledXCos - (scaledXSin * 2.0f)` also produced no relinked focused
  movement: full verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`,
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/position-array register-order
  family. Source was restored and final full verify passed; do not repeat this
  single-site x5 multiply-order spelling. Rewriting only `zPositions[5]` from
  `scaledXSin - (2.0f * scaledXCos)` to
  `scaledXSin - (scaledXCos * 2.0f)` also produced no relinked focused
  movement: full verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`,
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/outer-ring register-order family.
  Source was restored and final full verify passed; do not repeat this
  single-site z5 multiply-order spelling.
  Rewriting only `zPositions[6]` from
  `-(2.0f * scaledXCos) - scaledXSin` to
  `-(scaledXCos * 2.0f) - scaledXSin` also produced no relinked focused
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, relinked
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/outer-ring register-order family.
  Source was restored and final full verify passed; do not repeat this
  single-site z6 multiply-order spelling.
  Rewriting only `xPositions[6]` from
  `scaledXCos - (2.0f * scaledXSin)` to
  `-(2.0f * scaledXSin) + scaledXCos` also produced no useful movement: full
  verify failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`,
  the relinked focused score stayed `CURRENT (1808)`, and the diff remained in
  the same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site x6 operand-order
  spelling. Rewriting only `xPositions[6]` from
  `scaledXCos - (2.0f * scaledXSin)` to
  `scaledXCos + -(2.0f * scaledXSin)` also produced no useful movement: full
  verify failed with the known additive-double CRCs `0x93D338FF/0x03D9C8FE`,
  the relinked focused score stayed `CURRENT (1808)`, and the diff remained in
  the same early position-array register/order family. Source was restored and
  final full verify passed. Do not repeat this single-site x6 plus-negative
  spelling. Rewriting only `xPositions[6]` from
  `scaledXCos - (2.0f * scaledXSin)` to
  `scaledXCos - (scaledXSin * 2.0f)` also produced no relinked focused
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, relinked
  `./diff.sh trackbg_render_flashy` stayed `CURRENT (1808)`, and the diff
  remained in the same early negative-cosine/outer-ring register-order family.
  Source was restored and final full verify passed; do not repeat this
  single-site x6 multiply-order spelling. Rewriting only `xPositions[6]` as a
  grouped negated difference
  (`-((2.0f * scaledXSin) - scaledXCos)`) missed badly: full verify failed
  with calculated CRCs `0x701BB399/0xEE9EA39F`, the relinked focused score
  worsened from baseline `CURRENT (1808)` to `CURRENT (4468)`, and the diff
  moved the early negative-cosine carrier from target `$f18` to `$f16` while
  broadening first/outer position-array scheduling. Source was restored and
  final full verify passed. Do not repeat this single-site x6 grouped-negated
  difference spelling. Rewriting only `zPositions[6]` from
  `-(2.0f * scaledXCos) - scaledXSin` to
  `-scaledXSin - (2.0f * scaledXCos)` also missed: full verify failed with
  calculated CRCs `0x93D438FF/0x1A841372`, the relinked focused score worsened
  slightly to `CURRENT (1813)`, and the diff stayed in the same early
  position-array register/order family. Source was restored and final full
  verify passed. Do not repeat this single-site z6 operand-order spelling.
  Rewriting only `zPositions[6]` from
  `-(2.0f * scaledXCos) - scaledXSin` to
  `-((2.0f * scaledXCos) + scaledXSin)` also missed: full verify failed with
  calculated CRCs `0x53BD5BC9/0x0C6BD3FB`, the relinked focused score worsened
  to `CURRENT (3887)`, and the diff kept the early negative-cosine register
  mismatch while broadening first/outer position-array and UV scheduling.
  Source was restored and final full verify passed. Do not repeat this
  single-site z6 negated-sum spelling.
  Removing the fake duplicate
  `var_a2 = texHeader->height * 16 * gCurrentLevelHeader2->unkA1` assignment
  before the UV block compiled but badly widened the relinked focused score to
  `CURRENT (11477)`, failed full verify with calculated CRCs
  `0xC5B710C5/0x71187E4F`, changed the early negative-cosine register family
  from target `$f18` to `$f16`, and reshuffled the first/outer position-array
  stores. Source was restored and final full verify passed. Do not remove this
  fake `var_a2` assignment. Collapsing the UV scale setup from the two-step
  `var_f14 = 1280.0f; var_f14 *= 0.25f` into `var_f14 = 320.0f` also missed:
  full verify failed with calculated CRCs `0x027233EC/0x55516330`, relinked
  `./diff.sh trackbg_render_flashy` worsened from the promoted baseline
  `CURRENT (1808)` to `CURRENT (3510)`, and the diff shifted the scale
  setup plus first/outer position-array schedule instead of matching target.
  Source was restored and final full verify passed; do not repeat this
  collapsed `var_f14` UV-scale spelling. Reversing the two-step UV scale
  multiplier order (`var_f14 = 0.25f; var_f14 *= 1280.0f`) also missed: full
  verify failed with calculated CRCs `0xCBC5BBA5/0xBDF6EEC6`, and relinked
  `./diff.sh trackbg_render_flashy` worsened from promoted baseline
  `CURRENT (1808)` to `CURRENT (2028)`. The diff shifted the early
  negative-cosine FPR from target `$f18` toward `$f16`, moved scale setup, and
  broadened first/outer position-array scheduling. Source was restored and
  final full verify passed; do not repeat this UV scale multiplier-order
  spelling.
  Routing the doubled outer-ring cosine term through the existing unused
  `pad_sp100` local (`pad_sp100 = scaledXCos + scaledXCos`, then using it for
  `zPositions[5..8]`) also produced no useful movement: promoted full verify
  failed with the known calculated CRCs `0x93D338FF/0x03D9C8FE`, relinked
  focused score stayed `CURRENT (1808)`, and the diff stayed in the same
  early negative-cosine/doubled-cosine register family. Source was restored
  and final full verify passed. Do not repeat this `pad_sp100` doubled-cosine
  carrier.
  Routing the first/outer negative scaled-cosine terms through existing
  `pad_sp100` as a negative-cosine carrier (`pad_sp100 = -scaledXCos`, then
  using it for `xPositions[0]`, `zPositions[0]`, `zPositions[1]`,
  `xPositions[3]`, `xPositions[5]`, and `xPositions[8]`) also missed:
  promoted full verify failed with calculated CRCs `0xDC79F591/0x31DBA03C`,
  relinked focused score worsened to `CURRENT (2893)`, and the diff shifted
  global offsets and later scheduling while keeping the early negative-cosine
  register mismatch. Source was restored and final full verify passed. Do not
  repeat this existing-`pad_sp100` negative-cosine carrier. Routing the same
  first/outer negative scaled-cosine terms through existing `pad_sp108` as the
  carrier also missed: object-only `./diff.sh trackbg_render_flashy` first
  printed stale `CURRENT (0)`, but full verify failed with the same calculated
  CRCs `0xDC79F591/0x31DBA03C`; the relinked focused score worsened to
  `CURRENT (3108)`, moved the early negative-cosine carrier from target `$f18`
  to `$f16`, and shifted outer position-array/global-offset scheduling. Source
  was restored and final full verify passed. Do not repeat this existing
  `pad_sp108` negative-cosine carrier. Routing the paired first-ring
  `scaledXCos - (xSin * 1280.0f)` value through the unused existing
  `pad_sp100` local for `xPositions[1]` and `zPositions[2]` also collapsed
  into the bad frame-shrink family: object-only `./diff.sh
  trackbg_render_flashy` first printed stale `CURRENT (0)`, but promoted full
  verify failed with calculated CRCs `0x218F9FFA/0x18F4A6D6`; the relinked
  focused score worsened to `CURRENT (13821)`, the frame shrank to `0x150`,
  and the first/outer position-array stack schedule shifted broadly. Source
  was restored and final full verify passed. Do not repeat this unused
  `pad_sp100` x1/z2 carrier. Routing the paired first-ring
  `-scaledXCos + (xSin * 1280.0f)` value through the unused existing
  `pad_sp100` local for `zPositions[0]` and `xPositions[3]` missed in the
  same frame-shrink family: object-only `./diff.sh trackbg_render_flashy`
  initially printed stale `CURRENT (0)`, promoted full verify failed with
  calculated CRCs `0x218F9FFA/0x18F4A6D6`, and relinked focused diff reported
  `CURRENT (13821)` with the frame shrunk to `0x150`. Source was restored and
  final full verify passed. Do not repeat this unused `pad_sp100` z0/x3
  carrier. A combined first-ring plus outer-ring target-store-order probe also
  missed: promoting `trackbg_render_flashy`, ordering the first-ring stores as
  `x0/z1/x1/z2/z0/x3/x2/z3`, and ordering the first outer-ring stores as
  `x5/z5/z6/x6` failed full verify with calculated CRCs
  `0x8EAD21EA/0x274096CC`. The relinked focused diff worsened to
  `CURRENT (3810)`, shrank the frame from target `0x158` to `0x150`, moved the
  early negative-cosine carrier from target `$f18` to `$f16`, and broadly
  shifted first/outer position-array plus later UV/global scheduling. Source
  was restored and final full verify passed; do not repeat this combined
  first/outer target-store-order probe.
  A final vertex `vertY` explicit-cast probe (`vertY = (s16)
  (camera->trans.y_position + 192.0f)`) produced no useful movement:
  object-only `./diff.sh trackbg_render_flashy --no-pager` first printed stale
  `CURRENT (0)`, promoted full verify failed with calculated CRCs
  `0x93D338FF/0x03D9C8FE`, and relinked focused score stayed
  `CURRENT (1808)`. The diff remained in the same early
  negative-cosine/doubled-cosine register drift family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and
  `./score.sh -s` remained 97.30%. Do not repeat this final vertex `vertY`
  explicit-cast spelling.
- `func_8002B0F4` is active, not parked. A declaration-only `register s32
  XInInt` / `register s32 ZInInt` hint in the current promoted source missed:
  relinked focused score worsened to `CURRENT (2860)`, full verify failed with
  calculated CRCs `0x7856718A/0x66208CAA`, and the same unwanted
  `gCurrentLevelModel` spill appeared at `0x60(sp)`. Source was restored and
  final full verify passed; do not repeat this X/Z integer register-hint
  probe. Adding `register` to the `xIn`/`zIn` float parameters also missed:
  it recreated the target `$f20`/`$f22` prologue save/use shape, but full
  verify failed with calculated CRCs `0x7856718A/0x66208CAA`, the relinked
  focused score worsened to `CURRENT (2860)`, and the same unwanted early
  `gCurrentLevelModel` spill appeared at `0x60(sp)` before the segment loop.
  Source was restored and final full verify passed; do not repeat this float
  parameter register-hint probe without a separate fix for the model-spill
  family. Adding `register` only to the `levelSegmentIndex` parameter also
  missed in the same family: full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, relinked focused score was `CURRENT (2860)`, and
  the unwanted early `gCurrentLevelModel` spill appeared at `0x60(sp)` while
  the target-like `$f20`/`$f22` prologue remained. Source was restored and
  final full verify passed; do not repeat this segment-index register-parameter
  hint. Combining that float-parameter register hint with the better
  plain `pad3`-removed stack layout also missed: the target `$f20`/`$f22`
  prologue remained, but full verify failed with the plain `pad3`-removal CRC
  family `0x785671AA/0x0D6F6A4A`, the relinked focused score was
  `CURRENT (2868)`, and the unwanted early `gCurrentLevelModel` spill moved to
  `0x64(sp)`. Source was restored and final full verify passed; do not repeat
  this combined float-register plus `pad3`-removal shape. Promoting the
  existing C compiles, but
  linked focused diff scores `CURRENT (2780)` with broad drift starting around
  `gCurrentLevelModel` hoisting/caching and cascading through the grid loops.
  Rejected probes: inserting an empty `if (gCurrentLevelModel) {}` before the
  segment/bounding-box pointer setup worsened the linked score to
  `CURRENT (6347)` and introduced broader prologue/global-offset drift; swapping
  the setup order to compute `currentBoundingBox` before `currentSegment`
  worsened the linked score to `CURRENT (3885)` while still leaving the unwanted
  `gCurrentLevelModel` hoist; assigning `XInInt`/`ZInInt` before
  `get_inside_segment_count_xz` and passing those locals kept the target
  prologue conversion/call shape but inserted an early `gCurrentLevelModel`
  spill, regressed the relinked focused score to `CURRENT (2860)`, and failed
  full verify with calculated CRCs `0x7856718A/0x66208CAA`. A smaller
  direct-cast call-shape probe (`get_inside_segment_count_xz((s32) xIn,
  (s32) zIn, spB0)`) without hoisting `XInInt`/`ZInInt` locals recreated the
  same miss: relinked focused score `CURRENT (2860)`, full verify CRCs
  `0x7856718A/0x66208CAA`, and the same unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)`. Do not repeat this direct-cast
  call-shape spelling. Loading a local
  `LevelModel *levelModel` through a volatile pointer cast at the segment and
  texture access sites also left the linked score unchanged at `CURRENT (2780)`.
  Explicitly rewriting the
  `gTrackWaves` pointer population as a remainder loop followed by
  unrolled-by-four stores compiled but worsened the relinked score to
  `CURRENT (4623)` and shifted the same `gCurrentLevelModel`/global-offset
  schedule family; do not repeat that copy-loop spelling. Moving only the
  `XInInt = xIn` / `ZInInt = zIn` conversions immediately after `*arg3 =
  NULL` while still passing original `xIn`/`zIn` to
  `get_inside_segment_count_xz` compiled, but the relinked focused score stayed
  unchanged at `CURRENT (2780)`. Forcing direct volatile `gCurrentLevelModel`
  reloads at the initial `currentSegment` and `currentBoundingBox` setup sites
  compiled, but worsened the relinked focused score from `CURRENT (2780)` to
  `CURRENT (4395)` and shifted the same global-offset/tail-label drift family;
  do not repeat that direct volatile global-pointer read spelling. Introducing
  a direct `LevelModel *levelModel` local in the outer segment loop and using it
  for the initial segment/bounding-box setup plus texture lookup compiled, but
  widened the frame to `0x130` and worsened the relinked focused score from
  `CURRENT (2780)` to `CURRENT (2900)` (`--max-size 260`: `CURRENT (1435)` to
  `CURRENT (1470)`); do not repeat this direct local model-cache spelling.
  Removing the dead `pad3` local before `Vec4f tempVec4f` kept the target
  `0x128` frame and improved the relinked focused score to `CURRENT (1998)`,
  but still hoisted `gCurrentLevelModel`, spilling it at `0x64(sp)`, and failed
  full verify with calculated CRCs `0x785671AA/0x0D6F6A4A`. Moving `pad3` after
  `tempVec4f` fell back to the promoted-baseline CRC family
  `0x7856718A/0x66208CAA` and did not improve; do not repeat that simple
  moved-`pad3` stack-slot variant. Removing the unused `WaterProperties *wave2`
  while promoting the current C also collapsed into the plain `pad3`-removal
  CRC family: relinked focused score `CURRENT (2868)`, failed full verify with
  calculated CRCs `0x785671AA/0x0D6F6A4A`, and still inserted the early
  `gCurrentLevelModel` spill. Do not repeat this declaration-only
  unused-wave2 removal. Removing only unused `pad2` while promoting the current
  C also missed: relinked focused score `CURRENT (2878)`, failed full verify
  with calculated CRCs `0x78567132/0xCBE53596`, shifted `spB0` from target
  `0xb0(sp)` to `0xb4(sp)`, and preserved the early `gCurrentLevelModel` spill
  at `0x64(sp)`. Removing both unused `pad2` and dead `pad3` together shrank
  the frame to `0x120`, worsened the relinked focused score to
  `CURRENT (2928)`, failed full verify with calculated CRCs
  `0x78566FC2/0xC14E0CEA`, and still carried the early `gCurrentLevelModel`
  spill family. Removing the first dead `pad` local while promoting the current
  C also missed: full verify failed with calculated CRCs
  `0x7856713A/0x0D9BD727`, the relinked focused score worsened to
  `CURRENT (2886)`, `spB0` shifted from target `0xb0(sp)` to `0xb4(sp)`,
  `sp108` shifted to `0x10c(sp)`, and the unwanted early
  `gCurrentLevelModel` spill stayed at `0x64(sp)`. Source was restored and
  final full verify passed. Do not repeat this declaration-only `pad2` removal,
  first-dead-`pad` removal, or the combined `pad2`/`pad3` removal. Replacing
  the dead `pad3` slot with a local `TextureInfo *textures` at the batch
  texture-surface read improved over the promoted baseline but regressed versus
  plain `pad3` removal: relinked focused score `CURRENT (2425)`, failed full
  verify with calculated CRCs
  `0x780AE18A/0xED80C398`, and still inserted an early `gCurrentLevelModel`
  spill before the outer segment loop. Do not repeat this texture-pointer
  replacement shape; nesting the batch surface skip condition as
  `if (surface != SURFACE_WATER_CALM) { if (surface != SURFACE_WATER_UNK_F &&
  flags) ... }` also missed: full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, relinked focused score worsened to
  `CURRENT (2860)`, and the same early `gCurrentLevelModel` spill/register
  drift appeared before the segment loop. Source was restored and final full
  verify passed; do not repeat this nested surface-condition spelling. If
  continuing this function, prefer the simpler
  `pad3`-removed evidence path. Combining the `pad3`-removed branch with a
  pointer-increment `gTrackWaves` population loop (`for (var_v0 = 0, wave =
  D_8011D128; var_v0 < yOutCount; var_v0++, wave++)`) compiled but worsened
  the relinked focused score to `CURRENT (6366)`, shifted saved-register and
  loop scheduling from the top of the function, and failed full verify with
  calculated CRCs `0x47E07C97/0x7D45A79C`; do not repeat this pointer-copy
  spelling. Combining the better plain `pad3`-removed stack layout with early
  `XInInt`/`ZInInt` conversion before `get_inside_segment_count_xz` and passing
  those integer locals into the call compiled but failed full verify with the
  same calculated CRCs as plain `pad3` removal, `0x785671AA/0x0D6F6A4A`; the
  relinked focused score regressed to `CURRENT (2868)` and still showed the
  early `gCurrentLevelModel` spill family, so do not repeat this combined
  pad3-removal plus early-conversion call shape. A later variant kept the
  original `get_inside_segment_count_xz(xIn, zIn, spB0)` call shape, removed
  `pad3`, and moved only `XInInt = xIn; ZInInt = zIn;` out of the per-segment
  loop to just after `yOutCount = 0`; it compiled but failed full verify with
  the same calculated CRCs `0x785671AA/0x0D6F6A4A`, regressed the relinked
  focused score to `CURRENT (2853)`, and preserved the unwanted early
  `gCurrentLevelModel` spill at `0x64(sp)`. Do not repeat this pad3-removal
  plus post-call coordinate-hoist shape. A compressed focused diff printed stale
  `CURRENT (0)` before relink during both the 2026-05-15 packet and the
  2026-05-17 unrolled-copy probe; rely on a relinked focused diff and the full
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` gate before accepting this
  function. Unrolling only the Z grid mask loop into eight explicit checks
  compiled, but badly regressed the relinked focused score to `CURRENT (26603)`,
  swapped the x/z integer register family early in the function, and failed
  full verify with calculated CRCs `0xABA59E51/0x244BAFAC`; source was restored
  and final full verify passed. A narrower two-iteration/four-check Z-loop
  shape (`for (i = 0; i < 8; i += 4)` with four explicit checks per body)
  compiled and preserved the target prologue, but still regressed the relinked
  focused score to `CURRENT (3325)`, introduced the unwanted early
  `gCurrentLevelModel` spill family before the segment loop, and failed full
  verify with calculated CRCs `0x7856718A/0xC40F5151`; source was restored and
  final full verify passed. Hoisting the bubble-sort bound into the existing
  `i` local (`i = yOutCount - 1; for (var_v0 = 0; var_v0 < i; var_v0++)`)
  compiled but missed: relinked focused score `CURRENT (3175)`, failed full
  verify with calculated CRCs `0xAC7CA404/0x71455330`, and still carried the
  unwanted global-model hoist/tail drift. Source was restored and final full
  verify passed. Removing only the Z-grid `if (1) {}` barrier marked as
  `@fake for s3 vs s2` also missed: relinked focused score worsened to
  `CURRENT (2900)`, full verify failed with calculated CRCs
  `0x7884718A/0x8596E436`, and the diff showed an early `gCurrentLevelModel`
  spill at `0x60(sp)` plus broader register churn through the grid and tail
  loops. Do not repeat this Z-grid barrier-removal spelling. Rewriting only
  that Z-grid fake barrier from `if (1) {}` to `if (var_a1) {}` also missed:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, the
  relinked focused score was `CURRENT (2860)`, and the diff recreated the
  known early `gCurrentLevelModel` spill at `0x60(sp)` plus broad grid/tail
  register churn. Source was restored and final full verify passed. Do not
  repeat this live-`var_a1` Z-grid barrier spelling. Rewriting both grid
  bitmask doublings from `var_a1 *= 2` to `var_a1 += var_a1` also missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x79235F02/0xA15ADC5A`, and the relinked focused
  score worsened from promoted-baseline `CURRENT (2780)` to `CURRENT (3375)`.
  The diff inserted the known early `gCurrentLevelModel` spill at `0x60(sp)`
  and rotated the X/Z grid bitmask registers away from target `a1` toward
  `v1`, with tail drift unchanged. Source was restored and final full verify
  passed; do not repeat this grid bitmask `var_a1 += var_a1` spelling.
  Rewriting only the X-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 <<= 1` also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and the relinked focused score was
  `CURRENT (2860)`. The diff kept the known early `gCurrentLevelModel` spill at
  `0x60(sp)` plus broad grid/tail register drift. Source was restored and
  final full verify passed; do not repeat this X-grid `var_a1 <<= 1` spelling.
  Rewriting only the X-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 += var_a1` was a more interesting miss: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x78D4C012/0x0B98CE25`, and the relinked focused score improved from promoted
  baseline to `CURRENT (1805)`. The target `$f20`/`$f22` prologue shape stayed,
  but the diff still inserted the unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` and broadened segment/grid/tail drift. Source was restored and
  final full verify passed; do not repeat this single X-grid `var_a1 += var_a1`
  spelling.
  Rewriting only the Z-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 <<= 1` also missed in the same promoted-baseline family:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x7856718A/0x66208CAA`, and the relinked focused
  score was `CURRENT (2860)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` and shifted the X/Z grid and tail
  register schedule. Source was restored and final full verify passed; do not
  repeat this Z-grid `var_a1 <<= 1` spelling.
  Rewriting only the Z-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 += var_a1` also missed worse than the single X-grid sibling:
  object-only focused diff first printed stale `CURRENT (0)`, full verify failed
  with calculated CRCs `0x77E6007A/0x78D4AD50`, and the relinked focused score
  regressed to `CURRENT (4130)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)`, shifted the X/Z grid bitmask
  register family, and broadened tail drift. Source was restored and final full
  verify passed; do not repeat this single Z-grid `var_a1 += var_a1` spelling.
  Combining the better pad3-removal stack-shape branch with the single X-grid
  `var_a1 += var_a1` spelling also missed: full verify failed with calculated
  CRCs `0x78D4C01A/0xEA4191D0`, relinked `./diff.sh func_8002B0F4` reported
  `CURRENT (1813)`, and the unwanted early `gCurrentLevelModel` spill remained
  at `0x64(sp)` with broad segment/grid/tail drift. Source was restored and
  final full verify passed; do not repeat this combined pad3-removal plus
  X-grid doubling spelling.
  Rewriting the
  bottom `gTrackWaves` population loop from the existing backslash-preserved
  `for` into an explicit `while (var_v0 < yOutCount)` spelling also missed:
  relinked focused score worsened to `CURRENT (3080)`, full verify failed with
  calculated CRCs `0x7856718A/0x4AA98304`, and the diff shifted the bottom
  pointer-population/unrolled-copy schedule while preserving the same early
  `gCurrentLevelModel` spill family. Do not repeat this bottom population-loop
  `while` spelling. Reusing the existing `wave2` local as the preloaded
  `gTrackWaves[var_v0 + 1]` pointer in the bottom bubble sort also missed:
  full verify failed with calculated CRCs `0x7D23AFD2/0x75CB7537`, the
  relinked focused score worsened to `CURRENT (5200)`, and the same unwanted
  early `gCurrentLevelModel` spill/register-family drift moved through the
  grid and bottom sort schedule. Source was restored and final full verify
  passed. Do not repeat this bottom sort `wave2` next-pointer carrier. Removing
  only the dead-looking `wave = gTrackWaves[var_v0 + 1]` pre-load before the
  bottom bubble-sort compare also missed: full verify failed with calculated
  CRCs `0x78D6A18A/0xC1B8EB90`, the relinked focused score worsened to
  `CURRENT (3025)`, and the same global-model spill/register drift remained
  while the bottom sort/tail labels shifted. Source was restored and final full
  verify passed. Do not repeat this bottom sort pre-load removal.
  Rewriting only the outer segment loop from
  `for (var_fp = 0; var_fp < sp108; var_fp++)` to an equivalent
  `var_fp = 0; while (var_fp < sp108) { ...; var_fp++; }` compiled but
  produced no relinked object movement from the promoted baseline: focused
  score stayed `CURRENT (2860)`, full verify failed with the same calculated
  CRCs `0x7856718A/0x66208CAA`, and the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` remained. Source was restored and
  final full verify passed. Do not repeat this outer segment-loop `while`
  spelling. A later segment-index carrier through the existing `i` local
  (`i = spB0[var_fp]; currentSegment = &gCurrentLevelModel->segments[i];
  currentBoundingBox = &gCurrentLevelModel->segmentsBoundingBoxes[i]`) also
  missed: relinked focused score worsened to `CURRENT (2925)`, full verify
  failed with calculated CRCs `0x78BF118A/0x21FC9F7D`, the early
  `gCurrentLevelModel` spill at `0x60(sp)` remained, and the segment-index
  register family drifted from target/baseline `t1` toward `a3`/`t1`. Source
  was restored and final full verify passed. Do not repeat this segment-index
  `i` carrier. A 2026-05-17 segment-index carrier through the existing `temp`
  local (`temp = spB0[var_fp]; currentSegment =
  &gCurrentLevelModel->segments[temp]; currentBoundingBox =
  &gCurrentLevelModel->segmentsBoundingBoxes[temp]`) also missed: full verify
  failed with calculated CRCs `0x7DF5F18A/0xA4BAA9BB`, relinked focused score
  worsened to `CURRENT (3280)`, and the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` remained while the grid-loop register family shifted
  toward `a0`/`a1`/`a2`/`a3`. Source was restored and final full verify passed.
  Do not repeat this segment-index `temp` carrier. A later segment-index carrier
  through the existing `var_v0` local (`var_v0 = spB0[var_fp]; currentSegment =
  &gCurrentLevelModel->segments[var_v0]; currentBoundingBox =
  &gCurrentLevelModel->segmentsBoundingBoxes[var_v0]`) also missed: full verify
  failed with calculated CRCs `0x7719218A/0xB69630D8`, relinked focused score
  worsened to `CURRENT (2975)`, and the same unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` remained while segment setup shifted
  to a different integer-register family. Source was restored and final full
  verify passed. Do not repeat this segment-index `var_v0` carrier. Splitting
  the early
  `sp108 == 0 || sp108 >= 8` return into two separate `if` statements also
  missed: full verify failed with calculated CRCs `0x701EEB7B/0xA3DBFC65`,
  the relinked focused diff worsened to `CURRENT (3535)`, and the early return
  branch changed to a `bnez`/inserted return branch where target uses `beqz`
  then `slti`. Source was restored and final full verify passed; do not repeat
  this early `sp108` return-split spelling. Rewriting only the early guard from
  `sp108 == 0` to `sp108 <= 0` also missed: full verify failed with calculated
  CRCs `0xB856718A/0x8DC42D5F`, the relinked focused score worsened to
  `CURRENT (3060)`, and the guard changed the target `beqz` into `blez` while
  preserving the unwanted early `gCurrentLevelModel` spill family. Source was
  restored and final full verify passed. Do not repeat this early
  `sp108 <= 0` guard spelling. A sibling early `sp108` positive-range guard
  spelling (`if (!(sp108 != 0 && sp108 < 8))`) missed as a no-movement family:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, and
  relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager` stayed
  at promoted baseline `CURRENT (2860)`. The target-like early return shape
  was not the blocker; the known unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` plus broad segment/grid/tail register drift remained. Source was
  restored, final full verify passed, and `./score.sh -s` remained 97.30%; do
  not repeat this early `sp108` positive-range guard spelling. Rewriting only
  the outer
  segment-loop bound from
  `var_fp < sp108` to `var_fp != sp108` also missed: full verify failed with
  calculated CRCs `0x68167010/0x71B268DB`, the relinked focused score worsened
  to `CURRENT (3275)`, the loop entry changed from target `blez` to `beqz`, and
  the known unwanted early `gCurrentLevelModel` spill appeared at `0x60(sp)`.
  Source was restored and final full verify passed. Do not repeat this
  outer-loop `!= sp108` bound spelling.
  A pad3-removal branch that reused the existing `batchNum` local as the
  segment-index carrier (`batchNum = spB0[var_fp]; currentSegment =
  &gCurrentLevelModel->segments[batchNum]; currentBoundingBox =
  &gCurrentLevelModel->segmentsBoundingBoxes[batchNum]`) also missed after
  actually promoting the source out of the `NON_EQUIVALENT` guard: full verify
  failed with calculated CRCs `0x7B040FE0/0x432A7562`, relinked focused diff
  reported `CURRENT (3399)`, and the unwanted early `gCurrentLevelModel` spill
  plus saved-register drift remained. Source was restored and final full
  verify passed; do not repeat this pad3-removal plus `batchNum`
  segment-index carrier. Using the existing `wave` local as the preloaded
  `gTrackWaves[var_v0 + 1]` pointer in the bottom bubble-sort comparison
  (`wave = gTrackWaves[var_v0 + 1]`, then comparing
  `gTrackWaves[var_v0]->waveHeight < wave->waveHeight`) also missed: full
  verify failed with calculated CRCs `0x784DF080/0xEF59EED4`, the relinked
  focused diff worsened to `CURRENT (4535)`, and the bottom sort compare/swap
  schedule drifted further while the early `gCurrentLevelModel` spill family
  remained. Source was restored and final full verify passed. Do not repeat
  this bottom sort existing-`wave` next-pointer compare carrier.
  Spelling only the bottom bubble-sort repeat condition as
  `while (stopSorting == FALSE)` also missed: full verify failed with the known
  promoted CRC family `0x7856718A/0x66208CAA`, relinked focused diff reported
  `CURRENT (2860)`, and the unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` plus broad segment-loop register drift remained. Source was
  restored and final full verify passed; do not repeat this bottom sort
  explicit-`FALSE` condition spelling.
  Rewriting only the bottom bubble-sort loop bound from
  `var_v0 < yOutCount - 1` to `var_v0 + 1 < yOutCount` missed badly: full
  verify failed with calculated CRCs `0xC13F1C24/0xADE0DFB1`, relinked focused
  diff worsened to `CURRENT (17634)`, the frame shrank from target `0x128` to
  `0x120`, and global offsets/tail labels shifted broadly. Source was restored
  and final full verify passed; do not repeat this bottom sort
  `var_v0 + 1` bound spelling. Rewriting the bottom bubble sort into a
  target-shaped remainder loop plus four explicit adjacent comparisons per body
  also missed: full verify failed with calculated CRCs
  `0xA6D17436/0x0A68B3A1`, the relinked focused score worsened to
  `CURRENT (5326)`, and the frame shrank from target `0x128` to `0x120` while
  preserving the unwanted early `gCurrentLevelModel` spill/register drift.
  Source was restored and final full verify passed; do not repeat this explicit
  bottom-sort unroll spelling.
  Reordering only the baseline batch skip condition so the flags test comes
  before the two surface checks also missed: full verify failed with calculated
  CRCs `0x78567034/0xDF4C2B54`, relinked focused diff worsened from the
  promoted baseline `CURRENT (2780)` to `CURRENT (3825)`, and the same early
  `gCurrentLevelModel` spill at `0x60(sp)` plus broad segment-loop/tail label
  drift remained. Source was restored and final full verify passed; do not
  repeat this flag-first batch skip condition spelling.
  Adding an X-grid fake lifetime barrier after the
  first mask loop (`if (var_a1) {}` before the Z-grid setup) also missed:
  object-only focused diff printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x77D9E18A/0xB9F696E2`, and the relinked focused score was
  `CURRENT (2995)`. The diff still introduced the unwanted early
  `gCurrentLevelModel` load/spill at `0x60(sp)`, shifted the mask accumulator
  from target `s1` to `s2`, and moved tail/global labels by four bytes. Source
  was restored and final full verify passed; do not repeat this X-grid fake
  barrier spelling.
  Combining the plain `pad3`-removed branch with the earlier standalone
  setup-order idea (`currentBoundingBox` before `currentSegment`) also missed:
  object-only focused diff printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x785671AA/0x48BD26A8`, and the relinked focused score
  worsened to `CURRENT (3973)`. The diff still introduced the unwanted early
  `gCurrentLevelModel` spill at `0x64(sp)` and broadened the outer
  segment-loop register drift. Source was restored and final full verify
  passed; do not repeat this pad3-removal plus setup-order swap.
  Combining the plain `pad3`-removed branch with a three-level
  water-surface skip guard (`surface != SURFACE_WATER_CALM`, then
  `surface != SURFACE_WATER_UNK_F`, then flags) improved the relinked focused
  score to `CURRENT (1720)`, but still missed: object-only focused diff first
  printed stale `CURRENT (0)`, full verify failed with the plain pad3-removal
  CRC family `0x785671AA/0x0D6F6A4A`, and the unwanted early
  `gCurrentLevelModel` spill remained at `0x64(sp)`. Source was restored and
  final full verify passed; do not repeat this pad3-removal plus three-level
  surface-guard split without a separate fix for the model-spill family.
  Extending the pad3-removed three-level surface guard plus texture-index
  `temp` carrier by also routing `currentBatch->flags` through `temp` missed:
  full verify failed with calculated CRCs `0x7C5E203C/0xE0335DD6`, the
  relinked focused score worsened to `CURRENT (3268)`, and the same unwanted
  early `gCurrentLevelModel` spill remained before broader grid/tail drift.
  Source was restored and final full verify passed; do not repeat this
  flags-through-`temp` carrier on that branch.
  Adding direct volatile `gCurrentLevelModel` reloads at the initial
  `currentSegment`/`currentBoundingBox` setup on top of that same
  pad3-removed three-level guard branch also missed: object-only focused diff
  first printed stale `CURRENT (0)`, full verify failed with calculated CRCs
  `0x785671AA/0xB93C9C08`, the relinked focused score was `CURRENT (1920)`,
  and the unwanted early `gCurrentLevelModel` spill still appeared at
  `0x64(sp)`. Source was restored and final full verify passed; do not repeat
  this volatile-reload combination as a model-spill fix.
  Routing only `currentBatch->textureIndex` through the existing `temp` local
  before the surface read on that same pad3-removed three-level guard branch
  improved the relinked focused score to `CURRENT (1520)`, but still missed:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x7C4CE1AA/0x7C1438D3`, and the unwanted early
  `gCurrentLevelModel` spill remained at `0x64(sp)`. Source was restored and
  final full verify passed; do not repeat this texture-index `temp` carrier
  without a separate model-spill fix.
  A standalone current-source texture-index carrier
  (`temp = currentBatch->textureIndex; surface =
  gCurrentLevelModel->textures[temp].surfaceType`) also missed: full verify
  failed with calculated CRCs `0x7C4CE18A/0x3A298210`, and the relinked focused
  score improved from promoted-baseline `CURRENT (2780)` to `CURRENT (2435)`
  but still inserted the unwanted early `gCurrentLevelModel` spill at
  `0x60(sp)` with broad segment/grid/tail register drift. Source was restored
  and final full verify passed; do not repeat this standalone texture-index
  `temp` carrier without a separate model-spill fix.
  Combining the current-source texture-index `temp` carrier with a three-level
  water-surface skip guard also missed without moving the object family: full
  verify failed with the same calculated CRCs `0x7C4CE18A/0x3A298210`,
  relinked focused score stayed `CURRENT (2435)`, and the unwanted early
  `gCurrentLevelModel` spill remained at `0x60(sp)` with broad
  segment/grid/tail register drift. Source was restored and final full verify
  passed; do not repeat this current-layout texture-index plus three-level
  guard split.
  Combining the current-source texture-index `temp` carrier with moving the
  batch offset loads before the surface read also missed without moving the
  object family: full verify failed with the same calculated CRCs
  `0x7C4CE18A/0x3A298210`, relinked focused score stayed `CURRENT (2435)`,
  and the unwanted early `gCurrentLevelModel` spill remained at `0x60(sp)`
  with broad segment/grid/tail register drift. Source was restored and final
  full verify passed; do not repeat this current-layout texture-index plus
  batch-offset-before-surface-read ordering.
  Routing the same `currentBatch->textureIndex` through the existing `i` local
  on the pad3-removed three-level guard branch also missed: full verify failed
  with calculated CRCs `0x75D0E1AA/0xB8D0E2B5`, relinked focused diff scored
  `CURRENT (2393)`, and the unwanted early `gCurrentLevelModel` spill remained
  at `0x64(sp)` with broader segment/grid scheduling drift. Source was
  restored and final full verify passed; do not repeat this texture-index `i`
  carrier.
  Moving the batch offset loads (`facesOffset`, `verticesOffset`, and next
  `facesOffset`) before the texture-index `temp` surface read on that same
  pad3-removed three-level guard branch produced no object movement from the
  texture-index carrier: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x7C4CE1AA/0x7C1438D3`, relinked focused score stayed `CURRENT (1520)`,
  and the unwanted early `gCurrentLevelModel` spill remained at `0x64(sp)`.
  Source was restored and final full verify passed; do not repeat this
  batch-offset-before-surface-read ordering.
  Adding an existing-`faceNum` carrier for `currentBatch->flags` to that
  texture-index branch regressed versus the texture-index carrier alone:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x7B7E11AA/0x52CD4FC5`, relinked focused score
  widened to `CURRENT (1635)`, and the unwanted early `gCurrentLevelModel`
  spill remained at `0x64(sp)`. Source was restored and final full verify
  passed; do not repeat this flags-through-`faceNum` carrier.
  A later promoted current-source probe changed only the batch offset locals
  (`currentFaceOffset`, `nextFaceOffset`, and `currentVerticesOffset`) from
  `s32` to `s16` to mirror the struct field width. It missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x293A6FA7/0xE00D71A8`, the relinked focused diff regressed
  to `CURRENT (3103)`, `spB0` shifted from target `0xb0(sp)` to `0xb4(sp)`,
  and the known early `gCurrentLevelModel` spill remained at `0x64(sp)`.
  Source was restored and final full verify passed; do not repeat this
  batch-offset-local `s16` spelling.
  A promoted pad3-removed pointer-arithmetic segment setup
  (`currentSegment = gCurrentLevelModel->segments + spB0[var_fp]`;
  `currentBoundingBox = gCurrentLevelModel->segmentsBoundingBoxes +
  spB0[var_fp]`) also missed: full verify failed with the plain pad3-removal
  CRC family `0x785671AA/0x0D6F6A4A`, and the relinked focused diff reported
  `CURRENT (2868)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` load/spill at `0x64(sp)` and rotated the outer
  segment/grid registers, so do not repeat this pad3-removal plus
  pointer-arithmetic segment-setup spelling.
  Commuting only the collision-plane index multiplies in the promoted current
  source (`collisionPlanes[temp * 4 + n]` to `collisionPlanes[4 * temp + n]`)
  also missed: full verify failed with calculated CRCs
  `0x7856718A/0x66208CAA`, and the relinked focused score was
  `CURRENT (2860)`. The diff stayed in the known target `$f20`/`$f22`
  prologue plus unwanted early `gCurrentLevelModel` spill at `0x60(sp)` family
  with broad grid/tail register drift. Source was restored and final full
  verify passed; do not repeat this collision-plane index multiply-order
  spelling.
  A promoted current-source texture-index `temp` carrier combined with routing
  `currentBatch->flags` through the existing `faceNum` local before the face
  loop also missed: full verify failed with calculated CRCs
  `0x7B5E2034/0x63827015`, and the focused diff widened to
  `CURRENT (3260)`. The diff still kept the known unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)`, regressing from the standalone
  texture-index carrier's `CURRENT (2435)`. Source was restored and final full
  verify passed; do not repeat this current-source texture-index plus
  flags-through-`faceNum` carrier spelling.
  A sibling current-source texture-index `temp` carrier that reused `temp` for
  `currentBatch->flags` before the surface skip condition also missed: full
  verify failed with calculated CRCs `0x7C5E2034/0x8DDE76F8`, and the focused
  diff widened to `CURRENT (3260)`. The diff stayed in the same known early
  `gCurrentLevelModel` spill family at `0x60(sp)`, regressing from the
  standalone texture-index carrier's `CURRENT (2435)`. Source was restored and
  final full verify passed; do not repeat this current-source texture-index
  plus flags-through-`temp` carrier spelling.
  Moving only the bottom `SURFACE_WATER_WAVY` store before the
  `levelSegmentIndex` current-segment setup while promoting the current source
  also missed: object-only focused diff first printed stale `CURRENT (0)`,
  full verify failed with calculated CRCs `0x77D5718A/0x18F6F0C5`, and the
  relinked focused score worsened to `CURRENT (3730)`. The diff inserted the
  known unwanted early `gCurrentLevelModel` spill at `0x60(sp)` and broadly
  shifted segment/grid/tail labels. Source was restored and final full verify
  passed; do not repeat this bottom wave-type store-order spelling. Adding a
  `register` hint only to the `arg3` output-pointer parameter while promoting
  the current source also missed without object-family movement: full verify
  failed with calculated CRCs `0x7856718A/0x66208CAA`, relinked
  `./diff.sh func_8002B0F4` stayed `CURRENT (2860)`, and the known unwanted
  early `gCurrentLevelModel` spill at `0x60(sp)` remained. Source was restored
  and final full verify passed; do not repeat this `arg3` register-carrier
  spelling. A promoted current-source global-clear literal spelling
  (`D_8011D308 = FALSE` instead of `0`) also missed without object-family
  movement: full verify failed with calculated CRCs `0x7856718A/0x66208CAA`,
  and relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  stayed at `CURRENT (2860)`. The diff retained the known unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` plus broad segment/grid/tail
  register drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this global-clear `FALSE` literal spelling. A
  promoted current-source collision-output target-store-order probe
  also missed: ordering the hit writes as `type`, `rot.x`, `rot.y`, `rot.z`,
  then `waveHeight` failed full verify with calculated CRCs
  `0x7856718A/0x66208CAA`; relinked `./diff.sh func_8002B0F4` stayed
  `CURRENT (2860)` and still showed the unwanted early `gCurrentLevelModel`
  spill at `0x60(sp)` plus broad segment/grid/tail drift. Source was restored
  and final full verify passed; do not repeat this collision-output
  store-order spelling. A promoted current-source pointer-arithmetic
  segment-setup spelling without the earlier `pad3` removal (`currentSegment =
  gCurrentLevelModel->segments + spB0[var_fp]`; `currentBoundingBox =
  gCurrentLevelModel->segmentsBoundingBoxes + spB0[var_fp]`) also missed:
  full verify failed with the promoted-baseline CRC family
  `0x7856718A/0x66208CAA`, relinked `./diff.sh func_8002B0F4` stayed
  `CURRENT (2860)`, and the unwanted early `gCurrentLevelModel` spill remained
  at `0x60(sp)` with broad segment/grid/tail drift. Source was restored and
  final full verify passed; do not repeat this current-layout
  pointer-arithmetic segment-setup spelling.
  A promoted current-source bottom default-water store-order spelling that
  reordered the default path writes as `rot.x`, `rot.z`, `waveHeight`, then
  `rot.y` also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x281EE85B/0xEE22BD90`, and relinked `./diff.sh func_8002B0F4` regressed
  from promoted baseline `CURRENT (2780)` to `CURRENT (3745)`. The diff
  retained the known unwanted early `gCurrentLevelModel` spill family at
  `0x60(sp)` and broadened segment/grid/tail drift. Source was restored and
  final full verify passed; do not repeat this bottom default-water store-order
  spelling.
  A promoted current-source partial bottom default-water store-order spelling
  that reordered the default path writes as `rot.x`, `waveHeight`, `rot.z`,
  then `rot.y` also missed: object-only focused diff first printed stale
  `CURRENT (0)`, full verify failed with calculated CRCs
  `0x281EE85B/0x4ACE73BF`, and relinked `./diff.sh func_8002B0F4` regressed
  to `CURRENT (3835)`. The diff retained the known unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` and broadened segment/grid/tail
  drift. Source was restored and final full verify passed; do not repeat this
  partial bottom default-water store-order spelling.
  A promoted current-source bottom-water condition-order spelling that changed
  `if (currentSegment->hasWaves && gWaveBlockCount != 0)` to
  `if (gWaveBlockCount != 0 && currentSegment->hasWaves)` also missed: full
  verify failed with calculated CRCs `0x779A718A/0xE51286EE`, and relinked
  `./diff.sh func_8002B0F4` regressed to `CURRENT (4010)`. Source was restored
  and final full verify passed; do not repeat this condition-order spelling.
  A promoted current-source bottom segment-range guard reorder spelling that
  changed `if (levelSegmentIndex >= 0 && levelSegmentIndex <
  gCurrentLevelModel->numberOfSegments)` to `if (levelSegmentIndex <
  gCurrentLevelModel->numberOfSegments && levelSegmentIndex >= 0)` also missed:
  full verify failed with calculated CRCs `0x281EE7B3/0xDC10368B`, and relinked
  `./diff.sh func_8002B0F4` regressed to `CURRENT (4020)`. The diff retained
  the unwanted early `gCurrentLevelModel` spill family and broadened
  segment/grid/tail drift. Source was restored and final full verify passed; do
  not repeat this bottom segment-range guard reorder.
  A promoted current-source bottom default-water height cast spelling that
  changed `D_8011D128[yOutCount].waveHeight = currentSegment->unk38` to
  `D_8011D128[yOutCount].waveHeight = (f32) currentSegment->unk38` also missed:
  full verify failed with calculated CRCs `0x7856718A/0x66208CAA`, relinked
  `./diff.sh func_8002B0F4` stayed `CURRENT (2860)`, and the diff retained the
  unwanted early `gCurrentLevelModel` spill at `0x60(sp)` with broad
  segment/grid/tail drift. Source was restored and final full verify passed; do
  not repeat this explicit default-water height-cast spelling. A promoted
  current-source collision-plane index local type spelling that changed only
  `s32 temp` to `u16 temp` (matching the `basePlaneIndex` field and the nearby
  `collision_get_y` local type) also missed without object-family movement:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4` stayed at promoted baseline `CURRENT (2860)`. The
  diff retained the unwanted early `gCurrentLevelModel` spill at `0x60(sp)`
  plus broad segment/grid/tail register drift. Source was restored and final
  full verify passed; do not repeat this collision-plane index local type
  spelling. A promoted current-source collision-plane nonzero guard operand-
  order spelling (`if (0.0 != tempVec4f.y)`) also missed without object-family
  movement: object-only focused diff first printed stale `CURRENT (0)`, full
  verify failed with calculated CRCs `0x7856718A/0x66208CAA`, and relinked
  `./diff.sh func_8002B0F4` stayed at promoted baseline `CURRENT (2860)`. The
  diff retained the unwanted early `gCurrentLevelModel` spill at `0x60(sp)`
  plus broad segment/grid/tail register drift. Source was restored and final
  full verify passed; do not repeat this collision-plane nonzero guard
  operand-order spelling. A promoted current-source collision-plane nonzero
  literal-type spelling (`if (tempVec4f.y != 0.0f)` instead of the current
  double literal) also missed: full verify failed with calculated CRCs
  `0xF03EAC35/0x346A795F`, and relinked `./diff.sh func_8002B0F4` regressed
  to `CURRENT (3815)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` and broadened segment/grid/tail
  drift. Source was restored and final full verify passed; do not repeat this
  collision-plane nonzero `0.0f` literal spelling. A promoted current-source
  X/Z integer local type spelling that changed only `XInInt`/`ZInInt` from
  `s32` to `s16` also missed: full verify failed with calculated CRCs
  `0x93CE4D86/0x8EE561B4`, and relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` regressed to `CURRENT (4425)`. The diff
  inserted explicit sign-extension work for the narrowed X/Z locals and still
  kept the unwanted early `gCurrentLevelModel` spill family. Source was
  restored and final full verify passed; do not repeat this X/Z `s16` local
  type spelling. A promoted current-source field-base pointer reload spelling
  that introduced separate `segments` and `segmentsBoundingBoxes` locals before
  the initial segment/bounding-box indexing also missed: full verify failed
  with calculated CRCs `0x78E9013A/0xAD05D630`, and relinked `./diff.sh
  func_8002B0F4 --compress-matching 2 --no-pager` regressed to
  `CURRENT (4142)`. The diff widened the frame to `0x130`, kept the unwanted
  early `gCurrentLevelModel` spill at `0x60(sp)`, and changed the first segment
  setup into a worse base-pointer schedule. Source was restored and final full
  verify passed; do not repeat these separate field-base pointer locals.
  Keep this function active,
  but do not repeat those source
  shapes, either standalone Z-loop unroll, this sort-limit-hoist spelling, this
  bottom population-loop `while` spelling, this outer segment-loop `while`
  spelling, this segment-index `i` carrier, or this segment-index `temp`
  carrier.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.
