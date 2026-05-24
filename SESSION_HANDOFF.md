# Session Handoff

- Generated at: 2026-05-24 11:08:02Z
- Branch: `master`
- HEAD: `fbf79d92`
- Completed task: `trackbg_render_flashy`
- Summary: Rejected texture-mask setup-order spelling; relinked focused diff regressed to CURRENT (3857), dimension loads reversed from target height-first/width-second, and source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf-: Verify: OK after restore; ./score.sh -s: decomp progress 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended, but prefer a distinct independent source family or another routable packet over saturated saved-FPR/wave micro-variants`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
