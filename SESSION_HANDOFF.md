# Session Handoff

- Generated at: 2026-05-24 07:02:49Z
- Branch: `master`
- HEAD: `db034de6`
- Completed task: `func_80059208`
- Summary: Rejected promoted posZ subtraction regrouping probe; full verify failed after compressed diff false-positive, uncompressed diff was CURRENT (1575), source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK
- ./score.sh -s -> Decomp progress [us.v77]: 97.30%; Documentation progress: 65.47%
- python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 selector packet remains recommended; for func_80059208 do not repeat posZ subtract-product regrouping, next hypothesis should pivot away from sampling-loop sign spelling toward final object/checkpoint dot or another routable packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
