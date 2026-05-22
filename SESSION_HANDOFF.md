# Session Handoff

- Generated at: 2026-05-22 15:02:46Z
- Branch: `master`
- HEAD: `e80c487a`
- Completed task: `func_80049794`
- Summary: Tested retained-pad var_f2 z/y component-staging plus register var_f14; compiled, relinked focused diff CURRENT (3280), failed CRCs 0x5FEF1D9D/0x4258C5C1, source restored.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => failed for promoted register var_f14 retained-pad var_f2 probe, calculated CRCs 0x5FEF1D9D/0x4258C5C1
- ./diff.sh func_80049794 --format plain --no-pager --max-size 900 -U 80 => relinked CURRENT (3280)
- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run python3 tools/query_goal_state.py next --compact --refresh and continue one active candidate. For func_80049794, avoid the newly recorded retained-pad var_f2 plus register var_f14 probe; it kept the call-adjacent f14 save/reload at 0xdc(sp) but still lacked f20/f21 prologue saves, kept early f16 zero, and left wave a0/v1 drift. For func_80059208, func_8002B0F4, and trackbg_render_flashy, use ACTIVE.md before choosing a probe.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
