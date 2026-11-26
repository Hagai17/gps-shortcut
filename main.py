#!/usr/bin/env python3
"""Entry for make.fun bounty 'The GPS Swears It Was a Shortcut'.

Writes the GPS's one-line excuse to /output/entry.txt (program/v1).
"""

import os

# The excuse, beat by beat: the plea (the map's label makes it a shortcut
# "by definition"), the stakes (feeding time), the clock (two minutes to
# it), and the button, delivered in the GPS's polite instruction voice.
BEATS = [
    "The map called this a drive-through attraction,",
    "and a drive-through is a shortcut by definition.",
    "The lions are fed at four.",
    "It is 3:58.",
    "Please do not be the slowest vehicle here.",
]


def build_entry() -> str:
    return " ".join(BEATS)


def check_gate(entry: str) -> None:
    """Hold the line to the bounty gate: 1-200 chars, one line, not blank."""
    assert 1 <= len(entry) <= 200, f"entry is {len(entry)} chars"
    assert "\n" not in entry, "entry must be a single line"
    assert entry.strip(), "entry must not be only white space"


def main() -> None:
    entry = build_entry()
    check_gate(entry)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
