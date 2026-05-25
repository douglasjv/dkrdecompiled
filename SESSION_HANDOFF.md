# Session Handoff

- Generated at: 2026-05-25 02:23:29Z
- Branch: `master`
- HEAD: `0fdcf145`
- Completed task: `func_80049794-wave-scan-last-index-split`
- Summary: Rejected promoted func_80049794 wave-scan last-index split spelling; changed the NON_EQUIVALENT guard to #if 1, assigned var_v1 = gRacerWaveCount - 1, used for (var_a0 = var_v1; ...), and compared if (var_a0 == var_v1). Promoted baseline verify failed with calculated CRCs 0x5FDDE03F/0xEF7A0514; the split-index probe failed with calculated CRCs 0x5790053C/0x1C8C0179. Relinked ./diff.sh func_80049794 --compress-matching 2 --no-pager worsened from CURRENT (2760) to CURRENT (5755), spilling spA2 to 0xA2(sp) and shifting wave-scan temporaries farther from target. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_80049794 wave-scan split-index/register-shape microvariants unless paired with a distinct saved-FPR/register-pressure fix. Also avoid the already recorded func_80049794 late boost-emitter high-split compare, vehicle-particle guard operand-order, magnetTimer truthy, final spA1/unk201 tail booleans, early grounded-zero carriers, and throttle/brake literals; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
