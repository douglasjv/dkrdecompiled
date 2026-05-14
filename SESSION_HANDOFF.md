# Session Handoff

- Generated at: 2026-05-14 22:07:02Z
- Branch: `master`
- HEAD: `1a296630`
- Completed task: `DKR-PARK-FUNC-80017A18`
- Summary: Baserom is present and the func_80017A18 source promotion probe was parked with diff evidence; selector now advances to init_particle_buffers.

## Validation

- python3 tools/check_active_surface.py -> active surface ok
- python3 tools/query_goal_state.py next --compact --refresh -> recommends init_particle_buffers
- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK

## Blockers Or Unknowns

- Plain gmake -j4 still selects Homebrew mips-linux-gnu-ld; keep using CROSS=tools/binutils/mips64-elf-.
- func_8008FF1C and func_80017A18 are parked in research/tasks/PARKED.md; do not retry their recorded probe families as the next packet.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `DKR-MATCH-INIT-PARTICLE-BUFFERS`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
