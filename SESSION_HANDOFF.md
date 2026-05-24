# Session Handoff

- Generated at: 2026-05-24 07:49:13Z
- Branch: `master`
- HEAD: `b484aecd`
- Completed task: `func_8002B0F4-segment-bbox-first-setup-order`
- Summary: Rejected promoted segment setup assignment-order probe; relinked diff regressed to CURRENT (3965), added early gCurrentLevelModel spill at 0x60(sp), source restored.

## Validation

- ./diff.sh func_8002B0F4 --no-pager before full build: misleading CURRENT (0) against the pre-relink object
- gmake -j4 CROSS=tools/binutils/mips64-elf- after promotion: failed, calculated CRCs 0x7856718A/0xA6A743D8
- ./diff.sh func_8002B0F4 --no-pager after promotion/relink: CURRENT (3965), early gCurrentLevelModel spill at 0x60(sp), segment loop body shifted
- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK
- ./score.sh -s: Decomp progress [us.v77]: 97.30%
- python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default remains func_80049794 unless choosing a fresh non-repeat alternate hypothesis such as func_8002B0F4 segment loop setup without introducing a hoisted model spill`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
