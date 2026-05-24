# Session Handoff

- Generated at: 2026-05-24 09:26:20Z
- Branch: `master`
- HEAD: `9286fb08`
- Completed task: `func_80049794`
- Summary: Rejected main B-button brake condition-order spelling; promoted func_80049794 and rewrote only the main brake guard as (gCurrentStickY < -40 || racer->velocity < 0.0f) && (gCurrentRacerInput & B_BUTTON). Pre-build diff misleadingly reported CURRENT (0), full verify failed with calculated CRCs 0xF33115D9/0x3A459663, and relinked diff regressed to CURRENT (4150) with the known missing f20/f21 saves, early f16 versus target f14, wave-scan drift, and broader later scheduling. Source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector packet func_80049794 only if using an independent, unrecorded source-shape family; do not repeat main B-button brake guard order.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
