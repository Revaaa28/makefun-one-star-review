#!/usr/bin/env python3
"""One-Star Review of Something Essential entry.

Writes a single deadpan one-star review (102 characters) of gravity to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

LINE = (
    "Gravity works fine until you drop your phone face-down on concrete. "
    "Then it works perfectly. One star."
)


def main() -> None:
    # The gate allows 1-160 characters; refuse to write anything longer
    # so a bad edit can never silently produce an invalid entry. The
    # brief also demands one single line, so a newline inside the review
    # is a hard failure too.
    assert 1 <= len(LINE) <= 160, f"line is {len(LINE)} chars, gate is 1-160"
    assert "\n" not in LINE and "\r" not in LINE, "review must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
