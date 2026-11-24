"""Dad Joke Showdown: one dad joke, at most 200 characters.

Writes the joke to /output/entry.txt. Python 3.13, standard library only.
"""

import os

JOKE = (
    "I asked my phone for a joke about construction. "
    "It said it's still working on it."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single block of text, no newlines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} chars)")


if __name__ == "__main__":
    main()
