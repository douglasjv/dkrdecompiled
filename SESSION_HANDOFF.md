# Session Handoff

- Generated at: 2026-05-24 07:41:53Z
- Branch: `master`
- HEAD: `9bfb186d`
- Completed task: `init_particle_buffers`
- Summary: Recorded failed promotion and allocator-tag-local probe; source restored after relinked diff stayed at score 2098.

## Validation

- ./diff.sh init_particle_buffers --no-pager: relinked focused diff score 2098 after promotion; allocator-tag local made no object-code movement
- gmake -j4 CROSS=tools/binutils/mips64-elf-: Verify: OK after restore
- ./score.sh -s: Decomp progress [us.v77]: 97.30%
- python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default remains func_80049794 unless choosing a fresh non-repeat parked-target hypothesis`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
