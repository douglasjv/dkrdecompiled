# Session Handoff

- Generated at: 2026-05-24 05:45:49Z
- Branch: `master`
- HEAD: `306c3163`
- Completed task: `func_80049794`
- Summary: Rejected promoted early wave speed var_f14 carrier: removed the dedicated racerVelocity local and routed the early wave speed clamp/lift through var_f14; relinked object diff worsened to CURRENT (2704) and full verify failed with calculated CRCs 0x5FD89617/0xF4C6A984; source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restoring src/racer.c; ./score.sh -s -> 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run the selector again; continue func_80049794 only with a distinct non-repeat saved-FPR plus wave bound/index allocation hypothesis, otherwise pivot to func_80059208, trackbg_render_flashy, or func_8002B0F4 per selector.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
