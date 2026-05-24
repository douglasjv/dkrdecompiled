# Session Handoff

- Generated at: 2026-05-24 09:47:19Z
- Branch: `master`
- HEAD: `82c2db92`
- Completed task: `func_80059208`
- Summary: Rejected func_80059208 angle subtract grouping spelling; promoted source grouped steerVisualRotation mask plus 0x8000, but full verify failed with CRCs 0x53D141DF/0xB9D4B481 and relinked diff stayed CURRENT (870) in final object-dot/checkpoint-dot tail.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Return to selector routing; prefer an independent func_80049794 family that targets saved-FPR/frame pressure or wave allocation, or another active guarded candidate if selector packet remains saturated.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
