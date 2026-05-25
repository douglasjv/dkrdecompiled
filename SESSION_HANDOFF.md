# Session Handoff

- Generated at: 2026-05-25 03:19:02Z
- Branch: `master`
- HEAD: `f16bade7`
- Completed task: `func_8002B0F4`
- Summary: Recorded `func_8002B0F4` batch-skip flag-mask explicit-nonzero miss; source restored. Full verify failed with calculated CRCs `0x7856718A/0x66208CAA`; relinked focused diff stayed at `CURRENT (2860)` with the unwanted early `gCurrentLevelModel` spill and broad segment/grid/tail drift.

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
