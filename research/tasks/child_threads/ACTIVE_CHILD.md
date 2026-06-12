# DKR Parent Child Lane

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Policy: exactly one active child lane at a time.

## Active Lane

- Status: active child thread running.
- Child thread id: `019ebdc1-2430-72e0-8e5d-5d066a74a404`
- Child worktree: `/Users/douglas/.codex/worktrees/6f37/dkrdecompiled`
- Pending worktree id: `local:95869d83-251a-4954-9fbe-510fcd4d1b51`
- Target: `func_8002B0F4`
- Lane type: high-reasoning mechanism discovery packet before any source edits.
- Evidence checked: `research/tasks/ACTIVE.md`; `python3 tools/query_goal_state.py next --compact --refresh`; `python3 tools/query_goal_state.py tooling`; `research/tasks/func_8002B0F4_evidence.md` as required child reading.
- Rejected families: local segment-index, local model pointer, bottom-only segment-pointer split, assignment/order, texture/flag carrier, pointer-arithmetic setup, condition/literal/local-width, bottom store-order, unsafe `volatile`, accessor, artificial aliasing, helper reshaping, promoted object-slice/focused-`CURRENT (0)` acceptance.
- Mechanism hypothesis required: find a source-level mechanism that removes the promoted stack-resident model base at `0x60(sp)` and produces in-loop `gCurrentLevelModel` reloads for the batch-loop texture lookup while preserving the outer setup reload.
- Predicted asm movement: target-like `lui/lw gCurrentLevelModel` at the texture lookup site near `0x2C020/0x2C024`, no stack-resident model-base reload from `0x60(sp)`, and no regression of the outer setup reload near `0x2BDD4/0x2BDD8`.
- Stop condition: continue until `func_8002B0F4` byte-matches and commits source-level C, or records a true setup/toolchain/assets/behavior blocker or durable negative evidence that no mechanism-ready source patch exists.
- Reasoning tier: high.

## Parent Gate

- Do not create another child while this lane is active, dirty, or unresolved.
- Parent integration requires source-level C only and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaching `Verify: OK`, followed by `./score.sh -s`.

## Heartbeat Log

- 2026-06-12: Parent confirmed child thread remains active. Child worktree had no tracked diffs, only local setup symlinks/untracked inherited tracker files; parent sent a follow-up to keep generated setup unstaged, use `--ignore-submodules=all` for status if needed, restore/avoid status-breaking setup where possible, and reach baseline `Verify: OK` before source probes.
- 2026-06-12: Parent confirmed child is still active with no tracked diffs. Child reported baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`, then reproduced the known focused `CURRENT (0)` false positive in both promoted/nonmatching and matching-mode guarded diagnostics: `gCurrentLevelModel` still hoists before the segment loop, spills at `0x60(sp)`, and texture lookup reloads from that stack value. Child is now checking legitimate struct/type lifetime mechanisms before any source edit.
