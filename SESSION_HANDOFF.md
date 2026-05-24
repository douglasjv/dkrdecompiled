# Session Handoff

- Generated at: 2026-05-24 04:12:38Z
- Branch: `master`
- HEAD: `41a0763e`
- Completed task: `func_80049794-wave-pointer-carrier`
- Summary: Rejected close save-family decrementing WaterProperties pointer-carrier wave-scan probe: adding a wave pointer local widened the frame to 0x100, failed full verify, and worsened focused diff to CURRENT (8081). Source restored.

## Validation

- Probe full verify failed CRCs 0x9ED4C306/0xE6587C63; focused ./diff.sh func_80049794 --compress-matching 2 --no-pager reported CURRENT (8081). After restore, gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s => 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Pivot away from func_80049794 wave-scan allocation probes for the next packet; use selector candidates to try a bounded distinct hypothesis on func_80059208, trackbg_render_flashy, or func_8002B0F4 unless a new func_80049794 save-pressure hypothesis is materially different from the rejected wave local/pointer families.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
