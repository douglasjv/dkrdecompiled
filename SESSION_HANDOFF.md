# Session Handoff

- Generated at: 2026-05-24 09:15:58Z
- Branch: `master`
- HEAD: `8966e63a`
- Completed task: `func_8002B0F4`
- Summary: Rejected early sp108 return guard condition-order spelling; promoted source failed full verify with calculated CRCs 0x7856718E/0xC7219F23 and relinked diff regressed to CURRENT (2930).

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- after restore: Verify: OK; ./score.sh -s: 97.30%; python3 tools/check_active_surface.py: active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector again; prefer an independent func_80049794 family or another routable target. Avoid func_8002B0F4 early sp108 guard-order, sp108 > 7, sp108 <= 0, sp108 split/positive-range guards, and the known gCurrentLevelModel spill micro-variants; also avoid the recent func_80049794 throttle branch, side-force grouping, xRotationOffset denominator, pitch damping, tappedR, and late attach-point guard variants.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
