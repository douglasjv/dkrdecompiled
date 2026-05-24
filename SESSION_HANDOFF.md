# Session Handoff

- Generated at: 2026-05-24 02:20:28Z
- Branch: `master`
- HEAD: `34e8f0d8`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected promoted zPositions[3] raw xSin multiply spelling; full verify failed with CRCs 0xF82B92BE/0x5DCC04AE and relinked focused diff worsened to CURRENT (5579), then source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_80049794 only with fresh non-repeated full-gate evidence, or pivot among active packets with a new family rather than first-ring/raw-sine trackbg variants.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
