# Session Handoff

- Generated at: 2026-05-17 17:16:50Z
- Branch: `master`
- HEAD: `a6551cba`
- Completed task: `func_80059208`
- Summary: Tested a final object-dot x-product carrier in `func_80059208` by routing `splinePos * diffX` through the now-dead `scale` local before adding `diffZ * distance`. It compiled but missed, worsening the relinked focused score from the promoted baseline `CURRENT (870)` to `CURRENT (940)` and reversing the desired final object x/z load order. Source restored; final full verify passed. Keep `func_80059208` active, but do not retry this final object-dot `scale` carrier.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `./diff.sh func_80059208 --format plain --no-pager --max-size 1200 -U 20` => `CURRENT (940)`, failed full verify CRCs `0x53A518DF/0x0DEFF06A`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80059208 final object-dot scale carrier plus prior split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants, the trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, the func_8008FF1C s16/register selectedTrack/temp probes, func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
