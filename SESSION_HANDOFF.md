# Session Handoff

- Generated at: 2026-05-23 11:06:01Z
- Branch: `master`
- HEAD: `c8380620`
- Completed task: `func_80049794`
- Summary: Rejected late boost pointer += racerIndex probe; source restored after CURRENT (2760) miss

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not accept object-only CURRENT (0) for guarded functions that still fall back to assembly. Avoid recorded func_80049794 early spA1/early-zero/wave-register/throttle-rate/brake-rate/brake upper-clamp/brake lower-clamp/brake rumble-threshold/brake rumble guard-order/spinout brake literal/explicit wave-drift float-threshold/late boost-emitter branch-order/late boost-emitter nonzero compare/late boost pointer += racerIndex/attach-point postincrement/attach-point store-order/final unk201 condition-inversion/attach-point count > 2/attach-point -= 2.0/attach-point += 1.0f probes, and avoid recorded func_80059208 final-tail/normalization/checkpoint-distance literal probes; choose a fresh bounded source-shape probe or another active alternate with unrecorded evidence.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
