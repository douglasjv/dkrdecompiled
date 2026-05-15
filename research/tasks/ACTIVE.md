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
  introduce the target `$f20/$f21` prologue saves. Keep the function active; do
  not park it just because these allocation/scheduling probes missed.
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
  compiled but worsened the focused object score to `CURRENT (1015)`.
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
  compiled but left the uncompressed linked diff at `CURRENT (1808)`. A
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
  `gCurrentLevelModel` hoist. Keep this function active, but do not repeat those
  source shapes.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.
