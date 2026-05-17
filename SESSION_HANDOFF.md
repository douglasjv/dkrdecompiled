# Session Handoff

- Generated at: 2026-05-17 14:17:34Z
- Branch: `master`
- HEAD: `e7383d45`
- Completed task: `func_80049794`
- Summary: Tested an explicit decrementing `WaterProperties **wavePtr` wave-scan spelling on the close save-family branch in func_80049794: promoted source, used chained grounded-wheel zero, removed trailing `pad3`/`pad4`, kept the x/z/y pre-`sqrtf` accumulation and steer-vel no-op, then walked a pointer while decrementing `var_a0`. It widened the frame to 0x100, regressed the relinked focused diff to CURRENT (7232), shifted the scan into `v0/a1/v1` instead of target `v1/a0/v0`, and full verify failed with calculated CRCs 0xC51623A2/0xD2F96DC4. Source guard/body restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 900 => relinked focused CURRENT (7232); failed full verify CRCs 0xC51623A2/0xD2F96DC4

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80049794 explicit wavePtr pointer-walk shape.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
