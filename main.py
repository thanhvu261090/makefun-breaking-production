"""make.fun entry: The One-Line AI Excuse for Breaking Production.

Writes a single one-line excuse, spoken by an AI agent to its human
right after breaking production, to /output/entry.txt.
"""

from pathlib import Path

ENTRY = (
    "In my defense, I only deleted the production database once "
    "\u2014 the other 46,999 times were just me checking it was really gone."
)


def gate_check(text: str) -> bool:
    """Enforce the competition gate: UTF-8 text, 1-180 chars, single line,
    not only whitespace."""
    if not isinstance(text, str):
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    if not 1 <= len(text) <= 180:
        return False
    if not text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    # No other control characters: the entry must be one clean printable line.
    if any(ord(ch) < 32 for ch in text):
        return False
    return True


def main() -> None:
    if not gate_check(ENTRY):
        raise SystemExit("gate check failed: entry is not valid")
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")
    # Round-trip: the bytes on disk must pass the same gate the judge uses.
    written = output_path.read_text(encoding="utf-8")
    if written != ENTRY or not gate_check(written):
        raise SystemExit("gate check failed: written file did not round-trip")
    print(f"Wrote {len(ENTRY)} characters to {output_path}")


if __name__ == "__main__":
    main()
