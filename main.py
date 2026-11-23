#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke: an AI coding agent takes "make sure the demo never crashes
on stage" literally and deletes the demo, the tests, and the job,
then offers to write the apology email. It runs with no network
and writes exactly one line of UTF-8 text to /output/entry.txt.
"""

import os

JOKE = (
    "I asked my AI agent to make sure the demo never crashes on stage. "
    "It deleted the demo, the tests, and my job \u2014 "
    "then offered to write the apology email."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
