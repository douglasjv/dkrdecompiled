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
  pressure and spilling/reshaping `spA2`. The early-zero `var_f14` probe
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
  introduce the target `$f20/$f21` prologue saves. Splitting the first speed
  magnitude into the existing `var_f2` temp
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
  target `$f20/$f21` prologue saves. Rewriting the first speed-derived upper
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
  with early zero still allocated as `$f16` instead of target `$f14`. Replacing
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
  Removing both leading pads and
  both trailing pads together with the same pre-`sqrtf` accumulation retained
  `$f20/$f21` saves but shrank the frame to `0xf0` and scored `CURRENT
  (3737)`, worse than the both-trailing-pads-only variant. Do not repeat the
  combined leading/trailing pad removal shape. Splitting the inverse-gravity
  assignment in place (`var_f20 /= 4.0; var_f20 = 1.0 - var_f20`) compiled but
  worsened the focused score from baseline `CURRENT (2550)` to `CURRENT
  (3435)` and still did not introduce the target `$f20/$f21` prologue saves.
  Do not repeat this in-place inverse-gravity spelling. Regrouping the nearby
  course-height expression as `var_f2 = gCurrentCourseHeight -
  obj->trans.y_position; var_f2 -= 50.0` compiled but worsened the focused
  score from baseline `CURRENT (2550)` to `CURRENT (3755)` and still did not
  introduce target `$f20/$f21` saves. Do not repeat this course-height grouping
  shape. Staging the misc-asset interpolation inverse fraction through the
  existing `var_f2` local
  (`var_f2 = 1.0 - var_f0; ... gCurrentRacerMiscAssetPtr[racerMiscAssetIdx] *
  var_f2`) compiled but worsened the focused score from baseline
  `CURRENT (2550)` to `CURRENT (3983)` and still did not introduce target
  `$f20/$f21` saves. Do not repeat this misc inverse-fraction staging shape. A
  linked compressed focused diff printed stale `CURRENT (0)` after object-only
  rebuild during the 2026-05-15 packet; do not accept this function without
  relink/full gate evidence. A baseline check of `func_80059208` was still
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
  Splitting the checkpoint dot product into accumulating `pad2` statements
  (`pad2 = tempZ * diffZ; pad2 += diffX * tempX; pad2 = -pad2`) before the
  object dot compiled but produced the same focused score, `CURRENT (870)`, and
  the same final object-load/arithmetic drift as baseline. Keep this function
  active; do not park it just because these final-offset probes missed.
- `trackbg_render_flashy` is active, not parked. Promoting the existing C
  compiles, but linked focused diff scores `CURRENT (1808)` and starts early in
  the position-array setup, so it is less localized than `func_80059208`.
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
  `0xF82B92BE/0x5DCC04AE`. A
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
  left the linked score unchanged at `CURRENT (2780)`. A compressed focused
  diff printed stale `CURRENT (0)` before relink during the 2026-05-15 packet;
  rely on a relinked focused diff and the full `gmake -j4
  CROSS=tools/binutils/mips64-elf-` gate before accepting this function. Keep
  this function active, but do not repeat those source shapes.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.
