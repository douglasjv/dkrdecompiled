# Session Handoff

- Generated at: 2026-05-23 09:15:41Z
- Branch: `master`
- HEAD: `d411bde7`
- Completed task: `func_8002B0F4`
- Summary: Rejected partial bottom default-water store-order probe; promoting source with default writes ordered rot.x, waveHeight, rot.z, rot.y failed verify with CRCs 0x281EE85B/0x4ACE73BF and relinked focused diff regressed to CURRENT (3835), then source was restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after source restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; default route remains func_80049794, but consider another active alternate if no fresh func_80049794 hypothesis exists beyond saturated CURRENT (2760) family. For func_8002B0F4, do not repeat partial bottom default-water store-order, explicit default-water height-cast, target default-water store-order, bottom-water condition-order, bottom segment-range guard reorder, current-source texture-index carriers, grid bitmask rewrites, outer segment-loop while, or other recorded model-spill/tail spellings in ACTIVE.md.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
