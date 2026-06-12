# Session Handoff

- Generated at: 2026-06-12 21:44:00Z
- Branch: `master`
- HEAD: `41833d38`
- Completed task: `trackbg_render_flashy-child-evidence-import`
- Summary: Imported `trackbg_render_flashy` child evidence after the child committed a durable negative-evidence result.

## Validation

- `git status --short --branch` reported `## master...origin/master [ahead 1002]` before child evidence import edits.
- `python3 tools/check_active_surface.py` reported active surface ok.
- Current routing repair supersedes the older discovery-only result:
  `python3 tools/query_goal_state.py next --compact --refresh` reports 7
  routable guarded candidates, `skipped_exhausted=0`, and `recommended_next:
  func_8008FF1C`.
- `python3 tools/query_goal_state.py discovery`, `revival`, and `tooling`
  report routable candidates while preserving cooldown/readiness evidence as
  anti-repeat guidance.
- `python3 -m py_compile tools/query_goal_state.py` passed.
- `python3 tools/query_goal_state.py packet --function func_8008FF1C --template` emitted the parked packet skeleton.
- High worker result for `func_8008FF1C`: no landable source patch. Forced promotion reproduced stale focused `CURRENT (0)`, but full ROM verify failed with calculated CRCs `0xA63BE13D/0xB86942B3`; objdump showed `lh v1,0(s1)`, `sw v0,0(s0)` before the branch, then `beq v1,at,...`, not target `lh t2,0(s1)` with delay-slot `sw v0,0(s0)`.
- `python3 tools/query_goal_state.py packet --function func_8008FF1C` reports
  `ready_for_probe: true` with a readiness gap requiring a non-repeated child
  hypothesis.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reports decomp progress `97.30%` and documentation progress `65.47%`.
- Parent imported child evidence from `codex/func-8002b0f4-child-evidence` commit `b16fb37c` into `research/tasks/child_threads/func_8002B0F4_2026-06-12_child_evidence.md`.
- Child restored validation reached `Verify: OK`; the tested `register` probe on `currentSegment`, `currentBoundingBox`, and `currentBatch` produced no model-base spill movement and was reverted.
- New child thread: `019ebdcb-1042-7690-a495-cd91360dfc59`; worktree `/Users/douglas/.codex/worktrees/c3a6/dkrdecompiled`; pending worktree id `local:ac8dbccc-b093-4e13-8703-28fabf1519e8`; target `func_80049794`.
- Child `019ebdcb-1042-7690-a495-cd91360dfc59` committed evidence-only result
  `1e9cccf5` on `codex/func-80049794-child`; parent imported it to
  `research/tasks/child_threads/func_80049794_2026-06-12_child_evidence.md`.
  No source edit was made; child-local restored validation reached `Verify: OK`.
- New pending child worktree id: `local:809f1788-2fb6-4212-a1ed-6d73150c0652`;
  target `func_80059208`.
- Pending worktree resolved to child thread
  `019ebdd6-3f3b-7c61-a36f-0a9928ad0eb9` at
  `/Users/douglas/.codex/worktrees/1264/dkrdecompiled`; initial child status
  was detached `HEAD` with no tracked diffs.
- Parent heartbeat confirmed child remains active on branch
  `codex/func-80059208-child` with no tracked diffs or staged changes. The
  child has copied ignored local validation inputs, reproduced expected
  asm-backed focused `CURRENT (0)`, and is still resolving local setup inputs
  before baseline `Verify: OK`; latest setup item was `tools/dkr_assets_tool`.
- Later heartbeat confirmed child-local baseline validation reached `Verify: OK`
  and `./score.sh -s` reported decomp `97.30%`, docs `65.47%`. The child
  reported no distinct non-repeated final-tail mechanism and said it was
  applying evidence-only closeout edits, but the child worktree still had no
  tracked/staged changes and `HEAD` remained `c2ed22a3`; parent sent a
  follow-up asking the child to finish the evidence commit or report the exact
  blocker.
- Child `019ebdd6-3f3b-7c61-a36f-0a9928ad0eb9` committed evidence-only result
  `e09f5f42` on `codex/func-80059208-child`; parent imported it to
  `research/tasks/child_threads/func_80059208_2026-06-12_child_evidence.md`.
  No source edit was made; child-local restored validation reached `Verify: OK`.
- New pending child worktree id: `local:52703ce1-0286-41c7-8dff-cedfcb241432`;
  target `trackbg_render_flashy`.
- Pending worktree resolved to child thread
  `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2` at
  `/Users/douglas/.codex/worktrees/d949/dkrdecompiled`; initial child status
  was detached `HEAD` with no tracked diffs.
- Parent heartbeat confirmed child remains active with no tracked or staged
  changes. The child copied ignored validation inputs locally, reached
  child-local baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-` with
  `Verify: OK`, reproduced the expected asm-backed focused `CURRENT (0)`, and
  is forcing/promoting `build/src/tracks.c.o` under `NON_MATCHING=1` to inspect
  first-ring FPR allocation drift before deciding whether a non-repeated source
  mechanism exists.
- Child `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2` committed evidence-only result
  `6207d9c5` on `codex/trackbg-render-flashy-child`; parent imported it to
  `research/tasks/child_threads/trackbg_render_flashy_2026-06-12_child_evidence.md`.
  No source edit was made; child-local restored validation reached `Verify: OK`.

## Blockers Or Unknowns

- No setup blocker recorded.
- Parent routing correction on 2026-06-12: no function is off limits. Cooldown,
  saturation, parked, and negative-evidence notes are only anti-repeat evidence
  for the next child hypothesis. The selector now keeps all remaining guarded
  functions routable (`skipped_exhausted=0`) under the heartbeat parent /
  exactly-one-active-child pattern until 100 percent byte-matching source is
  reached.
- Active child lane: `func_8008FF1C` thread
  `019ebe01-34c2-7310-b8aa-4aa5cff50faa` in
  `/Users/douglas/.codex/worktrees/00e8/dkrdecompiled` on branch
  `codex/func-8008ff1c-mechanism-discovery`. Do not create another child until
  this lane byte-matches and commits source-level C, or records a true
  setup/toolchain/assets/unresolved-behavior blocker.
- Fresh parent-child negative evidence exists for several candidates, but that
  evidence does not close those functions or block future work. Use it to avoid
  repeating source-shape families while keeping every remaining function
  routable.
- For `func_8002B0F4`, do not repeat promoted-object `CURRENT (0)`, promoted-object-slice refreshes, unsafe `volatile`/accessor/artificial-alias/helper reshaping, ordinary local/order/carrier spellings, or `register` on `currentSegment`/`currentBoundingBox`/`currentBatch`. A future packet must remove the stack-resident model base at `0x60(sp)`, replace the texture lookup stack reload with an in-loop global `lui/lw gCurrentLevelModel` pair like target `0x2C020/0x2C024`, and preserve the outer setup global reload around `0x2BDD4/0x2BDD8`.
- For `trackbg_render_flashy`, do not trust focused `CURRENT (0)` or repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, pair-result scratch locals, first-two-store ordering, `var_f16` negative-cos lifetime extension, scheduling/lifetime barriers, doubled-cos spelling/literal variants, volatile/alias forcing, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes. A future packet must predict initial negative-cos in `$f18` without broad stack-slot/downstream drift and must pass full ROM verify.
- For `func_8008FF1C`, require a mechanism that predicts target `lh t2,0(s1)` plus delay-slot `sw v0,0(s0)`; do not repeat direct-table/common-store/pointer-to-selected-track-cell/temp-carrier variants.
- For `init_particle_buffers`, require a new saved-register allocation mechanism that predicts target counts `s1/s3/s7/s4/s8`, point count in `s8/fp`, first allocation arithmetic using line count in `s4` and point count in `fp`, and colour tag `s2` for every semitrans-grey allocation while frame stays `0x68`; do not repeat register hints, count aliases, triangle-buffer pointer, all-call colour-tag, unused-pad removal, initial-only colour-tag, declaration/local-carrier probes, or focused-`CURRENT (0)` acceptance.
- For `func_80017A18`, require a mechanism predicting target frame `0x120` and bitmask in `s6`; do not repeat dead-local, edge-plane-inline, register-hint, loop-control bitmask, or combined dead-vector/`sum2` accumulator families.
- For `func_80059208`, do not repeat final-tail temp/order spelling, direct object-dot, object-X-first lifetime, separate negated checkpoint temp, ObjectTransform late-position lifetime, literal/condition staging, vertical alias/literal staging, or promoted-object focused `CURRENT (0)` acceptance without full ROM verify. Require a distinct mechanism predicting the target final-tail FPR/load order.
- For `func_80049794`, do not trust focused `CURRENT (0)` or reopen without a new mechanism that couples the close save-family with non-repeated wave allocation movement.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `monitor func_8008FF1C child lane until byte-match`
- Packet class: `parent_child_monitor`
- Packet status: `active child lane`
- Reasoning tier: `high` in child; parent remains low-reasoning orchestration.
- Active child lane: `func_8008FF1C` thread
  `019ebe01-34c2-7310-b8aa-4aa5cff50faa`, worktree
  `/Users/douglas/.codex/worktrees/00e8/dkrdecompiled`, branch
  `codex/func-8008ff1c-mechanism-discovery`, pending id
  `local:eba34148-bbbc-47c4-88c1-0c51a9718518`.
- Latest child status: child set the function-local goal, completed required
  startup, linked ignored validation inputs locally, recovered from missing
  `asm/nonmatchings/...` includes by linking the ignored `asm/` tree, and
  reached child-local `gmake -j4 CROSS=tools/binutils/mips64-elf-` with
  `Verify: OK`. Child committed checkpoint evidence `4351e435`; parent
  imported
  `research/tasks/child_threads/func_8008FF1C_2026-06-12_child_checkpoint.md`.
  The checkpoint records that close carrier-style shapes preserve the target
  delay-slot store but branch on `v1`, while direct-table shapes recover `t2`
  but hoist the hub-name store or fill the branch delay slot with other work.
  This is not lane closeout.
- Parent routing status: `python3 tools/query_goal_state.py next --compact
  --refresh` reports 7 routable guarded candidates, `skipped_exhausted=0`, and
  `recommended_next: func_8008FF1C`. Cooldown, parked, and negative-evidence
  notes are anti-repeat guidance only; no function is off limits.
- Next parent action: read this child status before doing anything else. Do not
  create another lane while this child is active, dirty, or unresolved. Parent
  integration accepts only source-level C after `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`, then `./score.sh -s`.
