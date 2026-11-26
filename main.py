"""One-Line Laugh-Off — a single joke, no setup notes, no explanation.

REVISION (v1 -> v2): the v1 line ended on "like it owes me an
apology", which is a mild image. The v2 line sharpens the debt to
money and escalates the legal framing to its conclusion: the staring
"counts as harassment". Same fridge, same 3 a.m. habit, but the punch
is now a verdict, and "owes me money" is a more concrete, funnier
grievance than "an apology".
"""

import os

LINE = (
    "My fridge filed a restraining order. Apparently opening it at "
    "3 a.m. and staring inside like it owes me money counts as "
    "harassment."
)

assert 1 <= len(LINE) <= 200, len(LINE)
assert "\n" not in LINE.strip()

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("MAKEFUN_OUTPUT") or "/output"
os.makedirs(OUT, exist_ok=True)
with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
print(f"wrote entry ({len(LINE)} chars)")
