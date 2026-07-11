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
- A corrected 2026-07-10 isolated permuter harness used the repository's real
  IDO `-O2 -mips1` command. After forcing a fresh menu compile, it reproduced
  full-link CRCs `0x53D420E7/0x231B2668`, focused `CURRENT (10)`, and permuter
  score `20` for the sole `t4`/`t3` pair. A 275-second four-worker run found no
  lower score; its final observable 20-second sample covered 1,696 iterations
  with 25 compile errors and produced no improved output. An initial apparent
  zero was a stale copied asm-backed object and was discarded. Do not repeat
  the invalid `-mips2` harness or treat stale object output as a match.
- A third real-`-mips1` IR pass confirmed that address-of indexed-element and
  full-index-assignment shapes can prevent the unwanted two-address
  coalescing, matching nearby source precedent. In this full function they
  recolor the block to `t8/t9` or `t8/t2` instead of target `t4/t5`; pointer-
  to-array association and redundant-use variants also miss or spill. Do not
  repeat these non-coalescing shapes without an independent global-coloring
  mechanism.
- A 2026-07-10 exact-size carrier follow-up assigned the complete index to a
  separate 32-bit local. IDO reliably prevented the unwanted coalescing, but
  rotated the three roles to `t8/t9/t3` instead of target `t3/t4/t5`; adding a
  second explicit index local was compiler-identical. The corresponding
  declaration/type-focused permuter search could only return to score `20`,
  the retained one-temporary baseline. This confirms that merely materializing
  the full index changes the correct interference edge but loses the required
  global coloring.
- A deterministic finite search then exhausted declaration and storage-class
  ordering as explanations. All 226 unique adjacent/single-move declaration
  orders compiled to one identical full-function digest and score `20`. All
  16,384 subsets of `register` qualifiers across the 14 active scalar/pointer
  locals also retained exactly the same two differing words at `0x1B8/0x1BC`;
  no subset changed even one instruction.
- A separate 23-form index-expression sweep covered embedded, staged, nested,
  comma, compound-assignment, commuted, shift/add, and shift/subtract forms.
  Nine forms kept exact text size and differed only at the same two words; all
  others grew text to `0x5F0`, `0x600`, or `0x610`. No expression emitted
  `t4`.
- A 217-variant explicit-cast matrix then covered signed/unsigned 8-, 16-,
  32-, and 64-bit casts plus `int`/`long` spellings on `trackX`, `trackY`, the
  multiplier, intermediate `new_var`, whole sum, array index, and all paired
  operand-width combinations. Sixty-eight variants preserved exact text and
  the same two-word miss; all others broadened the diff, changed size, or were
  rejected by IDO. Operand/result width coercion is therefore exhausted too.
- Historical-context restoration is also ruled out. The fork and current repo
  use identical real IDO `-O2 -mips1` flags, relevant tool revisions, typedefs,
  struct layouts, headers, and globals. Untouched `9f420e1d` has three stale
  implicit-int APIs, but direct compilation before and after adapting them is
  instruction-identical apart from relocation names and still emits the
  `t3/t3` pair. The older bQDRA-linked row/`s16` selected-track hybrid restores
  the old `v1` load and broadly recolors the index block; retaining only its
  separate row carrier is object-identical to the score-20 baseline.
- Historical control isolates the coupled allocator tradeoff: the pre-external
  two-load selected-track source naturally emits the target `t3 -> t4 -> s1`
  index block, while the corrected single selected-track load/`t2` branch
  globally recolors that later block. No matching repo precedent combines the
  signed-byte indexed load, `t4/t5`, and pointer reuse across the call.
- A follow-up address-DAG audit confirmed that target `t3` is genuinely dead
  at the first `addu`; target `t4` is a compiler coalescing choice, not required
  source liveness. Explicit element-pointer ownership through the otherwise
  unused `trackName`/`hubName` locals, row pointers, pointer-add dereferences,
  and commuted pointer arithmetic either remained the same `t3/t3` pair or
  broadly recolored. The plausible source story that `s1` was an explicit
  element pointer therefore does not reproduce target code under the retained
  global web.
- A bounded 32-variant real-IDO mechanism matrix covered pointer ownership,
  call-result carriers, condition carriers, inverse/nested/do/switch CFGs, and
  scoped lifetimes. Thirteen exact-size variants were instruction-identical to
  retained score `20`; every other variant changed size or added broader drift.
  Full results: `/private/tmp/dkr-menu-targeted-32/report.json`.
- Coupled row/selected-track web tests separated the single masked
  `gTrackSelectIDs` load from the row carrier and restored the older repeated
  direct menu-ID index. The best forms preserved the exact `lh t2`, branch, and
  delay-slot store, but recolored the desired address node to `t6/t7` or
  `t8/t9`, scoring `815`; combining that web split with full-index and explicit
  pointer shapes was worse. Additional fake-lifetime, carrier/type, and
  operand-association crosses either normalized to the retained score-20
  object or produced a nearest score-30 commuted `addu t3,s2,t3`, never target
  `addu t4,t3,s2`. Reports are under
  `/private/tmp/menu-pointer-owner-matrix`,
  `/private/tmp/menu-fake-lifetime-matrix`,
  `/private/tmp/menu-fake-cross-matrix`, `/private/tmp/menu-type-shape-cross`,
  `/private/tmp/menu-selected-web-matrix`, and
  `/private/tmp/menu-coupled-web-index`.

## Reopen Condition

Continue only with a source mechanism that preserves every already-exact
instruction, frame `0x80`, and size `0x5CC`, while preventing coalescing of the
`t3 + s2` result so the temporary is allocated to `t4`. Do not treat the
external commit or a focused score alone as acceptance; the full ROM must
reach `Verify: OK` with the C body promoted.
