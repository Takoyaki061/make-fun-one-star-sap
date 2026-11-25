#!/usr/bin/env python3
"""One Star, Written in Sap.

Writes a single one-line 1-star review, in the voice of a houseplant
reviewing its human owner, to /output/entry.txt.
"""
import os

REVIEW = (
    'You tapped my trunk for "a little syrup" with a drill bit from your '
    "toolbox \u2014 I'm a ficus, not a maple, one star, and the sap you "
    "stole was my entire personality."
)

# The sealed scorer's gate: /output/entry.txt must be UTF-8 text of
# 1 to 279 characters, not only white space. Fail loudly here rather
# than shipping an entry the gate would refuse.
assert REVIEW.strip(), "review must not be blank"
assert 1 <= len(REVIEW) <= 279, f"review is {len(REVIEW)} chars, gate needs 1-279"
assert "\n" not in REVIEW, "review must be a single line"


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"Wrote {len(REVIEW)} characters to {path}")


if __name__ == "__main__":
    main()
