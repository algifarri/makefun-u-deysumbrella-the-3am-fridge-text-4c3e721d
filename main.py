#!/usr/bin/env python3
"""Entry for make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes one line (113 characters) to /output/entry.txt: the message a smart
fridge sends its owner at 3am. Deterministic, stdlib-only, no network, no
randomness. The file holds exactly the line, with no trailing newline, so
the gate counts the line's characters alone.
"""

import os

LINE = (
    "3am. Your 2am self just ate the cake your 8pm self was saving "
    "for tomorrow. I have the footage. I am the footage."
)


def main() -> None:
    # The gate accepts 1 to 140 characters; fail loudly instead of
    # shipping a line the judge never sees.
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
