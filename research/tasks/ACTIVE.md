# Active Matching Surface

## Goal Context

- End goal: every original Diddy Kong Racing function has source-level C that keeps the matching ROM byte-identical.
- Loop: `research/tasks/GOAL_LOOP.md`.
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`.
- Exhausted probe notes: `research/tasks/PARKED.md`; these notes prevent blind retries, but they are not an off-limits list and are not skipped from routing. Every remaining function must stay routable through the heartbeat parent / single child lane pattern until 100 percent byte matching is reached.
- Default work: bounded `matching_impl` packets against one `GLOBAL_ASM`, `NON_MATCHING`, or `NON_EQUIVALENT` target.
- Default validation: `gmake -j4 CROSS=tools/binutils/mips64-elf-` in matching mode, then focused `./diff.sh <function>` only for diagnosis.
- Parent correction on 2026-06-12: child lanes must not be closed out for
  negative evidence alone. Negative evidence is a checkpoint for routing and
  mechanism discovery; the same child lane remains active until its assigned
  function byte-matches and commits source-level C, unless a true
  setup/toolchain/assets/unresolved-behavior blocker is recorded.

## Current Route

- Direct-mode update on 2026-07-09: imported the exact source match for
  `func_80059208` from upstream PR #742 as local commits `6a185583` and
  `3ee245dd`. Full matching validation reached `Verify: OK`; decomp progress is
  `97.91%`, and the refreshed selector reports 4 guarded candidates. The user
  retired the parent/child orchestration layer; continue directly in the
  primary checkout with one bounded source function at a time.
- Direct-mode `trackbg_render_flashy` update on 2026-07-09: a bounded local IDO
  permuter pass found a same-size raw-cosine lifetime shape that improved the
  promoted real-object diff from `CURRENT (1808)` to `CURRENT (1668)` while
  preserving frame `0x158`. The closer source is retained under
  `NON_MATCHING`; matching mode remains asm-backed and must still reach
  `Verify: OK`. A generated array-slot split reached `CURRENT (1342)` but
  added one instruction and shifted the rest of the object, so it was rejected.
- Direct-mode `func_8008FF1C` update on 2026-07-09: audited all 40 public forks
  and adapted JordanLongstaff commit `9f420e1d`, the only claimed newer match.
  The source is retained under `NON_MATCHING` because it fixes the prior
  selected-track `t2` load/branch/delay-slot gap and leaves only a two-
  instruction `t4` versus `t3` address-temporary drift (`CURRENT (10)`) with
  exact frame `0x80` and size `0x5CC`. Rebuilding the historical fork confirms
  that its claimed match has the same drift. Matching mode is restored and
  reaches `Verify: OK`; continue from
  `research/tasks/func_8008FF1C_2026-07-09_external_checkpoint.md`.
- Focused subagents are permitted for bounded source searches and public-source
  audits when useful, but integrate results directly in the primary checkout;
  do not recreate the retired heartbeat/child-ledger orchestration layer.
- Direct-mode `func_80017A18` update on 2026-07-09: the newest 16-member
  decomp.me family exposed scratch `Mw8Na` (`5971` standalone). A retained
  Mw8Na-derived A2/C2 source recovers exact frame `0x120`, result slot
  `sp+0xF8`, and the complete target saved-register family. The authoritative
  promoted linked diff improves from `CURRENT (8246)` to `CURRENT (7869)` but
  still fails CRC, so the body remains under `NON_EQUIVALENT`; matching mode
  reaches `Verify: OK`. Continue from
  `research/tasks/func_80017A18_2026-07-09_mw8na_checkpoint.md`.
- Upstream refresh on 2026-07-10 merged `upstream/master` commit `0adab627`
  (documentation/rename for the already matched `func_8002B0F4`). The canonical
  matching build remains `Verify: OK`; the live guarded count remains 4.
- A 2026-07-10 objects FPR-lifetime pass rejected radius-first ordering
  (`CURRENT (8783)`, saved-GPR regression) and sequential sum grouping
  (`CURRENT (7864)`, only 5 points better with the same missing
  `f18/f20/f22` lifetime). The retained A2/C2 source remains authoritative.
- A 2026-07-10 track global-color pass found no analogous matching source
  precedent. All-raw trig products grew text by `0x44` and saved `f20/f21`;
  declaration/definition swaps were object-identical. Continue only with an
  interference-node mechanism that preserves named carriers and exact size.
- A corrected real-`-mips1` menu permuter run reproduced `CURRENT (10)` and
  found no lower score in 275 seconds (1,696 iterations in the final observable
  sample). External racer and track precedent searches also found no new
  source-backed mechanism. All four guards remain necessary.
- A second 2026-07-10 direct mechanism pass found no promotable source. Menu
  full-index materialization prevents coalescing but rotates the live tuple to
  `t8/t9/t3`; track's `1342` improvement remains inseparable from a `+4`-byte
  array scratch store; objects loop-carried origin copies add `0x10` of frame;
  racer initializer sharing displaces correct count/pointer roles. Continue
  from the updated per-function ledgers, with all four guards intact.
- A finite menu allocator sweep on 2026-07-10 found no exact source: 226 unique
  declaration orders produced one object, all 16,384 `register`-qualifier
  subsets were instruction-identical, and 23 index-expression forms either
  retained the same two-word miss or grew text. Historical fork compiler,
  typedef, layout, prototype, and translation-unit context likewise reproduces
  the miss. Pure ordering/storage-class/context restoration is now exhausted.
- A third finite pass covered 217 menu cast placements, all 17 independent
  track array stores as scratch barriers, and all 27 direct/explicit/reused
  per-axis objects retry-carrier combinations. Menu casts never beat the same
  two-word miss; no track store restored target size; objects baseline remained
  best and no mixed ownership produced `f18/f20/f22`. All guards remain active.
- Further finite coverage compiled 4,536 racer loop-header forms and 42 objects
  axis-order variants. Racer produced nine objects but never target
  `v0/v1/a0/v0`; objects statement order never completed `f18/f20/f22` or beat
  baseline. A corrected track fakematch audit found no semantic one-instruction
  compensation; a behavior-invalid apparent result was discarded before
  integration. All four guards remain necessary.
- Public decomp.me family inspection on 2026-07-10 found two newer scratches.
  Racer `oR9oG` is valid and retained under `NON_EQUIVALENT`, improving linked
  `CURRENT (4365)` to authoritative shared `CURRENT (2905)` with exact frame
  `0xF8` and early `f14`; it remains 20 bytes short, lacks `f21/f20`, and keeps
  the swapped wave pair. Objects `96Vzj` reached raw `6280` but corrupted the
  mask and used wrong coordinates; semantic repairs regressed, so it was not
  retained. Track family best (`1898`) remains worse than retained `1668`, and
  the menu family exposes no result below score `20`.
- A follow-up 64-way racer lifetime/padding matrix found no improvement over
  retained `CURRENT (2905)`. Split `sqrtf` restores `f21/f20` saves but shrinks
  the function by another `0x68`; non-split shapes remain `0x14` short. An
  instruction-count audit attributes four of the five missing instructions to
  those saves/restores and identifies target-only `move t0,v1` in the
  `trickType == +/-1` path as the residual interior instruction. Sixteen
  semantic old-value/update carrier variants failed to emit that move; the
  only target-size variant used unrelated sign-extension noise. Keep the exact
  `oR9oG` source as the racer checkpoint.
- A bounded four-worker racer permuter run stopped at about 240 seconds. Its
  advisory metric improved only `5016 -> 5006`; no candidate was promoted or
  returned as a semantic patch. This does not supersede authoritative linked
  `CURRENT (2905)`.
- A new menu address-DAG pass found no improvement over the two-word
  `CURRENT (10)` frontier. Explicit element-pointer ownership, 32 bounded
  pointer/CFG/carrier mechanisms, fake-lifetime/type crosses, and the most
  promising coupled row/selected-track web split all missed. The coupled split
  preserves the exact `t2` branch/delay-slot region but colors the separate
  address node as `t6/t7` or `t8/t9`, not target `t4/t5`. Retain the external
  checkpoint unchanged and do not infer real `t3` liveness: target `t3` is
  dead at the first `addu`; this remains an IDO coalescing preference.
- A fresh track FPR-graph pass localized the retained drift to one three-range
  spill cycle. Target keeps negative cosine in `f18`, doubled sine in `f16`,
  and spills doubled cosine; current keeps negative cosine in `f16`, doubled
  cosine in `f18`, and spills doubled sine. Reusing the existing `var_f16` as
  a doubled-sine carrier reproduces the exact target color/spill topology at
  exact size, but its scheduler regresses advisory score to `3489` (best chain
  cross `2879`). Thirty-two chained first-ring forms, 29 tail orders, and
  reverse-nested pair forms did not beat retained linked `CURRENT (1668)`; the
  only promoted same-size chain was `CURRENT (3821)`. Retain the current source
  and continue from the exact-color carrier only with an independent scheduler
  mechanism.
- A coupled `func_80017A18` pass found a real guarded-source improvement.
  Replacing scalar `x2/y2/z2` with one `Vec3f origin` preserves frame `0x120`,
  size `0x444`, result `sp+0xF8`, and the exact saved-GPR family while improving
  the current promoted tree by 140 points (`7934 -> 7794`); it is retained.
  Target's missing six instructions are now proven to be three retry-header
  origin spills plus three latch reloads caused by historical in-`do` origin
  assignments. Scoped retry copies move toward that topology but widen the
  frame; cursor forms break GPR ownership. Target also caches target, not
  origin, A/C products in the gentle-slope branch; the behavior-correct product
  cross regresses to `8490` and is recorded as a future exact-match constraint.
- A new racer lifetime audit isolated two real target mechanisms without a
  promotable cross. A dedicated late x-velocity carrier recovers the exact
  `f21/f20` save family at frame `0xF8`, and mixed old-value ownership emits
  the target `move t0,v1`; however, the carrier shrinks text to `0x28B8` and
  regresses linked score to `3130`, while the copy alone leaves retained
  `CURRENT (2905)` unchanged. Ten intermediate square-root trees also failed
  to beat `2905`. Future racer work must couple this proven carrier topology
  with an independent source mechanism that restores `0x54` bytes; do not
  retry wave-local ownership or expression association.
- A live public-scratch refresh found no importable improvement: menu remains
  at score `20`, track family best is `1898` versus retained linked `1668`,
  objects still advertises the already rejected behavior-invalid `96Vzj`, and
  racer has no child below retained `oR9oG`. A distinct objects cross then
  moved retained `Vec3f origin` loads directly inside `do`; it preserved frame
  `0x120` and size `0x444` but regressed `7794 -> 8684`, kept mask `ra`, and
  failed to form target retry phis. Target-product and co-induction crosses
  regressed to `9396` and `9816`. Retain the current objects source and require
  a different contained GPR/interference mechanism.

- Parent heartbeat lane on 2026-06-12: child `019ebdc1-2430-72e0-8e5d-5d066a74a404`
  for `func_8002B0F4` recorded durable negative evidence on branch
  `codex/func-8002b0f4-child-evidence` at `b16fb37c`. Tracker:
  `research/tasks/child_threads/ACTIVE_CHILD.md`; child evidence:
  `research/tasks/child_threads/func_8002B0F4_2026-06-12_child_evidence.md`.
  The only new source probe, `register` on `currentSegment`,
  `currentBoundingBox`, and `currentBatch`, produced no model-base spill
  movement and was reverted before restored `Verify: OK`.
- Parent heartbeat lane on 2026-06-12: child `019ebdcb-1042-7690-a495-cd91360dfc59`
  for `func_80049794` recorded durable negative evidence on branch
  `codex/func-80049794-child` at `1e9cccf5`. Tracker:
  `research/tasks/child_threads/ACTIVE_CHILD.md`; child evidence:
  `research/tasks/child_threads/func_80049794_2026-06-12_child_evidence.md`.
  The child made no source edit because every named mechanism-ready source shape
  collapsed into already rejected evidence; restored child validation reached
  `Verify: OK`.
- Parent heartbeat lane on 2026-06-12: child `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2`
  for `trackbg_render_flashy` recorded durable negative evidence on branch
  `codex/trackbg-render-flashy-child` at `6207d9c5`. Tracker:
  `research/tasks/child_threads/ACTIVE_CHILD.md`; child evidence:
  `research/tasks/child_threads/trackbg_render_flashy_2026-06-12_child_evidence.md`.
  The child made no source edit because every named mechanism-ready source shape
  collapsed into already rejected evidence; restored child validation reached
  `Verify: OK`.
- Parent heartbeat lane on 2026-06-12: child `019ebdd6-3f3b-7c61-a36f-0a9928ad0eb9`
  for `func_80059208` recorded durable negative evidence on branch
  `codex/func-80059208-child` at `e09f5f42`. Tracker:
  `research/tasks/child_threads/ACTIVE_CHILD.md`; child evidence:
  `research/tasks/child_threads/func_80059208_2026-06-12_child_evidence.md`.
  The child made no source edit because every named mechanism-ready source shape
  collapsed into already rejected evidence; restored child validation reached
  `Verify: OK`.
- First route: run the selector and start with its `recommended_next`, while using cooldown/saturation evidence only to avoid blind repeated source shapes. A function is never removed from the work surface solely because prior probes missed.
- Upstream sync on 2026-06-23 merged `upstream/master` at `bba0365d`,
  including upstream matches for `init_particle_buffers` (`dcec92a2`) and
  `func_8002B0F4` (`0f7f99bc`). Refreshed selector state is 5 routable guarded
  candidates, 2 parked/exhausted notes, 3 cooldown ledgers,
  `skipped_exhausted=0`, and `recommended_next: func_8008FF1C` while the active
  child lane works that function. Cooldown and parked notes are evidence for
  the next child hypothesis, not a prohibition.
- Active `func_8008FF1C` child checkpoint: child thread
  `019ebe01-34c2-7310-b8aa-4aa5cff50faa` committed checkpoint evidence
  `4351e435` on `codex/func-8008ff1c-mechanism-discovery`; parent imported
  `research/tasks/child_threads/func_8008FF1C_2026-06-12_child_checkpoint.md`.
  This is durable negative evidence only, not lane closeout. Continue
  monitoring the same child until byte-match/source commit or a true
  setup/toolchain/assets/unresolved-behavior blocker.
- Active `func_8008FF1C` replacement lane on 2026-06-23: the old child thread
  was no longer readable through current Codex thread tools, while its worktree
  had advanced to evidence-only commit `3e4a2156` with no exact-match source.
  Parent created replacement branch `codex/func-8008ff1c-replacement-20260623`
  at `3e4a2156`, forked pending worktree
  `local:1a3103f0-c50c-4d84-9d8a-53f035eaef04`, and seeded replacement child
  thread `019ef6c2-c922-76b3-90fc-0db88540c680` in
  `/Users/douglas/.codex/worktrees/646c/dkrdecompiled`. Continue monitoring
  this replacement child only until `func_8008FF1C` byte-matches/source-commits
  or records a true setup/toolchain/assets/unresolved-behavior blocker.
- Current packet status: `func_80049794` is active but saturated for low-signal source spelling probes. Do not edit it again without a compact routing packet that names a distinct compiler-mechanism hypothesis and predicted asm movement.
- Evidence path checked: `research/tasks/func_80049794_evidence.md`.
- Latest do-not-repeat/cooldown note: a 2026-05-31 follow-up high mechanism discovery for `func_80049794` found no mechanism-ready source patch. Forced guarded object still lacks `$f20/$f21` saves, uses early zero `$f16`, and keeps wave scan as `v0` count with `a0` high bound and `v1` loop index; target needs `$f21/$f20` saves at `0x20/0x24(sp)`, early zero `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`. Focused `CURRENT (0)` was contradicted by objdump and treated as stale; nonmatching full link still fails before CRC on racer-provided DRM helper symbols. Matching object was restored and full verify passed.
- Latest parent-child note: a 2026-06-12 high child worker for `func_80049794`
  found no non-repeated mechanism-ready source patch and committed evidence-only
  result `1e9cccf5`. Do not reselect `func_80049794` without a truly distinct
  mechanism predicting both target saved-FPR allocation and the wave scan
  `v1` high bound / `a0` loop index / `v0` pointer-cursor movement.
- Latest direct racer note: a 2026-07-09 fresh block-scoped `waveLast` /
  `waveIndex` probe on the close save-family widened the frame to `0x100` and
  colored the wave tuple as `v1/a0/v0` instead of target `v0/v1/a0`; focused
  diff was `CURRENT (7306)`. The probe was fully reverted. Do not repeat lexical
  shadow/scoped wave locals.
- Latest direct racer mechanism note: the base close-save source reaches exact
  frame `0xF8`, `$f21/$f20` saves, early `$f14`, and `CURRENT (4365)`. The
  residual wave gap is specifically target stable bound `v1` plus mutable
  index `a0` versus current stable `a0` plus mutable `v1`; existing-local,
  declaration-order, no-op, and pad/steer carrier probes all rotated into
  worse register families and were rejected. Reopen only with a mechanism that
  reverses that initial copy direction while retaining `v0` pointer induction.
- Next hypothesis: keep cooldown-routed unless a high/xhigh isolated worker can name a new mechanism that couples the close save-family with non-repeated wave allocation movement. Otherwise pivot to another bounded candidate or run discovery/tooling to improve candidate ranking/cooldown behavior; do not repeat promoted-object `CURRENT (0)` acceptance for `func_80049794` unless the audit method preserves the DRM helper symbols and reaches the full ROM verify gate.
- Alternate evidence checked: `research/tasks/func_80059208_evidence.md`.
- Latest alternate-packet note: `func_80059208` remains active but saturated for final-tail pointer/FPR lifetime probes. A 2026-05-31 follow-up high mechanism discovery found no safe source-level packet beyond already rejected families and recommended cooldown. A valid future packet must predict object X into `$f16`, `5.0f` materialized before object Z, object Z into `$f6`, early `neg.s $f0,$f0`, add-after-negation final combine, and vertical tail through `$f6/$f10`. Stop if the proposal only changes temp/order spelling, object-dot spelling, pointer lifetime, literal staging, vertical aliases, or produces focused `CURRENT (0)` without full ROM `Verify: OK`.
- Latest child note: a 2026-06-12 high child worker for `func_80059208`
  found no non-repeated mechanism-ready source patch after rechecking the
  evidence ledger, selector template, current guarded C tail, and target asm
  tail around `0x5A22C-0x5A31C`. No source edit was made; child-local restored
  validation reached `Verify: OK`. Do not reselect `func_80059208` without a
  truly distinct mechanism predicting the required final-tail FPR/load-order
  movement beyond the recorded temp/order, object-dot, pointer-lifetime,
  literal-staging, vertical-alias, and focused-`CURRENT (0)` families.
- Track evidence checked: `research/tasks/trackbg_render_flashy_evidence.md`.
- Latest discovery/worker note: `trackbg_render_flashy` remains active but saturated for early FPR spelling/probe families. A 2026-05-31 follow-up high mechanism discovery found no landable source-level packet; current promoted shape still uses `neg.s $f16,$f12` and immediate doubled-cos `$f18`, while target keeps `$f18` as the negative-cos carrier and delays doubled-cos setup until after first-ring stack-temp stores. Do not trust focused `CURRENT (0)` or repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, pair-result scratch locals, first-two-store ordering, `var_f16` negative-cos lifetime extension, scheduling/lifetime barriers, doubled-cos spelling/literal variants, volatile/alias forcing, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes.
- Latest child note: a 2026-06-12 high child worker for
  `trackbg_render_flashy` found no non-repeated mechanism-ready source patch
  after rechecking the guarded first-ring body, target asm around `0x28D00`,
  promoted guarded object, and evidence ledger. No source edit was made;
  child-local restored validation reached `Verify: OK`. Do not reselect this
  target without a truly distinct mechanism predicting `$f18` negative-cos
  lifetime and delayed doubled-cos setup without frame/stack/scheduling drift.
- Latest direct note: the retained raw-cosine spelling shortens the named
  `scaledXCos` lifetime after `xPositions[0]` and improves the real promoted
  score to `CURRENT (1668)` without size/frame drift. The remaining first
  mismatch is still target `neg.s $f18,$f12` versus current `$f16`; continue
  from this closer candidate and do not reintroduce the rejected size-growing
  `xPositions[6]` scratch split.
- Latest tooling note: `tools/query_goal_state.py tooling` now reports routable candidates rather than blocked/off-limits candidates. It keeps cooldown and parked evidence visible as readiness gaps, next useful notes, latest promoted-object/focused-false-positive audit summaries, required packet fields (`target`, `evidence_checked`, `rejected_families`, `mechanism_hypothesis`, `predicted_asm_movement`, `stop_condition`, `reasoning_tier`), and a `packet --function <candidate> --template` command before delegation or source edits. A 2026-05-31 refresh ignores archived `## Extracted ACTIVE Notes` and recognizes follow-up/high mechanism-discovery lines when selecting a sidecar `latest_audit`, so all four live cooldown candidates surface current discovery evidence instead of stale object-slice or extracted-history notes.
- Historical `func_8002B0F4` evidence remains in
  `research/tasks/func_8002B0F4_evidence.md`, but upstream commit `0f7f99bc`
  matched the function. Do not route new child/source packets for
  `func_8002B0F4` unless a later regression or merge conflict reintroduces it
  to the selector.
- Latest parent-child note: a 2026-06-12 high child worker reproduced the known
  focused `CURRENT (0)` false positive under matching-mode guarded diagnostics:
  `gCurrentLevelModel` still hoisted before the segment loop, spilled at
  `0x60(sp)`, and texture lookup reloaded from that stack value. A bounded
  `register` pointer-local probe for `currentSegment`, `currentBoundingBox`,
  and `currentBatch` produced no movement and was reverted. Restored full
  validation reached `Verify: OK`; no mechanism-ready source patch was found.
- Latest selector-packet note: `func_8002B0F4` was previously active but
  saturated for model-load lifetime probes. Upstream commit `0f7f99bc` now
  provides the matching source, so the older do-not-repeat evidence is
  historical only.
- Current routing status after the 2026-06-23 upstream sync: all 5 remaining
  guarded candidates remain routable. `python3 tools/query_goal_state.py next
  --compact --refresh` reports `recommended_next: func_8008FF1C`; `python3
  tools/query_goal_state.py discovery` reports `func_80049794` as the next
  discovery/tooling-first live candidate; and cooldown evidence remains
  advisory only.
- Parent discovery/tooling heartbeat on 2026-06-12: no child lane was launched.
  Refreshed `next`, `discovery`, `tooling`, `revival`, and
  `check_active_surface`; at that time all 4 live candidates and all 3 parked
  candidates remained cooldown-routed, while `research/tasks/MECHANISM_PACKETS.md` still has
  no complete ready packet. Next useful work is to write a distinct
  compiler-mechanism packet with all required fields before source edits or
  child delegation; do not recycle the four 2026-06-12 evidence-only child
  targets without new predicted asm movement.
- Parent tooling repair on 2026-06-12: `tools/query_goal_state.py` now
  recognizes both `#pragma GLOBAL_ASM("...")` and macro-form
  `GLOBAL_ASM("...")`, but excludes `src/hasm/` handwritten assembly from
  source-C routing and reports it as `handwritten_asm_excluded=43`. This keeps
  the parent selector from silently missing macro-form entries while preserving
  the repo rule that handwritten ASM is not a byte-matching C packet. The
  heartbeat routing repair kept all then-current guarded candidates routable,
  reported `skipped_exhausted=0`, and treated cooldown evidence as anti-repeat
  guidance instead of a hard gate. After the 2026-06-23 upstream sync, the same
  selector reports 5 guarded candidates because upstream matched
  `func_8002B0F4` and `init_particle_buffers`.
- Pending parent child lane on 2026-06-12: created one high-reasoning
  worktree child for `func_8002B0F4` mechanism discovery, pending worktree id
  `local:7a717534-8df5-41a2-8dee-b0b05abdf97f`. The child must not edit source
  until it writes a complete packet or durable negative evidence; parent must
  not start a second lane while this pending lane is unresolved.
- Active parent child lane on 2026-06-12: pending worktree
  `local:7a717534-8df5-41a2-8dee-b0b05abdf97f` resolved to child thread
  `019ebdec-ac64-7131-9914-2faa3abe3568` at
  `/Users/douglas/.codex/worktrees/97e6/dkrdecompiled`. Parent sent the
  `func_8002B0F4` mechanism-discovery contract; monitor this one active lane
  before any further child creation.
- Latest child heartbeat: child `019ebdec-ac64-7131-9914-2faa3abe3568` is in
  progress and reached a setup permission issue while creating its branch
  because git refs are outside the child sandbox. It has requested git-ref
  write permission. Do not create another child while this lane is active.
- Latest parent worktree check: child branch
  `codex/func-8002b0f4-mechanism-discovery` now exists with no tracked diff;
  only local setup symlinks `.venv` and `assets` are untracked in the child
  worktree. No new child commit or mechanism packet is available yet; keep
  monitoring the active child lane.
- Latest child result: `func_8002B0F4` mechanism-discovery child
  `019ebdec-ac64-7131-9914-2faa3abe3568` committed durable negative evidence
  `5b0b972b` on `codex/func-8002b0f4-mechanism-discovery`; parent imported
  `research/tasks/child_threads/func_8002B0F4_2026-06-12_mechanism_discovery.md`.
  The child found no complete non-repeated mechanism packet; no source files
  were edited. Upstream commit `0f7f99bc` later matched `func_8002B0F4`, so
  this child result is historical only and does not require further monitoring.
- Pending parent child lane on 2026-06-12: created one high-reasoning
  worktree child for `func_80049794` mechanism discovery, pending worktree id
  `local:eba7130a-8a87-4f41-b8bb-c8929da5329e`. The child must not edit source
  until it writes a complete packet or durable negative evidence; parent must
  not start a second lane while this pending lane is unresolved.
- Active parent child lane on 2026-06-12: pending worktree
  `local:eba7130a-8a87-4f41-b8bb-c8929da5329e` resolved to child thread
  `019ebdf5-05f4-7b32-ba6f-03c838420dee` at
  `/Users/douglas/.codex/worktrees/9c4b/dkrdecompiled`. Parent sent the
  `func_80049794` mechanism-discovery contract; monitor this one active lane
  before any further child creation.
- Latest child result: `func_80049794` mechanism-discovery child
  `019ebdf5-05f4-7b32-ba6f-03c838420dee` committed durable negative evidence
  `1aa2b9d1` on `codex/func-80049794-mechanism-discovery`; parent imported
  `research/tasks/child_threads/func_80049794_2026-06-12_mechanism_discovery.md`.
  The child found no complete non-repeated mechanism packet after rechecking
  the live selector/tooling surfaces, packet template, current source, target
  asm, `MECHANISM_PACKETS.md`, and older `1e9cccf5` evidence. No source files
  were edited. Keep `func_80049794` cooldown-routed until a genuinely distinct
  saved-FPR plus wave-allocation mechanism is named.
- Parent discovery/tooling repair on 2026-06-12: `func_80059208` and
  `trackbg_render_flashy` sidecar ledgers now include parser-visible
  `2026-06-12 high mechanism-discovery found...` child-result lines for
  commits `e09f5f42` and `6207d9c5`. Refreshed `discovery` and `tooling` now
  surface June 12 child evidence as the latest audit for all four live
  cooldown candidates. No child lane was launched because no sidecar or
  `MECHANISM_PACKETS.md` entry names a complete distinct mechanism packet.
- Pending parent child lane on 2026-06-12: after refreshing `next`,
  `discovery`, `tooling`, `revival`, and `--include-exhausted` routing, parent
  created exactly one high-reasoning parked-revival mechanism-discovery child
  for `func_8008FF1C`, pending worktree id
  `local:eba34148-bbbc-47c4-88c1-0c51a9718518`. The child should continue until
  `func_8008FF1C` byte-matches and commits source-level C, unless a true
  setup/toolchain/assets/unresolved-behavior blocker is recorded. Negative
  evidence is allowed only as a checkpoint, not as lane closeout. The required
  mechanism must predict target `lh t2,0(s1)` / branch-on-`t2` allocation while
  preserving the target delay-slot `sw v0,0(s0)` for `cur->hubName =
  levelName`; do not repeat selected-track temp/carrier lifetime, direct table
  condition, common-store placement, duplicated branch-local store,
  condition/store comma ordering, register-hint, pointer-cell, object-only
  focused `CURRENT (0)`, or duplicated first-side-effect store families.
- The `func_8008FF1C` pending worktree resolved to child thread
  `019ebe01-34c2-7310-b8aa-4aa5cff50faa` at
  `/Users/douglas/.codex/worktrees/00e8/dkrdecompiled`; parent sent the
  corrected function-local prompt. This is the single active lane, and it must
  continue until byte-match/source commit or a true setup/toolchain/assets/
  unresolved-behavior blocker. Durable negative evidence is only a checkpoint.
- Latest parked revival note: a 2026-05-31 follow-up high mechanism discovery for `func_8008FF1C` found no landable source patch. Forced promotion reproduced stale focused `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xA63BE13D/0xB86942B3`; objdump showed `lh v1,0(s1)`, `sw v0,0(s0)` before the branch, then `beq v1,at,...`, not target `lh t2,0(s1)` with delay-slot `sw v0,0(s0)`. Do not repeat selected-track temp/carrier lifetime, direct table condition, common-store placement, duplicated branch-local store, condition/store comma ordering, register-hint, or focused-`CURRENT (0)` acceptance families.
- Latest parked object tooling note: a promoted object-slice audit for `func_80017A18` reproduced another focused false positive. `./diff.sh func_80017A18 --compress-matching 2 --no-pager` reported `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xD0505FD8/0xE965F5F5`; the promoted object still used frame `0x138` instead of target `0x120` and initialized the bitmask in `ra` instead of target `s6`. Matching object was restored and full verify passed. Do not trust focused `CURRENT (0)` or reopen without a mechanism predicting target frame and bitmask saved-register allocation.
- Latest parked revival probe: a 2026-05-31 combined `func_80017A18` dead-vector plus `sum2` edge-plane accumulator lifetime probe also produced stale focused `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0x0E9F297C/0xBB221418`. Source and matching-mode object were restored. Do not repeat this combined dead-vector/edge-plane accumulator family; any revival still needs a distinct mechanism predicting target frame `0x120` and bitmask in `s6`.
- Latest direct object note: a 2026-07-09 hybrid with primary/edge plane
  pointers and a dedicated `edgeSum` compiled to frame `0x130`, kept the mask
  in `ra`, and regressed to `CURRENT (8457)`; it was fully reverted. Historical
  candidate `eb131e6b` still demonstrates the target `0x120` frame, but a new
  source mechanism must keep the real outer index in `s1` to shift the saved
  register family toward target.
- Historical parked tooling note: a 2026-05-31 high mechanism-discovery worker
  for `init_particle_buffers` found no safe source-level packet. Upstream commit
  `dcec92a2` now matches `init_particle_buffers`, so this parked evidence is
  historical only and should not be routed unless a later regression or merge
  conflict reintroduces the function to the selector.
- Latest validation baseline: `python3 tools/check_active_surface.py`,
  `python3 tools/query_goal_state.py next --compact --refresh`, `python3
  tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py
  revival`, `python3 tools/query_goal_state.py tooling`, and `python3
  tools/query_goal_state.py packet --function func_8008FF1C` pass after the
  all-routable heartbeat repair. After the 2026-06-23 upstream sync, the
  selector reports 5 guarded candidates, `skipped_exhausted=0`, and
  `recommended_next: func_8008FF1C` while the active child lane works that
  target.
- Tooling import on 2026-06-23: DKR now has repo-local matching helpers adapted
  from Snowboard Kids workflow ideas: `.agents/skills/n64-ido-permuter/`,
  `tools/permuter`, `tools/find_similar_functions.py`,
  `tools/m2c_one_shot.py`, and `tools/data_diff.py`. These are discovery and
  near-match diagnostics only; they do not weaken the full `gmake -j4
  CROSS=tools/binutils/mips64-elf-` / `Verify: OK` acceptance gate and should
  not close or replace the active `func_8008FF1C` child lane.
- Snowboard candidate follow-up on 2026-06-23: DKR also has
  `tools/build-and-verify.sh` as a thin wrapper around the canonical `gmake -j4
  CROSS=tools/binutils/mips64-elf-` gate, `tools/score_asm_functions.py` for
  discovery ranking by rough complexity/available-asm similarity, and
  `.agents/skills/n64-display-list-macro-matching/` for Gfx macro matching
  packets. Snowboard data-file, ultralib-segment, and microcode guidance is
  conditional only: use the adapted display-list skill for DKR Gfx functions,
  and do not route generic data/ultralib packets unless the current DKR
  selector/work surface exposes a matching source-level C target.

## Routing Rules

- Before any source probe or worker delegation, produce a compact routing packet: target, evidence checked, rejected families, exact hypothesis, predicted asm movement, stop condition, and worker reasoning level if delegated.
- Do not run or delegate spelling/literal/condition-order microvariants after two same-family no-movement misses unless predicted asm movement is concrete and distinct.
- Treat pre-build `CURRENT (0)` on guarded promotions as stale unless rebuilt for that exact source state.
- Accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.

## Closeout Requirements

- For every miss, record function, hypothesis family, source-shape summary, focused diff, key drift, restore/validation status, next hypothesis, and cooldown/saturation status.
- Keep this file compact. Put detailed repeated probe history in per-function ledgers such as `research/tasks/func_80049794_evidence.md`.
- Update `SESSION_HANDOFF.md` with result, validation, blockers, evidence paths, next packet, and cooldown/saturation status.
