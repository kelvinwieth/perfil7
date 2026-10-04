import type { GameMode } from "@/lib/types";

/** Pontos do mediador = dicas reveladas (ações também contam como número escolhido). */
export function scoreNormal(revealedCount: number) {
  const mediator = Math.min(20, Math.max(0, revealedCount));
  const guesser = 20 - mediator;
  return { mediator, guesser };
}

/** Tabela da cartela-bônus do manual. */
export function scoreBonus(tipCount: number) {
  const table: Record<number, number> = {
    1: 10,
    2: 8,
    3: 6,
    4: 4,
    5: 2,
  };
  return table[tipCount] ?? 0;
}

export function describeScore(
  mode: GameMode,
  revealedCount: number,
  guessed: boolean,
) {
  if (mode === "bonus") {
    if (!guessed) {
      return {
        title: "Bônus sem acerto",
        detail: "Ninguém pontua nesta cartela-bônus.",
        guesser: 0,
        mediator: 0,
      };
    }
    const guesser = scoreBonus(revealedCount);
    return {
      title: "Bônus acertado!",
      detail: `Com ${revealedCount} dica${revealedCount === 1 ? "" : "s"}, avance ${guesser} casa${guesser === 1 ? "" : "s"}.`,
      guesser,
      mediator: 0,
    };
  }

  if (!guessed) {
    return {
      title: "Ninguém acertou",
      detail: "O mediador leva as 20 casas.",
      guesser: 0,
      mediator: 20,
    };
  }

  const { mediator, guesser } = scoreNormal(revealedCount);
  return {
    title: "Resposta certa!",
    detail: `Mediador +${mediator} · Quem acertou +${guesser}`,
    guesser,
    mediator,
  };
}
