# Session Handoff

- Generated at: 2026-05-25 03:41:05Z
- Branch: `master`
- HEAD: `00dd9098`
- Completed task: `func_80049794`
- Summary: Rejected update-rate guard == TRUE spelling; full verify failed and relinked diff regressed to CURRENT (5760), source restored

## Validation

- `./diff.sh func_80049794 --compress-matching 2 --no-pager` after the
  rejected probe relinked at `CURRENT (5760)`.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` after source restore reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. A forked worker also rejected the planned
  close-save-family no-spill early-zero follow-up as already represented in
  `ACTIVE.md`; do not micro-vary early zeroing unless the source shape also
  attacks the wave `v1` bound / `a0` loop-index allocation.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 wave bound/index allocation preserving known no-spill close save-family, or distinct live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
