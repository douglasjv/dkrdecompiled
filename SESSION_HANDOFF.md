# Session Handoff

- Generated at: 2026-05-24 05:50:54Z
- Branch: `master`
- HEAD: `b0b883d1`
- Completed task: `func_8002B0F4`
- Summary: Rejected promoted current-source output-pointer clear spelling arg3[0] = NULL; full verify failed with CRCs 0x7856718A/0x66208CAA and relinked func_8002B0F4 stayed CURRENT (2860) with the known early gCurrentLevelModel spill at 0x60(sp). Also recorded worker func_80049794 cached-bound for-loop miss: CRCs 0x5790053C/0x1C8C0179, focused CURRENT (5755), wave setup drifted to v1/a3/v0 and still missed saved FPRs.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restoring source; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector again; continue func_80049794 only with a distinct pointer-object current-wave cursor plus saved-FPR allocation hypothesis, otherwise pivot to func_80059208, trackbg_render_flashy, or func_8002B0F4 per non-repeat notes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
