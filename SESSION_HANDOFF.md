# Session Handoff

- Generated at: 2026-07-09
- Branch: `master`
- HEAD: `3ee245dd`
- Completed task: `match-func-80059208`
- Summary: Imported the source-level exact match from upstream PR #742. Four
  original functions remain.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.
- `./score.sh -a 1` reports decomp progress `97.91%`, 1848 decompiled
  functions, and 4 `GLOBAL_ASM` functions remaining.
- `python3 tools/query_goal_state.py next --compact --refresh` reports 4
  guarded candidates and `recommended_next: func_8008FF1C`.
- A bounded five-minute permuter pass against the promoted `func_8008FF1C`
  candidate found only semantically invalid lower-score mutations; none were
  applied. The source was restored before the final matching build.
- Two new `trackbg_render_flashy` probes (commuting `xPositions[2]` and swapping
  or registering the scaled-cos declaration) produced no object movement and
  were reverted before the final matching build.

## Blockers Or Unknowns

- No setup, toolchain, asset, or behavior blocker is active.
- `func_8008FF1C` remains a one-register mismatch (`v1` versus target `t2`)
  with the rest of the focused function identical.
- `trackbg_render_flashy` remains an early FPR-allocation mismatch beginning at
  `neg.s f18,f12`; the promoted source still chooses `f16`.

## Ask The User Only If

- The retail baserom or extracted assets become unavailable.
- A required setup dependency cannot be restored locally.
- A behavior question cannot be resolved from code, symbols, or target asm.

## Next Work Packet

- Work directly in the primary checkout, one remaining function at a time.
- Do not recreate the previous parent/child orchestration; it was retired at
  the user's request on 2026-07-09.
- Accept only ordinary source-level C followed by the full matching build
  reaching `Verify: OK` and a refreshed score.
