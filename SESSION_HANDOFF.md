# Session Handoff

- Generated at: 2026-05-23 01:37:06Z
- Branch: `master`
- HEAD: `b83ce19d`
- Completed task: `func_80049794`
- Summary: Promoted func_80049794 and routed the grounded-wheel zero stores through existing spD8. Full verify failed with calculated CRCs 0x5FDDE03F/0xEF7A0514, and relinked ./diff.sh func_80049794 stayed CURRENT (2760) with no f20/f21 saves or f14 early-zero movement. Source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector route at func_80049794 unless pivoting to active func_80059208, func_8002B0F4, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
