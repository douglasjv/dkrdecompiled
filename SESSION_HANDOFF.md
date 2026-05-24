# Session Handoff

- Generated at: 2026-05-24 04:20:58Z
- Branch: `master`
- HEAD: `37ea7454`
- Completed task: `func_8002B0F4-field-base-pointers`
- Summary: Rejected promoted current-source field-base pointer reload probe for func_8002B0F4; separate segments/segmentsBoundingBoxes base locals widened the frame and worsened focused diff while preserving the unwanted early gCurrentLevelModel spill family.

## Validation

- Probe gmake -j4 CROSS=tools/binutils/mips64-elf- failed with calculated CRCs 0x78E9013A/0xAD05D630; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager reported CURRENT (4142). After source restore, gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s reports 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_8002B0F4 only with a distinct model-spill/register-family hypothesis; do not repeat separate segments/segmentsBoundingBoxes base pointer locals.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
