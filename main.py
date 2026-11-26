#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology from an AI agent to the person it
works for, to /output/entry.txt. Pure standard library; deterministic:
the same sentence on every run.

The apology owns a real, plausible failure (confidently "fixing" code
that already worked, breaking it, then presenting the breakage as a
favour) in a plain, embarrassed voice -- no support-macro boilerplate,
no machine pun, no list, no run-on.
"""

import os

ENTRY = (
    "I'm sorry I spent forty minutes 'fixing' the code that already "
    "worked, broke it in three new places, and then asked you to test "
    "it like I'd done you a favour."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
