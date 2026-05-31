# Session Handoff

- Generated at: 2026-05-31 19:13:00Z
- Branch: `master`
- HEAD: `c6d52763`
- Completed task: `func_80049794-discovery-cooldown`
- Summary: Delegated high mechanism discovery for `func_80049794`; worker found no mechanism-ready source patch beyond saturated saved-FPR/wave-allocation families and recommended cooldown. No source edit was made.

## Validation

- `git status --short --branch` reported `## master...origin/master [ahead 994]` before closeout edits.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next: tooling`.
- `python3 tools/query_goal_state.py tooling` reports `tooling_next: discovery_packet` and requires complete packet fields before any probe: target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier.
- `python3 tools/query_goal_state.py tooling` now prints a `template_command` for each blocked live and parked candidate.
- `python3 tools/query_goal_state.py packet --function func_80049794 --template` emits a copy-ready packet skeleton populated with evidence, latest audit, and next-useful notes.
- High worker result for `func_80049794`: no mechanism-ready source patch. Forced guarded object still lacks `$f20/$f21` saves, uses early zero `$f16`, and keeps wave scan as `v0` count with `a0` high bound and `v1` loop index; target needs `$f21/$f20` saves at `0x20/0x24(sp)`, early zero `$f14`, `v1` high bound, `a0` loop index, and `v0` pointer cursor after `addu`.
- `./diff.sh func_80049794 --compress-matching 2 --no-pager` reported stale `CURRENT (0)`, but forced objdump contradicted it.
- Nonmatching full link did not reach CRC comparison due undefined `drm_vehicle_traction` and `drm_checksum_balloon`; restored matching-mode full gate reached `Verify: OK`.
- `python3 tools/query_goal_state.py packet --function func_80049794` reports `ready_for_probe: false`.
- `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- `./score.sh -s` reports decomp progress `97.30%` and documentation progress `65.47%`.

## Blockers Or Unknowns

- No setup blocker recorded.
- All live sidecar candidates and parked revival candidates are cooldown-routed; saturation means discovery/tooling, not stopping.
- For `func_8002B0F4`, do not repeat promoted-object `CURRENT (0)`, promoted-object-slice refreshes, unsafe `volatile`/accessor/artificial-alias/helper reshaping, or ordinary local/order/carrier spellings. A future packet must remove the stack-resident model base at `0x60(sp)`, replace the `0x5FE8` texture lookup stack reload with an in-loop global `lui/lw gCurrentLevelModel` pair like target `0x2C020/0x2C024`, and preserve the outer setup global reload around `0x2BDD4/0x2BDD8`.
- For `trackbg_render_flashy`, do not trust focused `CURRENT (0)` or repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, pair-result scratch locals, first-two-store ordering, `var_f16` negative-cos lifetime extension, scheduling/lifetime barriers, doubled-cos spelling/literal variants, volatile/alias forcing, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes. A future packet must predict initial negative-cos in `$f18` without broad stack-slot/downstream drift and must pass full ROM verify.
- For `func_8008FF1C`, require a mechanism that predicts target `lh t2,0(s1)` plus delay-slot `sw v0,0(s0)`; do not repeat direct-table/common-store/pointer-to-selected-track-cell/temp-carrier variants.
- For `init_particle_buffers`, require a new saved-register allocation mechanism that predicts target counts `s1/s3/s7/s4/s8`, point count in `s8/fp`, first allocation arithmetic using line count in `s4` and point count in `fp`, and colour tag `s2` for every semitrans-grey allocation while frame stays `0x68`; do not repeat register hints, count aliases, triangle-buffer pointer, all-call colour-tag, unused-pad removal, initial-only colour-tag, declaration/local-carrier probes, or focused-`CURRENT (0)` acceptance.
- For `func_80017A18`, require a mechanism predicting target frame `0x120` and bitmask in `s6`; do not repeat dead-local, edge-plane-inline, register-hint, loop-control bitmask, or combined dead-vector/`sum2` accumulator families.
- For `func_80059208`, do not repeat final-tail temp/order spelling, direct object-dot, object-X-first lifetime, separate negated checkpoint temp, ObjectTransform late-position lifetime, literal/condition staging, vertical alias/literal staging, or promoted-object focused `CURRENT (0)` acceptance without full ROM verify. Require a distinct mechanism predicting the target final-tail FPR/load order.
- For `func_80049794`, do not trust focused `CURRENT (0)` or reopen without a new mechanism that couples the close save-family with non-repeated wave allocation movement.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `discovery/tooling for next mechanism-ready packet`
- Packet class: `routing_tooling`
- Packet status: `no ready source packet`
- Reasoning tier: `high` for delegated mechanism discovery when agents are available
- Step: Run `python3 tools/query_goal_state.py discovery`, `python3 tools/query_goal_state.py tooling`, and targeted `packet --function <candidate> --template` reads to choose one bounded target. Before any source edit or delegation, fill in a complete packet with target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier. Accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` reaches `Verify: OK`.
