# Agent Instructions

This repo is a Diddy Kong Racing N64 byte-matching decompilation. Work should
preserve the upstream build layout and make forward progress by landing
source-level C that keeps the matching ROM byte-identical.

## Startup

1. Read `research/tasks/ACTIVE.md`.
2. Run `python3 tools/query_goal_state.py next --compact --refresh`.
3. Read only the relevant `SESSION_HANDOFF.md` sections if routing is unclear:
   `Next Work Packet`, `Validation`, `Blockers Or Unknowns`, and
   `Ask The User Only If`.
4. Run `python3 tools/check_active_surface.py` before making source edits.

## Matching Rules

- Matching progress means C source that passes the matching build gate. Do not
  satisfy a packet with inline asm, raw instruction words, handwritten assembly
  wrappers, or post-link patching.
- Prefer one bounded function or one very small source family per packet.
- Use the repo's existing style, naming, include layout, and `GLOBAL_ASM` /
  `NON_MATCHING` conventions.
- Do not park close functions just because a probe family failed. Record the
  rejected source shape and next hypothesis, then keep the function routable
  unless there is a concrete setup, asset, or behavior blocker.
- Keep original ROM assets ignored. Do not commit files from `baseroms/`,
  `assets/`, `asm/`, `build/`, or generated linker/map outputs.
- On macOS use `gmake` for build targets.

## Validation

The canonical exact-match gate for this checkout is:

```sh
gmake -j4 CROSS=tools/binutils/mips64-elf-
```

That target verifies the ROM SHA1 in matching mode. The explicit `CROSS=`
avoids Homebrew's `mips-linux-gnu-ld`, which rejects this checkout's generated
IDO objects at link time. Use `./diff.sh <function>` for focused assembly
diagnosis and `./score.sh -s` for progress reporting after a successful build.
A packet is not complete unless the matching build remains `Verify: OK`, or the
blocker is recorded precisely in `SESSION_HANDOFF.md`.

## Closeout

When a packet lands, records exhausted probe evidence, or changes
routing/tooling, update `research/tasks/ACTIVE.md` and `SESSION_HANDOFF.md`.
Prefer:

```sh
python3 tools/session_closeout.py --task <task-id> --summary "<short result>" \
  --validation "gmake -j4 CROSS=tools/binutils/mips64-elf-" \
  --next-task "<next packet>"
```

Add `--commit` only when the repo state is coherent and validation has been
recorded.
