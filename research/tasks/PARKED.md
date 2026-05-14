# Parked Matching Packets

Use this file for bounded source-level packets that were investigated but not
safe to retry blindly. `tools/query_goal_state.py` skips listed function names
when recommending the next packet.

## Parked

- `func_8008FF1C` (`src/menu.c`, `NON_MATCHING`): existing C candidate is very
  close in matching mode, but promotion fails final ROM verify. Focused
  `./diff.sh -o func_8008FF1C -s --compress-matching 2 --no-pager` shows the
  real byte drift is the selected-track halfword load/branch using `v1` instead
  of target `t2`; the render-loop end symbol difference is address-equivalent
  (`gPlayerSelectVehicle` vs `gTrackSelectRenderDetails+0x90`). Probes tried:
  branch on `temp`, reorder `selectedTrack`, and assign through `temp`; each
  either kept the `v1` load or cascaded register allocation. Revisit with a
  narrower allocator/lifetime hypothesis, not the same probes.

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
