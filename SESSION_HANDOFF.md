# Session Handoff

- Generated at: 2026-07-09
- Branch: `master`
- HEAD: `3b1448f3`
- Completed task: `match-func-80059208`
- Summary: Imported the source-level exact match from upstream PR #742. Four
  original functions remain.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.
- `./score.sh -a 1` reports decomp progress `97.91%`, 1848 decompiled
  functions, and 4 `GLOBAL_ASM` functions remaining.
- `python3 tools/query_goal_state.py next --compact --refresh` reports 4
  guarded candidates and `recommended_next: func_8008FF1C`.
- A bounded five-minute permuter pass against the promoted `func_8008FF1C`
  candidate found only semantically invalid lower-score mutations; none were
  applied. The source was restored before the final matching build.
- A second targeted pass tested its three best advisory shapes in the real
  build. Empty `trackY`/`levelName` liveness probes either made no movement or
  enlarged the function, while an empty `trackX` probe caused a broad saved-
  register swap. A direct `cur->hubName = level_name(...)` plus direct-table
  branch selected the target `t2`, but emitted the store before the load and
  shrank the frame; immediate `levelName` liveness and a third nested `temp`
  assignment were compiler-identical to the one-register baseline. All probes
  were reverted.
- Two new `trackbg_render_flashy` probes (commuting `xPositions[2]` and swapping
  or registering the scaled-cos declaration) produced no object movement and
  were reverted before the final matching build.
- A later bounded local IDO-permuter pass found a same-size raw-cosine lifetime
  rewrite for `trackbg_render_flashy`. Real promoted-object validation improved
  from `CURRENT (1808)` to `CURRENT (1668)` with frame `0x158`; that closer
  source is retained under `NON_MATCHING`. A two-statement `xPositions[6]`
  scratch variant reached `CURRENT (1342)` but added one instruction and was
  reverted.
- A direct `func_80049794` close-save-family probe isolated the wave bound and
  index in a nested lexical block. It widened the frame to `0x100`, produced
  `CURRENT (7306)`, and moved the wave tuple to `v1/a0/v0` rather than target
  `v0/v1/a0`; it was fully reverted.
- A direct `func_80017A18` historical/current hybrid used separate plane
  pointers plus a dedicated closest-edge sum. It compiled to frame `0x130`,
  kept the mask in `ra`, and regressed to `CURRENT (8457)`; it was fully
  reverted.

## Blockers Or Unknowns

- No setup, toolchain, asset, or behavior blocker is active.
- `func_8008FF1C` remains a one-register mismatch (`v1` versus target `t2`)
  with the rest of the focused function identical.
- `trackbg_render_flashy` remains an early FPR-allocation mismatch beginning at
  target `neg.s f18,f12`; the closer promoted source still chooses `f16`.

## Ask The User Only If

- The retail baserom or extracted assets become unavailable.
- A required setup dependency cannot be restored locally.
- A behavior question cannot be resolved from code, symbols, or target asm.

## Next Work Packet

- Work directly in the primary checkout, one remaining function at a time.
- Do not recreate the previous parent/child orchestration; it was retired at
  the user's request on 2026-07-09.
- Accept only ordinary source-level C followed by the full matching build
  reaching `Verify: OK` and a refreshed score.
