# Session Handoff

- Generated at: 2026-05-14 23:29:13Z
- Branch: `master`
- HEAD: `649eeec9`
- Completed task: `DKR-MATCH-FUNC-80049794-SPCC-ZERO-PROBE`
- Summary: No new source match landed. This pass rejected one ordinary-C `func_80049794` early-zero live-range probe while keeping the function active.

## Validation

- `python3 tools/check_active_surface.py` -> active surface ok
- `python3 tools/query_goal_state.py next --compact --refresh` -> recommends `func_80049794`; 4 default candidates, 3 exhausted notes skipped
- `gmake build/src/racer.c.o CROSS=tools/binutils/mips64-elf-` -> promoted `func_80049794` C candidate compiles
- `./diff.sh -o func_80049794 -s --compress-matching 3 --no-pager` -> baseline promoted C remains `CURRENT (2550)`; routing the early grounded-wheel zero through `spCC` also leaves `CURRENT (2550)`, nonmatching
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- Plain `gmake -j4` still selects Homebrew `mips-linux-gnu-ld`; keep using `CROSS=tools/binutils/mips64-elf-`.
- `func_80049794` remains active. Target saves `$f21/$f20` at `0x20/0x24(sp)` and uses `$f20` broadly for plane physics float temporaries; current promoted C keeps those values in caller-scratch float registers and does not save `$f20/$f21`.
- Rejected `func_80049794` probes: `register f32 var_f20`, moving `var_f20` declaration, explicit `f64 var_f20_d`, inline clamp casts, `/ 2.0` and `/ 4.0` multiply rewrites, splitting the initial `sqrtf` result into a named local, `register f32 var_f14`, moving `var_f14` into the early local group, `register f32 segmentZVelocity`, direct assignment of the misc-asset interpolation into `var_f14`, delaying the `segmentZVelocity` copy until `handle_racer_top_speed`, `register` hints on `spEC`/`spD8`/`spD4`/`spD0`, naming `gRacerWaveCount - 1` in `var_v1` before the wave scan, explicitly materializing the early zero through `var_f14` before the grounded wheel reset, moving `spA3 = FALSE` after the inverse-gravity calculation, combining `register f32 var_f20` with `register f32 var_f14`, and routing the early grounded-wheel zero through `spCC`. The wave-scan probe matched the intended `v1/a0` idea locally but worsened the focused score to `CURRENT (5445)` by increasing register pressure and spilling/reshaping `spA2`; the early-zero `var_f14`, `spA3` scheduling, combined register, and `spCC` zero probes compiled but left the score unchanged at `CURRENT (2550)` and did not move the `$f14/$f16` / `$f20` allocation split. Do not repeat those exact source shapes.
- The `FAKEMATCH` no-op around `gCurrentCarSteerVel` can improve the focused score from `2550` to `2490`, but it is still nonmatching and should not be accepted as progress without an exact-match path.
- `func_80059208` is close and should stay active. Existing C promotes to `CURRENT (870)`; target keeps the negated `pad2` temporary and adds it to `pad`, while current folds the expression into a subtract. Rejected probes: `pad`/`pad2` reorder, `pad += pad2`, `register f32 pad2`, signed-zero negation, removing `UNUSED`, two-step negation, operand-order swaps, inline `pad2`, split final assignment, delayed `z_position` load, `register f32 pad`, empty `if (1) {}` barrier near `pad2`, transient `distance` holder, `register f32 distance`, `pad - (-pad2)`, target-dataflow order that computes the checkpoint dot product first, object dot product second, then negates the checkpoint term, positive `pad2` with `diffX = -((pad - pad2) / divisor)`, inlining object position loads in the dot product, inlining only `obj->trans.x_position` while retaining the `distance` z temporary, and routing the checkpoint dot through `pad3` before negating into `pad2`. Positive `pad2` and `pad3` left the score unchanged at `CURRENT (870)`; inline object loads worsened to `CURRENT (1356)`, and inline-X-only worsened to `CURRENT (1826)`.
- `trackbg_render_flashy` promotes but is broader (`CURRENT (1808)`) and starts drifting in position-array setup. Rejected probes: replacing repeated first-four `(xSin * 1280.0f)` terms with `scaledXSin` widened the frame to `0x168` and worsened to `CURRENT (12121)`; reordering the index 5-8 x/z position stores to match the apparent target store sequence worsened to `CURRENT (2551)`.
- `func_8002B0F4` promotes but is broader (`CURRENT (2780)`) and starts drifting around `gCurrentLevelModel` hoisting/caching before the grid loops.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `DKR-MATCH-FUNC-80049794`
- Packet class: `matching_impl`
- Packet status: `active`
- Reasoning tier: `medium`
- Step: Continue with selector-recommended `func_80049794`, but do not repeat the rejected allocation, wave-scan, early-zero, `spA3`, combined-register, or `spCC` zero probes above. Next useful angle is likely not another simple local/register hint; inspect exact current generated assembly around the prologue and first `sqrtf` block to identify a source-shape change that affects allocation without adding wave-scan pressure. `func_80059208` remains a valid close alternate, but do not repeat the rejected final-offset expression/load-order probes above, including inline-X-only or `pad3` checkpoint-dot routing. Accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` reports `Verify: OK`. Keep `func_80049794`, `func_80059208`, `trackbg_render_flashy`, and `func_8002B0F4` active rather than parked.
