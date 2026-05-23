# Session Handoff

- Generated at: 2026-05-23 06:10:00Z
- Branch: `master`
- HEAD: `ecb81662`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline trailing pad3/pad4 removal. Object-only diff first showed stale CURRENT (0), full verify failed with calculated CRCs 0x5FDDE55F/0x6EE6C1E0, and relinked diff regressed to CURRENT (3261). It shrank the frame to 0xf0, shifted saved-register and parameter stack slots down by 8 bytes, still missed target $f20/$f21 saves plus early $f14 zero, and left the wave scan in current bound/index order. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline trailing pad3/pad4 removal, explicit first-compare/do-loop wave scan, split wave-bound spelling, course-height upper-cap compare-order spelling, course-height buoyancy subtract spelling, wave-drift clamp-assignment suffix, subtract-only suffix, close save-family plus wave-drift subtract-suffix, or the recorded normalization/first-speed/wave-bound/course-height aliases in ACTIVE.md. Continue with a fresh hypothesis targeting wave v1-bound/a0-loop order without stack-byte traffic/frame shrinkage, course-height grouping, first-speed arithmetic, or early $f14/$f20 save-family interaction.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
