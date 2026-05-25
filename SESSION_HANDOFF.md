# Session Handoff

- Generated at: 2026-05-25 02:55:33Z
- Branch: `master`
- HEAD: `89b4ab14`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted yOutCount high-water equality spelling: changed yOutCount >= 20 to yOutCount == 20; full verify failed with CRCs 0xA74DDBBC/0xC4B262D4 and relinked diff regressed to CURRENT (8360); source restored.

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
