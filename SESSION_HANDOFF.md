# Session Handoff

- Generated at: 2026-05-23 06:01:14Z
- Branch: `master`
- HEAD: `5090ad01`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline course-height upper-cap compare-order spelling: if (2.5 < var_f20). Object-only diff first showed stale CURRENT (0), full verify failed with the promoted-baseline CRCs 0x5FDDE03F/0xEF7A0514, and relinked diff stayed CURRENT (2760). Target $f20/$f21 saves stayed absent, early zero stayed in current $f16 rather than target $f14, and wave a0/v1 allocation stayed reversed. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline course-height upper-cap compare-order spelling, course-height buoyancy subtract spelling, wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound/course-height aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, first-speed arithmetic, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
