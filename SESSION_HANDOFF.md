# Session Handoff

- Generated at: 2026-05-23 05:46:46Z
- Branch: `master`
- HEAD: `3d7f3d67`
- Completed task: `func_80049794`
- Summary: Rejected close save-family plus wave-drift subtract-suffix probe: object-only diff first showed stale CURRENT (0), full verify failed with CRCs 0xA8F39A57/0xC08781AF, and relinked diff regressed to CURRENT (7769) while preserving the target 0xf8 frame, $f20/$f21 saves, and early $f14 zero but widening the wave a0/v1 drift.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat the close save-family plus wave-drift subtract-suffix combination; continue with a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, first-speed arithmetic, or the early $f14/$f20 save-family interaction without repeating recorded aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
