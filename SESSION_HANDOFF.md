# Session Handoff

- Generated at: 2026-05-17 14:49:11Z
- Branch: `master`
- HEAD: `b80ffc24`
- Completed task: `func_80049794`
- Summary: Tested promotion-only acceptance for func_80049794 after a stale focused object-only diff reported CURRENT (0). Full matching verify failed with calculated CRCs 0x5FDDE03F/0xEF7A0514, and the relinked focused diff reported CURRENT (2990), with the same missing target `$f20/$f21` prologue saves, shifted saved-register stack slots, early `$f16` zero, and wave a0/v1 drift. Source guard restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: promoting func_80049794 with only `#ifdef NON_EQUIVALENT` -> `#if 1` failed full verify with calculated CRCs 0x5FDDE03F/0xEF7A0514; ./diff.sh func_80049794 --format plain --no-pager --max-size 1200 after relink => CURRENT (2990)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and do not trust func_80049794 object-only CURRENT (0) without relink/full verify.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
