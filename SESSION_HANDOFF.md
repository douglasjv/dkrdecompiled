# Session Handoff

- Generated at: 2026-05-23 08:36:28Z
- Branch: `master`
- HEAD: `12596a07`
- Completed task: `func_8002B0F4`
- Summary: Rejected bottom segment-range guard reorder; promoted current source with levelSegmentIndex < gCurrentLevelModel->numberOfSegments before levelSegmentIndex >= 0 failed verify with CRCs 0x281EE7B3/0xDC10368B and relinked focused diff regressed to CURRENT (4020), then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but consider another active alternate if no fresh func_80049794 hypothesis exists beyond the saturated CURRENT (2760) family. For func_8002B0F4, do not repeat bottom segment-range guard reorder, bottom-water condition-order, bottom default-water store-order, or the recorded pad3/model-spill families in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
