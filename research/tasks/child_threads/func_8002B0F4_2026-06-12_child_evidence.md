# func_8002B0F4 Child Evidence - 2026-06-12

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Child worktree: `/Users/douglas/.codex/worktrees/6f37/dkrdecompiled`
Target: `func_8002B0F4`

## Local Validation Setup

This child worktree was missing ignored/generated validation inputs. To run the
canonical gate without committing ROM or generated artifacts, these local
symlinks were added and left unstaged:

- `.venv -> /Users/douglas/projects/dkrdecompiled/.venv`
- `assets -> /Users/douglas/projects/dkrdecompiled/assets`
- `asm -> /Users/douglas/projects/dkrdecompiled/asm`
- `baseroms/baserom.us.v77.z64 -> /Users/douglas/projects/dkrdecompiled/baseroms/baserom.us.v77.z64`
- `include/asset_enums.h -> /Users/douglas/projects/dkrdecompiled/include/asset_enums.h`
- `tools/binutils -> /Users/douglas/projects/dkrdecompiled/tools/binutils`
- `tools/ido-recomp -> /Users/douglas/projects/dkrdecompiled/tools/ido-recomp`
- `tools/n64crc -> /Users/douglas/projects/dkrdecompiled/tools/n64crc`
- `tools/dkr_assets_tool -> /Users/douglas/projects/dkrdecompiled/tools/dkr_assets_tool`
- `tools/Flips -> /Users/douglas/projects/dkrdecompiled/tools/Flips`
- `tools/asm-differ -> /Users/douglas/projects/dkrdecompiled/tools/asm-differ`
- `tools/asm-processor -> /Users/douglas/projects/dkrdecompiled/tools/asm-processor`
- `tools/m2c -> /Users/douglas/projects/dkrdecompiled/tools/m2c`
- `ver/dkr.us.v77.ld -> /Users/douglas/projects/dkrdecompiled/ver/dkr.us.v77.ld`

Use `git status --short --branch --ignore-submodules=all` in this child
worktree; plain `git status` is confused by the symlinked populated submodule
paths.

## Baseline Validation

- `python3 tools/check_active_surface.py` -> `active surface ok`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`, CRCs
  `0x53D440E7/0x7519B011`

After diagnostics, `build/src/tracks.c.o` was restored with:

```sh
gmake -B CROSS=tools/binutils/mips64-elf- build/src/tracks.c.o
```

Restored validation again reached `Verify: OK` with CRCs
`0x53D440E7/0x7519B011`.

## Diagnostic Baseline

Compiled the current guarded C body under matching-mode codegen:

```sh
gmake -B MATCHDEFS='ANTI_TAMPER=1 NON_EQUIVALENT=1' CROSS=tools/binutils/mips64-elf- build/src/tracks.c.o
./diff.sh func_8002B0F4 --compress-matching 2 --no-pager
```

Focused diff reported `CURRENT (0)`, but objdump still showed the known false
positive model-base family:

- `gCurrentLevelModel` load before the segment loop at object offsets
  `0x67D8/0x67DC`
- model base spill to `0x60(sp)` at `0x67F0`
- outer setup reload from `0x60(sp)` at `0x6800`
- texture lookup reload from `0x60(sp)` at `0x6A48`

This does not satisfy the packet because the target requires source that passes
the full ROM verify gate, and this focused `CURRENT (0)` shape is the already
recorded stale object-slice false positive.

## Rejected Probe

Hypothesis: use a narrow `register` storage-class probe on only the long-lived
pointer locals inside `func_8002B0F4`:

- `currentSegment`
- `currentBoundingBox`
- `currentBatch`

Prediction: changing pointer register allocation might stop IDO from preserving
the `gCurrentLevelModel` base at `0x60(sp)` and recover target-like single-use
global reloads at the outer setup and texture lookup sites.

Result: no movement. Matching-mode diagnostic compile plus focused diff still
reported `CURRENT (0)`, and objdump still showed:

- `gCurrentLevelModel` load at `0x67D8/0x67DC`
- spill to `0x60(sp)` at `0x67F0`
- outer setup reload from `0x60(sp)` at `0x6800`
- texture lookup reload from `0x60(sp)` at `0x6A48`

The source probe was reverted before restored validation.

## Current Conclusion

No source-level mechanism-ready patch was identified in this child lane. The
additional register-allocation probe collapses to the same promoted model-base
spill family as the current guarded body. Future work still needs a distinct
mechanism that predicts removal of the `0x60(sp)` model-base spill and an
in-loop `gCurrentLevelModel` reload for the texture lookup, without using
unsafe `volatile`, accessor calls, artificial aliasing side effects, helper
reshaping, local model pointers, texture carriers, or focused-`CURRENT (0)`
acceptance.
