"""One Word, First Thought — entry runner.

Writes the single entry word PETRICHOR to entry.txt in the output
directory (MAKEFUN_OUTPUT_DIR, default /output).

End-to-end check: verified by running — entry.txt is UTF-8, 9 code
points ("PETRICHOR"), not whitespace-only, no trailing newline.
"""

import os

WORD = "PETRICHOR"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
