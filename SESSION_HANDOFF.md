# Session Handoff

- Generated at: 2026-07-09
- Branch: `master`
- Integrated checkpoint: `1d7378e1`
- Current task: remaining-function source checkpoints
- Summary: Retained stronger guarded candidates for `func_8008FF1C`,
  `trackbg_render_flashy`, and `func_80017A18`. Four original functions still
  remain.

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
- A public-source audit checked all 40 GitHub forks. JordanLongstaff commit
  `9f420e1d` was the only claimed newer match. After adapting renamed APIs, its
  source has exact frame `0x80` and size `0x5CC`, fixes the prior selected-track
  `t2` gap, and leaves only target `addu t4,t3,s2; addu s1,t4,t5` versus
  current `addu t3,t3,s2; addu s1,t3,t5` (`CURRENT (10)`). Rebuilding the
  historical fork reproduces the same miss. The closer source is retained
  under `NON_MATCHING`; matching mode reaches `Verify: OK`.
- A second `trackbg_render_flashy` pass tested roughly 70 isolated variants.
  None changed the global target/current FPR color cycle while preserving frame
  `0x158` and exact size, so the retained real `CURRENT (1668)` checkpoint
  remains best.
- The current 16-member decomp.me family for `func_80017A18` exposed newer
  scratch `Mw8Na`. Its retained A2/C2 derivative improves the real linked diff
  from `CURRENT (8246)` to `CURRENT (7869)` and recovers exact frame `0x120`,
  result slot `sp+0xF8`, and the complete target saved-register family. It
  remains guarded; matching mode reaches `Verify: OK`.
- A third racer pass reproduced the close-save family at exact frame `0xF8`,
  `$f21/$f20` saves, early `$f14`, and `CURRENT (4365)`. Distinct existing-
  local and bound-carrier probes could not reverse the residual stable-bound
  `a0` / mutable-index `v1` pair into target `v1` / `a0`, so no racer source
  change was retained.
- A third menu IR pass proved that nearby address-of/index-assignment precedent
  can prevent the final temporary coalescing, but global coloring moves the
  result to `t8` rather than target `t4`; no additional menu source was kept.
- Final bounded precedent searches found no in-repo example for either the
  menu signed-byte indexed load with `t4/t5` plus across-call pointer reuse or
  the racer stable-first `v1 -> a0` bound copy plus pointer induction. The
  retained guarded sources and matching `Verify: OK` state were preserved.

## Blockers Or Unknowns

- No setup, toolchain, asset, or behavior blocker is active.
- `func_8008FF1C` now matches the prior `t2` region and remains a one-temporary
  mismatch at `0x90CD4`: current coalesces the address result into `t3`, while
  target allocates `t4`.
- `trackbg_render_flashy` remains an early FPR-allocation mismatch beginning at
  target `neg.s f18,f12`; the closer promoted source still chooses `f16`.

## Ask The User Only If

- The retail baserom or extracted assets become unavailable.
- A required setup dependency cannot be restored locally.
- A behavior question cannot be resolved from code, symbols, or target asm.

## Next Work Packet

- Work directly in the primary checkout, one remaining function at a time.
- Do not recreate the previous parent/child orchestration; it was retired at
  the user's request on 2026-07-09. Focused, disposable subagents are allowed
  when they reduce search latency.
- Accept only ordinary source-level C followed by the full matching build
  reaching `Verify: OK` and a refreshed score.
