# Session Handoff

- Generated at: 2026-05-24 10:33:21Z
- Branch: `master`
- HEAD: `a430cd27`
- Completed task: `func_80049794`
- Summary: Rejected promoted head-turn branch-order probe; relinked diff regressed to CURRENT (3090), dropped target f20/f21 saves, and restored source verifies OK

## Validation

- Rejected probe full build failed with calculated CRCs
  `0x3C39E22F/0x8EC77BBA`; relinked `./diff.sh func_80049794
  --compress-matching 2 --no-pager` regressed to `CURRENT (3090)`. After
  source restore, `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`, `./score.sh -s` remained 97.30%, and `python3
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
