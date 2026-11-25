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


def verify_written(path):
    """Second independent check: re-read what we wrote and re-apply the
    scorer's gate to the bytes on disk, not just to the in-memory string.
    A silent write truncation or encoding slip would otherwise ship an
    entry the gate refuses."""
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")  # raises if the file is not valid UTF-8
    assert text == REVIEW, "written file differs from the review"
    assert text.strip(), "written review must not be blank"
    assert 1 <= len(text) <= 279, f"written review is {len(text)} chars, gate needs 1-279"
    assert "\n" not in text, "written review must be a single line"
    return len(raw)


def main():
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)
    nbytes = verify_written(path)
    print(f"Wrote {len(REVIEW)} characters ({nbytes} bytes) to {path}")


if __name__ == "__main__":
    main()
