# func_8008FF1C Child Checkpoint - 2026-06-12

Parent thread: `019ebdc0-0955-7492-8ef4-34215cf7ce31`
Child thread: `019ebe01-34c2-7310-b8aa-4aa5cff50faa`
Child worktree: `/Users/douglas/.codex/worktrees/00e8/dkrdecompiled`
Child branch: `codex/func-8008ff1c-mechanism-discovery`
Child commit: `4351e435`
Target: `func_8008FF1C`

This is durable negative evidence only. It is not a lane closeout: the child
goal remains to keep searching until `func_8008FF1C` byte-matches as
source-level C, or a true setup/toolchain/assets/behavior blocker is hit.

## Startup And Setup

- `git status --short --branch --ignore-submodules=all` reported
  `## codex/func-8008ff1c-mechanism-discovery`.
- Required startup files and the `func_8008FF1C` parked entry were read.
- The child worktree initially lacked ignored validation inputs. Local symlinks
  were added for `.venv`, `assets`, `asm`, the baserom, local tools, asm
  processor files, and `ver/dkr.us.v77.ld`. These setup links and generated
  outputs were kept unstaged.

## Baseline Validation

- After linking `asm/`, restored asm-backed baseline
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK` with CRCs
  `0x53D440E7/0x7519B011`.
- `./score.sh -s` reported decomp progress `97.30%` and docs progress
  `65.47%`.
- `./diff.sh func_8008FF1C --compress-matching 2 --no-pager` on the asm-backed
  baseline reported `CURRENT (0)`, which is diagnostic only for this parked
  function.

## Source Probes

All probes were temporary local promotions of only `func_8008FF1C`; `src/menu.c`
was restored before this checkpoint. Final acceptance was not claimed for any
probe.

1. Promoted the current guarded C body with `#if 1`.
   - Full build failed verify with calculated CRCs `0x55C240E7/0x18E4F9B4`.
   - Focused linked evidence remained the known close miss:
     `lh v1,0(s1)`, `beq v1,at,...`, with target delay-slot
     `sw v0,0(s0)` present.

2. Hybrid direct-table branch while keeping the odd pre-branch temp load:
   `temp = (temp = gTrackSelectIDs[...]); cur->hubName = levelName;
   if (gTrackSelectIDs[trackY][trackX] != -1)`.
   - Object-level compile did not provide landable movement; the shape
     collapses back into the selected-track carrier family unless fully
     relinked and verified.

3. Compare operand-order and `hubName` liveness probes on the close baseline:
   `if (-1 != selectedTrack)` and `hubName = levelName; cur->hubName = hubName`.
   - Both stayed in the close baseline register family: branch operand remained
     `v1` while the delay-slot store remained correct.

4. Pointer/direct condition probe:
   `selectedTrackCell = &gTrackSelectIDs[trackY][trackX]` before the
   `level_name(level_world_id(...))` calls, followed by
   `if (*selectedTrackCell != -1)`.
   - Stayed in the close baseline miss: branch operand remained `v1` with the
     target delay-slot store present.

5. Clean direct-table branch with no selected-track carrier:
   `cur->hubName = levelName; if (gTrackSelectIDs[trackY][trackX] != -1)`.
   - Relinked objdump showed the expected opposite-family miss:
     `sw v0,0(s0)` before the selected-track load, then `lh t2,0(s1)`,
     `beq t2,at,...`, with the branch delay slot filled by the `gQMarkPtr`
     load instead of the target hub-name store.

6. Direct-table store-dependency spelling:
   `cur->hubName = (gTrackSelectIDs[trackY][trackX], levelName);`
   before the direct-table `if`.
   - The unused comma load optimized away; relinked objdump stayed in the same
     direct-table miss with store before `lh t2`.

7. `switch (gTrackSelectIDs[trackY][trackX])` and target-direction
   `if (gTrackSelectIDs[trackY][trackX] == -1)`.
   - Both retained the direct `t2` load family but changed the branch shape and
     still kept `sw v0,0(s0)` before the selected-track load.

8. Declaration-order and assignment-expression compare probes on the close
   baseline:
   - Moving `selectedTrack` before `i`.
   - `if ((selectedTrack = gTrackSelectIDs[trackY][trackX]) !=
     (cur->hubName = levelName, -1))`, with and without the odd `temp` load.
   - These preserved the delay-slot store but still branched on `v1`; the
     versions without the exact old carrier also broadened downstream register
     drift.

## Current Evidence

The search still splits into the same two mechanism halves:

- Close carrier-style source shapes preserve target delay-slot
  `sw v0,0(s0)` but branch on `v1`.
- Direct table source shapes recover `lh t2,0(s1)` / branch on `t2`, but hoist
  `sw v0,0(s0)` before the load or fill the branch delay slot with other work.

The next hypothesis should not replay simple direct-table, pointer-cell,
condition-assignment, declaration-order, or comma/store-order variants. It
needs a new mechanism that makes the compiler load the selected-track cell in
the direct `t2` family while also keeping the hub-name store schedulable in the
branch delay slot.
