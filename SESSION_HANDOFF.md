# Session Handoff

- Generated at: 2026-05-24 04:02:00Z
- Branch: `master`
- HEAD: `cc3ebc64`
- Completed task: `func_80049794-close-save-spinout-split`
- Summary: Rejected close save-family nested spinout-zap condition probe: x/z/y pre-sqrt accumulation, steer no-op, chained zero, removed trailing pads, and nested racer->unk1FE/spinout_timer condition preserved the close-family CRCs but regressed focused diff to CURRENT (4365). Source restored.

## Validation

- Probe full verify failed CRCs 0xB8DD79CD/0xE47454ED; after restore gmake -j4 CROSS=tools/binutils/mips64-elf- reached Verify: OK; ./score.sh -s => 97.30%.

## Blockers Or Unknowns

- No open blockers recorded.

## Ask The User Only If

- The retail baserom or extracted assets are missing.
- A required setup dependency cannot be installed or initialized.
- A behavior question cannot be resolved from code, symbols, or focused diff evidence.

## Next Work Packet

- Task: `Continue selector recommended_next func_80049794 only with a distinct close save-family hypothesis that fixes wave v1/a0 allocation or first-speed/register drift without repeating nested spinout split, wave-bound carriers, or first-speed carrier variants.`
- Packet class: `matching_impl`
- Packet status: `unchanged`
- Reasoning tier: `medium`
- Step: Run `python3 tools/query_goal_state.py next --compact --refresh`, inspect the selected source/asm pair, write ordinary C, diagnose with `./diff.sh <function>`, and accept only after `gmake -j4 CROSS=tools/binutils/mips64-elf-` verifies the matching ROM.
