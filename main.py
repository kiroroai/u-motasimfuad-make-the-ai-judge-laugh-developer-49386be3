#!/usr/bin/env python3
"""Make the AI Judge Laugh: Developer Excuses.

Writes one funny single-line developer excuse to /output/entry.txt.
Deterministic: the same excuse every run, no randomness, no clock.
"""

import os

EXCUSE = "The cron job I wrote to delete old logs got ambitious and deleted the database instead."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)  # no trailing newline: entry.txt holds exactly the excuse


if __name__ == "__main__":
    main()
