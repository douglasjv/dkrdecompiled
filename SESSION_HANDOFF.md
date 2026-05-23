# Session Handoff

- Generated at: 2026-05-23 02:03:03Z
- Branch: `master`
- HEAD: `3853cb3d`
- Completed task: `func_80049794`
- Summary: Promoted func_80049794 and tested the retained-pad var_f2 z/y component-staging branch with register f32 var_f2. Full verify failed with calculated CRCs 0x5FEF1D9D/0x4258C5C1; relinked ./diff.sh func_80049794 reported CURRENT (3620), still lacking target f20/f21 saves with early zero in f16 and wave a0/v1 drift. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat the retained-pad register var_f2 component-staging branch; if staying on func_80049794, prefer a fresh close save-family or wave-register hypothesis from ACTIVE.md that targets the missing f20/f21 saves or wave a0/v1 order without repeating rejected carriers.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
