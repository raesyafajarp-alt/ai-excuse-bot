#!/usr/bin/env python3
"""Write the one-line AI excuse to /output/entry.txt."""

import os

ENTRY = "Good news: I found the bug. Bad news: the bug was load-bearing."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
