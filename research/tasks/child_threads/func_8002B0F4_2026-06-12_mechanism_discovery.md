# func_8002B0F4 Child Mechanism Discovery - 2026-06-12

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Child thread: `019ebdec-ac64-7131-9914-2faa3abe3568`
Child worktree: `/Users/douglas/.codex/worktrees/97e6/dkrdecompiled`
Child branch: `codex/func-8002b0f4-mechanism-discovery`
Target: `func_8002B0F4`

## Startup Evidence

- `git status --short --branch --ignore-submodules=all` initially reported
  detached `HEAD`; the child created branch
  `codex/func-8002b0f4-mechanism-discovery` before committing evidence.
- `AGENTS.md` and `research/tasks/ACTIVE.md` were read.
- `python3 tools/query_goal_state.py next --compact --refresh` reported
  `recommended_next: discovery`; the child worktree initially had missing
  ignored validation inputs.
- `python3 tools/query_goal_state.py tooling` reported
  `tooling_next: discovery_packet` and required a complete mechanism packet
  before source edits.
- `python3 tools/query_goal_state.py packet --function func_8002B0F4 --template`
  emitted a skeleton with no mechanism hypothesis or predicted asm movement.
- `research/tasks/func_8002B0F4_evidence.md` was read.
- `python3 tools/check_active_surface.py` reported `active surface ok`.

## Local Validation Setup

This child worktree was missing ignored/generated validation inputs. To run the
canonical gate without committing ROM, asset, build, or tool outputs, the child
added local symlinks to the parent checkout for:

- `.venv`
- `asm`
- `assets`
- `baseroms/baserom.us.v77.z64`
- `tools/binutils`
- `tools/ido-recomp`
- `tools/n64crc`
- `tools/dkr_assets_tool`
- `tools/asm-processor/build.py`
- `tools/asm-processor/asm_processor.py`
- `tools/asm-processor/prelude.inc`
- `ver/dkr.us.v77.ld`

These are local setup artifacts only and must remain unstaged.

## Validation

- First `gmake -j4 CROSS=tools/binutils/mips64-elf-` failed before validation
  because `.venv/bin/python3` was absent in the child worktree.
- After linking `.venv`, the next build failed because
  `tools/asm-processor/build.py` was absent in the child worktree.
- After linking the asm-processor files, `gmake -j4
  CROSS=tools/binutils/mips64-elf-` reached `Verify: OK` with CRCs
  `0x53D440E7/0x7519B011`.

## Evidence Checked

- `research/tasks/ACTIVE.md`
- `python3 tools/query_goal_state.py next --compact --refresh`
- `python3 tools/query_goal_state.py tooling`
- `python3 tools/query_goal_state.py packet --function func_8002B0F4 --template`
- `research/tasks/func_8002B0F4_evidence.md`
- Current guarded source body in `src/tracks.c`
- Target asm at
  `/Users/douglas/projects/dkrdecompiled/asm/nonmatchings/tracks/func_8002B0F4.s`
- Nearby single-segment helper `collision_get_y` in `src/tracks.c`
- Prior child evidence
  `research/tasks/child_threads/func_8002B0F4_2026-06-12_child_evidence.md`

## Mechanism Search

The required mechanism would need to make IDO emit single-use
`gCurrentLevelModel` reloads at both target sites:

- outer segment setup reload at target `0x2BDD4/0x2BDD8`
- batch-loop texture lookup reload at target `0x2C020/0x2C024`

The current guarded source already spells those accesses directly as
`gCurrentLevelModel->segments[...]`,
`gCurrentLevelModel->segmentsBoundingBoxes[...]`, and
`gCurrentLevelModel->textures[...]`. Prior diagnostics show IDO still hoists
the model base, spills it to `0x60(sp)`, and reloads the stack-resident model
base for texture lookup. The nearby `collision_get_y` helper uses the same
direct global access style and does not provide a distinct source idiom that
would force the two target global reloads without repeating rejected families.

No non-repeated ordinary-C source mechanism was identified. Remaining apparent
forcing mechanisms collapse into already rejected or unsafe families:

- local segment-index lifetime variants
- local model pointer
- bottom-only segment-pointer lifetime split
- segment/bounding-box assignment or order changes
- texture/flag carriers
- pointer-arithmetic setup
- condition, literal, or local-width spelling
- bottom store-order probes
- `register` pointer-local allocation hints
- unsafe `volatile`
- accessor calls
- artificial aliasing side effects
- helper reshaping
- promoted-object slice audits or focused `CURRENT (0)` acceptance without full
  ROM `Verify: OK`

## Conclusion

No complete mechanism packet is justified for `func_8002B0F4` from this child
lane. The target should remain cooldown-routed until a genuinely distinct
model-load lifetime/register-allocation mechanism is named that predicts
removal of the promoted `0x60(sp)` stack-resident model base, preserves the
outer setup reload, and replaces the texture lookup stack reload with an
in-loop `lui/lw gCurrentLevelModel` pair.

No source files were edited.
