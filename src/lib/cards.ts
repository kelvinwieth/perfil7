import cardsData from "@/data/cards.json";
import type { Category, GameCard } from "@/lib/types";

export const ALL_CARDS = cardsData as GameCard[];

export const CATEGORIES: Category[] = [
  "PESSOA",
  "LUGAR",
  "COISA",
  "ANO",
  "DIGITAL",
];

export const CATEGORY_META: Record<
  Category,
  { label: string; blurb: string; tone: string }
> = {
  PESSOA: {
    label: "Pessoa",
    blurb: "Gente de verdade, personagens e grupos.",
    tone: "tone-pessoa",
  },
  LUGAR: {
    label: "Lugar",
    blurb: "Cidades, marcos, natureza e ficção.",
    tone: "tone-lugar",
  },
  COISA: {
    label: "Coisa",
    blurb: "Objetos, animais, comidas e ideias.",
    tone: "tone-coisa",
  },
  ANO: {
    label: "Ano",
    blurb: "Datas marcantes da história e da cultura.",
    tone: "tone-ano",
  },
  DIGITAL: {
    label: "Digital",
    blurb: "Apps, redes e o mundo online.",
    tone: "tone-digital",
  },
};

const USED_KEY = "perfil7-used-ids";

export function categoryPrompt(card: GameCard): string {
  if (card.category === "DIGITAL") {
    return "Diga aos jogadores que sou → DIGITAL";
  }
  return `Diga aos jogadores que sou ${card.article} ${card.category}`;
}

export function loadUsedIds(): Set<string> {
  if (typeof window === "undefined") return new Set();
  try {
    const raw = window.localStorage.getItem(USED_KEY);
    if (!raw) return new Set();
    const parsed = JSON.parse(raw) as string[];
    return new Set(parsed);
  } catch {
    return new Set();
  }
}

export function saveUsedIds(ids: Set<string>) {
  if (typeof window === "undefined") return;
  window.localStorage.setItem(USED_KEY, JSON.stringify([...ids]));
}

export function clearUsedIds() {
  if (typeof window === "undefined") return;
  window.localStorage.removeItem(USED_KEY);
}

export function pickCard(
  category: Category | "TODAS",
  usedIds: Set<string>,
): { card: GameCard; recycled: boolean } {
  const pool = ALL_CARDS.filter((c) =>
    category === "TODAS" ? true : c.category === category,
  );
  const fresh = pool.filter((c) => !usedIds.has(c.id));
  if (fresh.length > 0) {
    const card = fresh[Math.floor(Math.random() * fresh.length)]!;
    return { card, recycled: false };
  }
  const card = pool[Math.floor(Math.random() * pool.length)]!;
  return { card, recycled: true };
}

export function deckStats(category: Category | "TODAS", usedIds: Set<string>) {
  const pool = ALL_CARDS.filter((c) =>
    category === "TODAS" ? true : c.category === category,
  );
  const remaining = pool.filter((c) => !usedIds.has(c.id)).length;
  return { total: pool.length, remaining, used: pool.length - remaining };
}
