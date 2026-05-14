---
name: n64-ido-nonmatch-triage
description: Use when an N64 IDO decompilation function compiles but does not byte-match and needs focused asm-differ diagnosis before another source-shape probe.
---

# N64 IDO Nonmatch Triage

Use this after a C candidate exists and the focused diff still shows drift.

## Triage Order

1. Confirm the function, source path, asm path, and build mode.
2. Run or inspect `./diff.sh <function>`.
3. Classify the first material drift:
   - prologue, frame size, or saved register set
   - branch polarity or early return shape
   - signedness, zero/sign extension, or compare width
   - temporary lifetime or register allocation
   - load/store offset, pointer depth, or volatile ordering
   - rodata, switch table, or constant materialization
4. Propose at most two source-level probes.
5. If neither probe improves the diff, record the rejected shape and park or
   shrink the packet.

## DKR Acceptance Boundary

`NON_MATCHING=1` can prove behavior experiments compile, but it cannot complete
a matching packet. A packet is accepted only when
`gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
