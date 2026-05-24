# Session Handoff

- Generated at: 2026-05-24 03:42:59Z
- Branch: `master`
- HEAD: `a64711ee`
- Completed task: `func_80049794-ternary-wrap-and-trackbg-uv-scale`
- Summary: Rejected func_80049794 zipper wrap ternary promotion and trackbg_render_flashy UV scale commute probes; both failed full ROM verify, sources restored, baseline Verify: OK.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- (Verify: OK after restore); ./score.sh -s => 97.30%

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Run selector; func_80049794 remains recommended, but do not repeat direct guard removal/object-only CURRENT(0), zipper wrap ternary reassignment promotion, or trackbg_render_flashy UV scroll scale division-commute spelling without a distinct save-pressure/FPR allocation hypothesis.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
