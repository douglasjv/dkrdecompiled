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
- Current selector result on 2026-05-31 after cooldown-aware tooling: 4 default-routable guarded candidates, 3 skipped exhausted notes, 3 cooldown ledgers, recommended next `func_8002B0F4` in `src/tracks.c:2686`, asm `asm/nonmatchings/tracks/func_8002B0F4.s`, kind `NON_EQUIVALENT`.
- Current packet status: `func_80049794` is active but saturated for low-signal source spelling probes. Do not edit it again without a compact routing packet that names a distinct compiler-mechanism hypothesis and predicted asm movement.
- Evidence path checked: `research/tasks/func_80049794_evidence.md`.
- Latest do-not-repeat/cooldown note: avoid promotion-only/object-only `CURRENT (0)` acceptance, broad save/wave microvariants, opening `updateRateF` through `var_f20`, `register f32 var_f20`, carrier-width changes, and other spelling/literal/condition-order variants already recorded in the ledger.
- Next hypothesis: prefer a high/xhigh isolated worker only if it can name a concrete saved-FPR/register-allocation mechanism with predicted prologue, frame, saved-register, or wave-scan movement. Otherwise pivot to another bounded candidate or run discovery/tooling to improve candidate ranking/cooldown behavior.
- Alternate evidence checked: `research/tasks/func_80059208_evidence.md`.
- Latest alternate-packet note: `func_80059208` remains active after two promoted 2026-05-31 final-tail lifetime probes. Stepwise final-tail accumulation regressed to `CURRENT (1125)` with CRCs `0x24253B4A/0xE9DAC447`; object-X-first lifetime stayed `CURRENT (870)` with CRCs `0x53D141DF/0xB9D4B481`. Both retained the final-tail FPR/load-order family around `0x5a260`; do not repeat final-tail spelling-only probes without distinct predicted asm movement.
- Track evidence checked: `research/tasks/trackbg_render_flashy_evidence.md`.
- Latest discovery/worker note: `trackbg_render_flashy` plain promoted-current baseline on 2026-05-31 failed with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused diff was `CURRENT (1808)`. It still allocated the early negative-cos carrier as current `$f16` instead of target `$f18`; do not repeat plain promotion/current-shape or first-ring `scaledXSin` reuse probes.
- Latest tooling note: `tools/query_goal_state.py` now demotes active candidates with sidecar evidence ledgers that explicitly say saturated, cooling down, pivot/discovery, or pivot to another candidate. This keeps those functions routable but routes fresh continuations to `func_8002B0F4` until a distinct hypothesis is recorded for a cooled-down candidate.
- Current packet evidence checked: `research/tasks/func_8002B0F4_evidence.md`.
- Latest selector-packet note: `func_8002B0F4` remains active after a 2026-05-31 worker bbox-before-segment ordering miss. Full verify failed with CRCs `0x7856718A/0xA6A743D8`; relinked focused diff regressed to `CURRENT (3965)` and worsened the early `gCurrentLevelModel` spill at `0x60(sp)`. Do not repeat initial segment/bbox assignment-order pressure probes unless the next hypothesis predicts removal of that spill.
- Current routing status after this note: all 4 default-routable guarded candidates now have cooldown sidecars. `python3 tools/query_goal_state.py next --compact --refresh` reports `cooldown_notes=4` and recommends a cooldown-demoted `func_80049794`; treat that as a discovery/tooling route unless a distinct compiler-mechanism packet is named first.
- Latest validation baseline: `python3 tools/check_active_surface.py` reported active surface ok on 2026-05-31 before the latest restored validation.

## Routing Rules

- Before any source probe or worker delegation, produce a compact routing packet: target, evidence checked, rejected families, exact hypothesis, predicted asm movement, stop condition, and worker reasoning level if delegated.
- Do not run or delegate spelling/literal/condition-order microvariants after two same-family no-movement misses unless predicted asm movement is concrete and distinct.
- Treat pre-build `CURRENT (0)` on guarded promotions as stale unless rebuilt for that exact source state.
- Accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.

## Closeout Requirements

- For every miss, record function, hypothesis family, source-shape summary, focused diff, key drift, restore/validation status, next hypothesis, and cooldown/saturation status.
- Keep this file compact. Put detailed repeated probe history in per-function ledgers such as `research/tasks/func_80049794_evidence.md`.
- Update `SESSION_HANDOFF.md` with result, validation, blockers, evidence paths, next packet, and cooldown/saturation status.
