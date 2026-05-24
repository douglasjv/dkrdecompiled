# Session Handoff

- Generated at: 2026-05-24 01:02:06Z
- Branch: `master`
- HEAD: `bcc2dd51`
- Completed task: `func_8002B0F4`
- Summary: Rejected dead vert NULL seed probe; focused diff stayed CURRENT (2860), source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue func_8002B0F4 only with a fresh model-spill fix hypothesis, or pivot to another active routable target if no non-repeated shape remains.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
