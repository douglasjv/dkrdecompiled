# Session Handoff

- Generated at: 2026-05-14 22:45:08Z
- Branch: `master`
- HEAD: `7be437f9`
- Completed task: `DKR-MATCH-ACTIVE-CANDIDATE-SAMPLING`
- Summary: No new source match landed. This pass added focused evidence for `func_80059208`, `trackbg_render_flashy`, and `func_8002B0F4` without parking any of them.

## Validation

- `python3 tools/check_active_surface.py` -> active surface ok
- `python3 tools/query_goal_state.py next --compact --refresh` -> recommends `func_80049794`; 4 default candidates, 3 exhausted notes skipped
- `gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf-` -> promoted `func_80059208` probes compile
- `./diff.sh -o func_80059208 -s --compress-matching 3 --no-pager` -> best retained source shape still scores `CURRENT (870)`, nonmatching
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` with promoted track probes -> `trackbg_render_flashy` scores `CURRENT (1808)` and `func_8002B0F4` scores `CURRENT (2780)`, both nonmatching
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- Plain `gmake -j4` still selects Homebrew `mips-linux-gnu-ld`; keep using `CROSS=tools/binutils/mips64-elf-`.
- `func_80049794` remains active. Target saves `$f21/$f20` at `0x20/0x24(sp)` and uses `$f20` broadly for plane physics float temporaries; current promoted C keeps those values in caller-scratch float registers and does not save `$f20/$f21`.
- Rejected `func_80049794` probes: `register f32 var_f20`, moving `var_f20` declaration, explicit `f64 var_f20_d`, inline clamp casts, `/ 2.0` and `/ 4.0` multiply rewrites, splitting the initial `sqrtf` result into a named local, `register f32 var_f14`, moving `var_f14` into the early local group, `register f32 segmentZVelocity`, direct assignment of the misc-asset interpolation into `var_f14`, delaying the `segmentZVelocity` copy until `handle_racer_top_speed`, and `register` hints on `spEC`/`spD8`/`spD4`/`spD0`. Do not repeat those exact source shapes.
- The `FAKEMATCH` no-op around `gCurrentCarSteerVel` can improve the focused score from `2550` to `2490`, but it is still nonmatching and should not be accepted as progress without an exact-match path.
- `func_80059208` is close and should stay active. Existing C promotes to `CURRENT (870)`; target keeps the negated `pad2` temporary and adds it to `pad`, while current folds the expression into a subtract. Rejected probes: `pad`/`pad2` reorder, `pad += pad2`, `register f32 pad2`, signed-zero negation, removing `UNUSED`, two-step negation, operand-order swaps, inline `pad2`, and split final assignment.
- `trackbg_render_flashy` promotes but is broader (`CURRENT (1808)`) and starts drifting in position-array setup.
- `func_8002B0F4` promotes but is broader (`CURRENT (2780)`) and starts drifting around `gCurrentLevelModel` hoisting/caching before the grid loops.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `DKR-MATCH-FUNC-80059208`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Try `func_80059208` first because the remaining diff is localized and object-level expected output exists for `racer.c`. Continue ordinary-C lifetime/register-shape probes around the final offset math, avoid the rejected forms above, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` reports `Verify: OK`. Keep `func_80049794`, `trackbg_render_flashy`, and `func_8002B0F4` active rather than parked.
