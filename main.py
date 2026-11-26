"""Robot Vacuum's Funniest Excuse — make.fun entry (v2).

Writes the winning one-line excuse to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), then reads it back and validates it against
the contest gate before exiting.

Standard library only (os). Deterministic, no network, no reads outside
the repository.
"""

import os

LINE = "I ran over it three times. It is still there. At this point we are roommates."


def validate(text):
    """Assert the contest gate: 1-120 chars, not only whitespace,
    a single line, no leading/trailing space."""
    assert isinstance(text, str), "entry is not text"
    assert 1 <= len(text) <= 120, "entry must be 1-120 characters, got %d" % len(text)
    assert text.strip() != "", "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not start or end with a space"
    return True


validate(LINE)
assert LINE == "I ran over it three times. It is still there. At this point we are roommates."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")

with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(LINE + "\n")

# Read-back check: what is on disk must be exactly the winning line
# plus one trailing newline.
with open(path, "r", encoding="utf-8") as f:
    written = f.read()
assert written == LINE + "\n", "read-back mismatch"
validate(written.rstrip("\n"))
