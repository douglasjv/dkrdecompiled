# Session Handoff

- Generated at: 2026-05-24 00:47:19Z
- Branch: `master`
- HEAD: `474d1cba`
- Completed task: `func_80049794`
- Summary: Rejected current-baseline wave gate gRacerWaveCount > 0 probe; focused diff worsened to CURRENT (2960), source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_80049794 only for a fresh FPR lifetime/save-family hypothesis that avoids repeated wave-bound spelling, or pivot to another selector-routable active target if no non-repeated shape remains.`
- Packet class: `matching_impl`
- Packet status: `evidence`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
