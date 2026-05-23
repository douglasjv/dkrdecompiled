# Session Handoff

- Generated at: 2026-05-23 02:44:55Z
- Branch: `master`
- HEAD: `5b7e5a94`
- Completed task: `func_80049794`
- Summary: Close chained-zero/x/z/y/steer-noop save-family segmentZVelocity first-speed carrier missed; full verify failed with CRCs 0xB8DD79CD/0xCD5971FB and relinked focused diff stayed CURRENT (4365), collapsing into the segmentXVelocity carrier family. It kept the target frame/save prologue, but the wave a0/v1 swap and later scheduling drift remained. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794. Do not repeat current-baseline z-first or x/y/z speed magnitude expression orders, current-baseline var_t0/temp_t7/var_t9/i/var_v0 wave-bound carriers, close save-family temp_t7/var_t9 wave-bound carriers, close save-family explicit-break wave scan, close save-family segmentXVelocity/segmentZVelocity/racerVelocity first-speed carriers, or the func_8002B0F4 current-layout pointer-arithmetic segment setup. If staying on func_80049794, use a fresh hypothesis that targets wave v1-bound/a0-loop order or first-speed arithmetic without repeating recorded expression-order or bound-carrier aliases.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
