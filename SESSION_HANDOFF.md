# Session Handoff

- Generated at: 2026-05-24 12:04:12Z
- Branch: `master`
- HEAD: `099123ad`
- Completed task: `trackbg_render_flashy-rgb-decimal-literals`
- Summary: Rejected promoted final-vertex RGB decimal-literal spelling: changed only verts->r/g/b from 0xFF to 255. Full verify failed with CRCs 0x93D338FF/0x03D9C8FE; relinked ./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager stayed at CURRENT (1808) with the known early position-array FPR schedule drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid pure func_80049794 wave-bound/index variants, trackbg_render_flashy final RGB literal/store micro-variants, and func_8002B0F4 current-baseline model-spill micro-variants unless paired with a distinct register-family hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
