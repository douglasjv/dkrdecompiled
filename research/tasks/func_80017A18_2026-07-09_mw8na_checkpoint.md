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

## Reopen Condition

Continue from the retained A2/C2 source with a mechanism that keeps origin
values in the target `f18/f20/f22` retry-loop lifetime and reproduces the
target end-of-facet reload sequence while retaining the exact frame, result
slot, and saved-register family. Do not regress to current-baseline plane
indexing or the rejected pointer/edge-sum hybrid.
