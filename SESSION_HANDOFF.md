# Session Handoff

- Generated at: 2026-05-24 11:17:55Z
- Branch: `master`
- HEAD: `ef44e7e5`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted early sp108 zero-bang guard spelling; full verify failed with CRCs 0x7856718A/0x66208CAA and relinked diff stayed CURRENT (2860) with the known early gCurrentLevelModel spill, then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf-: Verify: OK after restore; ./score.sh -s: decomp progress 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with a non-repeated routable packet; avoid func_8002B0F4 early sp108 guard micro-variants unless paired with an independent gCurrentLevelModel spill fix.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
