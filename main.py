#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes one original one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, no timestamps.
"""

from pathlib import Path

JOKE = "My smart fridge judges my midnight snacks out loud, so now I eat standing in the dark like a raccoon with a mortgage."


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
