# Session Handoff

- Generated at: 2026-05-24 08:00:07Z
- Branch: `master`
- HEAD: `3e89d40e`
- Completed task: `func-80049794-wave-bound-split`
- Summary: Rejected explicit var_v1 wave bound/index split; relinked diff returned CURRENT (5755), source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK; ./score.sh -s: 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default remains func_80049794, but do not repeat explicit cached wave-bound/index split alone. Combine a known save-family shape with a different cursor-addressing form, or pivot to another routable packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
