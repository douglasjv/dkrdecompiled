---
name: n64-ido-permuter
description: Use when a DKR or N64 IDO decompilation function already compiles with matching control flow and needs decomp-permuter help for near-match register allocation, scheduling, or small source-shape drift. Use only as child-worktree diagnostic tooling; final acceptance still requires the repo matching build gate.
---

# N64 IDO Permuter

Use this skill for near-matching source-level C, not for early decompilation or
behavior discovery. The candidate should compile, preserve control flow, and
already be close enough that random source permutations can plausibly improve
register allocation or scheduling.

## Guardrails

- Run this only in an isolated child worktree or throwaway branch.
- Do not use permuter output as acceptance evidence. Treat it as a source-shape
  hint to reapply manually and review semantically.
- Do not accept deleted logic, invented side effects, inline asm, raw op words,
  asm wrappers, or post-link patches.
- Use a wall-clock limit. The wrapper supports `--seconds`; do not leave the
  permuter running indefinitely.
- Keep output under `nonmatchings/<function>/` or another child-local evidence
  path. Do not commit large generated output directories unless they are the
  agreed evidence artifact.

## DKR Flow

1. Confirm the candidate builds in the child worktree and the focused diff has
   no large control-flow or behavior mismatch.
2. Save the best standalone attempt, for example:

   ```sh
   mkdir -p nonmatchings/<function>
   cp <candidate-source>.c nonmatchings/<function>/base_0.c
   ```

3. Run the wrapper with the candidate file and function name:

   ```sh
   ./tools/permuter --source-file nonmatchings/<function>/base_0.c --seconds 300 <function>
   ```

4. Inspect generated `source.c` and `diff.txt` outputs. Reapply only changes
   that make semantic sense in the real source file.
5. Validate normally:

   ```sh
   ./diff.sh <function>
   gmake -j4 CROSS=tools/binutils/mips64-elf-
   ```

The only exact-match acceptance gate is `Verify: OK` from the full matching
build. Follow with `./score.sh -s` after a successful build.

## Setup

The wrapper expects decomp-permuter at `tools/decomp-permuter`. If it is
missing, install it as a local tool dependency before using this skill:

```sh
git submodule add https://github.com/simonlindholm/decomp-permuter.git tools/decomp-permuter
```

Do not fetch decomp.me scratches or network inputs during a parent heartbeat;
use repo-local candidate source and target asm.
