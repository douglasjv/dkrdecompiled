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
`./tools/build-and-verify.sh` is a convenience wrapper around the exact command
above; it does not replace the gate or relax validation.

## Matching Tooling

- `./tools/permuter --source-file <candidate.c> --seconds 300 <function>` wraps
  decomp-permuter for near-matching candidates only. Use it in a child
  worktree, inspect output as advisory source-shape evidence, and accept
  nothing until the full matching build reaches `Verify: OK`.
- `python3 tools/find_similar_functions.py <function>` ranks other function asm
  with similar normalized opcode/operand shape. Use it to form a distinct
  mechanism hypothesis when routing is saturated, not as proof of behavior.
- `python3 tools/find_residual_mechanisms.py <function> --top 20` searches the
  verified built ELF for short register-role patterns recorded in
  `research/tasks/residual_signatures.json`. It preserves destructive versus
  nondestructive register relationships and FPR identities, maps compiled hits
  back to C definitions, and suppresses already-audited references by default.
  Treat hits as source-backed mechanism precedents only; source retention still
  requires the full matching gate.
- `python3 tools/m2c_one_shot.py <function>` writes mips_to_c snapshots under
  `research/tasks/m2c_one_shot/` without editing live source. Treat output as a
  starting point only.
- `python3 tools/data_diff.py --rom-offset <offset> --size <size>` compares a
  ROM byte range between the baserom and built ROM when a data mismatch needs a
  small, reproducible diagnostic.
- `python3 tools/score_asm_functions.py asm/nonmatchings --by-similarity`
  ranks unresolved asm by rough complexity and similarity to available asm
  references. Use this for discovery/tooling packets after live candidates are
  saturated; it is advisory only.
- `.agents/skills/n64-display-list-macro-matching/` adapts Snowboard-style
  display-list macro matching to DKR's local `include/PR/gbi.h` and
  `include/PR/gs2dex.h`. Use it for Gfx command construction candidates, never
  as raw command-word acceptance.

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
