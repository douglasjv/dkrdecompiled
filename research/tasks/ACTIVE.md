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
- Latest do-not-repeat/cooldown note: a 2026-05-31 high discovery pass found no safe mechanism-ready packet for `func_80049794`; avoid promotion-only/object-only `CURRENT (0)` acceptance, broad save/wave microvariants, opening `updateRateF` through `var_f20`, `register f32 var_f20`, carrier-width changes, and other spelling/literal/condition-order variants already recorded in the ledger.
- Next hypothesis: prefer a high/xhigh isolated worker only if it can name a concrete saved-FPR/register-allocation mechanism with predicted prologue, frame, saved-register, or wave-scan movement. Otherwise pivot to another bounded candidate or run discovery/tooling to improve candidate ranking/cooldown behavior.
- Alternate evidence checked: `research/tasks/func_80059208_evidence.md`.
- Latest alternate-packet note: `func_80059208` remains active but saturated for final-tail pointer/FPR lifetime probes. The 2026-05-31 ObjectTransform pointer lifetime probe failed verify with CRCs `0x53D140E7/0x1EA38E5F`; relinked focused diff regressed to `CURRENT (1136)`, kept object X in `$f12` instead of target `$f16`, still materialized `5.0f` after object Z, and retained current `$f10/$f6` vertical-tail allocation. Do not repeat final-tail temp/order, direct object-dot, object-X-first, separate negated checkpoint temp, or transform-pointer lifetime variants without a different compiler mechanism.
- Track evidence checked: `research/tasks/trackbg_render_flashy_evidence.md`.
- Latest discovery/worker note: `trackbg_render_flashy` remains active but saturated for early FPR spelling probes. The 2026-05-31 inverted-primary-cos carrier probe failed verify with CRCs `0xDC79F591/0x31DBA03C`; relinked focused diff regressed to `CURRENT (3108)`, kept initial `0x28d00` `neg.s $f16,$f12` instead of target `$f18`, and only moved a later UV-block negation to `$f18`. Do not repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes.
- Latest tooling note: `tools/query_goal_state.py discovery` now exposes probe-readiness fields for cooldown candidates. It recognizes bulleted `Next useful work` sidecar lines, reports `ready_for_probe: false` when a sidecar still asks for discovery/tooling, and emits the required packet fields (`target`, `evidence_checked`, `rejected_families`, `mechanism_hypothesis`, `predicted_asm_movement`, `stop_condition`) before delegation or source edits.
- Current packet evidence checked: `research/tasks/func_8002B0F4_evidence.md`.
- Latest selector-packet note: `func_8002B0F4` remains active but saturated for model-load lifetime probes. The 2026-05-31 bottomSegment lifetime split failed full verify with CRCs `0x76D9116A/0x07C0B726`; relinked focused diff regressed to `CURRENT (3123)`, widened the frame to `0x130`, shifted `spB0` to `0xB4(sp)`, and still hoisted/spilled `gCurrentLevelModel` at `0x64(sp)`. Do not repeat local segment-index, bottom-only segment-pointer lifetime, initial assignment-order, condition, literal, or carrier variants unless the next hypothesis predicts a distinct model-load lifetime/register-allocation mechanism.
- Current routing status after this note: all 4 default-routable guarded candidates have cooldown sidecars and all 3 parked candidates have recent revival cooldown. `python3 tools/query_goal_state.py next --compact --refresh` reports `recommended_next: discovery`; `research/tasks/MECHANISM_PACKETS.md` is empty after the `func_80059208` ObjectTransform packet was rejected.
- Discovery selector: `python3 tools/query_goal_state.py discovery` reports `discovery_next: tooling` because no sidecar or mechanism ledger entry currently names a probe-ready packet. `python3 tools/query_goal_state.py revival` still reports `revival_next: tooling` because all parked candidates have recent revival cooldown evidence.
- Latest validation baseline: `python3 tools/check_active_surface.py`, `python3 tools/query_goal_state.py next --compact --refresh`, `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py discovery --json`, `python3 tools/query_goal_state.py packet --function func_80059208`, `python3 tools/query_goal_state.py revival`, `python3 -m py_compile tools/query_goal_state.py`, `gmake -j4 CROSS=tools/binutils/mips64-elf-`, and `./score.sh -s` passed on 2026-05-31 after the ObjectTransform packet was rejected and cleared. Matching build reached `Verify: OK`; score remained 97.30%.

## Routing Rules

- Before any source probe or worker delegation, produce a compact routing packet: target, evidence checked, rejected families, exact hypothesis, predicted asm movement, stop condition, and worker reasoning level if delegated.
- Do not run or delegate spelling/literal/condition-order microvariants after two same-family no-movement misses unless predicted asm movement is concrete and distinct.
- Treat pre-build `CURRENT (0)` on guarded promotions as stale unless rebuilt for that exact source state.
- Accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.

## Closeout Requirements

- For every miss, record function, hypothesis family, source-shape summary, focused diff, key drift, restore/validation status, next hypothesis, and cooldown/saturation status.
- Keep this file compact. Put detailed repeated probe history in per-function ledgers such as `research/tasks/func_80049794_evidence.md`.
- Update `SESSION_HANDOFF.md` with result, validation, blockers, evidence paths, next packet, and cooldown/saturation status.
