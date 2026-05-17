# Session Handoff

- Generated at: 2026-05-17 16:25:44Z
- Branch: `master`
- HEAD: `b2a2824b`
- Completed task: `func_80049794`
- Summary: Tested combining the close chained-zero x/z/y save-family branch with an existing-spCC preserve across apply_vehicle_rotation_offset (`spCC = var_f14; ...; var_f14 = spCC`). It compiled but missed badly: relinked focused score regressed to CURRENT (5976), full verify failed with calculated CRCs 0xF40EFA01/0x5672460E, and the diff showed broad f14 save/reload traffic through spinout and voice/sound scheduling. Source restored; final full verify passed. Keep func_80049794 active rather than parked.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: ./diff.sh func_80049794 --format plain --no-pager --max-size 1200 -U 4 => CURRENT (5976); failed full verify CRCs 0xF40EFA01/0x5672460E

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; keep close functions active and avoid the newly recorded func_80049794 close-branch spCC preserve combination plus prior func_80049794 chained-zero/wave-bound/save-family probes, func_80059208 final-offset variants, trackbg_render_flashy position/UV order-carrier probes, and func_8002B0F4 pad/early-conversion/loop probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
