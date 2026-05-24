# Session Handoff

- Generated at: 2026-05-24 12:54:29Z
- Branch: `master`
- HEAD: `3427ba22`
- Completed task: `func_80059208-lap-reset-guard-commute`
- Summary: Rejected promoted func_80059208 early lap-reset guard commute: changed the NON_MATCHING guard to #if 1 and rewrote only if ((level_id() == 0) && (racer->nextCheckpoint >= temp_v0)) as if ((racer->nextCheckpoint >= temp_v0) && (level_id() == 0)). Full verify failed with calculated CRCs 0x8A644220/0xBE221594; relinked ./diff.sh func_80059208 --compress-matching 2 --no-pager regressed to CURRENT (1585), moving the level_id() call after the checkpoint compare and still retaining the final object-dot/checkpoint-dot plus vertical FPR drift. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK after restore; ./score.sh -s remained 97.30%; python3 tools/check_active_surface.py reported active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; avoid func_80059208 early lap-reset guard commute, level_id boolean/nested guard, splineIndex boolean/comparison, pre-fill/fill-loop, normalization, wrong-way counter, final object-dot/checkpoint-dot, and final clamp/vertical-tail microvariants unless paired with a distinct final-tail allocation fix; otherwise choose another bounded routable active packet.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
