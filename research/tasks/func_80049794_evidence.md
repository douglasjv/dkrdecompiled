# func_80049794 Evidence Ledger

Purpose: durable negative evidence for `func_80049794` so `research/tasks/ACTIVE.md` can stay compact. Source remains active and routable; these entries prevent blind retries of saturated source-shape families.

Current compact read:
- Guarded source: `src/racer.c` under `#ifdef NON_EQUIVALENT`.
- Original asm: `asm/nonmatchings/racer/func_80049794.s`.
- Recurring baseline after restored source: focused relinked `./diff.sh func_80049794` around `CURRENT (2760)` with target saving `$f20/$f21` in the prologue while current source usually lacks those saves.
- Repeated no-movement/saturated families include broad save/wave spelling variants, opening `updateRateF`/`var_f20` carrier variants, register storage-class hints, and promotion-only/object-only `CURRENT (0)` evidence.
- Next useful work should be a distinct compiler-mechanism hypothesis or a pivot/discovery packet, not another spelling-only microvariant.

## 2026-05-31 Promoted Object-Slice Audit

- Promoted `build/src/racer.c.o` with `NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 NON_EQUIVALENT=1 AVOID_UB=1'`; focused `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported `CURRENT (0)`, but this remains object-only evidence, not acceptance.
- Objdump showed partial target-like shape: frame `0xF8`, `ra` at `0x2c(sp)`, `s1` at `0x28(sp)`, and `s0` at `0x24(sp)`. It still lacked the target `$f20/$f21` prologue saves at `0x24/0x20(sp)`, used early zero in `$f16` instead of target `$f14`, and only partially matched the wave scan allocation (`gRacerWaveCount` into `v0`, high bound through `a0/v1`, pointer cursor in `v0`).
- Full-gate attempt with the promoted racer object did not reach ROM CRC comparison: linking failed because restored `build/src/tracks.c.o` and `build/src/object_models.c.o` reference DRM helper symbols (`drm_checksum_balloon`, `drm_vehicle_traction`) that are supplied by the matching racer object but unavailable after this promoted object slice. This is a tooling/blocker result for object-slice auditing, not a source-match result.
- Restored `build/src/racer.c.o` in matching mode and reran `gmake -j4 CROSS=tools/binutils/mips64-elf-`; the build reached `Verify: OK`.
- Do not treat promoted-object `CURRENT (0)` as useful for `func_80049794` unless the audit method can preserve/replace the racer-provided DRM helper symbols and reach the full ROM verify gate.

## Discovery Notes

- 2026-05-31 high discovery pass found no safe mechanism-ready packet. The target shape still needs frame `0xF8`, `$f20/$f21` saves at `0x24/0x20(sp)`, early zero in `$f14`, and wave scan allocation with count in `v0`, high bound in `v1`, loop index in `a0`, and pointer cursor in `v0` after `addu`. Existing rejected families already cover plain promotion, `updateRateF`/`var_f20`, `register var_f20`, carrier-width changes, branch/condition/literal spellings, wave bound/index locals, pointer-cursor wave variants, selected-wave carriers, declaration-order/register hints, early-zero carriers, first-speed carriers, and close save-family combinations. Do not reopen `func_80049794` unless a high/xhigh worker first names a new mechanism that couples the close save-family with a non-repeated wave allocation mechanism.
- 2026-05-31 follow-up high mechanism discovery found no mechanism-ready source patch. The worker forced only `build/src/racer.c.o` with `NON_EQUIVALENT` and confirmed the guarded object still saves `ra/s1/s0` at `0x2c/0x28/0x24(sp)`, does not save `$f20/$f21`, uses early zero in `$f16`, and keeps wave scan as `v0` count with `a0` high bound and `v1` loop index. Target still needs `$f21/$f20` saves at `0x20/0x24(sp)`, early zero in `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`. Focused `./diff.sh func_80049794 --compress-matching 2 --no-pager` again reported stale `CURRENT (0)`, but forced objdump contradicted it. Nonmatching full link did not reach CRC comparison due undefined `drm_vehicle_traction` and `drm_checksum_balloon`; restored matching-mode full `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`. Keep cooldown-routed until a new mechanism couples the close save-family with non-repeated wave allocation movement.
- 2026-06-12 high mechanism-discovery found no complete non-repeated mechanism packet. Evidence checked by child lane `019ebdf5-05f4-7b32-ba6f-03c838420dee`: this ledger, `ACTIVE.md`, `MECHANISM_PACKETS.md`, selector `next`/`tooling`, packet template, current guarded `src/racer.c` body, target asm at `asm/nonmatchings/racer/func_80049794.s`, and older child evidence `1e9cccf5`. Child baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK` after local ignored setup links and `./score.sh -s` stayed decomp `97.30%`, docs `65.47%`. The target still requires coupled movement: frame `0xF8`, `$f21/$f20` saves at `0x20/0x24(sp)`, early zero in `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`; no ordinary-C mechanism beyond the rejected saved-FPR, `updateRateF`/`var_f20`, carrier-width, branch/condition/literal, wave-bound/index, pointer-cursor, selected-wave, declaration-order/register-hint, early-zero, first-speed, boost-duration, close-save-family, focused-`CURRENT (0)`, or object-slice families was identified. Child committed evidence `1aa2b9d1`, imported at `research/tasks/child_threads/func_80049794_2026-06-12_mechanism_discovery.md`. Keep cooldown-routed until a genuinely distinct mechanism predicts both saved-FPR and wave-allocation movement.
- 2026-07-09 direct scoped-wave probe: on the known close save-family
  (pre-`sqrtf` x/z/y accumulation, chained grounded zero, steer no-op, and no
  trailing `pad3`/`pad4`), the wave scan used fresh block-scoped `waveLast` and
  `waveIndex` locals. This distinct symbol-lifetime hypothesis failed its stop
  condition: full verify failed with calculated CRCs
  `0xEA2C6E12/0x5960F066`, relinked focused diff was `CURRENT (7306)`, and the
  frame widened to `0x100`. Although `$f20/$f21` saves remained, early zero
  stayed in `$f16`; the wave tuple colored as count `v1`, bound `a0`, and index
  `v0`, not target count `v0`, bound `v1`, index `a0`. Source was restored. Do
  not repeat block-scoped/shadow wave locals on the close save-family.
- 2026-07-09 third-pass close-family audit: the unscoped close-save source
  itself reached exact frame `0xF8`, `$f21/$f20` saves, early `$f14`, and
  target store order. Its full-build CRCs were `0xB8DD79CD/0xE47454ED` and
  focused diff was `CURRENT (4365)`. The remaining early wave drift is now
  isolated precisely: target uses `v0=count`, copies `v1=count-1` as a stable
  bound, copies that to mutable `a0`, then reuses `v0` as the pointer cursor;
  current keeps stable `a0` and mutable `v1`. Existing `var_v0`/`var_v1`
  transfers, declaration order, post-loop no-op lifetimes, `pad5` or
  `racerSteerAngle` bound reuse, and separate index carriers all rotated into
  worse `v1/a3/a0/v0`, `v1/a0/v0`, or `v1/a1/v0` families. Source was not
  retained. Reopen only with a mechanism that reverses the initial copy
  direction to `v1=count-1; a0=v1` while preserving `v0` pointer induction;
  do not retry scoped locals or these existing-local carrier variants.
- 2026-07-09 precedent search: the exact target `addiu v1,v0,-1; move a0,v1`
  chain appears only in this function. Closest matching source
  `func_8001E4C4` emits the opposite mutable-first/stable-copy ownership, and
  `ghostmenu_render` has the arithmetic prefix but no decrementing pointer
  loop. A dedicated bound lifetime based on that precedent still produced
  `v1/a0/v0` and pointer recomputation. Reopen only with an external IDO
  example that combines stable-first bound copy with pointer induction.

## Extracted ACTIVE Notes

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 forked-worker update-rate lifetime pressure miss. The worker
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only the opening
  update-rate path from direct `updateRateF *= 1.09` to
  `var_f20 = updateRateF; if (func_8000E138()) var_f20 *= 1.09; updateRateF =
  var_f20;`, targeting `$f20/$f21` saved-FPR pressure. The object-only focused
  diff first reported stale `CURRENT (0)`, but full verify failed with
  calculated CRCs `0xF2024655/0xB090BDA2`; relinked focused diff regressed to
  `CURRENT (8849)`. The probe still did not recover target `$f20/$f21`
  prologue saves, spilled/reloaded `updateRateF` through stack, shifted saved
  GPR slots, moved early zero into `$f18`, and broadened wave scan/register
  drift from target `v1`/`a0` into current `a0`/`v1`. Worker source was
  restored. Do not repeat this `updateRateF` through `var_f20` carrier; next
  `func_80049794` work needs a distinct saved-FPR/register-pressure source
  shape, or pivot to another live candidate.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 promoted `register f32 var_f20` storage-class hint missed. The
  source changed the `NON_EQUIVALENT` guard to `#if 1` and changed only
  `f32 var_f20;` to `register f32 var_f20;`, targeting the missing target
  `$f20/$f21` prologue saves. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  `CURRENT (2760)`. The diff still lacked target `$f20/$f21` prologue saves,
  kept early zero in current `$f16` instead of target `$f14`, and left the wave
  scan in the current `a0`-bound/`v1`-loop family. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3 tools/check_active_surface.py`
  reported active surface ok. Do not repeat this `register f32 var_f20`
  storage-class hint; next `func_80049794` hypothesis needs a distinct
  saved-FPR lifetime/wave allocation source shape, or pivot to another live
  candidate.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 promoted wave-scan top-bound carrier spelling missed. The worker
  changed the `NON_EQUIVALENT` guard to `#if 1`, introduced
  `var_v1 = gRacerWaveCount - 1`, initialized `var_a0 = var_v1`, and compared
  `if (var_a0 == var_v1)` to try to recover the target `v1` top bound with
  `a0` as the decrementing loop index. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x5790053C/0x1C8C0179`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (5755)`. The source shape still dropped target `$f20/$f21` prologue
  saves and kept early zero in `$f16` instead of `$f14`; the wave scan moved
  to current `v1` count / `a3` top-bound / `v0` loop-index allocation with
  repeated `sll`/`addu` pointer recomputation, not the target `v1` bound /
  `a0` decrement / pointer-decrement family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok. Do not repeat this explicit `var_v1` top-bound carrier spelling;
  next `func_80049794` hypothesis needs an independent saved-FPR lifetime
  source shape, or pivot to another live candidate.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 promoted update-rate guard `== TRUE` spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (func_8000E138())` as `if (func_8000E138() == TRUE)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x2B9B7CEA/0xA911238B`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` regressed to `CURRENT (5760)`. The
  equality-to-TRUE branch emitted `li t2,1`/`bne v0,t2`, dropped the target
  `$f20/$f21` prologue saves, shifted saved GPR slots down, kept early zero in
  current `$f16` instead of target `$f14`, and left the wave scan in the
  current `a0`-bound/`v1`-loop family. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok. Do not repeat this `func_8000E138() == TRUE` update-rate guard
  spelling; next `func_80049794` hypothesis should target wave bound/index
  allocation while preserving known no-spill close save-family evidence, or
  pivot to another live candidate.

- Latest worker-packet note: `func_80049794` remains active after a
  2026-05-25 forked-worker `var_v1`/`var_a0` declaration-order spelling
  missed. The worker changed the `NON_EQUIVALENT` guard to `#if 1` and swapped
  only the local declarations from `s32 var_v1; s32 var_a0;` to
  `s32 var_a0; s32 var_v1;`, targeting saved-FPR pressure and the early wave
  bound/index allocation. Worker full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and left the wave scan with current `a0` as bound and `v1` as
  loop index instead of target `v1` bound and `a0` loop index. Worker source
  was restored with no patch applied here; main checkout `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok. Do not repeat this `var_v1`/`var_a0` declaration-order spelling;
  next `func_80049794` hypothesis needs an independent saved-FPR lifetime
  source shape, or a pivot to another bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 promoted explicit update-rate guard spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (func_8000E138())` as `if (func_8000E138() != FALSE)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and left the wave scan in the current bound/index family.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok. Do not repeat this
  explicit `func_8000E138() != FALSE` update-rate guard spelling; next
  `func_80049794` hypothesis needs a distinct saved-FPR/wave allocation fix,
  or pivot to another bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-25 promoted normal-flight `trickType == +/-2` branch-order spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote
  only `else if (racer->trickType == 2 || racer->trickType == -2)` as
  `else if (racer->trickType == -2 || racer->trickType == 2)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0xDFDFE9E6/0xFD85A953`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` stayed at
  promoted baseline `CURRENT (2760)`. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and left the wave scan in the current bound/index family.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok. Do not repeat this
  `trickType == -2 || trickType == 2` branch-order spelling; next
  `func_80049794` hypothesis needs a distinct saved-FPR/wave allocation fix,
  or pivot to another bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted normal-flight pitch pre-shift spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1`, hoisted the shared
  `x_rotation` damping subtraction before the `R_TRIG` branch, materialized
  `var_t0 >>= 1`, and used `var_t0 * 19/30 * updateRate` in the branch terms.
  Pre-build `./diff.sh func_80049794 --compress-matching 2 --no-pager`
  misleadingly reported `CURRENT (0)`, but full verify failed with calculated
  CRCs `0x7CE05375/0x7BE89A6A`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` stayed at `CURRENT (2480)`, the same as the
  known pitch factor-out family. The target frame `0xF8` still kept `$f20/$f21`
  prologue saves absent from current, the early zero still had `$f16/$f14`
  drift, and the wave scan still had the bound/index registers reversed.
  Source was restored, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat this
  pre-shifted `var_t0` pitch-input spelling. Future `func_80049794` pitch
  factor-out combinations need a distinct saved-FPR/wave allocation fix, or
  pivot to another bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted saved-FPR/register-pressure double-carrier spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and changed
  only the main `var_f20` declaration from `f32 var_f20` to
  `double var_f20`. Pre-build `./diff.sh func_80049794 --compress-matching 2
  --no-pager` misleadingly reported `CURRENT (0)`, but full verify failed with
  calculated CRCs `0xABC4F62A/0x9D55B713`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` worsened to
  `CURRENT (14812)`. The frame widened from target `0xF8` to current `0x108`,
  the target `$f20`/`$f21` prologue saves were still absent, and broad wave,
  steering, boost, and tail FPR scheduling drift expanded. Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat this
  whole-function `var_f20` double-carrier spelling. Next hypothesis should
  avoid broad `func_80049794` carrier-width changes and use a narrower saved-FPR
  lifetime/register-pressure question, or pivot to another bounded routable
  packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted wave-scan last-index split spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1`, assigned
  `var_v1 = gRacerWaveCount - 1`, used `for (var_a0 = var_v1; ...)`, and
  compared `if (var_a0 == var_v1)` instead of recomputing
  `gRacerWaveCount - 1`. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`;
  promoted baseline full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`, while the split-index probe failed with calculated
  CRCs `0x5790053C/0x1C8C0179`. Relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` worsened from promoted baseline
  `CURRENT (2760)` to `CURRENT (5755)`, spilling `spA2` to `0xA2(sp)` and
  shifting the wave-scan temporaries farther from target (`v1/a0` target
  remained `a3/v0`/extra address arithmetic in current). Source was restored,
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat this
  wave-scan last-index split spelling. Next hypothesis should avoid
  `func_80049794` wave-scan split-index/register-shape microvariants unless
  paired with a distinct saved-FPR/register-pressure fix, or pivot to another
  bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted late boost-emitter high-split compare spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (var_t0 >= 10)` as `if (var_t0 > 9)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` stayed at promoted baseline
  `CURRENT (2760)`. The split compare produced no useful movement, and the
  diff retained the known missing target `$f20`/`$f21` prologue saves, early
  zero in current `$f16` instead of target `$f14`, and wave scan
  `a0`-bound/`v1`-loop drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this late boost-emitter `var_t0 > 9` spelling.
  Next hypothesis should avoid `func_80049794` late boost-emitter high-split
  compare, vehicle-particle guard operand-order, magnetTimer truthy, final
  `spA1`/`unk201` tail booleans, saved-FPR/wave-scan microvariants, early
  grounded-zero carriers, and throttle/brake literals unless paired with a
  distinct saved-FPR/register-pressure fix, or pivot to another bounded
  routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted final vehicle-particle guard operand-order spelling
  missed. The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote
  only `if (racer->vehicleIDPrev < VEHICLE_BOSSES)` as
  `if (VEHICLE_BOSSES > racer->vehicleIDPrev)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` stayed at promoted baseline
  `CURRENT (2760)`. The tail guard produced no useful movement, and the diff
  retained the known missing target `$f20`/`$f21` prologue saves, early zero in
  current `$f16` instead of target `$f14`, and wave scan
  `a0`-bound/`v1`-loop drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this vehicle-particle guard operand-order spelling.
  Next hypothesis should avoid `func_80049794` vehicle-particle guard
  operand-order, magnetTimer truthy, final `spA1`/`unk201` tail booleans,
  saved-FPR/wave-scan microvariants, early grounded-zero carriers, and
  throttle/brake literals unless paired with a distinct
  saved-FPR/register-pressure fix, or pivot to another bounded routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted magnetTimer truthy spelling missed. The source changed
  the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  `if (racer->magnetTimer != 0)` as `if (racer->magnetTimer)`. Pre-build
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` misleadingly
  reported `CURRENT (0)`, but full verify failed with calculated CRCs
  `0x5FDDE03F/0xEF7A0514`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` stayed at the promoted baseline
  `CURRENT (2760)`. The magnet override condition produced no useful
  movement, and the diff retained the known missing target `$f20`/`$f21`
  prologue saves, early zero in current `$f16` instead of target `$f14`, and
  wave scan `a0`-bound/`v1`-loop drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this magnetTimer truthy spelling. Next hypothesis
  should avoid `func_80049794` magnetTimer truthy, save/wave microvariants,
  early grounded-zero carriers, and throttle/brake literals unless paired with
  a distinct saved-FPR/register-pressure fix, or pivot to another bounded
  routable packet.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-probed pitch factor-out plus explicit `x_rotation_vel`
  self-assignment spelling missed. The worker promoted the `NON_EQUIVALENT`
  guard to `#if 1`, hoisted the shared normal-flight pitch damping subtraction
  before the `R_TRIG` branch, and changed only
  `racer->x_rotation_vel -= (racer->x_rotation_vel * updateRate) >> 4` to
  `var_v1 = racer->x_rotation_vel; racer->x_rotation_vel = var_v1 -
  ((var_v1 * updateRate) >> 4)`. Full relink/build failed with calculated
  CRCs `0x81BCA331/0x35054A7B`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` reported `CURRENT (2480)`, identical to
  the prior pitch factor-out-only family. The diff still lacked target
  `$f20/$f21` prologue saves, kept early zero in current `$f16` instead of
  target `$f14`, and retained the known wave scan drift. Worker restored
  `src/racer.c` and verified `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  reached `Verify: OK`; do not repeat pitch factor-out plus explicit
  `x_rotation_vel` self-assignment.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted late velocity store-order spelling missed. The source
  changed the `NON_EQUIVALENT` guard to `#if 1` and reordered only the final
  post-physics stores from `obj->x_velocity = var_f20; obj->z_velocity =
  spEC;` to `obj->z_velocity = spEC; obj->x_velocity = var_f20;`. Full verify
  failed with calculated CRCs `0x5FDDE03F/0x4C176571`; relinked `./diff.sh
  func_80049794 --compress-matching 2 --no-pager` stayed at the promoted
  baseline `CURRENT (2760)`. The late velocity store region produced no
  useful movement, and the diff retained the known missing target `$f20`/`$f21`
  prologue saves, early zero in current `$f16` instead of target `$f14`, and
  wave scan `a0`-bound/`v1`-loop drift. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this late velocity store-order spelling.

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 worker-probed early wave count-down-derived-index spelling
  missed. The worker changed the `NON_EQUIVALENT` guard to `#if 1`, scanned
  with `var_v1 = gRacerWaveCount` and `gRacerCurrentWave[var_v1 - 1]`, then
  derived `var_a0 = var_v1 - 1`. Full verify failed with calculated CRCs
  `0xA80DF324/0x1C0D36A7`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` regressed to `CURRENT (6300)`. The wave
  scan allocated around `a1/v1` with extra derived-index work instead of target
  `v0` count, `v1` bound, and `a0` loop index; target `$f20/$f21` prologue
  saves were still missing, and early zero stayed in current `$f16` instead of
  target `$f14`. Worker restored `src/racer.c`, verified `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and parent `python3
  tools/check_active_surface.py` reported active surface ok; do not repeat
  this wave count-down-derived-index spelling.

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

- Latest selector-packet note: `func_80049794` remains active after a
  2026-05-24 promoted initial grounded-wheel boolean guard spelling missed.
  The source changed the `NON_EQUIVALENT` guard to `#if 1` and rewrote only
  the early zeroing guard from `if (racer->groundedWheels > 0)` to
  `if (racer->groundedWheels)`. Pre-build `./diff.sh func_80049794
  --compress-matching 2 --no-pager` misleadingly reported `CURRENT (0)`, but
  full verify failed with calculated CRCs `0x5FDDE03F/0x408C160F`; relinked
  `./diff.sh func_80049794 --compress-matching 2 --no-pager` regressed to
  `CURRENT (2960)`. The guard changed away from target `blez` to `beqz`, kept
  early zeroing in current `$f16` instead of target `$f14`, and did not recover
  the target `$f20`/`$f21` prologue saves. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, `./score.sh -s`
  remained 97.30%, and `python3 tools/check_active_surface.py` reported active
  surface ok; do not repeat this initial grounded-wheel boolean guard spelling.

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
