# Session Handoff

- Generated at: 2026-05-24 05:09:23Z
- Branch: `master`
- HEAD: `b43b02df`
- Completed task: `func_8002B0F4`
- Summary: Promoted collision-hit post-increment limit equality probe missed: changing yOutCount >= 20 to yOutCount == 20 failed full verify with calculated CRCs 0xA74DDBBC/0xC4B262D4; relinked focused diff regressed to CURRENT (8360), with the hit-limit site compiling to li s7,0x14 plus bne s5,s7 instead of the target slti/bnez shape. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok; git diff --check clean.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue with func_8002B0F4 only on a distinct model-spill/register-family or plane-output lifetime hypothesis; do not repeat post-hit yOutCount == 20/equality limit spelling.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
