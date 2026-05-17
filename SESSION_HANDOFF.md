# Session Handoff

- Generated at: 2026-05-17 16:46:37Z
- Branch: `master`
- HEAD: `ed3cb9a5`
- Completed task: `func_80049794`
- Summary: Tested a current-baseline reversed chained-zero spelling for the grounded-wheel reset (`racer->unk84 = (racer->unk88 = 0.0f)`). It compiled, but missed: full verify failed with calculated CRCs 0x5FDDE03F/0x127A8488, focused diff worsened to CURRENT (3000), and the early zero stores reversed while still using $f16 and still lacking target $f20/$f21 prologue saves. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 1200 -U 6 => CURRENT (3000); failed full verify CRCs 0x5FDDE03F/0x127A8488

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80049794 reversed chained-zero current-baseline probe plus prior func_80049794 chained-zero/wave-bound/save-family probes, trackbg_render_flashy position/UV order-carrier probes, func_80059208 final-offset variants, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
