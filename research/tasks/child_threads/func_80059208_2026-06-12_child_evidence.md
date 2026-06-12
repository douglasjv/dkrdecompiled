# func_80059208 Child Evidence - 2026-06-12

Child thread: `019ebdd6-3f3b-7c61-a36f-0a9928ad0eb9`
Source thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Branch: `codex/func-80059208-child`
Child commit: `e09f5f42`
Base commit: `c2ed22a3`
Worktree: `/Users/douglas/.codex/worktrees/1264/dkrdecompiled`

## Target

- Function: `func_80059208`
- Guarded source: `src/racer.c`
- Original asm: `asm/nonmatchings/racer/func_80059208.s`
- Packet class: high child mechanism check for a source-only match candidate.

## Child Setup

This child worktree started without ignored/generated validation inputs. The
child mirrored local setup inputs from `/Users/douglas/projects/dkrdecompiled`
into the child worktree as ordinary ignored local files, not symlinks. Copied
inputs included `baseroms/baserom.us.v77.z64`, `asm/`, `assets/`, `build/`,
`.venv/`, `ver/dkr.us.v77.ld`, `tools/asm-differ`, `tools/asm-processor`,
`tools/binutils`, `tools/dkr_assets_tool`, `tools/ido-recomp`, and
`tools/n64crc`. All generated and ignored setup inputs were kept unstaged.

## Validation

- `git status --short --branch --ignore-submodules=all`: `## codex/func-80059208-child`
- `python3 tools/check_active_surface.py`: `active surface ok`
- `python3 tools/query_goal_state.py next --compact --refresh`: `recommended_next: discovery`
- `python3 tools/query_goal_state.py packet --function func_80059208 --template`: packet has no mechanism hypothesis and requires a new final-tail FPR/load-order mechanism.
- Restored baseline `./diff.sh func_80059208 --compress-matching 2 --no-pager`: `CURRENT (0)`, as expected for the asm-backed matching fallback.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-`: `Verify: OK`, CRCs `0x53D440E7/0x7519B011`
- `./score.sh -s`: decomp progress `97.30%`; documentation progress `65.47%`

## Mechanism Review

The child did not make a source edit. The required source-level mechanism would
need to predict the final tail around `0x5A22C-0x5A31C` moving to object X in
`$f16`, `5.0f` materialized before object Z, object Z in `$f6`, early
`neg.s $f0,$f0` for the checkpoint dot, add-after-negation final combine, and
vertical math through `$f6/$f10`.

The current guarded C tail already maps to the ledger-described saturated
family: object X/Z are carried through the current `$f12/$f0` allocation,
`5.0f` is materialized after the object loads, the dot is folded as a
subtract/late-negation shape, and the vertical tail uses `$f10/$f6`. Rechecked
evidence covered `research/tasks/ACTIVE.md`,
`research/tasks/func_80059208_evidence.md`, the selector packet template, the
current guarded C tail, and target asm tail `0x5A22C-0x5A31C`.

Every source mechanism available from that evidence collapses into an already
rejected family: `splineIndex` carrier-size tweaks, `tempZ`/`distance` carrier
spelling, direct normalization division, checkpoint-dot-first or positive
checkpoint-dot/subtract orderings, vertical `pad3` alias, explicit final-tail
accumulation split, object-X-first lifetime, separate negated checkpoint temp,
direct object-dot spelling, `ObjectTransform` late-position lifetime aliases,
literal/condition staging, vertical alias/literal staging, promoted-object
focused `CURRENT (0)` acceptance without full verify, or generic temp/order
spelling.

No non-repeated C mechanism was identified that would plausibly force the
target final-tail FPR allocation/load order while preserving the full ROM
verify gate. Running another source spelling probe would only repeat the
recorded saturated families.

## Result

No source-level C was landed for `func_80059208` in this child. The child
worktree setup validates locally, restored matching build reaches `Verify: OK`,
and durable negative evidence is this note.
