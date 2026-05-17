# Session Handoff

- Generated at: 2026-05-17 04:21:43Z
- Branch: `master`
- HEAD: `c5ae3378`
- Completed task: `DKR-MATCH-FUNC-80059208-DELAYED-DIFFZ-CHECKPOINT-DOT-PROBE`
- Summary: No new source match landed. Used active alternate func_80059208 and tested a delayed-diffZ positive-checkpoint-dot spelling: after diffY = diffX and diffX = diffZ, compute pad2 = (tempZ * -diffY) + (diffX * tempX), then assign diffZ = -diffY and use diffX = -((pad - pad2) / divisor). It compiled but worsened the relinked focused score and perturbed earlier float-register allocation, so guarded source was restored. func_80059208 remains active rather than parked.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; intentionally selected active alternate func_80059208; python3 tools/check_active_surface.py -> active surface ok; delayed-diffZ positive-checkpoint-dot probe failed full verify with calculated CRCs 0x538F82DF/0x50E88FA7; relinked focused ./diff.sh func_80059208 -s --format plain --no-pager --max-size 520 -> CURRENT (2365), worse than the promoted baseline CURRENT (870), with earlier float-register drift around 0x59fbc and final arithmetic drift; source restored; final gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Keep close candidates active rather than parked. If func_80059208 is used as a close alternate, avoid the delayed-diffZ positive-checkpoint-dot spelling from this packet plus the previously recorded final-offset carrier, term-negation, axis-swap, object-dot, clamp, and final-vertical source-shape misses. If func_8002B0F4 is used as a close alternate, use the pad3-removal evidence only for a new hoist/lifetime idea and do not repeat the recorded pad3 move/cache/volatile/copy-loop/setup-order shapes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
