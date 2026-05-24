# Session Handoff

- Generated at: 2026-05-24 03:37:19Z
- Branch: `master`
- HEAD: `3b993826`
- Completed task: `promotion-probes`
- Summary: Rejected direct C promotions for func_80049794 and func_8002B0F4: func_80049794 guard removal failed CRCs 0x5FDDE03F/0xEF7A0514 with focused CURRENT (2760), missing target f20/f21 saves, f16 zeroing, and reversed wave bound/index allocation; func_8002B0F4 guard removal failed CRCs 0x7856718A/0x66208CAA with focused CURRENT (2860), inserting early gCurrentLevelModel spill at 0x60(sp). Sources restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended but do not repeat direct guard removal/object-only CURRENT(0) promotion unless paired with a distinct save-pressure/wave allocation fix; consider the next bounded routable non-repeated hypothesis from ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
