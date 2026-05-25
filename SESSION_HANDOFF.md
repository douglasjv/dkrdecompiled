# Session Handoff

- Generated at: 2026-05-25 04:34:32Z
- Branch: `master`
- HEAD: `34ba7fd1`
- Completed task: `func_80059208`
- Summary: Worker rejected direct-division spline normalization; full verify failed with CRCs 0x78C710DC/0x4AD1E6BB and focused diff regressed to CURRENT (2580), source restored

## Validation

- Forked worker changed only the post-`sqrtf` normalization in `func_80059208`
  from `scale = 1.0f / distance; diffX *= scale; diffZ *= scale;` to
  `diffX = diffX / distance; diffZ = diffZ / distance;`.
- Worker full verify failed with calculated CRCs `0x78C710DC/0x4AD1E6BB`;
  relinked `./diff.sh func_80059208 --compress-matching 2 --no-pager`
  regressed to `CURRENT (2580)`.
- The probe removed the target `lui 0x3f80` reciprocal carrier and target
  `div.s`/`mul.s` normalization shape, emitted direct `div.s` operations,
  shifted later labels by `0x10`, and broadened the known final-tail FPR drift.
- Worker source was restored in its fork; the main checkout remained clean.
- Main checkout `gmake -j4 CROSS=tools/binutils/mips64-elf-` reached
  `Verify: OK`.
- `./score.sh -s` remained 97.30%.
- `python3 tools/check_active_surface.py` reported active surface ok.

## Blockers Or Unknowns

- No open blockers recorded. Do not repeat direct-division normalization; it
  moves away from the target reciprocal/multiply normalization shape.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `func_80059208 splineIndex/splinePos argument-passing or diffX/diffZ temp-lifetime probe, or pivot to another live candidate`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
