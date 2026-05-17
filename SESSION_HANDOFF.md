# Session Handoff

- Generated at: 2026-05-17 04:17:44Z
- Branch: `master`
- HEAD: `77272f96`
- Completed task: `DKR-MATCH-FUNC-80049794-ZERO-CARRIER-PROBE`
- Summary: No new source match landed. Worked selector-recommended func_80049794 and tested a dedicated early zero-carrier source family aimed at the target early `$f14` zero and missing `$f20/$f21` prologue saves. Promoted baseline still failed full verify and lacked the target float save family. Plain and register zero-carrier spellings both widened the frame to `0x100`, kept the early zero in `$f16`, and failed full verify, so guarded source was restored. `func_80049794` remains active rather than parked.

## Validation

- `python3 tools/query_goal_state.py next --compact --refresh` -> `func_80049794`; `python3 tools/check_active_surface.py` -> active surface ok; promoted baseline failed full verify with calculated CRCs `0x5FDDE03F/0xEF7A0514` and relinked focused diff scored `CURRENT (2430)` under `--max-size 900` / `CURRENT (644)` under `--max-size 120`, still missing `$f20/$f21` saves and using `$f16` for the early zero instead of target `$f14`; plain dedicated `f32 zero` carrier failed full verify with calculated CRCs `0x5FDDDEDF/0x01A99146` and relinked focused diff widened the frame to `0x100` with `CURRENT (944)` under `--max-size 520`; `register f32 zero` carrier produced the same CRCs `0x5FDDDEDF/0x01A99146` and still widened the frame to `0x100` / kept `$f16` for early zero; source restored; final `gmake -j4 CROSS=tools/binutils/mips64-elf-` -> `Verify: OK`

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Keep close candidates active rather than parked. For func_80049794, avoid the dedicated early zero-carrier family from this packet, including plain f32 zero and register f32 zero variants; both widen the frame and do not introduce target $f20/$f21 saves or target early $f14 zero. Also avoid the previously recorded allocation, wave-scan, wave-speed, early-zero, branch, and inverse-gravity source-shape misses. If choosing func_8002B0F4 as a close alternate, use the pad3-removal evidence only for a new hoist/lifetime idea and do not repeat the recorded pad3 move/cache/volatile/copy-loop/setup-order shapes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
