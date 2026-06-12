# DKR Parent Child Lane

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Policy: exactly one active child lane at a time.

## Active Lane

- Status: pending child worktree; no child thread id yet.
- Child thread id: pending
- Child worktree: pending
- Pending worktree id: `local:7a717534-8df5-41a2-8dee-b0b05abdf97f`
- Target: `func_8002B0F4`
- Lane type: high-reasoning mechanism discovery packet before any source edits.
- Evidence checked: `research/tasks/ACTIVE.md`; `python3 tools/query_goal_state.py next --compact --refresh`; `python3 tools/query_goal_state.py tooling`; `python3 tools/query_goal_state.py packet --function func_8002B0F4 --template`; `research/tasks/func_8002B0F4_evidence.md` as required child reading.
- Rejected families: local segment-index lifetime variants, local model pointer, bottom-only segment-pointer lifetime split, assignment/order changes, texture/flag carriers, pointer-arithmetic setup, condition/literal/local-width spellings, bottom store-order probes, unsafe `volatile`, accessor calls, artificial aliasing side effects, helper reshaping, promoted-object slice audits, and focused `CURRENT (0)` acceptance without full ROM `Verify: OK`.
- Mechanism hypothesis required: find a distinct model-load lifetime/register-allocation mechanism that predicts single-use `gCurrentLevelModel` global reloads at outer setup and batch-loop texture lookup.
- Predicted asm movement: remove the promoted stack-resident model base at `0x60(sp)`, preserve target-like outer setup reload around `0x2BDD4/0x2BDD8`, and replace the texture lookup reload from promoted `0x5FE8` with an in-loop global `lui/lw gCurrentLevelModel` pair like target `0x2C020/0x2C024`.
- Stop condition: write a complete mechanism packet in `research/tasks/MECHANISM_PACKETS.md` or durable negative evidence proving no non-repeated mechanism-ready source packet exists; do not make source edits in the child until the mechanism packet is complete and parent-routed.
- Reasoning tier: high.
- Child result: pending.

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
- 2026-06-12: Parent ran the required discovery/tooling heartbeat with no active child lane. `python3 tools/query_goal_state.py next --compact --refresh` still reports `recommended_next: discovery`; `discovery` routes to `tooling`; `tooling` routes to `discovery_packet`; `revival` routes to `tooling`; and `check_active_surface` passes. No new child was launched because all live and parked candidates are cooldown-routed and no complete mechanism packet exists in `research/tasks/MECHANISM_PACKETS.md`.
- 2026-06-12: Parent repaired the selector scanner so macro-form `GLOBAL_ASM("...")` is recognized while `src/hasm/` handwritten assembly is counted but excluded from source-C routing. Refreshed `next` reports `handwritten_asm_excluded=43` and still routes to discovery; no child was launched because no complete mechanism packet exists.
- 2026-06-12: Parent created one pending high-reasoning child worktree for `func_8002B0F4` mechanism discovery with pending worktree id `local:7a717534-8df5-41a2-8dee-b0b05abdf97f`. No child thread id or worktree path exists yet. Parent must not start another child lane until this pending lane resolves and either commits a complete mechanism packet/evidence or reports a true setup/toolchain/assets/behavior blocker.
