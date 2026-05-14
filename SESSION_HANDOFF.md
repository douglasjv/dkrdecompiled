# Session Handoff

- Generated at: 2026-05-14 22:12:18Z
- Branch: `master`
- HEAD: `b002d026`
- Completed task: `DKR-PARK-INIT-PARTICLE-BUFFERS`
- Summary: init_particle_buffers source promotion was investigated and parked with saved-register allocation evidence; selector now advances to func_80049794.

## Validation

- python3 tools/check_active_surface.py -> active surface ok
- python3 tools/query_goal_state.py next --compact --refresh -> recommends func_80049794
- ./diff.sh -o init_particle_buffers -s --compress-matching 3 --no-pager -> best promoted score 1816, nonmatching
- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK

## Blockers Or Unknowns

- Plain gmake -j4 still selects Homebrew mips-linux-gnu-ld; keep using CROSS=tools/binutils/mips64-elf-.
- func_8008FF1C, func_80017A18, and init_particle_buffers are parked in research/tasks/PARKED.md; do not retry their recorded probe families as the next packet.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `DKR-MATCH-FUNC-80049794`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
