# Session Handoff

- Generated at: 2026-05-24 07:24:56Z
- Branch: `master`
- HEAD: `eff54c7c`
- Completed task: `func_80049794-grounded-zero-literal`
- Summary: Rejected promoted grounded-wheel integer-zero literal probe for func_80049794; full gate failed and uncompressed diff showed the usual missing F20/F21 saves plus wave bound/index reversal.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 only with a distinct wave bound/index or saved-FPR allocation fix; otherwise pivot to another active packet instead of repeating literal-only or exhausted wave-scan spellings.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
