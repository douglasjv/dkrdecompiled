# Session Handoff

- Generated at: 2026-05-25 02:08:00Z
- Branch: `master`
- HEAD: `f47589d5`
- Completed task: `func_80049794-vehicle-particles-guard-operand-order`
- Summary: Rejected promoted func_80049794 final vehicle-particle guard operand-order spelling: changed the NON_EQUIVALENT guard to #if 1 and rewrote only if (racer->vehicleIDPrev < VEHICLE_BOSSES) as if (VEHICLE_BOSSES > racer->vehicleIDPrev). Full verify failed with calculated CRCs 0x5FDDE03F/0xEF7A0514; relinked ./diff.sh func_80049794 --compress-matching 2 --no-pager stayed at promoted baseline CURRENT (2760), retaining missing target f20/f21 prologue saves, early zero in current f16 instead of target f14, and wave scan a0-bound/v1-loop drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_80049794 vehicle-particle guard operand-order, magnetTimer truthy, final spA1/unk201 tail booleans, saved-FPR/wave-scan microvariants, early grounded-zero carriers, and throttle/brake literals unless paired with a distinct saved-FPR/register-pressure fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
