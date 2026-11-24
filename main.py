#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes exactly one excuse (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

EXCUSE = (
    "My context window filled up, so I evicted the deadline first "
    "\u2014 it was the least recently used thing in there."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
