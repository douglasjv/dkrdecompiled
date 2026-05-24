# Session Handoff

- Generated at: 2026-05-24 11:03:56Z
- Branch: `master`
- HEAD: `ce4e1d4e`
- Completed task: `func_8008FF1C`
- Summary: Rejected parked selected-track condition-assignment spelling; relinked focused diff regressed to CURRENT (1195), branch still used v1 instead of target t2, and source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf-: Verify: OK after restore
- ./score.sh -s: decomp progress 97.30%
- python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No setup or behavior blocker; func_8008FF1C remains parked/exhausted. Revisit only with a new shape that keeps direct-table t2 load while preserving target branch-delay-slot hub-name store.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended, but prefer a distinct independent source family or another routable packet over saturated saved-FPR/wave micro-variants`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
