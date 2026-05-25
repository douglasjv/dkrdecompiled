# Session Handoff

- Generated at: 2026-05-25 04:42:35Z
- Branch: `master`
- HEAD: `90fa9d0f`
- Completed task: `func_80059208`
- Summary: Rejected func_80059208 s8 splineIndex carrier and worker-rejected func_80049794 updateRateF-through-var_f20 carrier; both restored.

## Validation

- `func_80059208`: promoted guard and changed only `s32 splineIndex` to
  `s8 splineIndex`. Relinked `./diff.sh func_80059208 --compress-matching 2
  --no-pager` stayed `CURRENT (870)`. Full verify failed with calculated CRCs
  `0x53D141DF/0xB9D4B481`; final-tail FPR drift around `0x5a260` remained.
- Worker `func_80049794`: promoted guard and routed opening update-rate scaling
  through `var_f20`. Full verify failed with calculated CRCs
  `0xF2024655/0xB090BDA2`; relinked focused diff regressed to
  `CURRENT (8849)` and still lacked target `$f20/$f21` prologue saves.
- Both source probes were restored.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat `func_80059208` `s8 splineIndex`
  or `func_80049794` `updateRateF` through `var_f20`.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 distinct spline-call argument or diffX/diffZ lifetime probe, or pivot to another live candidate; avoid s8 splineIndex carrier and func_80049794 updateRateF-through-var_f20 carrier`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
