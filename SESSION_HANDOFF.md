# Session Handoff

- Generated at: 2026-05-31
- Branch: `master`
- HEAD: `b9b4058f`
- Completed task: `trackbg_render_flashy`
- Summary: Worker rejected plain promoted-current `trackbg_render_flashy` baseline; source restored.

## Validation

- Worker promoted the existing guarded `trackbg_render_flashy` C body with the
  current `scaledXSin`/`scaledXCos` first-ring shape intact. Full verify failed
  with CRCs `0x93D338FF/0x03D9C8FE`; relinked
  `./diff.sh trackbg_render_flashy --compress-matching 2 --no-pager` reported
  `CURRENT (1808)`.
- Key drift remained the early first-ring FPR allocation: target emits
  `neg.s $f18,$f12`, while promoted C carries the negative-cos value in
  current `$f16` and drifts in the two-wide ring setup around `0x28d5c`.
- Worker restored source and restored validation reached `Verify: OK`.

## Blockers Or Unknowns

- No setup blockers recorded. Do not repeat plain `trackbg_render_flashy`
  guarded-C promotion/current-shape probes, commuted `zPositions[3]`, or
  first-ring `scaledXSin` reuse. Evidence is in
  `research/tasks/trackbg_render_flashy_evidence.md`.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `pivot to another bounded live candidate or run discovery/tooling; func_80049794 is saturated, func_80059208 final-tail spelling-only probes are cooling down, and trackbg_render_flashy plain/current first-ring probes are cooling down`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
