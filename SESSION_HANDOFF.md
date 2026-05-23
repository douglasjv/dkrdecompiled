# Session Handoff

- Generated at: 2026-05-23 11:48:02Z
- Branch: `master`
- HEAD: `c07519b8`
- Completed task: `func_80049794`
- Summary: Rejected movement-block approachTarget pointer-test probe; source restored after CURRENT (2760) miss

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, with active alternates only for fresh bounded probes. Do not accept object-only CURRENT (0) for guarded functions that still fall back to assembly. Avoid recorded func_80049794 early spA1/early-zero/wave-register/throttle-rate/brake-rate/brake upper-clamp compare/brake upper-clamp double store-width/brake lower-clamp/brake rumble-threshold/brake rumble guard-order/spinout brake literal/pitch-flip 0x180 mask simplification/trick-input horizontal else-if/pitch-flip boost-duration decimal/pitch-flip boost-duration hex/grounded-wheel surface-scan condition-order/brake-particle viewport condition-order/zip-pad boost condition-order/Taj-pad condition-order/brake-drag condition-order/grounded-wheel spD8 multiplier literal/movement-block approachTarget pointer-test/explicit wave-drift float-threshold/late boost-emitter branch-order/late boost-emitter nonzero compare/late boost pointer += racerIndex/attach-point postincrement/attach-point store-order/final unk201 condition-inversion/attach-point count > 2/attach-point -= 2.0/attach-point += 1.0f probes; avoid recorded func_80059208 wrong-way angle branch-order/wrong-way velocity -1.0f/final-tail/normalization/checkpoint-distance/courseCheckpoint/splineIndex probes; avoid recorded trackbg_render_flashy outer-ring/store-order/triangle probes; avoid recorded func_8002B0F4 grid/collision-plane/bottom-water probes. Choose a fresh bounded source-shape probe or another active alternate with unrecorded evidence.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
