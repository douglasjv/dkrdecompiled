# Session Handoff

- Generated at: 2026-05-24 01:22:51Z
- Branch: `master`
- HEAD: `1bee8cf7`
- Completed task: `func_8002B0F4`
- Summary: Rejected pre-call coordinate conversion probe and worker wave-scan probe

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 only with a fresh non-repeated saved-FPR/wave-bound hypothesis, or pivot to another compact active packet with a non-repeated source-shape.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
