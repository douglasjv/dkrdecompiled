# Session Handoff

- Generated at: 2026-05-24 05:25:31Z
- Branch: `master`
- HEAD: `152ea9af`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected promoted direct xCos-scaled first-ring expression probe. A worker proposed changing only first-ring xPositions/zPositions to direct xCos * 1280.0f terms while preserving scaledXSin and stack layout; after main-thread promotion, full verify failed with calculated CRCs 0x93BF98FF/0x27187E1D and relinked focused diff reported CURRENT (1668). Frame stayed 0x158 and score improved over baseline, but early negative-cosine and outer-ring FPR allocation shifted across f18/f16 and later outer stores drifted. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s reported 97.30%; python3 tools/check_active_surface.py reported active surface ok; git diff -- src/tracks.c and git diff --check were clean.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue trackbg_render_flashy only with a distinct early FPR allocation hypothesis that preserves 0x158 frame and avoids direct xCos-scaled first-ring terms, or pivot to another routable candidate if no non-repeat family is available.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
