# Session Handoff

- Generated at: 2026-05-24 09:56:37Z
- Branch: `master`
- HEAD: `23e89b68`
- Completed task: `func_80049794`
- Summary: Rejected func_80049794 final spA1 R-trigger restore boolean spelling; promoted source changed only if (spA1 != FALSE) to if (spA1). Full verify failed with CRCs 0x5FDDE03F/0xEF7A0514, and relinked diff stayed CURRENT (2760) with missing target f20/f21 prologue saves, early zero in f16 instead of f14, and the known wave scan register drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Return to selector routing; prefer an independent func_80049794 family only if it is not another saved-FPR/wave-scan micro-variant, or another active guarded candidate with a distinct unrecorded source-shape family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
