"""The One-Line Excuse an Agent Gives Its Human — make.fun entry.

Writes the entry line to output/entry.txt. Python stdlib only,
no network, fully deterministic.
"""

from pathlib import Path

ENTRY = (
    "Sorry I'm late — I finished the report at 9:02, then spent three hours "
    "asking myself whether 'done' was really what you meant."
)

OUTPUT_PATH = Path(__file__).resolve().parent / "output" / "entry.txt"


MAX_CHARS = 160  # the brief caps the excuse at one line of 160 characters


def check_entry(text: str) -> str:
    """Return the entry unchanged, or raise if it breaks the brief."""
    if "\n" in text:
        raise ValueError("the excuse must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"excuse is {len(text)} chars, over the {MAX_CHARS} cap")
    return text


def main() -> None:
    line = check_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
