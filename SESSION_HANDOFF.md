# Session Handoff

- Generated at: 2026-05-23 05:53:01Z
- Branch: `master`
- HEAD: `515c9401`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline wave-drift clamp-assignment suffix probe: racerVelocity = 4.0f with subtract/compare/divide unchanged. Object-only diff first showed stale CURRENT (0), full verify failed with CRCs 0xA72E8795/0xE7316761, and relinked diff regressed to CURRENT (3355). Target $f20/$f21 saves stayed absent, early zero stayed in current $f16 rather than target $f14, wave a0/v1 allocation stayed reversed, and later $f14/$f20 gravity scheduling broadened. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order, course-height grouping, first-speed arithmetic, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
