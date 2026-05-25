# Session Handoff

- Generated at: 2026-05-25 04:01:57Z
- Branch: `master`
- HEAD: `92f6f6f2`
- Completed task: `func_8002B0F4`
- Summary: Rejected hoisted XInInt/ZInInt call spelling; full verify failed and relinked diff stayed at CURRENT (2860), source restored

## Validation

- Pre-build `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  reported stale `CURRENT (0)`.
- Promoted hoisted `XInInt`/`ZInInt` call probe failed full verify with
  calculated CRCs `0x7856718A/0x66208CAA`.
- Relinked `./diff.sh func_8002B0F4 --compress-matching 2 --no-pager`
  stayed at `CURRENT (2860)`.
- Source was restored and `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. The hoisted integer-coordinate call shape still
  inserted the unwanted early `gCurrentLevelModel` spill at `0x60(sp)`,
  rotated the segment/grid register family, and left bottom population/sort
  drift. Do not repeat this spelling.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_8002B0F4 distinct early model-load pressure shape, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
