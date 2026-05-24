# Session Handoff

- Generated at: 2026-05-24 11:20:45Z
- Branch: `master`
- HEAD: `c6356070`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted triangle-hit predicate operand-order spelling; full verify failed with CRCs 0xC349F192/0x2D70F23E and relinked diff worsened to CURRENT (3635), retaining the known early gCurrentLevelModel spill, then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf-: Verify: OK after restore; ./score.sh -s: decomp progress 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with a non-repeated routable packet; avoid func_8002B0F4 triangle-hit predicate operand-order variants unless paired with an independent gCurrentLevelModel spill fix.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
