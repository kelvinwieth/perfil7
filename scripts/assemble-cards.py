#!/usr/bin/env python3
"""Assemble raw category JSON into the final 350-card deck with board actions."""

from __future__ import annotations

import json
import random
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "src" / "data"

ACTIONS = [
    "Perca sua vez",
    "Avance 1 casa",
    "Avance 2 casas",
    "Avance 3 casas",
    "Volte 1 casa",
    "Volte 2 casas",
    "Volte 3 casas",
    "Escolha 1 jogador para avançar 1 casa",
    "Escolha 1 jogador para avançar 2 casas",
    "Escolha 1 jogador para avançar 3 casas",
    "Escolha 1 jogador para voltar 1 casa",
    "Escolha 1 jogador para voltar 2 casas",
    "Escolha 1 jogador para voltar 3 casas",
    "Um palpite a qualquer hora",
]

CATEGORIES = {
    "pessoa": ("PESSOA", "uma"),
    "lugar": ("LUGAR", "um"),
    "coisa": ("COISA", "uma"),
    "ano": ("ANO", "um"),
    "digital": ("DIGITAL", None),
}


def main() -> None:
    rng = random.Random(7)
    cards = []

    for key, (cat, article) in CATEGORIES.items():
        raw = json.loads((DATA / f"raw-{key}.json").read_text(encoding="utf-8"))
        assert len(raw) == 70, key
        for i, entry in enumerate(raw, 1):
            clues = list(entry["clues"])
            assert len(clues) == 17, (key, entry["answer"], len(clues))
            action_positions = sorted(rng.sample(range(20), 3))
            action_texts = rng.sample(ACTIONS, 3)
            items = []
            clue_i = 0
            action_i = 0
            for n in range(1, 21):
                if (n - 1) in action_positions:
                    items.append(
                        {"n": n, "type": "action", "text": action_texts[action_i]}
                    )
                    action_i += 1
                else:
                    items.append({"n": n, "type": "clue", "text": clues[clue_i]})
                    clue_i += 1
            assert clue_i == 17 and action_i == 3
            cards.append(
                {
                    "id": f"{cat.lower()}-{i:03d}",
                    "category": cat,
                    "article": article,
                    "answer": entry["answer"].strip().upper(),
                    "items": items,
                }
            )

    assert len(cards) == 350
    for cat in {c["category"] for c in cards}:
        answers = [c["answer"] for c in cards if c["category"] == cat]
        dups = [a for a, n in Counter(answers).items() if n > 1]
        assert not dups, (cat, dups)

    out = DATA / "cards.json"
    out.write_text(json.dumps(cards, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(cards)} cards -> {out}")
    print(dict(Counter(c["category"] for c in cards)))


if __name__ == "__main__":
    main()
