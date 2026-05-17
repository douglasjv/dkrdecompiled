# Session Handoff

- Generated at: 2026-05-17 17:12:38Z
- Branch: `master`
- HEAD: `100fce94`
- Completed task: `trackbg_render_flashy`
- Summary: Tested an all-first-ring `scaledXSin` spelling in `trackbg_render_flashy` by replacing every remaining first-ring `(xSin * 1280.0f)` term in `xPositions[0..3]` and `zPositions[0..2]` with the existing `scaledXSin` carrier. It compiled but missed badly, widening the frame to `0x168` and regressing the relinked focused diff to `CURRENT (13466)`. Source restored; final full verify passed. Keep `trackbg_render_flashy` active, but do not retry this all-first-ring scaled-sine rewrite.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh trackbg_render_flashy --format plain --no-pager --max-size 1200 -U 12` => `CURRENT (13466)`, failed full verify CRCs `0x8310DF9D/0x3EA48C03`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, the func_80059208 split-final-vertical and negative-object/positive-checkpoint numerator probes plus prior final-offset variants, the func_8008FF1C s16/register selectedTrack/temp probes, func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
