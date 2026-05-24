# Session Handoff

- Generated at: 2026-05-24 08:42:08Z
- Branch: `master`
- HEAD: `620367ec`
- Completed task: `func_80049794`
- Summary: Rejected plain current-C promotion; relinked diff regressed to CURRENT (2760) with lost f20/f21 saves and wave-bound allocation drift.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK; ./score.sh -s: 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector again; prefer a bounded routable target or independent func_80049794 source family, avoiding plain promotion and saturated save/wave micro-variants.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
