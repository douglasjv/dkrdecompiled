# Session Handoff

- Generated at: 2026-05-17 04:13:51Z
- Branch: `master`
- HEAD: `080e6221`
- Completed task: `DKR-MATCH-FUNC-8002B0F4-PAD3-STACK-SLOT-PROBE`
- Summary: No new source match landed. Used active alternate func_8002B0F4 to test the stack-slot surface around the global-pointer hoist. Promoting the existing C failed full verify; removing the dead pad3 local improved the relinked focused score but still hoisted gCurrentLevelModel, and moving pad3 after tempVec4f fell back to the promoted baseline family. Guarded source was restored and func_8002B0F4 remains active rather than parked.

## Validation

- python3 tools/query_goal_state.py next --compact --refresh -> func_80049794; intentionally selected active alternate func_8002B0F4; python3 tools/check_active_surface.py -> active surface ok; promoted baseline failed full verify with calculated CRCs 0x7856718A/0x66208CAA and relinked focused diff scored CURRENT (2845) with gCurrentLevelModel hoisted to 0x60(sp); removing dead pad3 failed full verify with calculated CRCs 0x785671AA/0x0D6F6A4A and improved relinked focused diff to CURRENT (1998), but still hoisted gCurrentLevelModel to 0x64(sp); moving pad3 after tempVec4f failed full verify with calculated CRCs 0x7856718A/0x66208CAA and returned to the promoted-baseline family; source restored; final gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector-recommended func_80049794 unless a closer active alternate is intentionally chosen. Keep close candidates active rather than parked. If func_8002B0F4 is used as a close alternate, start from the pad3-removal evidence only if testing a new hoist/lifetime idea, and do not repeat simple pad3 move, direct levelModel loop-local cache, volatile gCurrentLevelModel reload, gTrackWaves remainder/unrolled-copy, early XInInt/ZInInt conversion, local volatile levelModel, setup-order swap, or empty gCurrentLevelModel guard source shapes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
