# Session Handoff

- Generated at: 2026-05-24 09:43:12Z
- Branch: `master`
- HEAD: `f863aadf`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected `trackbg_render_flashy` explicit header pointer-load spelling. The promoted source changed only `var_t2 = *gCurrentLevelHeader2->unk74` to `var_t2 = gCurrentLevelHeader2->unk74[0]`. Pre-build focused diff misleadingly reported `CURRENT (0)`, full verify failed with calculated CRCs `0x93D338FF/0x03D9C8FE`, and relinked `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` stayed at promoted baseline `CURRENT (1808)` with the same position-array/FPR scheduling drift and no useful movement at the header pointer load. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Return to selector routing; prefer an independent func_80049794 family that targets saved-FPR/frame pressure or wave allocation, or another active guarded candidate if the selector packet remains saturated.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
