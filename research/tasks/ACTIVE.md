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
- Latest no-park routing note: `func_80049794` remains active and should not be
  parked solely because the current source-shape families are saturated. The
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
  broader wave-block register churn. Do not repeat this local-copy while-loop
  wave-bound spelling. The
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
  missing `$f20/$f21` prologue saves and early `$f16` zero allocation. A later
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
  not repeat this current-baseline predecrement wave-scan loop.
- `func_80059208` is also active, not parked. The 2026-05-17 final-offset
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
  Do not repeat either final `unk1BA` or `unk1BC` add-order spelling. An
  explicit-zero axis-negation spelling
  (`diffZ = 0.0f - diffY`) compiled but regressed the relinked focused score to
  `CURRENT (1626)` and failed full verify with calculated CRCs
  `0x53B93C23/0x99E6EAF5`; source was restored and final full verify passed.
  Commuting only the final object-dot x product from `splinePos * diffX` to
  `diffX * splinePos` compiled but regressed the relinked focused score from
  baseline `CURRENT (870)` to `CURRENT (875)` and failed full verify with
  calculated CRCs `0x53D0C1DF/0xC593C532`; source was restored and final full
  verify passed. Keep active, but do not repeat this axis-negation spelling or
  final object-dot x-multiply commute.
- `func_8002B0F4` is also active, not parked. The 2026-05-17 explicit
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
  spill. Keeping `pad3` intact but
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
  `gCurrentLevelModel` spill family. A later statement-order variant moved the existing
  `XInInt = xIn` / `ZInInt = zIn` conversions immediately after
  `D_8011D308 = 0`, then stored `*arg3 = NULL`, passed the integer locals into
  `get_inside_segment_count_xz`, and removed the per-segment reassignments; it
  recreated the same early-conversion call-shape miss with relinked focused
  `CURRENT (2860)`, failed full verify with calculated CRCs
  `0x7856718A/0x66208CAA`, and still inserted the unwanted pre-loop
  `gCurrentLevelModel` spill to `0x60(sp)`. Keep active; do not repeat the
  simple moved `pad3` variant, the pointer-increment population spelling,
  either early-conversion call shape, the direct-cast
  `get_inside_segment_count_xz` call shape, this `D_8011D308`-first
  conversion/order variant, the scalar plane-carrier replacement, the
  unused-wave2 removal, or the declaration-only `pad2` removal.
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
  the same additive-double CRC family `0x93D338FF/0x03D9C8FE`. A paired
  first-ring `pad_sp108` carrier for the duplicated `-scaledXCos +
  scaledXSin` value (`zPositions[0] = pad_sp108; xPositions[3] = pad_sp108`)
  also collapsed into the bad frame-shrink family: frame `0x150`, relinked
  focused `CURRENT (13471)`, and full-verify CRCs
  `0x218F9FFA/0x18F4A6D6`. A later unused-`pad_sp100` carrier for the
  duplicated `-scaledXCos - (xSin * 1280.0f)` value (`xPositions[0]` and
  `zPositions[1]`) also collapsed into that bad family: frame `0x150`,
  relinked focused `CURRENT (13706)`, and full-verify CRCs
  `0x218F9FFA/0x18F4A6D6`. Keep active and avoid repeating those no-op,
  single-site scaled-sine, first-ring existing-`var_f16` carrier,
  first-ring `pad_sp108`/unused-`pad_sp100` carrier, outer-ring
  assignment-order, single-site `zPositions[6]`/`xPositions[6]` reorder,
  exact outer-ring `x5/z5/z6/x6` store-order, `scaledXCos`-first assignment
  order, first-ring store-order grouping, single-site `zPositions[5]`
  subtract-chain, or `pad_sp108` x1/z2/double-cosine carrier shapes.
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
  cascade register allocation. Do not retry those same probes as the next
  packet.
- `func_80017A18` has exhausted probe notes in `research/tasks/PARKED.md`:
  existing C compiles when promoted, but diff evidence points at frame size,
  saved-register allocation, and float-temp lifetime mismatches. Do not retry
  the recorded dead-local, edge-plane-inline, or `register var_s6` probes as the
  next packet.
- `init_particle_buffers` has exhausted probe notes in
  `research/tasks/PARKED.md`: existing C compiles when promoted, but diff
  evidence points at saved-register allocation for the particle counts and
  allocator colour tag. Do not retry the recorded `register` parameter, local
  count alias, or pointer-to-global probes as the next packet.
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
  but left the focused score unchanged at `CURRENT (2550)`. Combining
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
  prologue saves. Combining `register f32 var_f20` with
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
  Adding `register` to `racerThrottle` compiled but produced no object movement
  from the current promoted baseline: uncompressed focused diff stayed
  `CURRENT (1926)`, full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, and the missing `$f20/$f21` prologue saves plus
  early `$f16` zero allocation remained unchanged; do not repeat this standalone
  `racerThrottle` register hint.
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
  introduce target `$f20/$f21` prologue saves. Rewriting the first
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
  drift. If continuing this family, inspect this improved variant rather than
  the weaker plain trailing-pad-removal shape. Combining that same steer-vel
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
  target `$f14` allocation together. Adding `register f32 var_f14` to this
  x/z/y save-family `spCC` preserve branch produced no improvement: original
  `spCC` stayed `CURRENT (3526)`, moved `spCC` stayed `CURRENT (3666)`, and
  the moved slot still spilled the wrong source FPR at `0xdc(sp)` instead of
  creating the target-like `$f14` reload. Do not repeat register-`var_f14` /
  `spCC` preserve combinations. A narrow `segmentZVelocity` carrier
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
  still absent, so do not repeat this register hint on that branch. Removing
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
  register-family drift. Reversing only the wave count comparison spelling to
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
  Rewriting the wave scan as a bound-local copy while-loop
  (`var_a0 = gRacerWaveCount - 1; var_v1 = var_a0; while (...) { var_a0--; };
  if (var_a0 == var_v1)`) also missed: full verify failed with calculated CRCs
  `0x527F28C9/0xA7E04D93`, the relinked focused score widened to `CURRENT
  (4252)`, and the diff showed extra `spA2` stack-byte traffic plus broader
  wave-block register churn rather than the target `a0`/`v1` allocation. Do
  not repeat this local-copy while-loop wave-bound spelling; keep the function
  active and continue by solving the wave register/order or first-speed
  arithmetic drift without losing the frame/save family. Two first-speed carrier variants on
  that same branch both regressed by losing the target frame/save family: using
  existing `var_f6` for the pre-`sqrtf` sum failed full verify with calculated
  CRCs `0x6035EC5F/0x4C26F14E` and relinked focused `CURRENT (2326)`, while
  keeping only the x/z sum in `var_f20` and adding the y component in the
  `sqrtf` argument failed with calculated CRCs `0x5F84A15F/0x79820DF5` and
  relinked focused `CURRENT (2311)`. Both shrank the frame to `0xf0` and
  dropped `$f20/$f21` saves, so do not repeat existing-temp or call-argument
  y-component first-speed carriers unless new evidence shows how to retain the
  save family. A 2026-05-17 save-family wave-bound comma-assignment probe
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
  A 2026-05-17 current-baseline split wave-bound probe also missed:
  promoting the current C and spelling `var_v1 = gRacerWaveCount - 1; for
  (var_a0 = var_v1; ...); if (var_a0 == var_v1)` worsened the relinked focused
  score from promoted-baseline `CURRENT (2430)` to `CURRENT (4920)`, failed
  full verify with calculated CRCs `0x5790053C/0x1C8C0179`, introduced `spA2`
  stack-byte traffic, and widened wave-scan register churn instead of matching
  target `v1` bound plus `a0` loop-index allocation. Source was restored and
  final full verify passed; do not repeat this current-baseline split
  wave-bound spelling.
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
  `do`-loop wave-scan spelling. A
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
  current-baseline probe. A baseline check of `func_80059208` was still
  `CURRENT (870)`, with the same final-offset expression/load-order drift; do
  not repeat its recorded rejected final-block source shapes as a fallback.
  Keep the function active; do not park it just because these
  allocation/scheduling probes missed.
- `func_80059208` is active, not parked. Promoting the existing C compiles and
  focused object diff scores `CURRENT (870)`. The remaining drift is localized
  near the final lateral/vertical offset math: target preserves the negated
  `pad2 = -((tempZ * diffZ) + (diffX * tempX))` temporary and adds it to `pad`,
  while current folds the equivalent math into a subtract. Rejected probes:
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
  compiled but worsened the focused object score to `CURRENT (1015)`. Replacing
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
  `CURRENT (1015)`. Making `pad2` volatile compiled but worsened the focused
  score to `CURRENT (955)` by forcing stack traffic and shifting final-block
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
  repeat this final-vertical carrier either. Rewriting the final lateral
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
  role-swap spelling. Routing the final clamped vertical value
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
  Do not repeat this positive numerator carrier.
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
  the focused score to `CURRENT (2551)` and shifted later scheduling. A
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
  Reordering only the `uCoords[7]` UV expression to put `pos.z` first
  (`uCoords[7] = (s16) (pos.z + (2.0f * xCos)) + var_v0`) compiled but did not
  move the function: focused diff stayed `CURRENT (1808)`, full verify failed
  with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the visible drift remained
  in the earlier position-array schedule. Do not repeat this `uCoords[7]`
  pos.z-first UV expression-order probe. Rewriting only `vCoords[7]` from
  `((2.0f * pos.x) - var_f16)` to `((pos.x + pos.x) - var_f16)` compiled but
  also did not move the function: focused diff stayed `CURRENT (1808)`, full
  verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and the visible
  drift remained in the earlier position-array schedule. Do not repeat this
  `vCoords[7]` additive-double UV spelling.
  Flipping
  only `xPositions[2]` to `(xSin * 1280.0f) + scaledXCos` compiled but left the
  linked focused score unchanged at `CURRENT (1808)`. Replacing only
  `xPositions[2]` with `scaledXCos + scaledXSin` compiled but worsened the
  focused score to `CURRENT (12021)` and changed the frame to `0x150`.
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
  Do not repeat this unused-`pad_sp100` x0/z1 carrier.
- `func_8002B0F4` is active, not parked. Promoting the existing C compiles, but
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
  spill family. Do not repeat this declaration-only `pad2` removal or the
  combined `pad2`/`pad3` removal. Replacing
  the dead `pad3` slot with a local `TextureInfo *textures` at the batch
  texture-surface read improved over the promoted baseline but regressed versus
  plain `pad3` removal: relinked focused score `CURRENT (2425)`, failed full
  verify with calculated CRCs
  `0x780AE18A/0xED80C398`, and still inserted an early `gCurrentLevelModel`
  spill before the outer segment loop. Do not repeat this texture-pointer
  replacement shape; if continuing this function, prefer the simpler
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
  loops. Do not repeat this Z-grid barrier-removal spelling. Keep this function
  active, but do not repeat those source shapes, either standalone Z-loop
  unroll, or this sort-limit-hoist spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.
