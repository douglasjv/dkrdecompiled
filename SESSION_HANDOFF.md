# Session Handoff

- Generated at: 2026-05-23 08:40:20Z
- Branch: `master`
- HEAD: `931420c6`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected final global pointer store-order probe; promoted current source with gTrackTriPtr stored before gTrackVtxPtr failed verify with CRCs 0x93D338FF/0x3EBCCB8F and relinked focused diff regressed to CURRENT (1846), then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but consider another active alternate if no fresh func_80049794 hypothesis exists beyond the saturated CURRENT (2760) family. For trackbg_render_flashy, do not repeat final global pointer store-order, final triangle postincrement, final triangle two-at-a-time unroll, final vertex alpha ternary, center position store-order, or the recorded position/UV aliases in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
