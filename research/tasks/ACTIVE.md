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
  parked solely because the current source-shape families are saturated. A
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
  current-baseline threshold-local spelling. A close save-family continuation
  with x/z/y pre-`sqrtf` accumulation, chained grounded-wheel zero, steer-vel
  no-op, and removed trailing `pad3`/`pad4` tested an existing-`var_t0`
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
  full verify passed; do not repeat this early `spA2` timing spelling.
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
  Do not repeat either final `unk1BA` or `unk1BC` add-order spelling. An
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
  top-speed multiply regrouping.
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
  introduce target `$f20/$f21` prologue saves. Reordering only the promoted
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
  target `$f14` allocation together. Adding `register f32 var_f14` to this
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
  `wavePtr` pointer-walk spelling. A current-baseline local
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
  wave-bound cache. A baseline
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
  `spD4` early-zero carrier.
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
  A close save-family
  wave-reset condition probe that cached `racer->trickType` into the existing
  `racerTrickType` local before testing `racerTrickType == 1 ||
  racerTrickType == -1 || wave->rot.y < 0.4` also missed: full verify failed
  with calculated CRCs `0xB14B79CD/0x12BCEA0A`, relinked focused score worsened
  to `CURRENT (4375)`, and the diff flipped the `trickType == -1` compare from
  target `beq t1,v0` to current `beq v0,t1` while leaving the wave bound/index
  allocation reversed. Source was restored and final full verify passed; do
  not repeat this close-branch `racerTrickType` wave-reset cache.
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
  order. A baseline current-checkout wave-gate condition reorder
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
  current-checkout first-speed carrier pair through existing float locals also
  missed: using `spEC` for the pre-`sqrtf` sum failed full verify with
  calculated CRCs `0x18B44436/0x9C5E8797` and worsened the relinked focused
  diff to `CURRENT (3320)`, while using `spCC` failed full verify with
  calculated CRCs `0x5FF63A3F/0x2631AADC` and relinked focused `CURRENT
  (3210)`. Both kept `$f20/$f21` prologue saves absent, kept early zero in
  `$f16` instead of target `$f14`, and left the wave bound/index allocation as
  current `a0`/`v1` instead of target `v1`/`a0`. Source was restored and final
  full verify passed; do not repeat these current-baseline `spEC`/`spCC`
  first-speed carrier probes. A baseline
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
  check of `func_80059208` was still
  `CURRENT (870)`, with the same final-offset expression/load-order drift; do
  not repeat its recorded rejected final-block source shapes as a fallback.
  Keep the function active; do not park it just because these
  allocation/scheduling probes missed.
- `func_80059208` is active, not parked. Promoting the existing C compiles and
  focused object diff scores `CURRENT (870)`. The remaining drift is localized
  near the final lateral/vertical offset math: target preserves the negated
  `pad2 = -((tempZ * diffZ) + (diffX * tempX))` temporary and adds it to `pad`,
  while current folds the equivalent math into a subtract. Rejected probes:
  reusing the already-loaded `distance` local in the early checkpoint-scale
  divisor expression (`divisor = ((scale - distance) * splinePos) + distance`)
  produced no relinked object movement: object-only focused diff first showed
  stale prior output, full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`, and the relinked focused score stayed
  `CURRENT (870)` with the same final object-dot plus negated-checkpoint-dot
  drift. Source was restored and final full verify passed; do not repeat this
  divisor-distance reuse spelling. Other rejected probes:
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
  do not repeat this final lateral `distance` clamp-limit carrier. Making
  `pad2` volatile compiled but worsened the focused
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
  repeat this final-vertical carrier either. Routing only the final vertical
  clamp limit through the existing dead `pad3` local (`pad3 = 100.0f; if
  (diffY > pad3) ...; if (diffY < -pad3) ...`) also missed: object-only
  focused diff first printed stale `CURRENT (0)`, full verify failed with
  calculated CRCs `0x4400230F/0x7B651F08`, and the relinked focused score
  worsened from promoted-baseline `CURRENT (870)` to `CURRENT (1995)`. The
  diff inserted extra vertical-clamp float traffic, shifted the final
  object-dot/checkpoint-dot register family, and moved the epilogue labels.
  Source was restored and final full verify passed; do not repeat this final
  vertical `pad3` clamp-limit carrier. Rewriting the final lateral
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
  Source was restored and final full verify passed; do not repeat this loop
  condition cleanup.
  Spelling only the cubic-spline boolean carrier literals as
  `splineIndex = 0` and `splineIndex = 1` instead of `FALSE`/`TRUE` also
  missed: full verify failed with the baseline calculated CRCs
  `0x53D141DF/0xB9D4B481`, the relinked focused score stayed
  `CURRENT (870)`, and the same final object-dot/checkpoint-dot plus vertical
  FPR drift remained. Source was restored and final full verify passed; do not
  repeat this `splineIndex` literal boolean spelling.
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
  initial scaled multiply operand-order spelling.
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
  grouped-negated-difference spelling. Commuting only `zPositions[8]` from
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
  single-site z7 grouped-negated-difference spelling. Commuting only
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
  spelling. Rewriting only `xPositions[6]` as a grouped negated difference
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
  collapsed `var_f14` UV-scale spelling.
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
  Rewriting only the Z-grid bitmask doubling from `var_a1 *= 2` to
  `var_a1 <<= 1` also missed in the same promoted-baseline family:
  object-only focused diff first printed stale `CURRENT (0)`, full verify
  failed with calculated CRCs `0x7856718A/0x66208CAA`, and the relinked focused
  score was `CURRENT (2860)`. The diff still inserted the unwanted early
  `gCurrentLevelModel` spill at `0x60(sp)` and shifted the X/Z grid and tail
  register schedule. Source was restored and final full verify passed; do not
  repeat this Z-grid `var_a1 <<= 1` spelling.
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
  `sp108 <= 0` guard spelling. Rewriting only the outer
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
  spelling. A promoted current-source collision-output target-store-order probe
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
