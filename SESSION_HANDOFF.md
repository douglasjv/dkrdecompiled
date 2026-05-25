# Session Handoff

- Generated at: 2026-05-25 02:57:53Z
- Branch: `master`
- HEAD: `eab0b00d`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected promoted single-site first-ring scaled-sine reuse: changed xPositions[1] to scaledXCos - scaledXSin; full verify failed with CRCs 0x218F9FFA/0x18F4A6D6 and relinked diff regressed to CURRENT (13821); source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 remains selector-recommended, but avoid saturated saved-FPR/wave/pitch families unless a distinct allocation fix is found; otherwise pivot among func_80059208, trackbg_render_flashy, or func_8002B0F4 with a non-repeated family.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
