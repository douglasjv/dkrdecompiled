# Session Handoff

- Generated at: 2026-05-25 02:26:22Z
- Branch: `master`
- HEAD: `3caa5eae`
- Completed task: `func_80049794-var_f20-double-carrier`
- Summary: Rejected promoted func_80049794 saved-FPR/register-pressure double-carrier spelling; changed the NON_EQUIVALENT guard to #if 1 and changed only the main var_f20 declaration from f32 to double. Full verify failed with calculated CRCs 0xABC4F62A/0x9D55B713; relinked ./diff.sh func_80049794 --compress-matching 2 --no-pager worsened to CURRENT (14812). The frame widened from target 0xF8 to current 0x108, the target f20/f21 prologue saves were still absent, and broad wave, steering, boost, and tail FPR scheduling drift expanded. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid broad func_80049794 carrier-width changes and use only a narrower saved-FPR lifetime/register-pressure question, or pivot to another bounded routable active packet. Also avoid the already recorded func_80049794 wave-scan split-index/register-shape microvariants, late boost-emitter high-split compare, vehicle-particle guard operand-order, magnetTimer truthy, final spA1/unk201 tail booleans, early grounded-zero carriers, and throttle/brake literals.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
