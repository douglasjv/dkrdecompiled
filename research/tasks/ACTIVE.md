# Active Matching Surface

## Goal Context

- End goal: every original Diddy Kong Racing function has source-level C that keeps the matching ROM byte-identical.
- Loop: `research/tasks/GOAL_LOOP.md`.
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`.
- Exhausted probe notes: `research/tasks/PARKED.md`; these notes prevent blind retries and are skipped by default, but they are not permanent removal from the project.
- Default work: bounded `matching_impl` packets against one `GLOBAL_ASM`, `NON_MATCHING`, or `NON_EQUIVALENT` target.
- Default validation: `gmake -j4 CROSS=tools/binutils/mips64-elf-` in matching mode, then focused `./diff.sh <function>` only for diagnosis.

## Current Route

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
- First route: run the selector and start with its `recommended_next` unless the latest evidence marks that packet saturated, cooling down, or pivot-only.
- Current selector result on 2026-05-31 after cooldown-aware tooling: 4 default-routable guarded candidates, 3 skipped exhausted notes, 4 cooldown ledgers, and `recommended_next: discovery` because every default-routable candidate is cooldown-routed.
- Current packet status: `func_80049794` is active but saturated for low-signal source spelling probes. Do not edit it again without a compact routing packet that names a distinct compiler-mechanism hypothesis and predicted asm movement.
- Evidence path checked: `research/tasks/func_80049794_evidence.md`.
- Latest do-not-repeat/cooldown note: a 2026-05-31 follow-up high mechanism discovery for `func_80049794` found no mechanism-ready source patch. Forced guarded object still lacks `$f20/$f21` saves, uses early zero `$f16`, and keeps wave scan as `v0` count with `a0` high bound and `v1` loop index; target needs `$f21/$f20` saves at `0x20/0x24(sp)`, early zero `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`. Focused `CURRENT (0)` was contradicted by objdump and treated as stale; nonmatching full link still fails before CRC on racer-provided DRM helper symbols. Matching object was restored and full verify passed.
- Latest parent-child note: a 2026-06-12 high child worker for `func_80049794`
  found no non-repeated mechanism-ready source patch and committed evidence-only
  result `1e9cccf5`. Do not reselect `func_80049794` without a truly distinct
  mechanism predicting both target saved-FPR allocation and the wave scan
  `v1` high bound / `a0` loop index / `v0` pointer-cursor movement.
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
- Latest tooling note: `tools/query_goal_state.py tooling` gives the compact discovery/tooling route when all candidates are cooldown-routed. It lists every blocked live and parked candidate, evidence path, readiness gap, next useful note, latest promoted-object/focused-false-positive audit summary, required packet fields (`target`, `evidence_checked`, `rejected_families`, `mechanism_hypothesis`, `predicted_asm_movement`, `stop_condition`, `reasoning_tier`), and a `packet --function <candidate> --template` command before delegation or source edits. A 2026-05-31 refresh ignores archived `## Extracted ACTIVE Notes` and recognizes follow-up/high mechanism-discovery lines when selecting a sidecar `latest_audit`, so all four live cooldown candidates surface current discovery evidence instead of stale object-slice or extracted-history notes.
- Current packet evidence checked: `research/tasks/func_8002B0F4_evidence.md`.
- Latest parent-child note: a 2026-06-12 high child worker reproduced the known
  focused `CURRENT (0)` false positive under matching-mode guarded diagnostics:
  `gCurrentLevelModel` still hoisted before the segment loop, spilled at
  `0x60(sp)`, and texture lookup reloaded from that stack value. A bounded
  `register` pointer-local probe for `currentSegment`, `currentBoundingBox`,
  and `currentBatch` produced no movement and was reverted. Restored full
  validation reached `Verify: OK`; no mechanism-ready source patch was found.
- Latest selector-packet note: `func_8002B0F4` remains active but saturated for model-load lifetime probes. A 2026-05-31 high mechanism-discovery worker found no safe source packet: current C already uses direct `gCurrentLevelModel` expressions, but IDO still CSE/hoists and spills the model base. A valid future packet must remove promoted stack-resident model base `0x60(sp)`, replace the texture lookup reload from `0x5FE8` with an in-loop global `lui/lw gCurrentLevelModel` like target `0x2C020/0x2C024`, and preserve the outer setup global reload around `0x2BDD4/0x2BDD8`. Do not trust focused `CURRENT (0)`, repeat promoted-object-slice auditing, or repeat local segment-index, local model pointer, bottom-only segment-pointer split, assignment/order, texture/flag carrier, pointer-arithmetic setup, condition/literal/local-width, bottom store-order, unsafe `volatile`, accessor, artificial aliasing, or helper reshaping probes.
- Current routing status after this note: all 4 default-routable guarded candidates have cooldown sidecars and all 3 parked candidates have recent revival cooldown. `python3 tools/query_goal_state.py next --compact --refresh` reports `recommended_next: discovery`; `research/tasks/MECHANISM_PACKETS.md` has no ready packets.
- Discovery selector: `python3 tools/query_goal_state.py discovery` still reports `discovery_next: tooling` for live cooldown candidates. `python3 tools/query_goal_state.py tooling` reports `tooling_next: discovery_packet` and lists blocked live/parked candidates. `python3 tools/query_goal_state.py revival` reports `revival_next: tooling`.
- Parent discovery/tooling heartbeat on 2026-06-12: no child lane was launched.
  Refreshed `next`, `discovery`, `tooling`, `revival`, and
  `check_active_surface`; all 4 live candidates and all 3 parked candidates
  remain cooldown-routed, while `research/tasks/MECHANISM_PACKETS.md` still has
  no complete ready packet. Next useful work is to write a distinct
  compiler-mechanism packet with all required fields before source edits or
  child delegation; do not recycle the four 2026-06-12 evidence-only child
  targets without new predicted asm movement.
- Parent tooling repair on 2026-06-12: `tools/query_goal_state.py` now
  recognizes both `#pragma GLOBAL_ASM("...")` and macro-form
  `GLOBAL_ASM("...")`, but excludes `src/hasm/` handwritten assembly from
  source-C routing and reports it as `handwritten_asm_excluded=43`. This keeps
  the parent selector from silently missing macro-form entries while preserving
  the repo rule that handwritten ASM is not a byte-matching C packet. Refreshed
  `next` still reports 4 guarded candidates, all cooldown-routed, with
  `recommended_next: discovery`; `tooling` still requires a complete mechanism
  packet before any child delegation.
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
  were edited. Keep `func_8002B0F4` cooldown-routed until a genuinely distinct
  model-load lifetime/register-allocation mechanism is named.
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
- Latest parked revival note: a 2026-05-31 follow-up high mechanism discovery for `func_8008FF1C` found no landable source patch. Forced promotion reproduced stale focused `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xA63BE13D/0xB86942B3`; objdump showed `lh v1,0(s1)`, `sw v0,0(s0)` before the branch, then `beq v1,at,...`, not target `lh t2,0(s1)` with delay-slot `sw v0,0(s0)`. Do not repeat selected-track temp/carrier lifetime, direct table condition, common-store placement, duplicated branch-local store, condition/store comma ordering, register-hint, or focused-`CURRENT (0)` acceptance families.
- Latest parked object tooling note: a promoted object-slice audit for `func_80017A18` reproduced another focused false positive. `./diff.sh func_80017A18 --compress-matching 2 --no-pager` reported `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xD0505FD8/0xE965F5F5`; the promoted object still used frame `0x138` instead of target `0x120` and initialized the bitmask in `ra` instead of target `s6`. Matching object was restored and full verify passed. Do not trust focused `CURRENT (0)` or reopen without a mechanism predicting target frame and bitmask saved-register allocation.
- Latest parked revival probe: a 2026-05-31 combined `func_80017A18` dead-vector plus `sum2` edge-plane accumulator lifetime probe also produced stale focused `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0x0E9F297C/0xBB221418`. Source and matching-mode object were restored. Do not repeat this combined dead-vector/edge-plane accumulator family; any revival still needs a distinct mechanism predicting target frame `0x120` and bitmask in `s6`.
- Latest parked tooling note: a 2026-05-31 high mechanism-discovery worker for `init_particle_buffers` found no safe source-level packet. A valid future packet must predict target counts `s1/s3/s7/s4/s8`, point count in `s8/fp`, first allocation arithmetic using line count in `s4` and point count in `fp`, and colour tag `0x80808080` in `s2` for every semitrans-grey `mempool_alloc_safe`, with frame still `0x68`. Stop if promoted code still has counts `s3/s1/s7/s2/s4`, colour tag `s0`, frame drift, or only focused `CURRENT (0)` without full ROM `Verify: OK`. Do not repeat register hints, count aliases, local triangle-buffer pointer, all-call colour-tag, unused-pad removal, initial-only colour-tag, declaration/local-carrier source probes, or focused-`CURRENT (0)` acceptance.
- Latest validation baseline: `python3 tools/check_active_surface.py`, `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py packet --function func_8002B0F4 --template`, and high worker read-only discovery passed on 2026-05-31. The selector still reports `recommended_next: discovery`; no mechanism-ready source packet is recorded.

## Routing Rules

- Before any source probe or worker delegation, produce a compact routing packet: target, evidence checked, rejected families, exact hypothesis, predicted asm movement, stop condition, and worker reasoning level if delegated.
- Do not run or delegate spelling/literal/condition-order microvariants after two same-family no-movement misses unless predicted asm movement is concrete and distinct.
- Treat pre-build `CURRENT (0)` on guarded promotions as stale unless rebuilt for that exact source state.
- Accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.

## Closeout Requirements

- For every miss, record function, hypothesis family, source-shape summary, focused diff, key drift, restore/validation status, next hypothesis, and cooldown/saturation status.
- Keep this file compact. Put detailed repeated probe history in per-function ledgers such as `research/tasks/func_80049794_evidence.md`.
- Update `SESSION_HANDOFF.md` with result, validation, blockers, evidence paths, next packet, and cooldown/saturation status.
