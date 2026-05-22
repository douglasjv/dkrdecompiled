# Session Handoff

- Generated at: 2026-05-22 23:34:46Z
- Branch: `master`
- HEAD: `28739b81`
- Completed task: `func_8008FF1C`
- Summary: Rejected post-if common hub-name store selected-track branch variants; one stayed in v1 branch drift and the no-temp sibling kept t2 but left the hub-name store after the join, then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default routing remains func_80049794 unless intentionally revisiting exhausted func_8008FF1C/func_80017A18/init_particle_buffers with PARKED.md notes checked first.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
