# Session Handoff

- Generated at: 2026-05-24 12:24:55Z
- Branch: `master`
- HEAD: `ae54edba`
- Completed task: `trackbg-render-flashy-uv-dimension-multiply-before-shift`
- Summary: Rejected promoted trackbg_render_flashy UV dimension multiply-before-shift spelling: changed only texHeader width/height scale setup from texHeader->width * 16 * unkA0 / texHeader->height * 16 * unkA1 to (texHeader->width * unkA0) << 4 / (texHeader->height * unkA1) << 4, including the duplicate height assignment. Full verify failed with CRCs 0x9D8339EB/0x5359A7D5; relinked ./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager worsened to CURRENT (2963), keeping the early negative-cosine FPR drift and inserting multiply-then-shift integer traffic. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid trackbg_render_flashy UV dimension shift/multiply-before-shift spellings, color/sentinel variants, and first-ring negative-cosine carriers unless paired with a distinct FPR allocation fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
