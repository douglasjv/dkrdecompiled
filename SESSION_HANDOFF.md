# Session Handoff

- Generated at: 2026-05-17 15:32:18Z
- Branch: `master`
- HEAD: `d33c1357`
- Completed task: `func_80059208`
- Summary: Tested a final lateral-offset carrier probe in `func_80059208`: promoted source and routed only the negated checkpoint-dot term through the now-dead `scale` local before adding it to the object dot. It compiled but produced no relinked object movement from the promoted baseline: focused score stayed `CURRENT (870)` and full verify failed with calculated CRCs `0x53D141DF/0xB9D4B481`. Source restored; final full verify passed. Keep `func_80059208` active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80059208 --format plain --no-pager --max-size 900 -U 4 after relink => CURRENT (870); failed full verify CRCs 0x53D141DF/0xB9D4B481

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the recorded func_80059208 negated-checkpoint scale-carrier probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
