# Session Handoff

- Generated at: 2026-05-22 19:22:41Z
- Branch: `master`
- HEAD: `5821da51`
- Completed task: `func_80049794`
- Summary: Rejected close save-family spEC wave-threshold carrier; full verify failed with calculated CRCs 0xC65CFFD3/0xC660208A and relinked focused diff worsened to CURRENT (8620), so source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (restored source): Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_80049794 from the close x/z/y save-family evidence, but do not repeat existing-var_f6 or spEC wave-threshold carriers; solve wave register/order or first-speed arithmetic drift without losing the 0xf8 frame and f20/f21 saves.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
