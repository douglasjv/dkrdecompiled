# Session Handoff

- Generated at: 2026-05-25 03:01:54Z
- Branch: `master`
- HEAD: `5a2c6c7f`
- Completed task: `init_particle_buffers`
- Summary: Promoted point-count lifetime alias probe missed; source restored. Shape: #if 1 plus pointParticleCount assigned after default clamp and used for gMaxPointParticles, vertex alloc, and point buffer alloc. Full verify failed with CRCs 0xC451FA59/0xCE058514; relinked diff CURRENT (2106), frame stayed 0x68 but saved-count registers remained off target (target s1/s3/s7/s4/s8 versus current s3/s1/s7/s2/s4) and colour tag stayed s0 instead of target s2.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- Verify: OK; ./score.sh -s 97.30%; python3 tools/check_active_surface.py active surface ok

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80049794 remains selector-recommended; avoid saturated saved-FPR/wave/pitch families unless a distinct allocation fix is found. Otherwise pivot among live candidates, or revisit a parked target only with a non-repeated hypothesis and compact evidence.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
