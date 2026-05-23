# Session Handoff

- Generated at: 2026-05-23 02:08:17Z
- Branch: `master`
- HEAD: `46ecdf8d`
- Completed task: `func_80049794`
- Summary: Promoted func_80049794 and tested the close save-family x/z/y/chained-zero/steer-noop branch with a register s32 var_t9 allocation hint. Full verify failed with calculated CRCs 0xB8DD79CD/0xE47454ED; relinked ./diff.sh func_80049794 reported CURRENT (4365), preserving the target 0xf8 frame, f20/f21 saves, and f14 early zero but leaving the wave a0/v1 bound/index allocation reversed. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat the close-branch register var_t9 allocation hint; if staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating close-branch register hints that only preserve the 0xf8 frame and f20/f21 save family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
