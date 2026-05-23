# Session Handoff

- Generated at: 2026-05-23 00:14:44Z
- Branch: `master`
- HEAD: `b8de928e`
- Completed task: `func_8002B0F4`
- Summary: Promoted func_8002B0F4 and tested the pad3-removed three-level surface guard plus textureIndex-through-temp path with currentBatch->flags also routed through temp; full verify failed with calculated CRCs 0x7C5E203C/0xE0335DD6 and relinked focused score worsened to CURRENT (3268). Source was restored and final verify passed; do not repeat this flags-through-temp carrier on that branch.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default routing remains func_80049794 unless pivoting to active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
