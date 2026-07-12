# Session Handoff

- Generated at: 2026-07-10
- Branch: `master`
- Integrated checkpoint: upstream merge `59674774` plus this evidence update
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
- Residual discovery now uses `tools/find_residual_mechanisms.py` with four
  structured signatures. Unit tests prove destructive and nondestructive GPR
  edges remain distinct and FPR identities survive normalization. The verified
  ELF integration control rediscovers the known menu trophy-race address DAG,
  while default known-reference suppression yields no false novel menu hit.
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
- Merged upstream `0adab627` (documentation/rename for already matched
  `func_8002B0F4`); full matching validation still reaches `Verify: OK` and
  the guarded count remains 4.
- A new objects pass rejected radius-first ordering and found only a
  nonmaterial `7869 -> 7864` sum-grouping movement with the same missing
  `f18/f20/f22` lifetime. A new track pass ruled out all-raw trig and named-
  carrier order as mechanisms. Neither source was changed.
- The corrected menu permuter used real IDO `-O2 -mips1` for 275 seconds and
  found no improvement over `CURRENT (10)`; its observable tail covered 1,696
  iterations. External racer and track searches found no independent C-source
  precedent for their remaining allocation cycles. The guards remain intact.
- A follow-up tested four distinct compiler mechanisms. Menu full-index
  materialization creates the needed interference edge but colors it
  `t8/t9/t3`; track's `CURRENT (1342)` shape requires one extra array store;
  objects retry copies add `0x10` of frame; racer expression sharing either
  normalizes away or disrupts the correct count/pointer roles. No guarded C
  body was changed.
- A deterministic menu search covered all 226 adjacent/single-move declaration
  orders, every one of 16,384 `register` subsets over active locals, and 23
  staged/embedded index expressions. None improved the two-word `CURRENT (10)`
  frontier. A historical-context audit confirmed identical compiler/tool/type/
  layout inputs and reproduced the same miss even before API-name adaptation.
- Further finite searches covered 217 menu cast placements, all 17 possible
  independent track-store barriers, and all 27 mixed per-axis objects retry
  carriers. None improved a retained checkpoint under its target frame/size/
  register constraints; no guarded source body changed.
- The next pass completed 4,536 racer loop-header variants and 42 objects
  ownership/order bodies, with no target tuple or FPR completion. Track's
  actual later fakematch assignment has no independently removable one-
  instruction RHS; manual review rejected an apparent exact-size probe that
  had accidentally changed live behavior. No source was promoted.
- Browser family inspection found current public improvements. Exact `oR9oG`
  racer source is retained under `NON_EQUIVALENT` and improves the authoritative
  shared linked diff to `CURRENT (2905)` while preserving frame `0xF8` and
  early `f14`; it remains nonexact. Objects `96Vzj` was rejected after semantic
  validation exposed mask corruption and wrong steep-correction coordinates.
- A 64-way real-IDO racer lifetime/padding matrix collapsed to 12 objects and
  did not improve retained `CURRENT (2905)`. Split square-root expressions
  recovered `f21/f20` saves but over-shrank the function; chained-zero and
  unused-pad variants supplied no missing allocation mechanism.
- A racer instruction-count audit found a five-instruction target gap: four
  saved-FPR save/restores plus target-only `move t0,v1` in the `trickType ==
  +/-1` update. Sixteen semantic old-value/update carrier variants failed to
  emit the move or recover the saved-FPR pair; the plain copy was byte-identical
  to the retained source.
- A bounded four-worker racer permuter pass stopped at about 240 seconds and
  found only a ten-point advisory improvement (`5016 -> 5006`). No semantic
  candidate was promoted; authoritative linked `CURRENT (2905)` remains the
  racer checkpoint.
- A fresh menu address-DAG search did not improve `CURRENT (10)`. A bounded
  32-variant mechanism matrix plus pointer-owner, fake-lifetime, type/shape,
  and coupled selected-track/index crosses preserved the exact branch region
  in several forms but never produced target `t4/t5`. The best coupled web
  split instead colored the separate address node `t6/t7` or `t8/t9`; no menu
  source change was retained.
- A track FPR-graph audit identified the exact spill cycle: target keeps
  negative cosine `f18` and doubled sine `f16` while spilling doubled cosine;
  current does the opposite. Reusing the existing `var_f16` for doubled sine
  reproduces target colors but is actually `0x970`, eight bytes over target;
  the earlier exact-size record was corrected. Its scheduling remains advisory
  `3489`, with best chained cross `2879`. A 32-variant chained-pair matrix and 29
  tail-order variants found no improvement over retained linked
  `CURRENT (1668)`; no track source change was retained.
- A ten-position carrier-placement sweep confirmed every doubled-sine
  assignment seam remains `0x970`. The predicted placement between
  `xPositions[3]` and `zPositions[3]` loses the target register colors, while
  crossing the exact-color carrier with `zPositions[0]`-first ordering links at
  `CURRENT (4404)`. This scheduler family is closed; retained track source is
  unchanged.
- `func_80017A18` now retains a coupled `Vec3f origin` representation. In the
  current authoritative promoted tree it improves linked score `7934 -> 7794`
  while preserving exact frame `0x120`, size `0x444`, result `sp+0xF8`, and
  saved-GPR ownership. Historical source and target asm prove its remaining
  six-instruction size gap is exactly three origin spills and three reloads at
  the retry boundary. Scoped-copy and pointer-cursor crosses missed the frame/
  GPR constraints. A target-dataflow audit also shows the final source must
  cache target A/C products for gentle slopes; that correction currently
  regresses and was not retained.
- A corrected function-local racer audit showed that the earlier x-velocity
  and mixed-old-value positives were object-wide false hits: the `0x28B8`
  x-velocity-owner function has no `f21/f20` saves, and the mixed-owner
  `+/-1` path has no `move t0,v1`. Exact asymmetric and branch-local copies
  coalesce. Split square-root source does genuinely recover `f21/f20` at frame
  `0xF8`, but shrinks text to `0x2890`; register/declaration variants do not
  grow it, and the behavior-safe x-velocity cross reaches only `0x28A0` versus
  target `0x290C`. Retained `0x28F8`, linked `CURRENT (2905)` source remains
  unchanged.
- A live refresh of all four public scratch families found no source better
  than the retained local checkpoints. The newest distinct objects packet
  tested retained `Vec3f origin` assignments directly inside the historical
  `do` placement. It keeps frame `0x120` and size `0x444` but regresses linked
  score `7794 -> 8684`, moves the mask to `ra`, and does not emit target
  `f18/f20/f22` retry phis. Behavior-correct target products and a matched-code
  outer co-induction cross regress to `9396` and `9816`; none is retained.
- A resumed objects retry packet found no promotable contained GPR repair.
  Duplicate outer/inner origin loads, mask `register`, empty liveness, and a
  mask+origin+hit aggregate all remain `0x444` or shrink while selecting mask
  `ra` and origin bases `s6/s7/s8`. A retained-Vec-to-retry-Vec copy preserves
  saved GPRs but widens the frame to `0x130`, moves the result to `sp+0x108`,
  and grows text to `0x464`. A tempting `0x45C` copied object was confirmed
  asm-backed by its `func_80017A18.NON_MATCHING` symbol, not C output.
- A fresh menu allocator packet tested short-circuit row-base placement,
  conditional identity expressions, existing-value row/index reuse, and a
  nonlocal index-to-menu-ID web. None preserves the exact function while
  producing target `t4`: exact-size identities remain `CURRENT (10)`, edge
  placement shrinks or broadens the function, and the exact-size nonlocal web
  changes 132 instructions. The retained menu source remains unchanged.
- The final dead-owner menu cross was also exhausted. Chaining unused `pad2`
  or `temp` to the correct selected-cell load yields the exact retained object
  hash and same `t3/t3` address pair. Late row-base liveness widens text to
  `0x5DC`/`0x5E4`; nested selected-cell self-assignment loses target `t2`;
  statement-order and volatile-pointee variants are identical or disturb the
  target delay slot. No menu source change was retained.
- The last distinct typed-owner menu mechanisms also missed. Two-field
  aggregates (both field orders) and a union overlay preserve exact size
  `0x5CC` but recolor the address chain to `t8/t9/t3`; enum owners and reusing
  unused parameter `updateRate` produce the rejected `t3/t8/t9` family. Nearby
  matching trophy-menu functions prove direct indexing can emit a
  non-destructive three-register chain, but that already-tested shape does not
  coexist with this function's exact earlier `t2` web. No source was retained.
- The remaining track doubled-sine identity crosses also missed. A scalar
  assignment embedded at first use keeps exact `0x968` size but leaves the
  retained FPR cycle unchanged. A fresh block-local carrier is `0x970` and
  loses target colors. Keeping the proven early `var_f16` target-color carrier
  while moving the later UV lifetime to `pad_sp100` still emits `0x970`, so
  the extra two instructions are not caused by same-symbol coupling. No source
  was retained; destructive `xSin` reuse was rejected as behavior-invalid.
- The remaining objects aggregate/CFG provenance probes missed. Marking the
  retained `Vec3f origin` as `register` is object-identical. A behavior-neutral
  mask comma-read on the first in-`do` origin load is removed before register
  allocation and cannot rotate mask/origin GPRs, in either aggregate or scalar
  form. Replacing the retry `do/while` with an explicit label/backedge keeps
  frame `0x120` and the exact saved-GPR family but emits `0x450` text without
  target `f18/f20/f22` retry spills/reloads. No source was retained.

## Blockers Or Unknowns

- No setup, toolchain, asset, or behavior blocker is active.
- `func_8008FF1C` matches the prior `t2` region and remains a one-temporary
  coalescer mismatch at `0x90CD4`; scalar, pointer, aggregate, union, enum, and
  parameter-owner mechanisms are now all represented in its evidence ledger.
- `trackbg_render_flashy` remains an early FPR-allocation mismatch beginning at
  target `neg.s f18,f12`; the closer promoted source still chooses `f16`.

## Ask The User Only If

- The retail baserom or extracted assets become unavailable.
- A required setup dependency cannot be restored locally.
- A behavior question cannot be resolved from code, symbols, or target asm.

## Next Work Packet

- Work directly in the primary checkout, one remaining function at a time.
- Run `python3 tools/query_goal_state.py tooling --compact`, then use its
  `residual_helper` command to mine matched C precedents before selecting a new
  source mechanism. Add genuine precedents to the signature metadata only
  after inspecting their source and compiled window.
- Do not recreate the previous parent/child orchestration; it was retired at
  the user's request on 2026-07-09. Focused, disposable subagents are allowed
  when they reduce search latency.
- Accept only ordinary source-level C followed by the full matching build
  reaching `Verify: OK` and a refreshed score.
