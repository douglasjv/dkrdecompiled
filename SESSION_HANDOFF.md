# Session Handoff

- Generated at: 2026-05-24 10:46:07Z
- Branch: `master`
- HEAD: `41d5aa2a`
- Completed task: `func_8008FF1C`
- Summary: Rejected parked func_8008FF1C current-shape temp-removal probe; relinked diff worsened to CURRENT (935) and source restored verifies OK

## Validation

- Rejected parked-packet probe full build failed with calculated CRCs
  `0x553930E7/0x227AD4A3`; relinked `./diff.sh func_8008FF1C --no-pager`
  worsened from parked baseline `CURRENT (10)` to `CURRENT (935)`. The
  selected-track load/branch shifted away from target `t2` into `v1` and
  broadened register drift through the visible-track block. After source
  restore, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`,
  `./score.sh -s` remained 97.30%, and `python3
  tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended but saturated, so continue only with a distinct independent source family or pivot to another active routable candidate.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
