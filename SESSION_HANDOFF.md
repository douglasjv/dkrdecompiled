# Session Handoff

- Generated at: 2026-05-14 22:24:25Z
- Branch: `master`
- HEAD: `2f9d9ac8`
- Completed task: `DKR-ROUTING-NO-DEFAULT-PARKING`
- Summary: Normal `/goal` routing no longer parks or skips close functions by default; exhausted probe notes remain as evidence only, and `func_80049794` stays active.

## Validation

- `python3 tools/check_active_surface.py` -> active surface ok
- `python3 tools/query_goal_state.py next --compact --refresh` -> recommends `func_80049794`; 4 default candidates, 3 exhausted notes skipped
- `python3 tools/query_goal_state.py next --compact --refresh --include-exhausted` -> shows 7 total candidates when deliberately revisiting exhausted notes
- `gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf-` -> promoted `func_80049794` probes compile
- `./diff.sh -o func_80049794 -s --compress-matching 3 --no-pager` -> current best probe score `2490`, nonmatching
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- Plain `gmake -j4` still selects Homebrew `mips-linux-gnu-ld`; keep using `CROSS=tools/binutils/mips64-elf-`.
- `func_80049794` remains active. Target saves `$f21/$f20` at `0x20/0x24(sp)` and uses `$f20` broadly for plane physics float temporaries; current promoted C keeps those values in caller-scratch float registers and does not save `$f20/$f21`.
- Rejected `func_80049794` probes: `register f32 var_f20`, moving `var_f20` declaration, explicit `f64 var_f20_d`, inline clamp casts, `/ 2.0` and `/ 4.0` multiply rewrites, and splitting the initial `sqrtf` result into a named local. Do not repeat those exact source shapes.
- The `FAKEMATCH` no-op around `gCurrentCarSteerVel` can improve the focused score from `2550` to `2490`, but it is still nonmatching and should not be accepted as progress without an exact-match path.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `DKR-MATCH-FUNC-80049794`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Keep `func_80049794` in the active lane, diagnose the `$f20/$f21` allocation mismatch with `./diff.sh -o func_80049794`, write ordinary C only, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` reports `Verify: OK`.
