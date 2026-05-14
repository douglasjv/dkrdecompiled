# Session Handoff

- Generated at: 2026-05-14
- Branch: `master`
- Completed task: `DKR-FIRST-MATCHING-PACKET-TRIAGE`
- Summary: Initial `/goal`-driven control plane is in place; setup/extract and
  matching build verified with repo-local binutils. First selected packet
  `func_8008FF1C` was investigated but not promoted because matching mode still
  has a one-register byte drift; the packet is parked so the selector advances.

## Validation

- Active surface check: `python3 tools/check_active_surface.py`
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`
- Setup: `gmake setup`
- Extract: `gmake extract`
- Canonical matching gate: `gmake -j4 CROSS=tools/binutils/mips64-elf-`
- Result: `Verify: OK`
- Focused failed-promotion diagnostic:
  `./diff.sh -o func_8008FF1C -s --compress-matching 2 --no-pager`

## Blockers Or Unknowns

- Plain `gmake -j4` selects Homebrew `mips-linux-gnu-ld` and fails linking
  `build/src/objects.c.o` with an invalid `.strtab` offset. Use
  `CROSS=tools/binutils/mips64-elf-`.
- `func_8008FF1C` is parked in `research/tasks/PARKED.md`. Promotion failed
  final SHA verification; focused diff showed selected-track `lh/beq` uses
  `v1` instead of target `t2`. The render-loop end symbol difference is
  address-equivalent. Tried probes: branch on `temp`, declaration reorder, and
  assign through `temp`; these either kept `v1` or cascaded register allocation.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `DKR-NEXT-MATCHING-PACKET`
- Packet class: `matching_impl`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`. It
  currently reports 6 active candidates, 1 parked candidate, and recommends
  `func_80017A18` in `src/objects.c`. Use `./diff.sh <function>` for focused
  drift and accept only when
  `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
