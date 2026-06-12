# func_80049794 Child Evidence - 2026-06-12

Child thread: `019ebdcb-1042-7690-a495-cd91360dfc59`
Source thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Branch: `codex/func-80049794-child`
Child commit: `1e9cccf5`
Base commit: `41833d38`
Worktree: `/Users/douglas/.codex/worktrees/c3a6/dkrdecompiled`

## Target

- Function: `func_80049794`
- Guarded source: `src/racer.c`
- Original asm: `asm/nonmatchings/racer/func_80049794.s`
- Packet class: high child mechanism check for a source-only match candidate.

## Child Setup

This child worktree was missing ignored/generated validation inputs. The child
mirrored only local setup inputs from `/Users/douglas/projects/dkrdecompiled`
into the child worktree and kept them unstaged. One initial copied `build/`
tree produced mixed-object link failures, so the child ran `gmake clean` and
rebuilt `build/` locally from child inputs.

## Validation

- `git status --short --branch`: `## codex/func-80049794-child`
- `python3 tools/check_active_surface.py`: `active surface ok`
- `python3 tools/query_goal_state.py next --compact --refresh`: `recommended_next: discovery`
- `python3 tools/query_goal_state.py packet --function func_80049794 --template`: packet requires a new mechanism hypothesis and predicted asm movement.
- `python3 tools/query_goal_state.py tooling`: `tooling_next: discovery_packet`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-`: `Verify: OK`
- `./score.sh -s`: decomp progress `97.30%`; documentation progress `65.47%`
- Baseline `./diff.sh func_80049794 --compress-matching 2 --no-pager` against the asm-backed build reports `CURRENT (0)`, as expected for the restored matching fallback.

## Mechanism Review

The child did not make a source edit. The required mechanism is a distinct
source shape that couples the missing target saved-FPR family with non-repeated
wave allocation movement. The current ledger already covers plain promotion,
focused/object-only `CURRENT (0)` acceptance, `updateRateF` / `var_f20`
lifetime carriers, `register var_f20`, carrier-width, declaration-order,
register-hint, branch/condition/literal, early-zero, first-speed, close
save-family variants, wave-bound carriers, pointer-cursor/pointer-walk
variants, threshold carriers, predecrement, while/break, first-compare/do-loop,
post-scan increment, and selected-wave reuse forms.

The target still needs frame `0xF8`, `$f21/$f20` saves at `0x20/0x24(sp)`,
early zero in `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer
cursor after `addu`. Every candidate source mechanism the child could name
from the current source and ledger is already recorded as rejected or collapses
into an already rejected family. Therefore this child records no
mechanism-ready source patch for `func_80049794` rather than repeating a
spelling-only or object-only false-positive probe.

## Result

No source-level C was landed for `func_80049794` in this child. The child
worktree setup validates locally, and the restored matching build reaches
`Verify: OK`. Durable negative evidence is this note.
