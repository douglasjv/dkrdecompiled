# Session Handoff

- Generated at: 2026-05-24 04:35:20Z
- Branch: `master`
- HEAD: `7edb3ccf`
- Completed task: `func_8002B0F4-direct-skip-offset`
- Summary: Rejected func_8002B0F4 direct batch skip-offset assignment; it worsened the model-spill family.

## Validation

- Probe gmake -j4 CROSS=tools/binutils/mips64-elf- failed with calculated CRCs 0x2A78E7DF/0xC1A5BFE8; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager reported CURRENT (3190), still inserted the unwanted early gCurrentLevelModel load/spill at 0x60(sp), and broadened segment/grid/tail drift. After source restore, gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s reports 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Pivot away from func_8002B0F4 batch-skip offset lifetime variants unless paired with a separate model-spill fix; choose a different routable candidate or a distinct non-model-spill source-shape hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
