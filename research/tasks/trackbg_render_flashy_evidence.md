# trackbg_render_flashy Evidence Ledger

Purpose: durable negative evidence for `trackbg_render_flashy` so `research/tasks/ACTIVE.md` can stay compact. Source remains active and routable; these entries prevent blind retries of saturated source-shape families.

Current compact read:
- Guarded source: `src/tracks.c` under `#ifdef NON_MATCHING`.
- Original asm: `asm/nonmatchings/tracks/trackbg_render_flashy.s`.
- Recurring promoted-source baseline: full verify fails with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reports `CURRENT (1808)`.
- Known drift is the early first-ring FPR allocation around `0x28d00`: target computes scaled cos in `$f12`, scaled sin in `$f2`, emits `neg.s $f18,$f12`, then stores first-ring x/z arrays through stack temps. Promoted C allocates the negative-cos carrier as `$f16` and drifts through the two-wide ring setup around `0x28d5c` with different `$f18/$f8/$f16` lifetimes and stack-store ordering.

## Rejected Probes

- Prior commuted `zPositions[3]` scaled-carrier ordering: changed only `zPositions[3] = scaledXCos + scaledXSin` to the commuted order. Full verify failed with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused diff stayed `CURRENT (1808)`. Do not repeat this commuted single-site ordering.
- Prior all-first-ring `scaledXSin` reuse: rewrote first-ring `xSin * 1280.0f` expressions to reuse `scaledXSin`. Full verify failed with CRCs `0x8310DF9D/0x3EA48C03`; relinked focused diff regressed to `CURRENT (13581)` and widened the frame to `0x168` with saved `$f20/$f21`. Do not repeat first-ring `scaledXSin` reuse probes.
- 2026-05-31 worker plain promoted-current baseline: promoted the existing guarded C body with the current `scaledXSin`/`scaledXCos` first-ring shape intact. Full verify failed with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused diff was `CURRENT (1808)`. Source was restored and restored validation reached `Verify: OK`. Do not repeat plain guarded-C promotion or current-shape baseline probes.

Next useful work needs a distinct early FPR-allocation/source-lifetime hypothesis that predicts movement of the negative-cos carrier into target `$f18` without saved-FPR/frame growth, or pivot to another bounded candidate/discovery packet.
