# Session Handoff

- Generated at: 2026-05-22 21:26:54Z
- Branch: `master`
- HEAD: `1a8c4ec6`
- Completed task: `func_8002B0F4`
- Summary: Recorded pad3-removed three-level surface guard plus texture-index temp with batch-offset-before-surface-read order miss; relinked focused stayed CURRENT (1520), full verify failed with CRCs 0x7C4CE1AA/0x7C1438D3, then source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; continue func_8002B0F4 only with a new non-repeated model-spill fix that improves beyond the pad3-removed three-level guard plus texture-index temp carrier, otherwise pivot among active func_80049794, func_80059208, or trackbg_render_flashy with ACTIVE.md miss notes checked first.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
