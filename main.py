"""The Internet in One Word entry for make.fun competition
u-ronigrv-the-internet-in-one-word-e388f33b.

Writes exactly one word — "feral" — to entry.txt, nothing else.
"""

import os

WORD = "feral"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == WORD, "entry.txt does not match WORD exactly"
    assert 1 <= len(written) <= 30, "entry.txt must be 1-30 characters"
    assert "\n" not in written, "entry.txt must contain no newline"
    assert " " not in written, "entry.txt must be a single word, no spaces"
    assert written.strip(), "entry.txt must not be only whitespace"
    print(WORD)


if __name__ == "__main__":
    main()
