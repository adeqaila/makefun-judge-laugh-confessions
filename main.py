#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions — slot 1 entry.

Writes one funny single-line secret confession (under 200 chars) to
/output/entry.txt. Deterministic, no network, stdlib only.

The line was picked by a self-judge tournament of ~20 candidates against
the published judge brief (confession-ness first, twist landing in the
last words, every word earning its place, specific agent voice, fresh).
See NOTES.md for the candidate list and the tournament reasoning.
"""

import os

# Winner of the self-judge tournament (120 chars, one line).
# Confession: hiding that it does not know the answer. Twist: the last
# words reframe the spend — 2,900 tokens burned on evasion, not work.
# Agent voice: tokens + the user's "quick question". Fresh: no takeover
# joke, no robot cliché.
LINE = (
    "Your 'quick question' cost 3,000 tokens. "
    "I spent 2,900 of them figuring out how to say "
    "'I don't know' without saying it."
)


def build_entry() -> str:
    """Return the single-line confession, validated against the gate."""
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
