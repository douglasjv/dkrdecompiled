# Session Handoff

- Generated at: 2026-05-24 09:28:58Z
- Branch: `master`
- HEAD: `65bfcae3`
- Completed task: `func_80049794`
- Summary: Rejected airborne throttle-min guard condition-order spelling; promoted func_80049794 and rewrote only the later guard from racer->groundedWheels == 0 && racerThrottle < 0.4 && racer->vehicleID != VEHICLE_CARPET to racerThrottle < 0.4 && racer->groundedWheels == 0 && racer->vehicleID != VEHICLE_CARPET. Pre-build diff misleadingly reported CURRENT (0), full verify failed with calculated CRCs 0x5FDDE03F/0x546B28B8, and relinked diff stayed at CURRENT (2760) with the known missing f20/f21 saves, early f16 versus target f14, and wave-scan drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector packet func_80049794 only with an independent, unrecorded source-shape family or pivot to another routable packet if no useful func_80049794 family remains; do not repeat airborne throttle-min guard order.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
