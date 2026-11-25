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


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    print(f"Wrote {len(REVIEW)} characters to {path}")


if __name__ == "__main__":
    main()
