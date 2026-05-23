# Session Handoff

- Generated at: 2026-05-23 06:05:19Z
- Branch: `master`
- HEAD: `1db8ce1d`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline explicit first-compare/do-loop wave-scan spelling. Object-only diff first showed stale CURRENT (0), full verify failed with known split-bound CRCs 0x5790053C/0x1C8C0179, and relinked diff regressed to CURRENT (5755). It allocated the saved wave bound in a3 and the walking index in v0 rather than target v1/a0, inserted spA2 stack-byte traffic, and still missed target $f20/$f21 saves plus early $f14 zero. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline explicit first-compare/do-loop wave scan, split wave-bound spelling, course-height upper-cap compare-order spelling, course-height buoyancy subtract spelling, wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound/course-height aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order without split-bound stack-byte traffic, course-height grouping, first-speed arithmetic, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
