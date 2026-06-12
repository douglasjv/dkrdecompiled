# trackbg_render_flashy Child Evidence - 2026-06-12

Child thread: `019ebddf-90fd-7c91-9fab-b9a5a42b4cc2`
Source thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Branch: `codex/trackbg-render-flashy-child`
Child commit: `6207d9c5`
Base commit: `86f685b2`
Worktree: `/Users/douglas/.codex/worktrees/d949/dkrdecompiled`

## Target

- Function: `trackbg_render_flashy`
- Guarded source: `src/tracks.c` under `#ifdef NON_MATCHING`
- Original asm: `asm/nonmatchings/tracks/trackbg_render_flashy.s`
- Packet class: high child mechanism check for a source-only match candidate.

## Child Setup

This child worktree started without ignored/generated validation inputs. The
child mirrored only local setup inputs from
`/Users/douglas/projects/dkrdecompiled` into the child worktree: the baserom,
extracted `asm/`, `assets/`, generated linker/symbol files, `.venv`, binutils,
IDO recomp tools, `tools/dkr_assets_tool`, `tools/n64crc`,
`tools/asm-processor`, and `tools/asm-differ`. These inputs stayed ignored and
unstaged. No `build/` symlink was used; `build/` was generated locally.

## Validation And Diagnostics

- `git status --short --branch --ignore-submodules=all`: detached `HEAD`
  initially, then branch `codex/trackbg-render-flashy-child`.
- `python3 tools/check_active_surface.py`: `active surface ok`; before setup it
  warned about missing `baseroms/` and absent `build/`.
- `python3 tools/query_goal_state.py next --compact --refresh`:
  `recommended_next: discovery`; all default-routable candidates have cooldown
  evidence and require a distinct compiler-mechanism hypothesis before probing.
- `python3 tools/query_goal_state.py packet --function trackbg_render_flashy --template`:
  packet requires a high-reasoning mechanism hypothesis and predicted asm
  movement.
- Baseline `gmake -j4 CROSS=tools/binutils/mips64-elf-`: reached `Verify: OK`
  after child-local setup.
- Matching-object `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager`:
  reported `CURRENT (0)`, as expected for the restored asm-backed object and not
  accepted as source evidence.
- Forced promoted guarded object:
  `gmake -B build/src/tracks.c.o NON_MATCHING=1 CROSS=tools/binutils/mips64-elf-`.
  Objdump of `build/src/tracks.c.o` reproduced the known drift: frame `0x158`,
  scaled cos in `$f12`, scaled sin in `$f2`, `neg.s $f16,$f12`, immediate
  doubled cos in `$f18`, then first-ring stack stores. This is not target-like.
- Restored matching object:
  `gmake -B build/src/tracks.c.o CROSS=tools/binutils/mips64-elf-`.
- Final validation:
  `gmake -j4 CROSS=tools/binutils/mips64-elf-`: `Verify: OK`.
- `./score.sh -s`: decomp progress `97.30%`; documentation progress `65.47%`.

## Mechanism Review

No source edit was made. The required mechanism is a distinct early
FPR-allocation/source-lifetime shape that predicts target-like scaled cos in
`$f12`, scaled sin in `$f2`, initial negative cos as `neg.s $f18,$f12`, delayed
doubled-cos setup until after the first-ring stack-temp stores, and no broad
frame, stack-slot, or downstream scheduling drift from the target `0x158`
pattern.

The current ledger already rejects the source families that could plausibly
force that movement from ordinary C spelling: plain guarded-C promotion,
commuted `zPositions[3]`, all-first-ring `scaledXSin` reuse, ordinary
negative-scaled-cos temps, inverted primary cos carrier or positive-cos scratch
locals, first-ring pair-result scratch locals, promoted-object focused
`CURRENT (0)`, first-two-store ordering, `var_f16` negative-cos lifetime
extension, scheduling/lifetime barriers, doubled-cos spelling or literal
variants, volatile/alias forcing, and first-ring scratch reuse that predicts
broad stack-slot/downstream drift.

Rechecking the current guarded first-ring body and target asm around `0x28D00`
left no non-repeated mechanism-ready source patch. The only available levers
still collapse into one of the rejected spelling/lifetime families, or they
predict the already-observed failure mode where `$f18` movement comes with broad
stack-slot and downstream scheduling drift instead of a contained match.

## Result

No source-level C was landed for `trackbg_render_flashy` in this child. The
child records durable negative evidence after restoring the matching object and
reaching full `Verify: OK`, rather than repeating a spelling-only or
focused-diff false-positive probe. A future packet should stay cooldown-routed
unless it names a genuinely distinct compiler mechanism that predicts the
required `$f18` negative-cos lifetime and delayed doubled-cos setup without
disturbing the target frame and stack-temp pattern.
