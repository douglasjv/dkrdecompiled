# DKR Parent Child Lane

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Policy: exactly one active child lane at a time.

## Active Lane

- Status: active child thread running.
- Child thread id: `019ebdcb-1042-7690-a495-cd91360dfc59`
- Child worktree: `/Users/douglas/.codex/worktrees/c3a6/dkrdecompiled`
- Pending worktree id: `local:ac8dbccc-b093-4e13-8703-28fabf1519e8`
- Target: `func_80049794`
- Lane type: high-reasoning mechanism discovery packet before any source edits.
- Evidence checked: `research/tasks/ACTIVE.md`; `python3 tools/query_goal_state.py next --compact --refresh`; `python3 tools/query_goal_state.py tooling`; `python3 tools/query_goal_state.py packet --function func_80049794 --template`; `research/tasks/func_80049794_evidence.md` as required child reading.
- Rejected families: plain promotion, object-only/focused-`CURRENT (0)` acceptance, `updateRateF`/`var_f20` carrier variants, `register var_f20`, carrier-width changes, branch/condition/literal spellings, wave bound/index locals, pointer-cursor wave variants, selected-wave carriers, declaration-order/register hints, early-zero carriers, first-speed carriers, and close save-family combinations that do not move wave allocation.
- Mechanism hypothesis required: find a distinct compiler mechanism that couples the missing target saved-FPR family with a non-repeated wave allocation change.
- Predicted asm movement: recover target frame `0xF8`, `$f21/$f20` prologue saves at `0x20/0x24(sp)`, early zero in `$f14`, and wave scan allocation with `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`.
- Stop condition: continue until `func_80049794` byte-matches and commits source-level C, or records a true setup/toolchain/assets/behavior blocker or durable negative evidence that no mechanism-ready source patch exists.
- Reasoning tier: high.

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
