# Session Handoff

- Generated at: 2026-05-25 02:52:52Z
- Branch: `master`
- HEAD: `203d6cec`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected promoted gSPVertexDKR final-flag macro spelling: changed final 0 to FALSE; full verify failed with CRCs 0x93D338FF/0x03D9C8FE and relinked diff stayed CURRENT (1808); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 remains selector-recommended, but avoid saturated saved-FPR/wave/pitch families unless a distinct allocation fix is found; otherwise pivot to a live candidate with a non-repeated family.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
