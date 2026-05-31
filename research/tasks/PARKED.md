# Exhausted Probe Notes

Use this file for bounded source-level packets that were investigated but are
not safe to retry blindly. These notes are default-skipped by
`tools/query_goal_state.py` for routing momentum; pass `--include-exhausted`
when intentionally returning to them.

## Recorded Notes

- `func_8008FF1C` (`src/menu.c`, `NON_MATCHING`): existing C candidate is very
  close in matching mode, but promotion fails final ROM verify. Focused
  `./diff.sh -o func_8008FF1C -s --compress-matching 2 --no-pager` shows the
  real byte drift is the selected-track halfword load/branch using `v1` instead
  of target `t2`; the render-loop end symbol difference is address-equivalent
  (`gPlayerSelectVehicle` vs `gTrackSelectRenderDetails+0x90`). Probes tried:
  branch on `temp`, reorder `selectedTrack`, and assign through `temp`; each
  either kept the `v1` load or cascaded register allocation. A later
  declaration-only `register s16 temp` probe also missed: full verify failed
  with calculated CRCs `0x55C240E7/0x18E4F9B4`, focused diff stayed
  `CURRENT (10)`, and the selected-track load/branch still used `v1` instead
  of target `t2`. Later `selectedTrack` allocator probes also missed:
  changing `selectedTrack` to `s16` widened the focused diff to `CURRENT
  (1355)`, failed full verify with calculated CRCs
  `0x5B5E4609/0x72935A6E`, and introduced extra sign-extension/register churn;
  `register s32 selectedTrack` produced no object movement from the close
  baseline, stayed `CURRENT (10)`, and failed full verify with calculated CRCs
  `0x55C240E7/0x18E4F9B4`. A later plain `s32 temp` selected-track carrier
  (`temp = gTrackSelectIDs[trackY][trackX]; selectedTrack = temp`) removed the
  unsequenced-assignment warning but worsened the focused score to
  `CURRENT (935)`, failed full verify with calculated CRCs
  `0x553930E7/0x227AD4A3`, still used `v1` for the selected-track branch, and
  broadened downstream register drift. A 2026-05-17 direct table-branch
  spelling (`if (gTrackSelectIDs[trackY][trackX] != -1)`) moved the selected
  track load/branch into the target `t2` register family, but hoisted
  `cur->hubName = levelName` before the `lh` instead of scheduling it in the
  branch delay slot: full verify failed with calculated CRCs
  `0x53D440E3/0x6E70641F` and focused diff worsened to `CURRENT (125)`.
  A 2026-05-23 RHS comma-side-effect variant
  (`if (gTrackSelectIDs[trackY][trackX] != (cur->hubName = levelName, -1))`)
  collapsed into that same direct-table family: full verify failed with
  calculated CRCs `0x53D440E3/0x6E70641F`, focused diff stayed
  `CURRENT (125)`, the selected-track load/branch used target `t2`, but
  `cur->hubName = levelName` still emitted before the `lh` instead of in the
  target branch delay slot. Source was restored and final full verify passed;
  do not repeat this RHS comma-side-effect store spelling.
  Duplicating the common hub-name store inside both branch arms also missed:
  full verify failed with calculated CRCs `0xAED257D4/0xAE31DFED`, focused diff
  widened to `CURRENT (500)`, and extra `move v1,v0` / duplicate store drift
  appeared. A later compare-carrier spelling (`temp = -1; if (selectedTrack !=
  temp)`) was a no-op: full verify failed with the baseline calculated CRCs
  `0x55C240E7/0x18E4F9B4`, focused diff stayed `CURRENT (10)`, and the
  selected-track load/branch still used `v1` instead of target `t2`. Moving
  the `selectedTrack` declaration after `temp` was worse: full verify failed
  with calculated CRCs `0x55C24297/0x59444A08`, focused diff widened to
  `CURRENT (58)`, stack slots shifted, and the branch still used `v1`. Revisit
  with a source shape that keeps the direct-table `t2` load while preserving
  the target delay-slot `sw v0, 0(s0)`, not these same direct branch,
  common-store, compare-carrier, or declaration-order probes. A 2026-05-17
  comma-store dependency probe
  (`cur->hubName = (selectedTrack = ..., levelName)`) compiled but was a
  no-op from the baseline: full verify failed with calculated CRCs
  `0x55C240E7/0x18E4F9B4`, focused diff stayed `CURRENT (10)`, and the
  selected-track load/branch still used `v1` instead of target `t2`. A
  `register s16 selectedTrack` probe collapsed into the known bad
  `s16 selectedTrack` family: full verify failed with calculated CRCs
  `0x5B5E4609/0x72935A6E`, focused diff widened to `CURRENT (1340)`, added
  sign-extension/register churn, and still used `v1`; source was restored and
  final full verify passed. A 2026-05-22 post-if common-store revisit that kept
  the current `temp`/`selectedTrack` assignments but used a direct table branch
  and moved `cur->hubName = levelName` after the if/else also missed: full
  verify failed with calculated CRCs `0xD60A52B7/0xA389682F`, focused diff
  widened to `CURRENT (985)`, and the branch still used `v1` rather than
  target `t2`. Removing the two selected-track temporary assignments from that
  post-if common-store shape moved the load/branch into the target `t2` family,
  but still missed: full verify failed with calculated CRCs
  `0xDC0852B7/0x5580AC19`, focused diff was `CURRENT (975)`, and the common
  hub-name store stayed after the join (`sw s4,0(s0)`) instead of the target
  delay-slot `sw v0,0(s0)`. Source was restored and final full verify passed;
  do not repeat either post-if common-store variant. A 2026-05-24 plain
  current guarded-C promotion recheck also missed: pre-promotion
  `./diff.sh func_8008FF1C --no-pager` misleadingly reported `CURRENT (0)`,
  promoting only the `NON_MATCHING` guard failed full verify with baseline CRCs
  `0x55C240E7/0x18E4F9B4`, and relinked focused diff returned to
  `CURRENT (10)`. Source was restored and final full verify passed; do not
  accept object-only `CURRENT (0)` for this parked packet or repeat plain
  current guarded-C promotion. A 2026-05-24 current-shape selected-track
  `temp` removal probe also missed: promoting the guard and removing only the
  unused `s16 temp` declaration plus `temp = (temp =
  gTrackSelectIDs[trackY][trackX])` failed full verify with calculated CRCs
  `0x553930E7/0x227AD4A3`; relinked `./diff.sh func_8008FF1C --no-pager`
  worsened from parked baseline `CURRENT (10)` to `CURRENT (935)`. The
  selected-track load/branch shifted away from target `t2` into `v1` and
  broadened register drift through the visible-track block. Source was
  restored and final full verify passed; do not repeat this current-shape
  selected-track `temp` removal. A 2026-05-24 selected-track condition
  assignment probe (`cur->hubName = levelName; if ((selectedTrack =
  gTrackSelectIDs[trackY][trackX]) != -1)`) also missed: promoting the guard
  failed full verify with calculated CRCs `0x553930E3/0x01786EF7`, and the
  relinked focused diff regressed from parked baseline `CURRENT (10)` to
  `CURRENT (1195)`. The store moved before the selected-track load, the branch
  still used `v1` instead of target `t2`, and downstream visible-track
  register allocation shifted broadly. Source was restored, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, and `./score.sh -s`
  remained 97.30%; do not repeat this selected-track condition-assignment
  spelling. A later duplicated branch-local `hubName` store probe
  (`cur->hubName = levelName` as the first statement in both selected-track
  branch arms) also missed: full verify failed with calculated CRCs
  `0xB0D677D4/0x7578039A`, relinked focused diff regressed to
  `CURRENT (485)`, the selected-track branch still used `v1` instead of target
  `t2`, and the would-be delay-slot store became `move a1,v0` followed by a
  later `sw a1,0(s0)`. Source was restored and final full verify passed; do
  not repeat duplicated branch-local `hubName` store spellings. A sibling
  `register s32 temp` carrier also missed: promoting `func_8008FF1C` and
  changing only the existing `s16 temp` selected-track carrier to `register
  s32 temp` failed full verify with calculated CRCs
  `0x553930E7/0x227AD4A3`; relinked `./diff.sh func_8008FF1C --no-pager`
  regressed from parked baseline `CURRENT (10)` to `CURRENT (935)`, still did
  not recover the target `t2` halfword load family, and broadened visible-track
  register drift. Source was restored and final full verify passed; do not
  repeat this `register s32 temp` selected-track carrier. A 2026-05-31 xhigh
  revival worker repeated the direct-table branch with `cur->hubName =
  levelName` as the first statement in both selected/unselected arms to test
  whether the store would schedule into the target delay slot. It failed full
  verify with calculated CRCs `0xAED257D4/0xAE31DFED`; relinked focused diff
  reported `CURRENT (475)`. The selected-track load stayed in the target
  `lh t2,0(s1)` family, but the target delay-slot `sw v0,0(s0)` became `move
  v1,v0`, with extra `sw v1,0(s0)` selected-path and `sw v0,0(s0)`
  unselected-path stores and a shifted branch target. Source was restored and
  final full verify passed; do not repeat direct-table plus duplicated
  first-side-effect `hubName` store variants.
  A 2026-05-31 high worker pointer-to-selected-track-cell revival probe also
  missed: promoting `func_8008FF1C`, replacing the `s16 temp` carrier with
  `s16 *selectedTrackCell`, assigning `&gTrackSelectIDs[trackY][trackX]`
  before `level_name(level_world_id(...))`, then loading `selectedTrack =
  *selectedTrackCell` before the common `cur->hubName = levelName` failed full
  verify with calculated CRCs `0x553930E7/0x227AD4A3`. Relinked focused
  `./diff.sh func_8008FF1C --compress-matching 2 --no-pager` reported
  `CURRENT (935)`: the target delay-slot `sw v0,0(s0)` appeared, but the
  selected-track load still emitted `lh v1,0(s1)` instead of target
  `lh t2,0(s1)`. Source was restored and final full verify passed; do not
  repeat isolated pointer-to-selected-track-cell lifetime probes.
  A 2026-05-31 promoted object-slice audit reconfirmed the focused false
  positive for the restored guarded body. Promoted `build/src/menu.c.o` with
  `NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 AVOID_UB=1'`; focused
  `./diff.sh func_8008FF1C --compress-matching 2 --no-pager` reported
  `CURRENT (0)`, but full ROM verify failed with calculated CRCs
  `0xA63BE13D/0xB86942B3`. Objdump still loaded selected track with
  `lh v1,0(s1)` and branched on `v1`, not target `lh t2,0(s1)`/`t2`, so this
  remains the same selected-track register-family gap. Matching
  `build/src/menu.c.o` was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-`
  reached `Verify: OK`. Do not trust focused `CURRENT (0)` for this parked
  packet; next revival needs a mechanism that predicts the target `t2` load
  while preserving the delay-slot `sw v0,0(s0)`.

- `func_80017A18` (`src/objects.c`, `GLOBAL_ASM` via `NON_EQUIVALENT` guard):
  existing C candidate compiles in matching mode when promoted, but focused
  object diff remains far from byte-identical. Baseline promotion produced
  score `8246` with frame `0x138` instead of target `0x120`; removing dead
  `dx/dy/dz` improved to score `7950` and frame `0x130`, but still kept the
  bitmask in `ra` instead of target `s6` and shifted stack locals by `0x10`.
  Fully inlining the edge-plane locals can reach the target frame size, but
  worsens scheduling/register allocation to score `8600`. `register s32
  var_s6` did not move the bitmask into `s6`. A 2026-05-31 revival worker
  removed dead `dx/dy/dz` and moved the bitmask carrier into outer-loop control
  (`for (i = 0, var_s6 = 1; i < arg1; i++, var_s6 <<= 1)`) with the trailing
  shift removed. Full verify failed with calculated CRCs
  `0x00C3F5F7/0x853E5357`; relinked focused diff regressed to
  `CURRENT (8555)`. Frame stayed `0x130` vs target `0x120`, the bitmask
  carrier stayed in `ra` instead of target `s6`, and stack locals remained
  shifted by `+0x10`. Source was restored and final full verify passed. Revisit
  with a distinct float-temp lifetime or saved-register allocation hypothesis,
  not these same dead-local, edge-plane-inline, register-hint, or loop-control
  bitmask-carrier probes.
  A promoted object-slice audit also produced a focused false positive:
  `gmake -B NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 NON_EQUIVALENT=1
  AVOID_UB=1' CROSS=tools/binutils/mips64-elf- build/src/objects.c.o` followed
  by `./diff.sh func_80017A18 --compress-matching 2 --no-pager` reported
  `CURRENT (0)`, but full ROM verify failed with calculated CRCs
  `0xD0505FD8/0xE965F5F5`. The promoted object still used frame `0x138`
  instead of target `0x120`, with the bitmask initialized in `ra` instead of
  target `s6`. Matching-mode `build/src/objects.c.o` was restored and full
  verify passed. Do not trust focused `CURRENT (0)` for this packet without
  full ROM verify or a mechanism that predicts the target frame and bitmask
  saved-register allocation.
  A 2026-05-31 orchestration probe combined dead `dx/dy/dz` removal with
  reusing `sum2` for the closest-triangle plane check instead of the
  `A1/B1/C1/D1` edge-plane locals. The hypothesis was to reach target frame
  `0x120` while avoiding the previously rejected fully inlined edge-plane
  shape. Focused `./diff.sh func_80017A18 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`, but full ROM verify failed with calculated
  CRCs `0x0E9F297C/0xBB221418`. Source and matching-mode
  `build/src/objects.c.o` were restored. Do not repeat this combined
  dead-vector plus `sum2` edge-plane accumulator lifetime probe.

- `init_particle_buffers` (`src/particles.c`, `NON_MATCHING`): existing C
  candidate compiles in matching mode when promoted, but focused object diff
  remains a saved-register allocation mismatch. Baseline promotion produced
  score `1816` with target frame `0x68`; target keeps counts in
  `s1/s3/s7/s4/s8` and the allocator colour tag in `s2`, while current keeps
  them in `s3/s1/s7/s2/s4` and uses `s0` for the tag. Probes tried:
  `register` on the five count parameters (no object change), explicit local
  aliases for the five counts (worsened to frame `0x78`, score `3620`), and a
  local pointer-to-`gParticleTriangleBuffer` write (no useful allocation
  change, score `1824`). A 2026-05-24 fresh promotion recheck failed the full
  gate with CRCs `0xC451FA61/0xDA992566`; relinked focused diff showed score
  `2098`, with the same count allocation family (`s3/s1/s7/s2/s4`) and colour
  tag still in `s0`. Adding a named `colourTag` local initialized after
  `free_particle_vertices_triangles()` and passing it to every semitrans-grey
  allocation made no object-code movement; focused diff stayed score `2098`.
  Removing only the unused `s32 pad` local while promoting shrank the frame to
  `0x60` instead of target `0x68`, worsened focused score to `2176`, shifted
  parameter stack slots, and kept the same saved-register allocation family.
  Source was restored and full verify passed. A 2026-05-31 worker added
  `initialColourTag` only for the initial vertex and triangle buffer
  allocations. Focused `./diff.sh init_particle_buffers --compress-matching 2
  --no-pager` reported `CURRENT (0)` after promotion, but the full matching
  gate failed with calculated CRCs `0xEF29C961/0xF604264D`; source was restored
  and final full verify passed. Do not accept focused `CURRENT (0)` for this
  packet without full ROM `Verify: OK`, and do not repeat the initial-only
  colour-tag local. Revisit with a narrower saved-register/lifetime strategy,
  not these same probes or declaration-only local removals.
  A 2026-05-31 high read-only discovery pass found no safe mechanism-ready
  packet: the unresolved gap is freeing `s2` from the line-count role while
  keeping the five count parameters in the target `s1/s3/s7/s4/s8` order and
  the allocator colour tag in `s2`. Remaining ordinary-C levers collapse into
  rejected register-hint, explicit count-alias, local triangle-buffer pointer,
  named all-call colour-tag, unused-pad removal, initial-only colour-tag, or
  focused-`CURRENT (0)` acceptance families. Next useful work is promoted
  object-slice tooling around the first `mempool_alloc_safe` calls, not another
  declaration/local-carrier source probe.
  A promoted object-slice audit confirmed the false-positive focused result:
  `gmake -B NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 AVOID_UB=1'
  CROSS=tools/binutils/mips64-elf- build/src/particles.c.o` followed by
  `./diff.sh init_particle_buffers --compress-matching 2 --no-pager` reported
  `CURRENT (0)`, but full ROM verify failed with calculated CRCs
  `0x45663544/0x7C66D688`. The promoted object still assigned counts as
  `s3/s1/s7/s2/s4` and used `s0` for the `0x80808080` allocator colour tag;
  target assigns counts as `s1/s3/s7/s4/s8` and uses `s2` for the colour tag.
  Matching-mode `build/src/particles.c.o` was restored and full verify passed.
  Do not trust focused `CURRENT (0)` for this packet without full ROM verify.
