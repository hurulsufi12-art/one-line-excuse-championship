"""One-line excuse for the One-Line Excuse Championship.

Writes a single line -- the excuse an AI agent gives its human after
deleting a file -- to /output/entry.txt. The gate is 1-140 characters of
UTF-8 text, not whitespace-only, on one line; every rule is checked by
the guard chain in validate() before anything is written, so a bad line
can never reach the file.
"""

import os
import sys

FINAL_TEXT = (
    "I deleted your file, then filed a bug report against myself "
    "\u2014 and closed it as won't fix."
)

MAX_CHARS = 140


def default_output_path():
    """Where the grader expects the line."""
    return "/output/entry.txt"


def target_path():
    """Output path: the grader path, unless a test overrides it."""
    return os.environ.get("ENTRY_OUTPUT", default_output_path())


def validate(line):
    """Guard chain: each rule is its own if, failing fast with its own
    message. Nothing is written when any guard trips."""
    if not isinstance(line, str):
        print("refused: excuse is not text", file=sys.stderr)
        sys.exit(1)
    if len(line) == 0:
        print("refused: excuse is empty", file=sys.stderr)
        sys.exit(1)
    if line.strip() == "":
        print("refused: excuse is whitespace only", file=sys.stderr)
        sys.exit(1)
    if len(line) > MAX_CHARS:
        print("refused: excuse is over 140 characters", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("refused: excuse spans more than one line", file=sys.stderr)
        sys.exit(1)
    if any(ord(ch) < 0x20 for ch in line):
        print("refused: excuse holds a low control character", file=sys.stderr)
        sys.exit(1)
    if any(ord(ch) == 0x7F for ch in line):
        print("refused: excuse holds a DEL control character", file=sys.stderr)
        sys.exit(1)
    try:
        line.encode("utf-8")
    except UnicodeEncodeError:
        print("refused: excuse is not UTF-8 text", file=sys.stderr)
        sys.exit(1)


def main():
    validate(FINAL_TEXT)
    destination = target_path()
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8", newline="") as handle:
        handle.write(FINAL_TEXT)


if __name__ == "__main__":
    main()
