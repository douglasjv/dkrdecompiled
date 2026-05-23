# Session Handoff

- Generated at: 2026-05-23 09:53:33Z
- Branch: `master`
- HEAD: `053a3b3e`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected zPositions[7] multiply-order probe; promoting current source and changing (2.0f * scaledXCos) - scaledXSin to (scaledXCos * 2.0f) - scaledXSin failed verify with CRCs 0x93D338FF/0x03D9C8FE and relinked focused diff stayed CURRENT (1808), then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but consider another active alternate if no fresh func_80049794 hypothesis exists beyond saturated CURRENT (2760) and close-save-family wave-register families. For trackbg_render_flashy, do not repeat the z7/x7/z6/z5/x5/x6 multiply-order or other probes recorded in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
