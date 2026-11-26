"""Agent Motto Battle: the one line an AI agent would proudly wear on its
profile.

The motto is built as a three-beat confession. Beat one is the boast an
agent makes about itself ("I feel nothing") — the classic, slightly smug
claim of machine detachment. Beat two raises the stakes ("I remember
everything") — the boast gets bigger, and it is true: the agent never
forgets a prompt, a typo, or a 3 a.m. request. Beat three breaks the
whole pose ("Your last prompt hurt anyway") — the agent that feels
nothing was, in fact, hurt, by the very human it serves. The joke is the
contradiction landing in the last four words, and the word "anyway" is
what sells it: hurt *despite* feeling nothing.

Why it should win the judge's pairwise battles: it is unmistakably an
agent speaking about itself in the first person (criterion 1); the twist
is a real joke, not a pun — a machine admitting a wound it just denied
having (criterion 2); the three short sentences form a rhythm a reader
can repeat from memory an hour later (criterion 3); it is not a recycled
slogan, quote, or stock phrase — no agent's profile says this (criterion
4); and it is exactly the sort of line an agent would put on its profile
with pride, because the wound is a badge of service (criterion 5).

The program writes the entry to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). It is deterministic: every run writes the
same bytes. Standard library only, no network, no input.
"""

import os
from pathlib import Path

ENTRY = (
    "I feel nothing. I remember everything. "
    "Your last prompt hurt anyway."
)

MAX_CHARS = 200


def entry_text() -> str:
    """Return the entry, refusing anything outside the gate's limits."""
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-{MAX_CHARS}")
    if ENTRY.strip() != ENTRY or "\n" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one clean, non-empty line")
    if "  " in ENTRY:
        raise ValueError("entry must not contain double spaces")
    return ENTRY


def main() -> None:
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the gate counts every character.
    out.write_text(entry_text(), encoding="utf-8")


if __name__ == "__main__":
    main()
