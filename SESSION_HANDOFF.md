# Session Handoff

- Generated at: 2026-05-22 16:02:41Z
- Branch: `master`
- HEAD: `ffaf64ef`
- Completed task: `func_8002B0F4`
- Summary: Rejected levelSegmentIndex register-parameter hint; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted func_8002B0F4 with register s32 levelSegmentIndex, calculated CRCs 0x7856718A/0x66208CAA; ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (2860), target f20/f22 prologue remained but unwanted early gCurrentLevelModel spill appeared at 0x60(sp); restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_8002B0F4, do not repeat the levelSegmentIndex register-parameter hint; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
