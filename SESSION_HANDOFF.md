# Session Handoff

- Generated at: 2026-05-25 02:20:35Z
- Branch: `master`
- HEAD: `290b3898`
- Completed task: `func_8002B0F4-x-grid-predicate-operand-order`
- Summary: Rejected promoted func_8002B0F4 X-grid predicate operand-order spelling; changed the NON_EQUIVALENT guard to #if 1 and rewrote only var_t0 >= XInInt && XInInt >= var_t1 as XInInt <= var_t0 && var_t1 <= XInInt. Full verify failed with calculated CRCs 0x7046F28A/0xDC00632D; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager stayed at CURRENT (2860), retaining the unwanted early gCurrentLevelModel spill at 0x60(sp) plus broad segment/grid/tail drift. Source restored. Worker also rejected func_80059208 lap-- to lap -= 1 in a forked checkout; relinked diff reported CURRENT (870), source restored, no patch applied here.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_8002B0F4 X-grid predicate operand-order spelling and saturated model-spill/grid/texture/tail families unless paired with a distinct model-spill/register allocation fix. Also avoid func_80059208 upper-half lap-decrement spelling unless using a distinct final-tail allocation or spline dataflow family; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
