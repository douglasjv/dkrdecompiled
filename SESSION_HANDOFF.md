# Session Handoff

- Generated at: 2026-05-31 17:44:15Z
- Branch: `master`
- HEAD: `b69edea2`
- Completed task: `discovery-tooling-refresh`
- Summary: Delegated high mechanism discovery for `func_8002B0F4`; worker found no safe source-level packet and recommended cooldown. No source edit was made.

## Validation

- `git status --short --branch` reported `## master...origin/master [ahead 987]` before closeout edits.
- `python3 tools/check_active_surface.py` reported active surface ok.
- `python3 tools/query_goal_state.py next --compact --refresh` reports `recommended_next: discovery`.
- `python3 tools/query_goal_state.py discovery` reports `discovery_next: tooling` and lists the four live cooldown candidates.
- `python3 tools/query_goal_state.py tooling` reports `tooling_next: discovery_packet` and requires complete packet fields before any probe: target, evidence checked, rejected families, mechanism hypothesis, predicted asm movement, stop condition, and reasoning tier.
- `python3 tools/query_goal_state.py tooling` now prints a `template_command` for each blocked live and parked candidate.
- `python3 tools/query_goal_state.py packet --function func_8002B0F4 --template` emits a copy-ready packet skeleton populated with evidence, latest audit, and next-useful notes.
- `python3 -m py_compile tools/query_goal_state.py` passed after the template-mode change.
- `python3 tools/query_goal_state.py packet --function func_8002B0F4` reports `ready_for_probe: false`.
- `python3 tools/query_goal_state.py packet --function func_8008FF1C` reports `ready_for_probe: false`.
- `python3 tools/query_goal_state.py packet --function init_particle_buffers` reports `ready_for_probe: false`.
- `python3 tools/query_goal_state.py packet --function init_particle_buffers --template` emitted a packet skeleton from `research/tasks/PARKED.md`.
- `python3 tools/query_goal_state.py packet --function init_particle_buffers --json` emitted full parked context for the worker.
- Existing completed worker reports were checked: `func_80049794` still has no safe high/xhigh mechanism beyond the close save-family plus wave-allocation gap, and the `func_80059208` ObjectTransform pointer lifetime miss is already recorded in `research/tasks/func_80059208_evidence.md`.
- High worker result for `init_particle_buffers`: no unrejected C lever predicts target counts `s1/s3/s7/s4/s8`, point count in `s8/fp`, line-count arithmetic in `s4`, and allocator colour tag `s2` while keeping frame `0x68`.
- High worker result for `trackbg_render_flashy` recommended probing existing `var_f16` as a long-lived negative-cos carrier through first-ring and two-wide-ring sites.
- Promoted that `trackbg_render_flashy` shape with `gmake -B NON_MATCHING=1 MATCHDEFS='NON_MATCHING=1 AVOID_UB=1' CROSS=tools/binutils/mips64-elf- build/src/tracks.c.o`.
- Focused `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported stale `CURRENT (0)`, but full `gmake -j4 CROSS=tools/binutils/mips64-elf-` failed ROM verify with calculated CRCs `0xD783EB77/0xFFE69FF1`.
- Restored `src/tracks.c` and matching-mode `build/src/tracks.c.o`; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached `Verify: OK`.
- High worker result for `func_8002B0F4`: no unrejected C lever predicts removing the promoted stack-resident model base at `0x60(sp)`, replacing the texture lookup reload from `0x5FE8` with an in-loop global `lui/lw gCurrentLevelModel` pair like target `0x2C020/0x2C024`, and preserving the outer setup global reload around `0x2BDD4/0x2BDD8`.

## Blockers Or Unknowns

- No setup blocker recorded.
- All live sidecar candidates and parked revival candidates are cooldown-routed; saturation means discovery/tooling, not stopping.
- For `func_8002B0F4`, do not repeat promoted-object `CURRENT (0)`, promoted-object-slice refreshes, unsafe `volatile`/accessor/artificial-alias/helper reshaping, or ordinary local/order/carrier spellings. A future packet must remove the stack-resident model base at `0x60(sp)`, replace the `0x5FE8` texture lookup stack reload with an in-loop global `lui/lw gCurrentLevelModel` pair like target `0x2C020/0x2C024`, and preserve the outer setup global reload around `0x2BDD4/0x2BDD8`.
- For `trackbg_render_flashy`, do not trust focused `CURRENT (0)` or repeat ordinary negative-cos temp, inverted primary cos carrier, positive-cos scratch-local, pair-result scratch locals, first-two-store ordering, `var_f16` negative-cos lifetime extension, plain promotion/current-shape, or first-ring `scaledXSin` reuse probes. A future packet must predict initial negative-cos in `$f18` without broad stack-slot/downstream drift and must pass full ROM verify.
- For `func_8008FF1C`, require a mechanism that predicts target `lh t2,0(s1)` plus delay-slot `sw v0,0(s0)`; do not repeat direct-table/common-store/pointer-to-selected-track-cell/temp-carrier variants.
- For `init_particle_buffers`, require a new saved-register allocation mechanism that predicts target counts `s1/s3/s7/s4/s8`, point count in `s8/fp`, first allocation arithmetic using line count in `s4` and point count in `fp`, and colour tag `s2` for every semitrans-grey allocation while frame stays `0x68`; do not repeat register hints, count aliases, triangle-buffer pointer, all-call colour-tag, unused-pad removal, initial-only colour-tag, declaration/local-carrier probes, or focused-`CURRENT (0)` acceptance.
- For `func_80017A18`, require a mechanism predicting target frame `0x120` and bitmask in `s6`; do not repeat dead-local, edge-plane-inline, register-hint, loop-control bitmask, or combined dead-vector/`sum2` accumulator families.
- For `func_80049794` and `func_80059208`, do not trust focused `CURRENT (0)` or reopen without a distinct saved-FPR/wave-allocation or final-tail FPR/load-order mechanism.

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
