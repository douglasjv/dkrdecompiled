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
