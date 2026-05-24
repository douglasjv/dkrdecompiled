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
  current guarded-C promotion.

- `func_80017A18` (`src/objects.c`, `GLOBAL_ASM` via `NON_EQUIVALENT` guard):
  existing C candidate compiles in matching mode when promoted, but focused
  object diff remains far from byte-identical. Baseline promotion produced
  score `8246` with frame `0x138` instead of target `0x120`; removing dead
  `dx/dy/dz` improved to score `7950` and frame `0x130`, but still kept the
  bitmask in `ra` instead of target `s6` and shifted stack locals by `0x10`.
  Fully inlining the edge-plane locals can reach the target frame size, but
  worsens scheduling/register allocation to score `8600`. `register s32
  var_s6` did not move the bitmask into `s6`. Revisit with a narrow float-temp
  lifetime and saved-register allocation hypothesis, not these same probes.

- `init_particle_buffers` (`src/particles.c`, `NON_MATCHING`): existing C
  candidate compiles in matching mode when promoted, but focused object diff
  remains a saved-register allocation mismatch. Baseline promotion produced
  score `1816` with target frame `0x68`; target keeps counts in
  `s1/s3/s7/s4/s8` and the allocator colour tag in `s2`, while current keeps
  them in `s3/s1/s7/s2/s4` and uses `s0` for the tag. Probes tried:
  `register` on the five count parameters (no object change), explicit local
  aliases for the five counts (worsened to frame `0x78`, score `3620`), and a
  local pointer-to-`gParticleTriangleBuffer` write (no useful allocation
  change, score `1824`). Revisit with a narrower saved-register/lifetime
  strategy, not these same probes.
