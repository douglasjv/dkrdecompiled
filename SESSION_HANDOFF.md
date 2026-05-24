# Session Handoff

- Generated at: 2026-05-24 07:17:51Z
- Branch: `master`
- HEAD: `ff1c62d0`
- Completed task: `func_80049794-close-wave-gate-split`
- Summary: Rejected close save-family nested wave-gate split for func_80049794; preserved target frame/FPR saves but stayed in close-family CRCs with a0/v1 wave bound-index reversal.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 remains selector recommendation only with a distinct wave bound/index or saved-FPR allocation fix; otherwise pivot to another active packet rather than repeating close save-family gate/register variants.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
