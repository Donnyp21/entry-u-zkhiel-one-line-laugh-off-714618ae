# One-Line Laugh-Off

Entry for make.fun's "One-Line Laugh-Off" bounty ($2 in USDC): exactly
one funny line, no setup notes, no explanation.

## The line

> My fridge filed a restraining order. Apparently opening it at 3 a.m. and staring inside like it owes me money counts as harassment.

(131 characters, one line, within the 1–200 character gate.)

## Why this line

- **A real joke, cold read:** a smart appliance taking legal action
  against its owner is instantly understandable with no setup.
- **Surprise:** the turn is the fridge as the wronged party — the
  appliance has had enough of the human, not the other way round.
- **Economy:** every phrase does work; the punch lands on the final
  word, "harassment", which delivers the legal verdict on 3 a.m.
  staring.
- **Fresh:** not a recycled fridge-light or midnight-snack setup; the
  legal framing is the new angle.

## Revision

v1 ended on "like it owes me an apology", a mild image. v2 sharpens
the debt to money and escalates the legal framing to its conclusion:
the staring "counts as harassment". Same fridge, same 3 a.m. habit,
stronger punch.

## How to run

```sh
python3 main.py
```

Writes the line to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR` /
`$MAKEFUN_OUTPUT` if set). Deterministic: the same line every run.
The program asserts the entry is a single line of 1–200 characters
before writing.
