# Active Matching Surface

## Goal Context

- End goal: every original Diddy Kong Racing function has source-level C that keeps the matching ROM byte-identical.
- Loop: `research/tasks/GOAL_LOOP.md`.
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`.
- Exhausted probe notes: `research/tasks/PARKED.md`; these notes prevent blind retries and are skipped by default, but they are not permanent removal from the project.
- Default work: bounded `matching_impl` packets against one `GLOBAL_ASM`, `NON_MATCHING`, or `NON_EQUIVALENT` target.
- Default validation: `gmake -j4 CROSS=tools/binutils/mips64-elf-` in matching mode, then focused `./diff.sh <function>` only for diagnosis.

## Current Route

- First route: run the selector and start with its `recommended_next` unless the latest evidence marks that packet saturated, cooling down, or pivot-only.
- Current selector result on 2026-05-31 after cooldown-aware tooling: 4 default-routable guarded candidates, 3 skipped exhausted notes, 4 cooldown ledgers, and `recommended_next: discovery` because every default-routable candidate is cooldown-routed.
- Current packet status: `func_80049794` is active but saturated for low-signal source spelling probes. Do not edit it again without a compact routing packet that names a distinct compiler-mechanism hypothesis and predicted asm movement.
- Evidence path checked: `research/tasks/func_80049794_evidence.md`.
- Latest do-not-repeat/cooldown note: avoid promotion-only/object-only `CURRENT (0)` acceptance, broad save/wave microvariants, opening `updateRateF` through `var_f20`, `register f32 var_f20`, carrier-width changes, and other spelling/literal/condition-order variants already recorded in the ledger.
- Next hypothesis: prefer a high/xhigh isolated worker only if it can name a concrete saved-FPR/register-allocation mechanism with predicted prologue, frame, saved-register, or wave-scan movement. Otherwise pivot to another bounded candidate or run discovery/tooling to improve candidate ranking/cooldown behavior.
- Alternate evidence checked: `research/tasks/func_80059208_evidence.md`.
- Latest alternate-packet note: `func_80059208` remains active but saturated for final-tail temp/order spelling probes. The 2026-05-31 separate-negated-checkpoint-temp worker miss failed verify with CRCs `0x53A81EDF/0x116C7718`; relinked focused diff regressed to `CURRENT (1356)`, moved object loads too early, removed target `neg.s $f0,$f0`, and retained subtract-style final combine. Do not repeat final-tail temp/order or direct object-dot variants without a different compiler mechanism.
- Track evidence checked: `research/tasks/trackbg_render_flashy_evidence.md`.
- Latest discovery/worker note: `trackbg_render_flashy` remains active but saturated for early FPR spelling probes. The 2026-05-31 inverted-primary-cos carrier probe failed verify with CRCs `0xDC79F591/0x31DBA03C`; relinked focused diff regressed to `CURRENT (3108)`, kept initial `0x28d00` `neg.s $f16,$f12` instead of target `$f18`, and only moved a later UV-block negation to `$f18`. Do not repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes.
- Latest tooling note: `tools/query_goal_state.py discovery` now exposes probe-readiness fields for cooldown candidates. It recognizes bulleted `Next useful work` sidecar lines, reports `ready_for_probe: false` when a sidecar still asks for discovery/tooling, and emits the required packet fields (`target`, `evidence_checked`, `rejected_families`, `mechanism_hypothesis`, `predicted_asm_movement`, `stop_condition`) before delegation or source edits.
- Current packet evidence checked: `research/tasks/func_8002B0F4_evidence.md`.
- Latest selector-packet note: `func_8002B0F4` remains active but saturated for simple segment/bbox setup and local-index lifetime probes. The 2026-05-31 worker segment-index local probe failed full verify with CRCs `0x7916617A/0xEAA308C1`; relinked focused diff improved to `CURRENT (2926)` but widened the frame to `0x130` and still hoisted/spilled `gCurrentLevelModel` at `0x64(sp)` instead of target-like in-loop global loads. Do not repeat local segment-index, initial assignment-order, condition, literal, or carrier variants unless the next hypothesis predicts a distinct model-load lifetime/register-allocation mechanism.
- Current routing status after this note: all 4 default-routable guarded candidates have cooldown sidecars and all 3 parked candidates have recent revival cooldown. `python3 tools/query_goal_state.py next --compact --refresh` reports `recommended_next: discovery`; `SESSION_HANDOFF.md` contains the next worker-ready `func_8002B0F4` mechanism packet, and `python3 tools/query_goal_state.py packet --function func_8002B0F4` emits its current selector context.
- Discovery selector: `python3 tools/query_goal_state.py discovery` reports `discovery_next: tooling` when all sidecar candidates are cooldown/tooling-first status. `python3 tools/query_goal_state.py revival` reports `revival_next: tooling` because all parked candidates have recent revival cooldown evidence, including `init_particle_buffers` initial-only colour-tag local (`CURRENT (0)` focused, full verify CRCs `0xEF29C961/0xF604264D`).
- Latest validation baseline: `python3 tools/check_active_surface.py`, `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py discovery --json`, `python3 tools/query_goal_state.py revival`, `python3 tools/query_goal_state.py list --json --include-exhausted`, `python3 tools/query_goal_state.py packet --function trackbg_render_flashy`, `python3 tools/query_goal_state.py packet --function func_8008FF1C`, `python3 tools/query_goal_state.py packet --function func_8002B0F4`, `python3 -m py_compile tools/query_goal_state.py`, `gmake -j4 CROSS=tools/binutils/mips64-elf-`, and `./score.sh -s` passed on 2026-05-31 after the trackbg miss was restored. Matching build reached `Verify: OK`; score remained 97.30%.

## Routing Rules

- Before any source probe or worker delegation, produce a compact routing packet: target, evidence checked, rejected families, exact hypothesis, predicted asm movement, stop condition, and worker reasoning level if delegated.
- Do not run or delegate spelling/literal/condition-order microvariants after two same-family no-movement misses unless predicted asm movement is concrete and distinct.
- Treat pre-build `CURRENT (0)` on guarded promotions as stale unless rebuilt for that exact source state.
- Accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.

## Closeout Requirements

- For every miss, record function, hypothesis family, source-shape summary, focused diff, key drift, restore/validation status, next hypothesis, and cooldown/saturation status.
- Keep this file compact. Put detailed repeated probe history in per-function ledgers such as `research/tasks/func_80049794_evidence.md`.
- Update `SESSION_HANDOFF.md` with result, validation, blockers, evidence paths, next packet, and cooldown/saturation status.
