# Session Handoff

- Generated at: 2026-05-17 17:08:54Z
- Branch: `master`
- HEAD: `2e01e258`
- Completed task: `func_80059208`
- Summary: Tested two final-tail source shapes in func_80059208. Splitting the final vertical offset into `diffY = obj->trans.y_position; diffY -= tempY; diffY /= divisor;` compiled but missed, widening the relinked focused diff to CURRENT (1922). A negative object-dot plus positive checkpoint-dot lateral numerator spelling compiled but reproduced the known positive-numerator miss, CURRENT (1300). Source restored; final full verify passed. Keep func_80059208 active, but do not retry these tail-carrier spellings.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: split final vertical carrier => ./diff.sh func_80059208 --format plain --no-pager --max-size 1200 -U 12 => CURRENT (1922), failed full verify CRCs 0xDACE25C4/0x70185CA9; negative-object/positive-checkpoint numerator => CURRENT (1300), failed full verify CRCs 0xC7D996EA/0xC6D1DFDE

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80059208 split-final-vertical and negative-object/positive-checkpoint numerator probes plus prior final-offset variants, the func_8008FF1C s16/register selectedTrack/temp probes, func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes, func_8002B0F4 pad/early-conversion/loop probes, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
