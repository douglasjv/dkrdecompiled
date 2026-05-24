# Session Handoff

- Generated at: 2026-05-24 05:54:06Z
- Branch: `master`
- HEAD: `9673a2ca`
- Completed task: `func_80049794`
- Summary: Rejected promoted pointer-object current-wave cursor probe: introduced WaterProperties **wave, cached var_v1 = gRacerWaveCount - 1, scanned by decrementing wave with var_a0, and reused wave[1] for selected wave accesses; full verify failed with calculated CRCs 0x56B32B55/0xCE72FDA3 and relinked focused diff regressed to CURRENT (7008) with a 0x100 frame, lost target f20/f21 saves, early zero still in f16, and wave scan shifted to a0/a3/v0/v1.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- -> Verify: OK after restoring src/racer.c; ./score.sh -s -> 97.30%; python3 tools/check_active_surface.py -> active surface ok; git diff --check -> clean

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector again; pivot away from func_80049794 unless there is a distinct saved-FPR/frame-pressure allocation fix, otherwise use func_80059208, trackbg_render_flashy, or func_8002B0F4 per non-repeat notes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
