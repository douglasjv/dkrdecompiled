# Session Handoff

- Generated at: 2026-05-23 01:46:49Z
- Branch: `master`
- HEAD: `967ed48f`
- Completed task: `func_8002B0F4`
- Summary: Promoted func_8002B0F4 and tested collision-output target-store-order spelling: type, rot.x, rot.y, rot.z, then waveHeight. Full verify failed with calculated CRCs 0x7856718A/0x66208CAA; relinked ./diff.sh func_8002B0F4 stayed CURRENT (2860) with the unwanted early gCurrentLevelModel spill at 0x60(sp). Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but avoid repeating saturated early-zero/wave families. If pivoting, func_8002B0F4 remains active with the collision-output store-order spelling now rejected.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
