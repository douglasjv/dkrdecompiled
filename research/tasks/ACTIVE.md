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
  allocated the early zero in `$f16` instead of target `$f14`. Keep
  `func_80049794` active rather than parked.
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
  relinked focused score to `CURRENT (2043)`. The sibling term-negation spelling
  (`pad2 = (tempZ * -diffZ) - (diffX * tempX)`) worsened the relinked focused
  score from `CURRENT (870)` to `CURRENT (1165)` and failed full verify with
  calculated CRCs `0x53AB58B5/0xBC82B0CE`.
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
  and did not solve the hoist. Keep active; do not repeat the simple moved
  `pad3` variant.
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
  do not repeat this simple `var_f2` early-zero carrier. Combining `register
  f32 var_f20` with `register f32 segmentZVelocity` compiled but produced no
  object change from the promoted baseline, stayed focused
  `CURRENT (2550)`, and still did not introduce the target `$f20/$f21` prologue
  saves. Splitting the first speed-magnitude operands into dedicated
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
  candidate rather than the weaker two-step x/z sum spelling. The sibling
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
  `a0`/`v1` swap. Do not repeat this exact chained-zero save-family shape or
  the comparison-only wave operand spelling; keep the function active and
  continue by solving the wave register/order or first-speed arithmetic drift
  without losing the frame/save family. Two first-speed carrier variants on
  that same branch both regressed by losing the target frame/save family: using
  existing `var_f6` for the pre-`sqrtf` sum failed full verify with calculated
  CRCs `0x6035EC5F/0x4C26F14E` and relinked focused `CURRENT (2326)`, while
  keeping only the x/z sum in `var_f20` and adding the y component in the
  `sqrtf` argument failed with calculated CRCs `0x5F84A15F/0x79820DF5` and
  relinked focused `CURRENT (2311)`. Both shrank the frame to `0xf0` and
  dropped `$f20/$f21` saves, so do not repeat existing-temp or call-argument
  y-component first-speed carriers unless new evidence shows how to retain the
  save family. A
  linked compressed focused diff printed stale `CURRENT (0)` after object-only
  rebuild during the 2026-05-15 packet, and the 2026-05-17 promotion repeated
  the trap: object-only diff printed `CURRENT (0)`, but relink/full gate
  failed and the relinked focused diff returned to `CURRENT (2760)`; do not
  accept this function without relink/full gate evidence. A baseline check of
  `func_80059208` was still
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
  repeat this final-vertical carrier either.
  Reusing the final-block `pad` local as the axis-swap temporary
  (`pad = diffX; diffX = diffZ; diffZ = -pad`) compiled and produced a
  deceptively low compressed score (`--max-size 260`: `CURRENT (20)`), but
  relinked full focused score worsened to `CURRENT (1698)` and full verify
  failed with calculated CRCs `0x0A689858/0x4CFBB1F6` because the final
  block/epilogue shifted. Reusing `pad2` as that axis-swap temporary produced
  the same relinked score and CRC family; do not repeat either `pad`/`pad2`
  axis-swap carrier.
  Splitting the checkpoint dot product into accumulating `pad2` statements
  (`pad2 = tempZ * diffZ; pad2 += diffX * tempX; pad2 = -pad2`) before the
  object dot compiled but produced the same focused score, `CURRENT (870)`, and
  the same final object-load/arithmetic drift as baseline. Routing the final
  `pad + pad2` sum through the now-dead `scale` local
  (`scale = pad + pad2; diffX = -(scale / divisor)`) also compiled but left the
  focused score unchanged at `CURRENT (870)`, with the same final
  arithmetic/register-family drift. Routing the final clamped vertical value
  through the now-dead `diffX` before the `unk1BC` cast/add
  (`diffX = diffY; racer->unk1BC += (s32) diffX`) compiled but worsened to
  `CURRENT (1030)` by inserting an extra `swc1` before the final conversion
  while leaving the lateral drift unchanged. Spelling the negated checkpoint
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
  improvement and left the same final arithmetic/register drift. Adding
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
  `splinePos` carrier shape. Computing the negated checkpoint dot before the
  object-position locals, then splitting the final object dot into
  `pad = splinePos * diffX; pad += diffZ * distance`, also compiled to the
  promoted baseline shape: full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, relinked focused diff stayed `CURRENT (870)`, and
  the same final object-load/arithmetic drift remained. Do not repeat this
  split-object-dot-after-checkpoint spelling.
  Keep this function active; do not park it just because these final-offset
  probes missed.
- `trackbg_render_flashy` is active, not parked. Promoting the existing C
  compiles, but linked focused diff scores `CURRENT (1753)` in the current
  checkout and starts early in the position-array setup, so it is less localized
  than `func_80059208`.
  Rejected probes: replacing the repeated `(xSin * 1280.0f)` terms in the first
  four x/z position assignments with `scaledXSin` widened the frame to `0x168`
  and worsened the focused score to `CURRENT (12121)`; reordering the index
  5-8 x/z position stores to match the apparent target store sequence worsened
  the focused score to `CURRENT (2551)` and shifted later scheduling. Flipping
  only `xPositions[2]` to `(xSin * 1280.0f) + scaledXCos` compiled but left the
  linked focused score unchanged at `CURRENT (1808)`. Replacing only
  `xPositions[2]` with `scaledXCos + scaledXSin` compiled but worsened the
  focused score to `CURRENT (12021)` and changed the frame to `0x150`.
  Replacing the outer-ring `2.0f * scaledXCos/scaledXSin` terms with additive
  doubles (`scaledXCos + scaledXCos`, `scaledXSin + scaledXSin`) compiled but
  left the uncompressed linked diff at `CURRENT (1808)` and a promoted full
  build failed verify with CRC `0x93D338FF/0x03D9C8FE`. Adding a named
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
  the frame to `0x150`; do not repeat this single-site scaled-sine rewrite. A
  compressed `-s --compress-matching` focused diff can misleadingly print
  `CURRENT (0)` for this function; rely on the uncompressed linked diff and the
  full verify gate before accepting anything.
- `func_8002B0F4` is active, not parked. Promoting the existing C compiles, but
  linked focused diff scores `CURRENT (2780)` with broad drift starting around
  `gCurrentLevelModel` hoisting/caching and cascading through the grid loops.
  Rejected probes: inserting an empty `if (gCurrentLevelModel) {}` before the
  segment/bounding-box pointer setup worsened the linked score to
  `CURRENT (6347)` and introduced broader prologue/global-offset drift; swapping
  the setup order to compute `currentBoundingBox` before `currentSegment`
  worsened the linked score to `CURRENT (3885)` while still leaving the unwanted
  `gCurrentLevelModel` hoist; assigning `XInInt`/`ZInInt` before
  `get_inside_segment_count_xz` and passing those locals left the linked score
  unchanged at `CURRENT (2780)`; loading a local `LevelModel *levelModel`
  through a volatile pointer cast at the segment and texture access sites also
  left the linked score unchanged at `CURRENT (2780)`. Explicitly rewriting the
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
  moved-`pad3` stack-slot variant. A compressed focused diff printed stale
  `CURRENT (0)` before relink during both the 2026-05-15 packet and the
  2026-05-17 unrolled-copy probe; rely on a relinked focused diff and the full
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` gate before accepting this
  function. Keep this function active, but do not repeat those source shapes.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.
