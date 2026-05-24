# Session Handoff

- Generated at: 2026-05-24 11:56:30Z
- Branch: `master`
- HEAD: `44ff5828`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted batch offset-load-before-surface-read scheduling probe: full verify failed with CRCs 0x7856718A/0x66208CAA; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager stayed at CURRENT (2860) with unwanted early gCurrentLevelModel spill at 0x60(sp). Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_8002B0F4 only with a distinct model-spill/register-family hypothesis, or pivot back to selector func_80049794 with an independent non-repeat family.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
