# func_80059208 Evidence Ledger

Purpose: durable negative evidence for `func_80059208` so `research/tasks/ACTIVE.md` can stay compact. Source remains active and routable; these entries prevent blind retries of saturated source-shape families.

Current compact read:
- Guarded source: `src/racer.c` under `#ifdef NON_MATCHING`.
- Original asm: `asm/nonmatchings/racer/func_80059208.s`.
- Recurring baseline after promoted source: full verify fails with CRCs `0x53D141DF/0xB9D4B481`; relinked focused `./diff.sh func_80059208 --compress-matching 2 --no-pager` reports `CURRENT (870)`.
- Known drift is the final-tail FPR allocation/load-order family around `0x5a260`: target loads object X into `$f16`, materializes the `5.0f` constant before object Z, emits an early `neg.s $f0,$f0` for the checkpoint dot, then adds object and checkpoint dots. Current loads object X/Z into `$f12/$f0`, folds the dot as `sub.s`, and carries later vertical math through `$f10/$f6` instead of target `$f6/$f10`.

## Rejected Probes

- 2026-05-25 `s8 splineIndex` carrier: changed only `s32 splineIndex` to `s8 splineIndex` while promoting the guard. Relinked focused diff stayed `CURRENT (870)` and full verify failed with CRCs `0x53D141DF/0xB9D4B481`. Do not repeat carrier-size tweaks for `splineIndex`.
- 2026-05-25 `tempZ` through `distance` carrier: changed the third spline result assignment to route through `distance` before `tempZ`. Relinked focused diff stayed `CURRENT (870)` and full verify failed with CRCs `0x53D141DF/0xB9D4B481`. Do not repeat this result-carrier spelling.
- 2026-05-25 direct normalization division: changed reciprocal/multiply normalization to direct `diffX / distance` and `diffZ / distance`. Relinked focused diff regressed to `CURRENT (2580)` and removed the target reciprocal carrier. Do not repeat direct-division normalization.
- 2026-05-25 checkpoint-dot-first and positive checkpoint-dot/subtract final-tail orderings: both stayed in the known final-tail family at `CURRENT (870)` with CRCs `0x53D141DF/0xB9D4B481`. Do not repeat these operand-order spellings.
- 2026-05-25 vertical `pad3` alias: routed the Y delta through `pad3`; relinked focused diff regressed to `CURRENT (1840)`. Do not repeat this vertical alias spelling.
- 2026-05-31 explicit final-tail accumulation split: promoted the guard, split object dot/checkpoint dot into stepwise `pad`, `pad2`, `diffX /= divisor`, then `diffX = -diffX`. Full verify failed with CRCs `0x24253B4A/0xE9DAC447`; relinked focused diff regressed to `CURRENT (1125)`, inserted an extra `swc1 $f4,0x54(sp)`, and still missed the target early `neg.s`/object-load order. Do not repeat stepwise accumulation split.
- 2026-05-31 object-X-first final-tail lifetime: promoted the guard, computed `pad = splinePos * diffX`, then checkpoint-dot `pad2`, then loaded object Z and added it to `pad`. Full verify failed with CRCs `0x53D141DF/0xB9D4B481`; relinked focused diff stayed `CURRENT (870)` with identical final-tail FPR/load-order drift. Do not repeat object-X-first lifetime spelling.

Next useful work should use a distinct compiler-mechanism hypothesis for final-tail FPR allocation or pivot to another bounded candidate/discovery packet. Avoid more final-tail spelling-only probes unless predicted asm movement is concrete and different from the entries above.
