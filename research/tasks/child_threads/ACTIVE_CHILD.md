# DKR Parent Child Lane

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Policy: exactly one active child lane at a time.

## Active Lane

- Status: no active child lane; latest child evidence imported.
- Child thread id: `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2`
- Child worktree: `/Users/douglas/.codex/worktrees/d949/dkrdecompiled`
- Pending worktree id: `local:52703ce1-0286-41c7-8dff-cedfcb241432`
- Target: `trackbg_render_flashy`
- Lane type: high-reasoning mechanism discovery packet before any source edits.
- Evidence checked: `research/tasks/ACTIVE.md`; `python3 tools/query_goal_state.py next --compact --refresh`; `python3 tools/query_goal_state.py tooling`; `python3 tools/query_goal_state.py packet --function trackbg_render_flashy --template`; `research/tasks/trackbg_render_flashy_evidence.md` as required child reading.
- Rejected families: commuted single-site `zPositions[3]` ordering, all-first-ring `scaledXSin` reuse, plain/current guarded-C promotion, ordinary negative-scaled-cos temp variants, inverted primary cos carrier or positive-cos scratch locals, first-ring pair-result scratch locals, promoted-object focused `CURRENT (0)`, first-two-store ordering probes, `var_f16` negative-cos lifetime extension, scheduling/lifetime barriers, doubled-cos spelling/literal variants, volatile/alias forcing, and first-ring scratch reuse that predicts broad stack-slot/downstream drift.
- Mechanism hypothesis required: find a distinct early FPR-allocation/source-lifetime mechanism for the first-ring setup that is not one of the rejected spelling families.
- Predicted asm movement: target-like scaled cos in `$f12`, scaled sin in `$f2`, initial negative cos as `neg.s $f18,$f12`, delayed doubled-cos setup until after first-ring stack-temp stores, and no broad frame/stack-slot/downstream scheduling drift from the target `0x158` frame pattern.
- Stop condition: continue until `trackbg_render_flashy` byte-matches and commits source-level C, or records a true setup/toolchain/assets/behavior blocker or durable negative evidence that no mechanism-ready source patch exists.
- Reasoning tier: high.
- Child result: durable negative evidence committed on
  `codex/trackbg-render-flashy-child` at `6207d9c5` and imported to
  `research/tasks/child_threads/trackbg_render_flashy_2026-06-12_child_evidence.md`.

## Parent Gate

- Do not create another child while this lane is active, dirty, or unresolved.
- Parent integration requires source-level C only and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaching `Verify: OK`, followed by `./score.sh -s`.

## Heartbeat Log

- 2026-06-12: Parent confirmed child thread remains active. Child worktree had no tracked diffs, only local setup symlinks/untracked inherited tracker files; parent sent a follow-up to keep generated setup unstaged, use `--ignore-submodules=all` for status if needed, restore/avoid status-breaking setup where possible, and reach baseline `Verify: OK` before source probes.
- 2026-06-12: Parent confirmed child is still active with no tracked diffs. Child reported baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, then reproduced the known focused `CURRENT (0)` false positive in both promoted/nonmatching and matching-mode guarded diagnostics: `gCurrentLevelModel` still hoists before the segment loop, spills at `0x60(sp)`, and texture lookup reloads from that stack value. Child is now checking legitimate struct/type lifetime mechanisms before any source edit.
- 2026-06-12: Child committed durable negative evidence on `codex/func-8002b0f4-child-evidence` at `b16fb37c`. The only tested source probe, `register` on `currentSegment`, `currentBoundingBox`, and `currentBatch`, produced no model-base spill movement and was reverted before restored `Verify: OK`.
- 2026-06-12: Parent imported `func_8002B0F4` child evidence, refreshed routing, skipped reselecting `func_8002B0F4`, and created the next single child lane for `func_80049794` with pending worktree id `local:ac8dbccc-b093-4e13-8703-28fabf1519e8`.
- 2026-06-12: Pending `func_80049794` worktree resolved to child thread `019ebdcb-1042-7690-a495-cd91360dfc59` at `/Users/douglas/.codex/worktrees/c3a6/dkrdecompiled`.
- 2026-06-12: Parent confirmed child remains active on branch `codex/func-80049794-child` with only untracked local `build` setup visible. Parent sent a follow-up to keep generated outputs local to the child worktree, avoid symlinking `build` back to the parent checkout, keep setup inputs unstaged, and require baseline child-local `Verify: OK` before any source probe.
- 2026-06-12: Parent confirmed child remains active and tracked-clean while mirroring ignored validation inputs locally. Child has copied local `build`, `assets`, `ver/dkr.us.v77.ld`, generated helper binaries, IDO recomp bundle, `.venv`, and is correcting the `tools/asm-processor` submodule layout before rerunning the baseline gate. No source probe or child commit yet.
- 2026-06-12: Parent confirmed child reached child-local baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` with `Verify: OK`, populated local `tools/asm-differ` for diagnostics, and is reading target asm plus recent evidence before deciding whether a source mechanism probe is justified. Child tracked worktree remains clean; no source probe or child commit yet.
- 2026-06-12: Child committed durable negative evidence on `codex/func-80049794-child` at `1e9cccf5`; no source edit was made because every named mechanism-ready source shape collapsed into already rejected evidence. Parent imported the evidence note and can select the next single child lane after refreshed routing.
- 2026-06-12: Parent refreshed tooling, skipped the two just-resolved child lanes (`func_8002B0F4`, `func_80049794`), and created the next single child lane for `func_80059208` with pending worktree id `local:809f1788-2fb6-4212-a1ed-6d73150c0652`.
- 2026-06-12: Pending `func_80059208` worktree resolved to child thread `019ebdd6-3f3b-7c61-a36f-0a9928ad0eb9` at `/Users/douglas/.codex/worktrees/1264/dkrdecompiled`. Initial child status was detached `HEAD` with no tracked diffs.
- 2026-06-12: Parent confirmed child remains active on branch `codex/func-80059208-child` with no tracked diffs or staged changes. Child created the branch, copied ignored local validation inputs into the child worktree, reproduced expected asm-backed focused `CURRENT (0)`, and is still resolving ignored setup dependencies before child-local baseline `Verify: OK`; latest setup item was local `tools/dkr_assets_tool`.
- 2026-06-12: Parent confirmed child reached child-local baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` with `Verify: OK` and `./score.sh -s` reported decomp `97.30%`, docs `65.47%`. Child reported no distinct non-repeated final-tail mechanism and said it was applying evidence-only closeout edits, but the child worktree still had no tracked/staged changes and `HEAD` remained `c2ed22a3`; parent sent a follow-up asking the child to finish the evidence commit or report the exact blocker.
- 2026-06-12: Child committed durable negative evidence on `codex/func-80059208-child` at `e09f5f42`; no source edit was made because every named final-tail mechanism-ready source shape collapsed into already rejected evidence. Parent imported the evidence note and can select the next single child lane after refreshed routing.
- 2026-06-12: Parent refreshed tooling, skipped the three just-resolved child lanes (`func_8002B0F4`, `func_80049794`, `func_80059208`), and created the next single child lane for `trackbg_render_flashy` with pending worktree id `local:52703ce1-0286-41c7-8dff-cedfcb241432`.
- 2026-06-12: Pending `trackbg_render_flashy` worktree resolved to child thread `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2` at `/Users/douglas/.codex/worktrees/d949/dkrdecompiled`. Initial child status was detached `HEAD` with no tracked diffs.
- 2026-06-12: Parent confirmed child remains active with no tracked or staged changes. Child copied ignored validation inputs locally, reached child-local baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` with `Verify: OK`, reproduced the expected asm-backed focused `CURRENT (0)`, and is now forcing/promoting `build/src/tracks.c.o` under `NON_MATCHING=1` to inspect the first-ring FPR allocation drift before deciding whether a non-repeated source mechanism exists.
- 2026-06-12: Child committed durable negative evidence on `codex/trackbg-render-flashy-child` at `6207d9c5`; no source edit was made because every named first-ring FPR/source-lifetime mechanism-ready source shape collapsed into already rejected evidence. Parent imported the evidence note; all four default-routable live candidates now have 2026-06-12 parent-child negative evidence.
