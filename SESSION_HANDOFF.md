# Session Handoff

- Generated at: 2026-05-24 12:48:24Z
- Branch: `master`
- HEAD: `d62ddb2e`
- Completed task: `func_8002B0F4-collision-plane-zero-branch`
- Summary: Rejected promoted func_8002B0F4 collision-plane zero-branch spelling: changed the NON_EQUIVALENT guard to #if 1 and rewrote only if (tempVec4f.y != 0.0) as if (tempVec4f.y == 0.0) { } else { ... }. Full verify failed with calculated CRCs 0x77D9E18A/0xB9F696E2; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager regressed to CURRENT (2995), collapsing into the known X-grid fake-barrier family with early gCurrentLevelModel spill at 0x60(sp), X-grid accumulator shifted from target s1 to current s2, and broad segment/grid/tail drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_8002B0F4 collision-plane zero-branch, collision-plane scalar guard variants, X-grid fake barrier variants, initial clear-order/model-spill/texture-index carrier/batch-offset microvariants unless paired with a distinct model-spill fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
