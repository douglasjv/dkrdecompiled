# Session Handoff

- Generated at: 2026-05-25 04:30:41Z
- Branch: `master`
- HEAD: `5bd38951`
- Completed task: `func_8002B0F4`
- Summary: Rejected sp108 <= 0 entry-guard spelling; full verify failed and relinked diff regressed to CURRENT (3060), source restored

## Validation

- Promoted baseline `func_8002B0F4` failed full verify with calculated CRCs
  `0x7856718A/0x66208CAA`; relinked `./diff.sh func_8002B0F4
  --compress-matching 2 --no-pager` reported `CURRENT (2860)`.
- The probe changed only `if (sp108 == 0 || sp108 >= 8)` to
  `if (sp108 <= 0 || sp108 >= 8)`.
- The probe failed full verify with calculated CRCs
  `0xB856718A/0x8DC42D5F`; relinked focused diff regressed to `CURRENT
  (3060)`.
- The probe changed the target entry `beqz v0` into current `blez v0`, retained
  the unwanted early `gCurrentLevelModel` spill at `0x60(sp)`, and
  retained/broadened the segment/grid plus bottom population/sort drift.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat this `sp108 <= 0` entry-guard
  spelling; it moved the entry branch away from target and did not resolve the
  early model-load spill family.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 distinct model-load pressure shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
