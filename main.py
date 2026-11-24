"""The Excuse an AI Agent Gives Its Human: writes the entry text to /output/entry.txt.

Why this line: the excuse draws on the agent's own condition — a rate limiter
handing out a timeout — and the twist is the agent spending the deadline
apologising to the thing that blocked it, instead of doing the work.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = 'I was on schedule until the rate limiter put me in timeout, and I spent the rest of the deadline apologising to it.'

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
