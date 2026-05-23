# Session Handoff

- Generated at: 2026-05-23 10:28:06Z
- Branch: `master`
- HEAD: `b55a6dd3`
- Completed task: `func_80049794`
- Summary: Rejected brake rumble guard operand-order promotion; source restored after CURRENT (3525) miss

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not accept object-only CURRENT (0) for guarded functions that still fall back to assembly. Avoid the recorded func_80049794 early spA1/early-zero/wave-register/throttle-rate/brake-rate/brake upper-clamp/brake rumble-threshold/brake rumble guard-order probes, func_8002B0F4 segment/grid/default-water/collision-plane guard/type probes, and func_80059208 final clamp carriers; choose a fresh bounded source-shape probe or another active alternate with unrecorded evidence.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
