# Session Handoff

- Generated at: 2026-05-24 09:19:35Z
- Branch: `master`
- HEAD: `99f79b4f`
- Completed task: `func_80049794`
- Summary: Rejected low-boost fallback condition-order spelling; promoted source failed full verify with calculated CRCs 0x105BE9DA/0x11DA74B9 and relinked diff stayed at CURRENT (2760).

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK; ./score.sh -s: 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector again; prefer an independent func_80049794 family or another routable target. Avoid func_80049794 low-boost fallback condition order, throttle branch, side-force grouping, xRotationOffset denominator, pitch damping, tappedR, late attach-point guard, saved-FPR/wave-scan micro-variants, and gravity/boost-emitter variants already recorded.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
