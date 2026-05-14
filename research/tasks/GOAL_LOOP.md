# Goal Continuation Loop

This is the compact contract for `/goal` sessions in this N64 decompilation.
It is adapted from the Skies control-plane pattern, but uses DKR's native
Splat/IDO/asm-differ build gates.

## Objective

Keep landing source-level C for original Diddy Kong Racing functions while the
matching ROM remains byte-identical. Exhausted probe evidence is evidence about
that packet only; it is not evidence that the project is out of work.

## Startup Order

1. Read `AGENTS.md` and `research/tasks/ACTIVE.md`.
2. Run `python3 tools/query_goal_state.py next --compact --refresh`.
3. If no concrete target is selected, read only these `SESSION_HANDOFF.md`
   sections: `Next Work Packet`, `Validation`, `Blockers Or Unknowns`, and
   `Ask The User Only If`.
4. Run `python3 tools/check_active_surface.py`.
5. If the selector cannot inspect build state yet, use its source scan and the
   README score as the temporary routing surface.

## Packet Rules

- Work one bounded function or one tightly coupled source family at a time.
- Replace `GLOBAL_ASM` or guarded nonmatching source with ordinary C only.
- Do not use inline asm, raw instruction-word tricks, handwritten asm wrappers,
  or post-link binary patching.
- Keep existing include, typedef, and style conventions. Add headers only when
  the source owner genuinely needs them.
- If exact matching fails, use `./diff.sh <function>` to classify the drift
  before opening another source-shape family.
- Record rejected source shapes, current best diff, and next probe in
  `SESSION_HANDOFF.md`.
- Do not add close functions to the exhausted-note skip list just because a
  probe family failed. Keep them active unless there is a concrete setup, asset,
  or behavior blocker.

## Validation

Acceptance gate:

```sh
gmake -j4 CROSS=tools/binutils/mips64-elf-
```

The packet is complete only when matching mode still verifies the ROM SHA1.
Useful diagnostic gates:

```sh
./diff.sh <function_name>
./score.sh -s
./score.sh -t 10
```

If validation cannot run, close out with the exact missing dependency, asset, or
tool command instead of claiming progress.

In this checkout, plain `gmake -j4` selects Homebrew `mips-linux-gnu-ld` and
fails at link time on `build/src/objects.c.o`. Use the repo-local binutils
prefix built by `tools/get-binutils.sh`.

## Reasoning Policy

Default packet reasoning is medium. Escalate the next continuation only when
the handoff records an exact-match ambiguity, the focused diff evidence path,
the best source-shape metric, and a narrow question. Return to medium after the
question lands or narrows.

## Stop Conditions

Ask the user only for missing retail assets/setup, missing toolchain dependency,
or unresolved behavior ambiguity. Otherwise continue by choosing another ready
target, a smaller coherent adjacent function, or a validation/routing repair.

## Closeout

Keep `ACTIVE.md` compact. Put detailed evidence in `SESSION_HANDOFF.md`, source
comments only when they clarify real code, and future packet docs only when a
pattern repeats. Use `tools/session_closeout.py` to refresh handoff state and
optionally commit coherent progress.
