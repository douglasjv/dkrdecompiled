# `func_8008FF1C` External-Source Checkpoint (2026-07-09)

## Outcome

The source shape from JordanLongstaff commit
[`9f420e1d`](https://github.com/JordanLongstaff/Diddy-Kong-Racing/commit/9f420e1d9fee13529dee0657379acb238d40fad3)
is retained under `NON_MATCHING` after adapting only the renamed local APIs.
It is the strongest current source checkpoint, but it is not an exact match.
Matching mode remains asm-backed and the full build reaches `Verify: OK`.

## Promoted Result

- Function size and frame match the target: `0x5CC` and `0x80`.
- Focused diff: `CURRENT (10)`.
- The selected-track load, branch, and delay-slot store now match exactly:
  `lh t2,0(s1)`, branch on `t2`, and `sw v0,0(s0)` in the delay slot.
- The sole code drift is the track-name address temporary at `0x90CD4`:
  target emits `addu t4,t3,s2; addu s1,t4,t5`, while current emits
  `addu t3,t3,s2; addu s1,t3,t5`.
- Promoted full-ROM CRCs are `0x53D420E7/0x231B2668`; therefore the source
  must stay guarded until those two instructions match.

The historical fork was also rebuilt in an isolated checkout after mapping
its three missing API names. It reproduces the same exact-size `t4`/`t3`
register drift, so the public commit title is not proof of an exact match.
Its apparent `gPlayerSelectVehicle` versus
`gTrackSelectRenderDetails + 0x90` relocation difference is address-equivalent
and does not affect linked code.

## Rejected Bounded Variants

- `gTrackSelectX / 320.0f`: no object movement.
- Commuting or splitting the `(trackY * 6) + trackX` index: no improvement or
  widened the focused diff.
- Signed/unsigned 32-bit `new_var`, explicit casts, pointer/dereference forms,
  shift decompositions, and staged index locals: broadened allocation or
  introduced 64-bit spills and frame drift.
- Empty liveness probes near the index (`trackX`, `pad2`, `new_var`) and moving
  the existing `if (1) {}`: widened the frame to `0xB8` and regressed broadly.
- Redundant result casts, `unsigned long long new_var`, and algebraic multiply
  spellings: no movement from `CURRENT (10)`.
- The older ignored permuter environment compiles this translation unit with
  `-mips2`; its scores and branch-likely output are invalid for the real
  `-mips1` object. The bounded follow-up used the real `-mips1` compiler path.
- A third real-`-mips1` IR pass confirmed that address-of indexed-element and
  full-index-assignment shapes can prevent the unwanted two-address
  coalescing, matching nearby source precedent. In this full function they
  recolor the block to `t8/t9` or `t8/t2` instead of target `t4/t5`; pointer-
  to-array association and redundant-use variants also miss or spill. Do not
  repeat these non-coalescing shapes without an independent global-coloring
  mechanism.

## Reopen Condition

Continue only with a source mechanism that preserves every already-exact
instruction, frame `0x80`, and size `0x5CC`, while preventing coalescing of the
`t3 + s2` result so the temporary is allocated to `t4`. Do not treat the
external commit or a focused score alone as acceptance; the full ROM must
reach `Verify: OK` with the C body promoted.
