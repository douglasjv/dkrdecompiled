# Session Handoff

- Generated at: 2026-05-24 05:17:06Z
- Branch: `master`
- HEAD: `7a940349`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted pad3-removal plus scaled collision-plane index local probe. Removing pad3 and storing basePlaneIndex * 4 in temp failed full verify with calculated CRCs 0x7E7421AA/0xA14ED9A9; relinked focused diff reported CURRENT (2733), slightly worse than the scaled-index-only CURRENT (2725), with the unwanted early gCurrentLevelModel spill retained at 0x64(sp). Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok; git diff -- src/tracks.c clean; git diff --check clean.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_8002B0F4 only with a distinct model-spill/register-family fix; do not repeat pad3 removal plus scaled collision-plane index local, or pivot to another routable candidate if no model-spill hypothesis is available.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
