# Session Handoff

- Generated at: 2026-05-14
- Branch: `master`
- Completed task: `DKR-CONTROL-PLANE-BOOTSTRAP`
- Summary: Initial `/goal`-driven control plane for DKR N64 matching work;
  setup/extract completed and matching build verified with repo-local binutils.

## Validation

- Active surface check: `python3 tools/check_active_surface.py`
- Selector: `python3 tools/query_goal_state.py next --compact --refresh`
- Setup: `gmake setup`
- Extract: `gmake extract`
- Canonical matching gate: `gmake -j4 CROSS=tools/binutils/mips64-elf-`
- Result: `Verify: OK`

## Blockers Or Unknowns

- Plain `gmake -j4` selects Homebrew `mips-linux-gnu-ld` and fails linking
  `build/src/objects.c.o` with an invalid `.strtab` offset. Use
  `CROSS=tools/binutils/mips64-elf-`.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff
  evidence.

## Next Work Packet

- Task: `DKR-FIRST-MATCHING-PACKET`
- Packet class: `matching_impl`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, then
  use the selected source-backed `GLOBAL_ASM`, `NON_MATCHING`, or
  `NON_EQUIVALENT` target. Use `./diff.sh <function>` for focused drift and
  accept only when `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the
  matching ROM.
