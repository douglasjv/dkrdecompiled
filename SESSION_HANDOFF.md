# Session Handoff

- Generated at: 2026-05-24 12:30:08Z
- Branch: `master`
- HEAD: `5140d9ce`
- Completed task: `func_8002B0F4-initial-clear-order`
- Summary: Rejected promoted func_8002B0F4 initial clear-order spelling: changed only initial ordering from D_8011D308 = 0; *arg3 = NULL; to *arg3 = NULL; D_8011D308 = 0. Full verify failed with CRCs 0x281EE857/0x10F947B1; relinked ./diff.sh func_8002B0F4 --compress-matching 2 --no-pager worsened to CURRENT (6088), moving the global clear after stack/save setup and retaining the unwanted early gCurrentLevelModel spill at 0x60(sp) plus broad segment/grid/tail drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_8002B0F4 initial clear-order, model-spill, texture-index carrier, and batch-offset microvariants unless paired with a distinct segment-loop register-family fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
