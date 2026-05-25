# Session Handoff

- Generated at: 2026-05-25 03:16:14Z
- Branch: `master`
- HEAD: `96b7435f`
- Completed task: `func_80049794`
- Summary: Recorded `func_80049794` normal-flight `trickType == -2 || trickType == 2` branch-order miss; source restored. Full verify failed with calculated CRCs `0xDFDFE9E6/0xFD85A953`; relinked focused diff stayed at `CURRENT (2760)` with missing `$f20/$f21` saves, early-zero `$f16` drift, and wave bound/index drift.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 remains selector-recommended; avoid saturated saved-FPR/wave/pitch/trick-branch families unless a distinct allocation fix is found. Otherwise pivot among live candidates with non-repeated hypotheses.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
