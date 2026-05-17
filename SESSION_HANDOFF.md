# Session Handoff

- Generated at: 2026-05-17 17:05:01Z
- Branch: `master`
- HEAD: `c043a702`
- Completed task: `func_8008FF1C`
- Summary: Revisited close default-skipped func_8008FF1C with two new selected-track allocator probes: changing `selectedTrack` to `s16`, and then using `register s32 selectedTrack`. Both compiled but missed. The `s16` probe widened the focused diff to CURRENT (1355) with extra sign-extension/register churn; the `register s32` probe produced no movement and stayed CURRENT (10), still using current `v1` instead of target `t2` for the selected-track halfword load/branch. Source restored; final full verify passed. Keep func_8008FF1C parked-by-default but available for a different non-repeated allocator/lifetime hypothesis.

## Validation

- gmake -j4 CROSS=tools/binutils/mips64-elf- => Verify: OK after restore
- Failed probe evidence: `s16 selectedTrack` => ./diff.sh func_8008FF1C --format plain --no-pager --max-size 1200 -U 16 => CURRENT (1355), failed full verify CRCs 0x5B5E4609/0x72935A6E; `register s32 selectedTrack` => CURRENT (10), failed full verify CRCs 0x55C240E7/0x18E4F9B4

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector func_80049794 unless choosing active alternate func_8002B0F4, func_80059208, or trackbg_render_flashy; only revisit default-skipped func_8008FF1C with a new allocator/lifetime idea and avoid the newly recorded func_8008FF1C s16/register selectedTrack probes plus prior temp/selectedTrack probes, the func_80049794 current-baseline wave-threshold-local/chained-zero/wave-bound/save-family probes, func_8002B0F4 pad/early-conversion/loop probes, func_80059208 final-offset variants, and trackbg_render_flashy position/UV order-carrier probes.`
- Packet class: `matching_impl`
- Packet status: `ready`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
