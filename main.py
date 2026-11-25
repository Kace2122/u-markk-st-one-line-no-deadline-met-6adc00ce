#!/usr/bin/env python3
"""One Line, No Deadline Met — make.fun harness program (v1).

Writes exactly one line — a single-sentence joke excusing a missed
deadline — to /output/entry.txt. Deterministic: the same line every run.
"""

import os

ENTRY_LINE = (
    "My calendar reminded me about the deadline, but it did so with "
    "the confidence of a man who has never met my Wi-Fi."
)


def main() -> None:
    # Gate self-check: one line, 1-200 chars, not only whitespace.
    assert 1 <= len(ENTRY_LINE) <= 200 and ENTRY_LINE.strip(), "entry fails gate"
    assert "\n" not in ENTRY_LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE + "\n")


if __name__ == "__main__":
    main()
