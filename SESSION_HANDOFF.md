# Session Handoff

- Generated at: 2026-05-24 09:51:20Z
- Branch: `master`
- HEAD: `d859cd00`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected trackbg_render_flashy final triangle flags store-order spelling; promoted source moved tris->flags = 0x40 after the vi/uv stores in the triangle loop. Full verify failed with CRCs 0x93C6F83F/0x0C9FB0E5, and relinked diff regressed to CURRENT (2018) with early position-array FPR drift plus the expected tail flags-store movement. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Return to selector routing; prefer an independent func_80049794 family only if it is not another saved-FPR/wave-scan micro-variant, or another active guarded candidate with a distinct unrecorded source-shape family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
