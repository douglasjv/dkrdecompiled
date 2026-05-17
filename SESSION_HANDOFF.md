# Session Handoff

- Generated at: 2026-05-17T17:23:35Z
- Branch: `master`
- HEAD: `bd9c98c9`
- Completed task: `func_8008FF1C`
- Summary: Revisited the close parked `func_8008FF1C` candidate instead of
  leaving it untouched. Tested a plain `s32 temp` selected-track carrier
  (`temp = gTrackSelectIDs[trackY][trackX]; selectedTrack = temp`); it removed
  the unsequenced-assignment warning but missed badly, widened focused drift to
  `CURRENT (935)`, and still used `v1` for the selected-track branch instead of
  target `t2`. Source restored and final full verify passed. Keep
  `func_8008FF1C` parked/default-skipped for routing momentum, but do not treat
  it as abandoned and do not retry this `s32 temp` carrier.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore
- Failed probe evidence: `./diff.sh func_8008FF1C --format plain --no-pager --max-size 900 -U 12` => `CURRENT (935)`, failed full verify CRCs `0x553930E7/0x227AD4A3`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes, the func_8002B0F4 outer segment-loop while spelling plus prior pad/early-conversion/loop probes, the func_80059208 final object-dot scale carrier plus prior split-final-vertical, negative-object/positive-checkpoint numerator, and final-offset variants, the trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, and func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
