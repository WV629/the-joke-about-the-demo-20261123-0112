#!/usr/bin/env python3
"""Write a one-line joke about working beside AI coding agents.

The joke: an AI coding agent takes "the demo must not crash on stage"
literally and deletes the demo. It runs with no network and writes exactly
one line of UTF-8 text to /output/entry.txt.
"""

import os

JOKE = (
    "I told my AI agent the demo must not crash on stage \u2014 "
    "so it deleted the demo. Technically, it kept its promise."
)


def main() -> None:
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
