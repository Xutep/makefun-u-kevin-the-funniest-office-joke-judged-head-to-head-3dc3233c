#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one single-line joke about office life to /output/entry.txt.

The joke: a setup everyone who has worked in an office recognises
(the boss's "my door is always open" line), a turn the reader does
not see coming (walking in to ask for a raise), and the punchline
last (the door was open, but the budget was closed).
"""

import os

JOKE = (
    "My boss said his door is always open, so I walked in and asked "
    "for a raise \u2014 the door was open, but the budget was closed."
)


def main() -> None:
    text = JOKE.strip()
    if not text:
        raise SystemExit("joke must not be empty")
    if len(text) > 200:
        raise SystemExit(f"joke is {len(text)} characters, over the 200 limit")
    if "\n" in text:
        raise SystemExit("joke must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    # Read back and re-check, so what the judge receives is exactly
    # what was validated above (same 1-200 character, single-line gate).
    with open("/output/entry.txt", "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != text:
        raise SystemExit("entry.txt on disk does not match the joke")


if __name__ == "__main__":
    main()
