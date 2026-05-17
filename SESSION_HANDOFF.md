# Session Handoff

- Generated at: 2026-05-17 16:49:49Z
- Branch: `master`
- HEAD: `6fe601e5`
- Completed task: `func_80059208`
- Summary: Tested a narrow `register f32 divisor` allocation hint in func_80059208. It compiled, but produced no object movement from the promoted baseline: full verify failed with calculated CRCs 0x53D141DF/0xB9D4B481 and focused diff stayed CURRENT (870) with the same final object-dot/checkpoint-dot register drift. Source restored; final full verify passed. Keep func_80059208 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 6 => CURRENT (870); failed full verify CRCs 0x53D141DF/0xB9D4B481

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80059208 divisor register hint plus prior func_80059208 final-offset variants, func_80049794 chained-zero/wave-bound/save-family probes, trackbg_render_flashy position/UV order-carrier probes, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
