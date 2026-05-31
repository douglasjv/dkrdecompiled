# func_8002B0F4 Evidence Ledger

Purpose: durable negative evidence for `func_8002B0F4` so `research/tasks/ACTIVE.md` can stay compact. Source remains active and routable; these entries prevent blind retries of saturated source-shape families.

Current compact read:
- Guarded source: `src/tracks.c` under `#ifdef NON_EQUIVALENT`.
- Original asm: `asm/nonmatchings/tracks/func_8002B0F4.s`.
- Recurring promoted-source family: current C tends to hoist `gCurrentLevelModel` before the segment loop and spill it around `0x60(sp)`, while target reloads `gCurrentLevelModel` inside the loop. Segment/grid and bottom water scheduling then drift broadly.

## Rejected Probes

- 2026-05-25 `sp108 <= 0` entry-guard spelling: changed `if (sp108 == 0 || sp108 >= 8)` to `if (sp108 <= 0 || sp108 >= 8)`. Relinked focused diff regressed from promoted baseline `CURRENT (2860)` to `CURRENT (3060)`, changed target `beqz v0` into current `blez v0`, and retained the unwanted early `gCurrentLevelModel` spill. Do not repeat this entry-guard spelling.
- Prior inner face-loop `!=` bound spelling: changed `faceNum < nextFaceOffset` to `faceNum != nextFaceOffset`. Relinked focused diff regressed to `CURRENT (3870)`, changed the inner loop family from target `slt`/`bnez` to `bne`, and reintroduced the model spill. Do not repeat loop-bound spellings.
- Prior local `LevelModel *levelModel` pressure spelling: introduced a local model pointer for segment, bounding-box, texture, and bottom segment accesses. Relinked focused diff regressed to `CURRENT (4208)`, widened the frame to `0x130`, and spilled the model pointer. Do not repeat local model-pointer pressure probes.
- Prior texture-index carriers, flags carriers, pointer-arithmetic segment setup, bottom store-order, condition-order, literal/cast, and local-width spellings repeatedly retained the early model spill family and regressed or stayed in the same broad segment/grid drift. Do not repeat those spelling families without a distinct mechanism that predicts removal of the model spill.
- 2026-05-31 worker bbox-before-segment ordering: promoted the guard and reordered initial loop setup to assign `currentBoundingBox` before `currentSegment`. Full verify failed with CRCs `0x7856718A/0xA6A743D8`; relinked focused diff regressed to `CURRENT (3965)`. The probe made the early model-load family worse by hoisting `gCurrentLevelModel` before the segment loop and spilling it to `0x60(sp)`, then reloading it; target loads `gCurrentLevelModel` inside the loop. Source was restored and restored validation reached `Verify: OK`. Do not repeat initial segment/bbox assignment-order pressure probes unless the next hypothesis specifically predicts removal of the early model stack spill.

Next useful work needs a distinct model-load lifetime/register-allocation mechanism that predicts target-like in-loop `gCurrentLevelModel` loads or removal of the `0x60(sp)` model spill, not another ordering, condition, literal, or carrier spelling.
