# Session Handoff

- Generated at: 2026-05-17T17:30:43Z
- Branch: `master`
- HEAD: `70efb7c1`
- Completed task: `func_80059208`
- Summary: Tested a staged positive-checkpoint/split-object-dot spelling in
  the final lateral offset block:
  `pad2 = checkpointDot; pad = objX * diffX; pad2 = -pad2; distance = objZ;
  pad += diffZ * distance`. It compiled but produced no relinked object
  movement from the promoted baseline: focused score stayed `CURRENT (870)`,
  full verify failed with the same CRC family, and the final object-position
  loads/arithmetic still missed the target negated-checkpoint schedule. Source
  restored and final full verify passed. Keep `func_80059208` active, but do
  not retry this split-object-dot-after-positive-checkpoint spelling.

## Validation

- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => failed while promoted with calculated CRCs `0x53D141DF/0xB9D4B481`
- `./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 34` after relink => `CURRENT (870)`
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` => `Verify: OK` after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; avoid the newly recorded func_80059208 split-object-dot-after-positive-checkpoint spelling plus prior final object-dot scale carrier, split-final-vertical, negative-object/positive-checkpoint numerator, final-offset variants, promotion-only func_80049794 acceptance from object-only CURRENT (0), the func_8008FF1C s32 temp carrier plus prior s16/register selectedTrack/temp probes, the func_8002B0F4 outer segment-loop while spelling plus prior pad/early-conversion/loop probes, the trackbg_render_flashy all-first-ring scaledXSin rewrite plus prior position/UV order-carrier probes, and func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
