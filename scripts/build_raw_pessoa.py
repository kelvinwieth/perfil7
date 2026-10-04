#!/usr/bin/env python3
"""Assemble raw-pessoa.json from rewrite parts."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from pessoa_cards_part1 import PART1
from pessoa_cards_part2 import PART2
from pessoa_cards_part3 import PART3

OUT = ROOT / "src/data/raw-pessoa.json"


def main() -> None:
    cards = PART1 + PART2 + PART3
    if len(cards) != 70:
        raise SystemExit(f"Expected 70 entries, got {len(cards)}")
    for i, card in enumerate(cards, 1):
        clues = card.get("clues", [])
        if len(clues) != 17:
            raise SystemExit(
                f"Entry {i} ({card.get('answer')!r}): expected 17 clues, got {len(clues)}"
            )
        if not card.get("answer"):
            raise SystemExit(f"Entry {i}: missing answer")

    with OUT.open("w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {OUT} ({len(cards)} cards)")


if __name__ == "__main__":
    main()
