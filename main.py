"""One Line, One Laugh — entry program.

Writes a single original one-liner (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Stdlib only; nothing is written inside
the repository, so the grader can run this from a read-only checkout.
"""

import os

LINE = "I asked my password manager for a joke \u2014 it said \u2018incorrect, try again in 30 seconds.\u2019"


def main():
    text = LINE.strip()
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} characters, must be 1-200")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
