# Session Handoff

- Generated at: 2026-05-22 16:13:01Z
- Branch: `master`
- HEAD: `8ae54f6c`
- Completed task: `func_80049794`
- Summary: Rejected close save-family compare-only wave-bound cache; source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore; rejected probe failed with CRCs 0x52412037/0x63D27627 and ./diff.sh func_80049794 => relinked CURRENT (5795).

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate; for func_80049794 do not repeat the close save-family compare-only wave-bound cache.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
