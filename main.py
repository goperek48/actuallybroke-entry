#!/usr/bin/env python3
"""Drop one line of honest error copy into the output file.

The bounty asks for a single line of text: the message a program should
have shown when it destroyed the user's unsaved work, told straight and
with a laugh in it. This script writes precisely that line to
/output/entry.txt and nothing else.

No input is read, no network is touched, nothing is random. The whole
entry sits in one constant further down, so the file reads top to bottom
in a minute. The scorer wants UTF-8 text of 1 to 200 characters; what we
write is 138 characters, four clipped sentences that end on a jab.
"""

import os
import sys

# The entry itself. What broke is named without hedging: work the user
# never saved, wiped out, with autosave switched off. The opening
# sentences play the eulogy dead straight — the work was beautiful, it is
# gone for good — and then the final clause hands the fault back to the
# person reading the dialog, who left the safety net off themselves. That
# reversal is the laugh, and it is short enough to be quoted verbatim.
ENTRY = "ERROR: Your unsaved work has been deleted. It was beautiful. You will never see it again. Autosave was off \u2014 and so, apparently, were you."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
