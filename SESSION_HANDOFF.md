# Session Handoff

- Generated at: 2026-05-24 03:58:56Z
- Branch: `master`
- HEAD: `4ea0c83d`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted XInInt/ZInInt s16 local-type probe; focused diff regressed to CURRENT (4425) with sign-extension churn and the known early gCurrentLevelModel spill.

## Validation

- Probe full verify failed CRCs 0x93CE4D86/0x8EE561B4; after restore gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s => 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with selector recommended_next func_80049794 only if a distinct save-pressure/wave-allocation hypothesis is available; otherwise use func_8002B0F4 pad3-removed/model-spill family or trackbg_render_flashy early negative-cosine family without repeating recorded probes.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
