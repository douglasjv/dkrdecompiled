# Session Handoff

- Generated at: 2026-05-14 22:34:19Z
- Branch: `master`
- HEAD: `7be437f9`
- Completed task: `DKR-MATCH-FUNC-80049794-PROBE-PASS`
- Summary: `func_80049794` remains active. This pass rejected several ordinary-C allocation probes without parking the function.

## Validation

- `python3 tools/check_active_surface.py` -> active surface ok
- `python3 tools/query_goal_state.py next --compact --refresh` -> recommends `func_80049794`; 4 default candidates, 3 exhausted notes skipped
- `python3 tools/query_goal_state.py next --compact --refresh --include-exhausted` -> shows 7 total candidates when deliberately revisiting exhausted notes
- `gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf-` -> promoted `func_80049794` probes compile
- `./diff.sh -o func_80049794 -s --compress-matching 3 --no-pager` -> ordinary-C probes still score `2550`, nonmatching
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- Plain `gmake -j4` still selects Homebrew `mips-linux-gnu-ld`; keep using `CROSS=tools/binutils/mips64-elf-`.
- `func_80049794` remains active. Target saves `$f21/$f20` at `0x20/0x24(sp)` and uses `$f20` broadly for plane physics float temporaries; current promoted C keeps those values in caller-scratch float registers and does not save `$f20/$f21`.
- Rejected `func_80049794` probes: `register f32 var_f20`, moving `var_f20` declaration, explicit `f64 var_f20_d`, inline clamp casts, `/ 2.0` and `/ 4.0` multiply rewrites, splitting the initial `sqrtf` result into a named local, `register f32 var_f14`, moving `var_f14` into the early local group, `register f32 segmentZVelocity`, direct assignment of the misc-asset interpolation into `var_f14`, delaying the `segmentZVelocity` copy until `handle_racer_top_speed`, and `register` hints on `spEC`/`spD8`/`spD4`/`spD0`. Do not repeat those exact source shapes.
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
- Step: Keep `func_80049794` in the active lane, diagnose the `$f20/$f21` allocation mismatch with `./diff.sh -o func_80049794`, write ordinary C only, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` reports `Verify: OK`. Do not park this function for missed register-allocation probes alone.
