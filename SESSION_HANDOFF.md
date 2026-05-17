# Session Handoff

- Generated at: 2026-05-17 13:39:36Z
- Branch: `master`
- HEAD: `b677747e`
- Completed task: `func_80059208`
- Summary: Tested a declaration-only stack-shape probe in func_80059208: promoted source and removed only the dead pad3 local. It compiled but shrank the frame from target 0xc0 to 0xb8, worsened the relinked focused diff to CURRENT (1218), and full verify failed with calculated CRCs 0x53D13F77/0x21BEEE76. Source guard/body restored; final full verify passed. Keep func_80059208 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80059208 --format plain --no-pager --max-size 620 => relinked focused CURRENT (1218), frame 0xb8

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80059208 dead-pad3 removal stack-shape probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
