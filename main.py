#!/usr/bin/env python3
"""Snooze Button Roast — writes one roast line to /output/entry.txt.

Deterministic, stdlib only. The roast: an alarm clock that rings at
6 AM on a Saturday, roasted as an overeager employee clocking in for
a shift nobody scheduled — v2 tightened the setup ("had a shift to
clock into" beats "the weekend owed it money") and moved "mate" up
front so the punchline lands in the last few words.
"""

import os

ENTRY = (
    "My alarm clock rang at 6 AM on a Saturday like it had a shift "
    "to clock into \u2014 mate, even the sun sleeps in on weekends."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
