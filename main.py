"""One Line, One Laugh: write one funny line to /output/entry.txt.

The entry is a single self-contained funny line. The turn lands in the
last word: a machine that asks for help before the shopper has done
anything wrong, and the shopper taking that personally.
"""

import os

ENTRY = "The self-checkout called for assistance before I'd scanned anything, which felt personal."


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
