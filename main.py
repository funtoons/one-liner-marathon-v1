#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one original one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, no timestamps.
"""

from pathlib import Path

# The joke: exactly one line, 117 characters, no trailing newline.
# Kept as a single literal so the output is fixed by construction.
JOKE = "My smart fridge judges my midnight snacks out loud, so now I eat standing in the dark like a raccoon with a mortgage."

OUTPUT = Path("/output/entry.txt")


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
