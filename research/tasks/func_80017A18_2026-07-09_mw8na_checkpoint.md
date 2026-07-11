# `func_80017A18` Mw8Na/A2-C2 Checkpoint (2026-07-09)

## Outcome

The guarded C body now uses the strongest target-structured source family found
in the current decomp.me lineage. Matching mode remains asm-backed and the full
build reaches `Verify: OK`.

The public `func_80017A18` scratch family has 16 members. Its newest best source,
[`Mw8Na`](https://decomp.me/scratch/Mw8Na), scores `5971` in decomp.me and
recovers the target `0x120` frame, but colors the outer index and mask away from
the target saved registers. The retained local candidate adds persistent
`x2/y2/z2` origin values plus `A2/C2` products to that source.

## Promoted Real-Tree Result

- Full-ROM CRCs: `0x573A8C93/0x453F46E9` (nonmatching, so the guard remains).
- Focused real linked diff: `CURRENT (7869)`, improved from the previous
  retained baseline `CURRENT (8246)`.
- Frame: exact `0x120`.
- Result accumulator: exact `sp+0xF8` slot.
- Saved-register family is now exact:
  - outer index: `s1`
  - target X/Y/Z pointers: `s2/s3/s4`
  - surfaces pointer: `s5`
  - result bitmask: `s6`
  - origin X/Y/Z pointers: `s7/s8/ra`
  - collision-radius pointer: spilled
- The candidate is still `0x18` bytes shorter than target and retains broad
  floating-point scheduling/color drift.

The isolated function scorer reported `7504`; the authoritative linked repo
object reports `7869`. Use the linked real-tree result for acceptance and future
comparison.

## Mechanism And Rejected Siblings

- Loading `x2/y2/z2` before radius is the mechanism that recovered the entire
  target saved-register family.
- Keeping `A2 = A * x2` and `C2 = C * z2` live for both the primary sum and the
  steep-plane correction places the result accumulator at exact `sp+0xF8` and
  preserves frame `0x120`.
- Plain Mw8Na has the better standalone numeric score but wrong saved-register
  ownership.
- A declaration-only `s32 pad[2]` sibling preserved the saved-register family
  and frame `0x120`, but left the result at `sp+0xF0` and scored worse in the
  isolated pass.
- The earlier base/edge-plane pointer plus dedicated-edge-sum hybrid stayed at
  frame `0x130`, kept the mask in `ra`, and remains rejected.
- Moving `x2/y2/z2` assignments into the retry loop regressed to isolated
  `8202` and broke the recovered mapping (mask `ra`, origins `s6/s7/s8`).
- Adding `register` to the retained outer `x2/y2/z2` declarations produced no
  object movement; promoted CRCs stayed `0x573A8C93/0x453F46E9`.
- A 2026-07-10 radius-first assignment-order probe preserved frame/result but
  regressed saved-GPR ownership and focused score to `CURRENT (8783)`.
- Rewriting the primary and target-plane sums as sequential accumulations
  preserved frame `0x120`, `sp+0xF8`, saved GPRs, and size `0x444`, but only
  moved the focused score from `7869` to `7864`; origin values still spilled
  at `A8/A4/A0` with none of target `f18/f20/f22` retry lifetime. This is not
  material enough to retain and rules out simple sum grouping.
- A 2026-07-10 retry-lifetime pass showed that explicit loop-header copies of
  all three origins do create loop-carried FPRs, but color them
  `f22/f26/f24`, widen the frame to `0x130`, and grow text to `0x464` (target
  `0x45C`). Reusing `x3/y3/z3` instead creates `f16/f18/f20` copies but
  collapses the frame to `0x110` and text to `0x43C`. A condition self-
  assignment was object-identical. The needed mechanism is therefore a
  loop-carried origin lifetime that preserves separate intersection ownership
  without adding three locals.
- A complete 27-way per-axis ownership matrix independently selected direct
  origin, explicit retry local, or `x3/y3/z3` reuse for X/Y/Z. All combinations
  compiled to unique bodies and preserved the saved-GPR family; none matched.
  Seven retained target frame `0x120`, result `sp+0xF8`, and size ceiling, but
  baseline direct/direct/direct remained best. Reuse/reuse/direct recovered
  partial header colors `f18/f20` while leaving Z stack-resident; no combination
  produced target `f18/f20/f22`. Axis-local ownership is now saturated and the
  next mechanism must couple interference across axes.
- The seven target-constrained ownership families were then crossed with all
  six X/Y/Z statement orders (42 bodies, 22 unique instruction streams). Every
  body preserved frame `0x120`, result `sp+0xF8`, saved GPRs, and size ceiling;
  none beat the direct/direct/direct baseline or produced all
  `f18/f20/f22`. Order changes only perturb interpolation scheduling: RRD keeps
  partial X/Y, DER keeps Y/Z, and RED assigns X to the wrong `f22` role.
- Public family lineage exposed newer scratch `96Vzj` (standalone `3934`). Raw
  promotion is numerically closer at linked `CURRENT (6280)` and size `0x450`,
  but it is behaviorally invalid: it overwrites the persistent collision mask
  with edge-plane indices and uses target rather than origin coordinates in the
  steep correction. Minimal semantic repairs scored `8999` and `9744`, with
  wrong frames/register ownership. The raw source and repairs are rejected;
  retained A2/C2 remains the strongest valid checkpoint.
- A coupled-origin representation pass replaced the three scalar origin locals
  with one `Vec3f origin` and used its members in the primary sum,
  interpolation, and timeout reset. With the authoritative shared promotion
  flags (`ANTI_TAMPER=1 NON_EQUIVALENT=1 AVOID_UB=1`), the current-tree linked
  score improves by 140 points, `CURRENT (7934) -> CURRENT (7794)`. The older
  `7869` ledger baseline predates the retained racer checkpoint; compare
  candidates within one promoted tree. The vector form keeps exact frame
  `0x120`, size `0x444`, result `sp+0xF8`, and the complete saved-GPR family.
  It only reverses the three permanent origin spill slots and still loads the
  origins as `f8/f10/f4`, not target `f18/f20/f22`. This source is retained.
- The target's `0x18` size excess is now fully explained: it loads persistent
  origin X/Y/Z into `f18/f20/f22`, spills them to `sp+A4/A0/9C` at the retry
  header, then reloads them in reverse order at the retry latch. Historical
  source before commit `105913c7` assigns the three origins inside the `do`
  loop and even annotates those exact stack slots, proving the source cause of
  all six missing instructions. Moving those loads into `do` alone was already
  rejected because it breaks saved-GPR ownership; future work must pair that
  known FPR mechanism with a contained GPR-allocation mechanism.
- Scoped scalar/`Vec3f` retry copies combined with target-product ownership get
  closer to the correct topology (`f22/f24/f26`) but widen the frame to
  `0x128`, move the result to `sp+0x100`, and grow text to `0x460`. Direct or
  local origin-pointer cursors collapse the frame or saved-GPR mapping and are
  rejected. Lexical scoping does not shorten the copy lifetimes in IDO.
- A semantic target-dataflow audit corrected an earlier assumption: target
  caches `A * x1` and `C * z1` for the gentle-slope correction, consistent with
  `src/hasm/collision.c`; retained A2/C2 instead caches origin products. The
  scalar target-product correction preserves frame/size/GPRs but regresses the
  current-tree linked score to `CURRENT (8490)`, and its retry-copy cross still
  misses frame/color constraints, so it is not retained. An exact future match
  must eventually recover this target-product ownership as well as the retry
  origin phis.

## Reopen Condition

Continue from the retained A2/C2 source with a mechanism that keeps origin
values in the target `f18/f20/f22` retry-loop lifetime and reproduces the
target end-of-facet reload sequence while retaining the exact frame, result
slot, and saved-register family. Do not regress to current-baseline plane
indexing or the rejected pointer/edge-sum hybrid.
