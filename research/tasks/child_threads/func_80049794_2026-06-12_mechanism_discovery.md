# func_80049794 Child Mechanism Discovery - 2026-06-12

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Child thread: active lane resumed in worktree `9c4b`
Child worktree: `/Users/douglas/.codex/worktrees/9c4b/dkrdecompiled`
Child branch: `codex/func-80049794-mechanism-discovery`
Starting commit: `d09af5d8`
Target: `func_80049794`

## Startup Evidence

- `git status --short --branch --ignore-submodules=all` reported
  `## codex/func-80049794-mechanism-discovery`.
- `AGENTS.md` and `research/tasks/ACTIVE.md` were read before evidence work.
- `python3 tools/query_goal_state.py next --compact --refresh` reported
  `recommended_next: discovery`.
- `python3 tools/query_goal_state.py tooling` reported
  `tooling_next: discovery_packet` and specifically listed
  `func_80049794` as blocked until a complete mechanism packet is written.
- `python3 tools/query_goal_state.py packet --function func_80049794 --template`
  still emitted an incomplete packet with blank `Mechanism hypothesis`,
  `Predicted asm movement`, and `Stop condition` fields.
- `research/tasks/func_80049794_evidence.md` was read.
- `python3 tools/check_active_surface.py` reported `active surface ok`.

## Local Validation Setup

This child worktree was missing ignored validation inputs. To run the baseline
gate without committing ROM, asset, build, or tool outputs, the child added
local symlinks to the parent checkout for:

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

The visible local setup links `.venv` and `assets` remained unstaged. Generated
`build/` output and generated asset files were also kept unstaged/ignored.

## Validation

- `python3 tools/check_active_surface.py`: `active surface ok`
  after a warning that `build/` was initially absent.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-`: completed successfully and
  reached `Verify: OK` with CRCs `0x53D440E7/0x7519B011`.
- `./score.sh -s`: decomp progress `97.30%`; documentation progress `65.47%`.

## Evidence Checked In This Lane

- `research/tasks/ACTIVE.md`
- `research/tasks/MECHANISM_PACKETS.md`
- `research/tasks/func_80049794_evidence.md`
- `research/tasks/child_threads/func_80049794_2026-06-12_child_evidence.md`
  from older branch `codex/func-80049794-child` at commit `1e9cccf5`
- `python3 tools/query_goal_state.py next --compact --refresh`
- `python3 tools/query_goal_state.py tooling`
- `python3 tools/query_goal_state.py packet --function func_80049794 --template`
- Current guarded source body in `src/racer.c`
- Target asm at `asm/nonmatchings/racer/func_80049794.s`

## Mechanism Search

The older resolved child note at `1e9cccf5` already recorded that no source edit
was made because every named source mechanism collapsed into rejected evidence:
plain promotion, object-only/focused `CURRENT (0)` acceptance, `updateRateF` /
`var_f20` carriers, `register var_f20`, carrier-width changes,
branch/condition/literal spellings, wave bound/index locals, pointer-cursor
wave variants, selected-wave carriers, declaration-order/register hints,
early-zero carriers, first-speed carriers, trick-input completion spellings,
boost-duration literal spellings, and close save-family combinations that do
not also move wave allocation.

This active mechanism-discovery lane rechecked the live selector/tooling
surface, the packet template, the current source, the target asm, and the older
child evidence. The required mechanism is still the same coupled movement:
recover target frame `0xF8`, `$f21/$f20` saves at `0x20/0x24(sp)`, early zero in
`$f14`, `v1` as the high bound, `a0` as the loop index, and `v0` as the wave
pointer cursor after `addu`, without broad frame or scheduling regressions.

No new ordinary-C mechanism was identified that predicts both the missing
saved-FPR family and the non-repeated wave allocation change. The refreshed
packet template remains blank for the mechanism and predicted movement fields,
and `research/tasks/MECHANISM_PACKETS.md` still records no ready packets.
Starting a source probe from this lane would therefore repeat an already
documented spelling/object-slice family rather than test a new mechanism.

## Conclusion

No complete mechanism packet is justified for `func_80049794` from this active
lane. Parent-routed source probing is not justified until discovery names a
distinct compiler mechanism that predicts the coupled saved-FPR and wave
allocation movement above.

No source files were edited.
