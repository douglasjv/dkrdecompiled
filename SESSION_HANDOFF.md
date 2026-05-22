# Session Handoff

- Generated at: 2026-05-22 15:56:31Z
- Branch: `master`
- HEAD: `ab01baab`
- Completed task: `func_8002B0F4`
- Summary: Rejected combined xIn/zIn register-parameter plus pad3-removal probe; source restored

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- failed for promoted func_8002B0F4 with register f32 xIn/zIn and pad3 removed, calculated CRCs 0x785671AA/0x0D6F6A4A; ./diff.sh func_8002B0F4 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (2868), target f20/f22 prologue remained but unwanted early gCurrentLevelModel spill moved to 0x64(sp); restored source and reran gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_8002B0F4, do not repeat the combined xIn/zIn float register-parameter plus pad3-removal shape; use ACTIVE.md before choosing another probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
