# Session Handoff

- Generated at: 2026-05-24 04:48:40Z
- Branch: `master`
- HEAD: `84ea9720`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted func_8002B0F4 var_s1 late-zero scheduling probe; relinked focused diff regressed to CURRENT (3070) with the known early gCurrentLevelModel spill at 0x60(sp).

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK); ./score.sh -s (97.30%)

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with func_8002B0F4 only if pairing a model-spill fix with a non-repeated grid/surface scheduling hypothesis; otherwise pivot to another routable candidate with fresh evidence.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
