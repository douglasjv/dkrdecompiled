# Session Handoff

- Generated at: 2026-05-23 02:27:22Z
- Branch: `master`
- HEAD: `f4c408ee`
- Completed task: `func_80049794`
- Summary: Promoted current-baseline existing-var_t0 wave-bound carrier missed; full verify failed with CRCs 0x9AF972E0/0xD531DD3C and relinked focused diff worsened to CURRENT (4970), shifting the wave scan into t0/v0/v1 churn without recovering target f20/f21 saves or early f14 zero. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating bound-carrier register aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
