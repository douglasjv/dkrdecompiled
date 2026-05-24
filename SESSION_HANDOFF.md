# Session Handoff

- Generated at: 2026-05-24 10:03:20Z
- Branch: `master`
- HEAD: `388e4a89`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected promoted final vertex store-order spelling; source changed only the vertex loop order to write y, x, RGB, z, alpha. Pre-build focused diff reported CURRENT (0), full verify failed with CRCs 0x93D338FF/0x8D381EFE, and relinked diff worsened to CURRENT (2263) with early negative-cosine/position-array FPR drift plus shifted final vertex store schedule. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run the selector and prefer a distinct unrecorded family on an active guarded candidate; avoid trackbg_render_flashy final vertex store-order/alpha/pointer-loop spellings unless paired with an early negative-cosine position-array fix.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
