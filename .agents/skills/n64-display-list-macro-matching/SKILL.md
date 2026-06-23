---
name: n64-display-list-macro-matching
description: Use when matching DKR or N64 IDO C that builds display lists or writes Gfx words directly, especially when replacing raw command-word writes with PR/gbi.h or PR/gs2dex.h macros may improve source clarity and byte matching.
---

# N64 Display List Macro Matching

Use this skill for source-level C only. Display-list macro matching can explain
why a function wrote a pair of 32-bit words, but it is not a license to keep raw
instruction words, inline asm, handwritten wrappers, or post-link patches.

## DKR Flow

1. Confirm the function manipulates `Gfx`, `gCurrDisplayList`, a `Gfx **dList`,
   or 8-byte display-list command words.
2. Identify the command family from local headers first:

   ```sh
   rg -n "gSP|gDP|G_[A-Z0-9_]+|gsSP|gsDP" include/PR/gbi.h include/PR/gs2dex.h
   ```

3. Prefer the repo's existing macro style. DKR commonly uses pointer-increment
   forms such as `gDPFullSync(gCurrDisplayList++)` and pointer-to-pointer forms
   through `Gfx **dList`.
4. Replace direct `words.w0` / `words.w1` command construction only when the
   macro is semantically equivalent and preserves the expected pointer
   increment/order. Aggregate texture-loading macros can alter scheduling and
   should be checked with a focused diff before any broader cleanup.
5. Validate normally:

   ```sh
   ./diff.sh <function>
   gmake -j4 CROSS=tools/binutils/mips64-elf-
   ```

The exact-match gate remains the full matching build reaching `Verify: OK`.

## Guardrails

- Do not introduce raw display-list command constants when an existing local
  macro expresses the same command.
- Do not rename struct fields or widen local types just to make a macro compile
  unless the surrounding source and headers support that type.
- Do not assume Snowboard Kids uses the same microcode version or macro set.
  Check DKR's local `include/PR/gbi.h` and `include/PR/gs2dex.h`.
- If the function is not already close, use macro conversion as a behavior
  clarity step, not as a random scheduling probe.
