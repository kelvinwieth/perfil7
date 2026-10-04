#!/usr/bin/env python3
"""Build src/data/raw-lugar.json from clue parts."""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lugar_clues_part1 import CLUES_PART1
from lugar_clues_part2 import CLUES_PART2
from lugar_clues_part3 import CLUES_PART3
from lugar_clues_part4 import CLUES_PART4

ORDER = [
    "CRISTO REDENTOR",
    "PÃO DE AÇÚCAR",
    "CATARATAS DO IGUAÇU",
    "PANTANAL",
    "LENÇÓIS MARANHENSES",
    "FERNANDO DE NORONHA",
    "RIO DE JANEIRO",
    "SÃO PAULO",
    "SALVADOR",
    "BRASÍLIA",
    "RECIFE",
    "CURITIBA",
    "MANAUS",
    "FLORIANÓPOLIS",
    "OURO PRETO",
    "MARACANÃ",
    "COPACABANA",
    "CHAPADA DIAMANTINA",
    "JALAPÃO",
    "BONITO",
    "RIO AMAZONAS",
    "SERRA DA CAPIVARA",
    "BELO HORIZONTE",
    "CHAPADA DOS VEADEIROS",
    "TORRE EIFFEL",
    "ESTÁTUA DA LIBERDADE",
    "GRANDE MURALHA DA CHINA",
    "COLISEU",
    "PIRÂMIDES DE GIZÉ",
    "TAJ MAHAL",
    "MACHU PICCHU",
    "BIG BEN",
    "TORRE DE PISA",
    "PARTENON",
    "STONEHENGE",
    "CATARATAS DO NIÁGARA",
    "GRAND CANYON",
    "EVEREST",
    "DESERTO DO SAARA",
    "ANTÁRTIDA",
    "NOVA YORK",
    "PARIS",
    "LONDRES",
    "TÓQUIO",
    "ROMA",
    "EGITO",
    "JAPÃO",
    "ARGENTINA",
    "PORTUGAL",
    "MARTE",
    "LUA",
    "DISNEYLAND",
    "HOGWARTS",
    "NÁRNIA",
    "ATLÂNTIDA",
    "ASGARD",
    "VENEZA",
    "DUBAI",
    "LAS VEGAS",
    "HOLLYWOOD",
    "VATICANO",
    "ILHA DE PÁSCOA",
    "ILHAS GALÁPAGOS",
    "MONTE KILIMANJARO",
    "ALPES",
    "CARIBE",
    "PETRA",
    "MURO DAS LAMENTAÇÕES",
    "HAVAÍ",
    "SYDNEY",
]

ALL = {**CLUES_PART1, **CLUES_PART2, **CLUES_PART3, **CLUES_PART4}

FORBIDDEN_DASH = ("—", "–")


def validate():
    errors = []
    if len(ORDER) != 70:
        errors.append(f"ORDER length {len(ORDER)}, expected 70")
    if set(ALL.keys()) != set(ORDER):
        missing = set(ORDER) - set(ALL.keys())
        extra = set(ALL.keys()) - set(ORDER)
        if missing:
            errors.append(f"missing clues: {missing}")
        if extra:
            errors.append(f"extra clues: {extra}")
    for answer in ORDER:
        clues = ALL[answer]
        if len(clues) != 17:
            errors.append(f"{answer}: {len(clues)} clues")
        for i, c in enumerate(clues, 1):
            if not c.strip():
                errors.append(f"{answer} clue {i}: empty")
            for d in FORBIDDEN_DASH:
                if d in c:
                    errors.append(f"{answer} clue {i}: forbidden dash")
            if c.strip().upper() == answer:
                errors.append(f"{answer} clue {i}: equals answer")
    return errors


def main():
    errors = validate()
    if errors:
        print("Validation failed:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(1)

    out = [{"answer": a, "clues": ALL[a]} for a in ORDER]
    target = ROOT / "src/data/raw-lugar.json"
    target.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {target} ({len(out)} cards)")


if __name__ == "__main__":
    main()
