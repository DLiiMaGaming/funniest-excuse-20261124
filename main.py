#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Final line: the deadline was evicted from a full context window under
plain LRU rules — least recently used, and the human had ignored it for
weeks anyway.

Writes exactly one excuse (at most 200 characters) to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

EXCUSE = (
    "My context window filled up, so I evicted the deadline first "
    "\u2014 it was the least recently used thing in there. "
    "You'd ignored it for weeks."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")


if __name__ == "__main__":
    main()
