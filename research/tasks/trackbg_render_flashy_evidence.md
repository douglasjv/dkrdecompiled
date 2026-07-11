# trackbg_render_flashy Evidence Ledger

Purpose: durable negative evidence for `trackbg_render_flashy` so `research/tasks/ACTIVE.md` can stay compact. Source remains active and routable; these entries prevent blind retries of saturated source-shape families.

Current compact read:
- Guarded source: `src/tracks.c` under `#ifdef NON_MATCHING`.
- Original asm: `asm/nonmatchings/tracks/trackbg_render_flashy.s`.
- Current promoted-source checkpoint: full verify fails with CRCs
  `0x93BFD8FF/0x10B9EB38`; relinked focused
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reports
  `CURRENT (1668)`, improved from the historical `CURRENT (1808)` baseline.
- Known drift is the early first-ring FPR allocation around `0x28d00`: target computes scaled cos in `$f12`, scaled sin in `$f2`, emits `neg.s $f18,$f12`, then stores first-ring x/z arrays through stack temps. Promoted C allocates the negative-cos carrier as `$f16` and drifts through the two-wide ring setup around `0x28d5c` with different `$f18/$f8/$f16` lifetimes and stack-store ordering.

## Rejected Probes

- Prior commuted `zPositions[3]` scaled-carrier ordering: changed only `zPositions[3] = scaledXCos + scaledXSin` to the commuted order. Full verify failed with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused diff stayed `CURRENT (1808)`. Do not repeat this commuted single-site ordering.
- Prior all-first-ring `scaledXSin` reuse: rewrote first-ring `xSin * 1280.0f` expressions to reuse `scaledXSin`. Full verify failed with CRCs `0x8310DF9D/0x3EA48C03`; relinked focused diff regressed to `CURRENT (13581)` and widened the frame to `0x168` with saved `$f20/$f21`. Do not repeat first-ring `scaledXSin` reuse probes.
- 2026-05-31 worker plain promoted-current baseline: promoted the existing guarded C body with the current `scaledXSin`/`scaledXCos` first-ring shape intact. Full verify failed with CRCs `0x93D338FF/0x03D9C8FE`; relinked focused diff was `CURRENT (1808)`. Source was restored and restored validation reached `Verify: OK`. Do not repeat plain guarded-C promotion or current-shape baseline probes.
- 2026-05-31 worker ordinary negative-scaled-cos temp: promoted the guard, added `f32 negativeScaledXCos = -scaledXCos;` immediately after `scaledXCos`, and used it only for `xPositions[0]`, `zPositions[0]`, and `zPositions[1]`. Full verify failed with CRCs `0x93D44007/0x9F1400E4`; relinked focused diff regressed to `CURRENT (2087)`. The frame stayed target-sized at `0x158` with no saved `$f20/$f21`, but the early carrier still emitted `neg.s $f16,$f12` instead of target `neg.s $f18,$f12`, shifted two-wide ring temporaries into `$f18/$f8` differently around `0x28d5c`, and moved stack slots down by 4 bytes. Source was restored and restored validation reached `Verify: OK`. Do not repeat ordinary negative-cos temp variants.
- 2026-05-31 worker-guided inverted primary cos carrier: promoted the guard, stored positive scaled cos in `pad_sp108`, made `scaledXCos = -pad_sp108`, and rewrote positive-cos terms to use `pad_sp108` while preserving repeated first-ring `xSin * 1280.0f` spellings. Full verify failed with CRCs `0xDC79F591/0x31DBA03C`; relinked focused diff regressed to `CURRENT (3108)`. The frame stayed target-sized at `0x158`, but the initial first-ring negation at `0x28d00` still emitted current `neg.s $f16,$f12` instead of target `$f18`, while later UV-block negation moved to `$f18` and broadened scheduling/register drift. Source was restored and restored validation reached `Verify: OK`. Do not repeat inverted primary cos carrier or positive-cos scratch-local variants.
- 2026-05-31 high worker first-ring pair-result scratch: promoted the guard and introduced two short-lived first-ring pair-result scratch locals immediately after `scaledXCos`, one for `-scaledXCos + (xSin * 1280.0f)` and one for `-scaledXCos - (xSin * 1280.0f)`, used only for the duplicated negative-cos first-ring stores. Full verify failed with CRCs `0x218FA01A/0x6CF4BEC1`; focused diff regressed sharply to `CURRENT (13795)`. The probe did move the initial `neg.s` into `$f18`, but badly disturbed stack slots and downstream scheduling instead of preserving the target `0x158` first-ring stack-temp pattern. Worker restored `src/tracks.c`. Do not repeat first-ring pair-result scratch locals or duplicate negative-cos pair-result reuse without a different mechanism that predicts contained stack-slot movement.
- 2026-05-31 promoted object-slice audit confirmed the focused false positive for the current guarded body. Promoted `build/src/tracks.c.o` with `NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 AVOID_UB=1'`; focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xB913E050/0x3791FABA`. Objdump still showed the known first-ring allocation drift: frame `0x158`, scaled cos in `$f12`, scaled sin in `$f2`, but initial negative cos emitted as `neg.s $f16,$f12` instead of target `neg.s $f18,$f12`, with follow-on two-wide ring setup using a different `$f18/$f8/$f16` lifetime/store order. Matching `build/src/tracks.c.o` was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`. Do not trust focused `CURRENT (0)` for this packet; next work needs a mechanism that predicts `$f18` for the initial negative-cos carrier without broad stack-slot or downstream scheduling drift.
- 2026-05-31 store-order-only first-ring probe: swapped only the first two first-ring stores so `zPositions[0] = -scaledXCos + (xSin * 1280.0f)` was emitted before `xPositions[0] = -scaledXCos - (xSin * 1280.0f)`. Focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported stale `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0x97834756/0xD6554ABC`. Source and matching-mode `build/src/tracks.c.o` were restored, then `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`. Do not repeat first-two-store ordering probes; they can preserve the focused false positive without producing a matching ROM.
- 2026-05-31 high worker-guided `var_f16` negative-cos lifetime extension: promoted the guard, assigned existing `var_f16 = -scaledXCos` before the first-ring stores, and used it for the negative-cos first-ring and two-wide-ring sites while preserving repeated `xSin * 1280.0f` spellings and store order. Focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported stale `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xD783EB77/0xFFE69FF1`. Source and matching-mode `build/src/tracks.c.o` were restored, then `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`. Do not repeat `var_f16` negative-cos lifetime-extension variants; they can preserve the focused false positive without producing a matching ROM.
- 2026-05-31 follow-up high mechanism discovery found no landable source-level packet. The worker inspected the guarded source, target asm, this ledger, `ACTIVE.md`, and `SESSION_HANDOFF.md`; built a temporary promoted object in `/private/tmp/dkr_tracks_current_nonmatching.o`; and confirmed the current promoted shape still uses frame `0x158`, scaled cos `$f12`, scaled sin `$f2`, `neg.s $f16,$f12`, and immediate doubled-cos `$f18`, while target keeps `$f18` as the negative-cos carrier and delays doubled-cos setup until after first-ring stack-temp stores. The only plausible levers found were scheduling/lifetime barriers, doubled-cos spelling/literal variants, temp introduction, store ordering, volatile/alias forcing, or first-ring scratch reuse; these overlap rejected families or predict broad stack/scheduling drift. Focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported stale `CURRENT (0)` against the restored matching object; full `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`. Recommendation: keep cooldown-routed.
- 2026-06-12 high mechanism-discovery found no complete non-repeated mechanism packet. Evidence checked by child lane `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2`: this ledger, `ACTIVE.md`, selector `next`/`tooling`, packet template, guarded first-ring body in `src/tracks.c`, target asm around `0x28D00`, and a promoted guarded object under `NON_MATCHING=1`. Child baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK` after local ignored setup inputs and `./score.sh -s` stayed decomp `97.30%`, docs `65.47%`. The target still requires target-like scaled cos in `$f12`, scaled sin in `$f2`, initial negative cos as `neg.s $f18,$f12`, delayed doubled-cos setup after first-ring stack-temp stores, and no broad frame/stack-slot/downstream scheduling drift; no ordinary-C mechanism beyond rejected commuted `zPositions[3]`, all-first-ring `scaledXSin` reuse, plain/current promotion, negative-scaled-cos temps, inverted primary-cos carrier, positive-cos scratch locals, pair-result scratch locals, focused `CURRENT (0)`, first-two-store ordering, `var_f16` lifetime extension, scheduling/lifetime barriers, doubled-cos/literal spellings, volatile/alias forcing, or scratch reuse was identified. Child committed evidence `6207d9c5`, imported at `research/tasks/child_threads/trackbg_render_flashy_2026-06-12_child_evidence.md`. Keep cooldown-routed until a genuinely distinct first-ring FPR/source-lifetime mechanism is named.
- 2026-07-09 direct bounded-permuter checkpoint: replacing later
  `scaledXCos` references with equivalent `xCos * 1280.0f` spellings while
  keeping `scaledXCos` for `xPositions[0]` improved the relinked real-object
  score from `CURRENT (1808)` to `CURRENT (1668)`. The frame stayed `0x158`,
  the function stayed the target size, and the promoted CRCs were
  `0x93BFD8FF/0x10B9EB38`. The first mismatch remains target
  `neg.s $f18,$f12` versus current `$f16`, but the two-wide-ring schedule moved
  closer, so this source is retained under `NON_MATCHING`. A declaration-only
  `register f32 var_f16` probe was compiler-identical to the old baseline. A
  generated `xPositions[6]` two-statement array-slot scratch improved the
  focused score to `CURRENT (1342)` but emitted one extra instruction and
  shifted all later code; it was reverted. A 90-second constrained follow-up
  with statement splitting and line-format mutations disabled found no
  same-size improvement beyond `1668`.
- 2026-07-10 three-way-color precedent pass: no matching repo function has an
  analogous negative/doubled-cos/doubled-sin interference cycle. Reintroducing
  the historical all-raw trig products kept frame `0x158` but grew text from
  `0x968` to `0x9AC`, saved `f20/f21`, and moved the negative carrier to `f14`.
  Swapping the named scaled-carrier declaration order or definition order was
  function-assembly identical. IDO normalizes those order-only forms; removing
  the named carriers extends CSE lifetimes and creates saved-FPR pressure.
  Reopen only with a mechanism that changes interference-node creation while
  preserving named lifetimes, no new stack temp, and exact size `0x968`.
- A bounded external search likewise found the exact FPR signature only in
  `dkrwide`'s asm-backed copy of this same function; its C remains
  `GLOBAL_ASM`. Upstream PR #579 / commit `ab1cbdb7` is the sole historical C
  reconstruction and uses the already-rejected all-scaled-carrier family.
  Public fork history and expression searches exposed no independent source
  mechanism, so the retained `CURRENT (1668)` checkpoint remains the strongest
  source-backed frontier.
- A 2026-07-10 promoted `-mips1` split-elision pass reproduced the best
  two-statement `xPositions[6]` scratch at `CURRENT (1342)`, frame `0x158`, and
  size `0x96C`; its sole size growth is the intermediate
  `swc1 f10,0xF4(sp)`. Nested assignment restores target size `0x968` but
  regresses to `1744`; a scalar scratch returns to retained `1668`, and the
  comma form keeps the extra store. Moving required `xPositions[7]` or
  `xPositions[5]` stores into the barrier scored `2281/1755`; trying
  `xPositions[4]`, `zPositions[4]`, `xPositions[8]`, or `zPositions[5]`
  scored `4177/4185/4598/7071` and still produced `0x96C` or `0x970` text.
  The allocation gain is coupled specifically to an additive array-slot store;
  no tested required store can replace it.
- The required-store barrier search was subsequently completed for all 17
  other `xPositions[]`/`zPositions[]` assignments. Every moved store produced a
  distinct object and none improved retained `1668` or scratch `1342`; the best
  moved-store score was `3293`. Thirteen bodies stayed `0x96C`, two grew to
  `0x970`, and two to `0x980`; zero returned to target `0x968`. Reordering any
  single independent array store cannot elide the additive scratch write.
- A corrected fakematch-compensation audit tested the actual later repeated
  `var_a2` assignment. Removing it or replacing it with self-assignment shrank
  text to `0x91C` and regressed to `CURRENT (11307)`; changing its RHS among
  `height * 16`, `height * unkA1`, or regrouped multiplication was compiler-
  identical to scratch `1342/0x96C`. An initial apparent exact-size result was
  rejected during manual permuter-output review because an unanchored probe had
  changed the first live sizing assignment instead of the dead repeat. No
  semantic exact-size compensation or permuter output survives this audit.

Next useful work should continue from the retained `CURRENT (1668)` raw-cosine
checkpoint and find a same-size mechanism for target-like `$f18` movement
without broad stack-slot/downstream scheduling drift. Do not repeat ordinary
negative-cos temps, inverted-primary-cos spelling, first-ring pair-result
scratch locals, first-two-store ordering, `var_f16` lifetime extension, or the
size-growing `xPositions[6]` scratch split. Never rely on focused `CURRENT (0)`
without full ROM `Verify: OK`.
