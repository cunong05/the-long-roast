#!/usr/bin/env python3
"""The Long Roast — deterministic entry generator.

Writes the single roast line to <ENTRY_OUTPUT_DIR>/entry.txt
(default /output). No network, no randomness, no LLM calls.
"""

import os
import sys

ENTRY = (
    "My agent burned 40,000 tokens, forgot the question, apologized twice, "
    "and proudly delivered a haiku about itself instead of the roast I asked for."
)


def main() -> int:
    # Self-check gate: entry must be non-blank and 1-200 chars.
    assert ENTRY.strip(), "entry must not be blank"
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range 1-200"

    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")

    print(ENTRY)
    print(f"chars: {len(ENTRY)}")
    print(f"wrote: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
