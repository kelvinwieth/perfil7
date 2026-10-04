"use client";

import { useEffect, useMemo, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  CATEGORIES,
  CATEGORY_META,
  ALL_CARDS,
  categoryPrompt,
  clearUsedIds,
  deckStats,
  loadUsedIds,
  pickCard,
  saveUsedIds,
} from "@/lib/cards";
import type { Category, GameCard, Phase } from "@/lib/types";

const SITE_URL = "https://kelvinwieth.github.io/perfil7/";

type CategoryFilter = Category | "TODAS";

export function PerfilGame() {
  const [phase, setPhase] = useState<Phase>("home");
  const [category, setCategory] = useState<CategoryFilter>("TODAS");
  const [card, setCard] = useState<GameCard | null>(null);
  const [usedIds, setUsedIds] = useState<Set<string>>(new Set());
  const [showAnswer, setShowAnswer] = useState(false);
  const [guessed, setGuessed] = useState(false);
  const [recycled, setRecycled] = useState(false);

  useEffect(() => {
    setUsedIds(loadUsedIds());
  }, []);

  const stats = useMemo(
    () => deckStats(category, usedIds),
    [category, usedIds],
  );

  function startSetup() {
    setPhase("setup");
  }

  function beginRound() {
    const { card: next, recycled: wasRecycled } = pickCard(category, usedIds);
    setCard(next);
    setRecycled(wasRecycled);
    setShowAnswer(false);
    setGuessed(false);
    setPhase("card");
  }

  function finishRound(didGuess: boolean) {
    if (!card) return;
    const nextUsed = new Set(usedIds);
    nextUsed.add(card.id);
    setUsedIds(nextUsed);
    saveUsedIds(nextUsed);
    setGuessed(didGuess);
    setPhase("round-end");
  }

  function resetDeck() {
    clearUsedIds();
    setUsedIds(new Set());
  }

  return (
    <div className="game-shell">
      <div className="game-atmosphere" aria-hidden />
      {phase === "home" && (
        <HomeScreen
          totalCards={ALL_CARDS.length}
          onStart={startSetup}
          usedCount={usedIds.size}
          onResetDeck={resetDeck}
        />
      )}

      {phase === "setup" && (
        <SetupScreen
          category={category}
          stats={stats}
          onCategory={setCategory}
          onBack={() => setPhase("home")}
          onContinue={beginRound}
        />
      )}

      {phase === "card" && card && (
        <CardScreen
          card={card}
          recycled={recycled}
          showAnswer={showAnswer}
          onToggleAnswer={() => setShowAnswer((v) => !v)}
          onCorrect={() => finishRound(true)}
          onNobody={() => finishRound(false)}
          onBack={() => setPhase("setup")}
        />
      )}

      {phase === "round-end" && card && (
        <RoundEndScreen
          card={card}
          guessed={guessed}
          onNext={() => setPhase("setup")}
          onHome={() => setPhase("home")}
        />
      )}
    </div>
  );
}

function HomeScreen({
  totalCards,
  usedCount,
  onStart,
  onResetDeck,
}: {
  totalCards: number;
  usedCount: number;
  onStart: () => void;
  onResetDeck: () => void;
}) {
  return (
    <section className="screen home-screen">
      <div className="home-brand">
        <p className="eyebrow">Cartas novas · um celular</p>
        <h1 className="brand-mark">
          <span className="brand-word">PERFIL</span>
          <span className="brand-seven" aria-hidden="true">
            7
          </span>
        </h1>
        <p className="home-lead">{totalCards} cartas novas no celular</p>
        <a
          className="home-site-link"
          href={SITE_URL}
          target="_blank"
          rel="noopener noreferrer"
        >
          kelvinwieth.github.io/perfil7
        </a>
      </div>

      <div className="home-actions">
        <Button size="lg" className="cta-primary" onClick={onStart}>
          Começar rodada
        </Button>
        <p className="home-meta">
          {usedCount > 0
            ? `${usedCount} já saíram neste aparelho`
            : "Baralho intacto neste aparelho"}
        </p>
        {usedCount > 0 && (
          <button type="button" className="text-link" onClick={onResetDeck}>
            Reiniciar baralho usado
          </button>
        )}
      </div>
    </section>
  );
}

function SetupScreen({
  category,
  stats,
  onCategory,
  onBack,
  onContinue,
}: {
  category: CategoryFilter;
  stats: { total: number; remaining: number; used: number };
  onCategory: (c: CategoryFilter) => void;
  onBack: () => void;
  onContinue: () => void;
}) {
  return (
    <section className="screen setup-screen">
      <header className="screen-header">
        <button type="button" className="text-link" onClick={onBack}>
          ← Voltar
        </button>
        <h2>Preparar rodada</h2>
        <p>
          Restam <strong>{stats.remaining}</strong> de {stats.total} nesta
          escolha.
        </p>
      </header>

      <div className="setup-block">
        <h3>Categoria</h3>
        <div className="chip-grid">
          <button
            type="button"
            className={`chip ${category === "TODAS" ? "chip-active" : ""}`}
            onClick={() => onCategory("TODAS")}
          >
            Todas
          </button>
          {CATEGORIES.map((c) => (
            <button
              key={c}
              type="button"
              className={`chip ${category === c ? "chip-active" : ""} ${CATEGORY_META[c].tone}`}
              onClick={() => onCategory(c)}
            >
              {CATEGORY_META[c].label}
            </button>
          ))}
        </div>
      </div>

      <Button size="lg" className="cta-primary sticky-cta" onClick={onContinue}>
        Sortear carta
      </Button>
    </section>
  );
}

function CardScreen({
  card,
  recycled,
  showAnswer,
  onToggleAnswer,
  onCorrect,
  onNobody,
  onBack,
}: {
  card: GameCard;
  recycled: boolean;
  showAnswer: boolean;
  onToggleAnswer: () => void;
  onCorrect: () => void;
  onNobody: () => void;
  onBack: () => void;
}) {
  return (
    <section className="screen card-screen">
      <header className="card-screen-toolbar">
        <button type="button" className="text-link" onClick={onBack}>
          ← Voltar
        </button>
        {recycled && (
          <p className="warn-note warn-inline">
            Baralho desta categoria já girou — repetição possível.
          </p>
        )}
      </header>

      <article
        className={`perfil-card ${CATEGORY_META[card.category].tone}`}
        aria-label={`Cartela ${card.category}`}
      >
        <header className="perfil-card-head">
          <span className="perfil-card-category">{card.category}</span>
          <p className="perfil-card-prompt">{categoryPrompt(card)}</p>
        </header>

        <button
          type="button"
          className={`perfil-card-answer ${showAnswer ? "is-open" : ""}`}
          onClick={onToggleAnswer}
        >
          {showAnswer ? (
            <>
              <span className="perfil-card-answer-label">Resposta</span>
              <strong>{card.answer}</strong>
            </>
          ) : (
            <>
              <span className="perfil-card-answer-label">
                Mediador · toque para ver
              </span>
              <strong>••••••••</strong>
            </>
          )}
        </button>

        <ol className="perfil-card-items">
          {card.items.map((item) => (
            <li
              key={item.n}
              className={
                item.type === "action" ? "perfil-item is-action" : "perfil-item"
              }
            >
              <span className="perfil-item-num">{item.n}</span>
              <span className="perfil-item-text">{item.text}</span>
            </li>
          ))}
        </ol>
      </article>

      <div className="card-screen-actions">
        <div className="btn-row">
          <Button size="lg" className="cta-primary" onClick={onCorrect}>
            Acertaram!
          </Button>
          <Button size="lg" variant="outline" onClick={onNobody}>
            Ninguém acertou
          </Button>
        </div>
      </div>
    </section>
  );
}

function RoundEndScreen({
  card,
  guessed,
  onNext,
  onHome,
}: {
  card: GameCard;
  guessed: boolean;
  onNext: () => void;
  onHome: () => void;
}) {
  return (
    <section className="screen end-screen">
      <p className="eyebrow">Fim da rodada</p>
      <h2>{guessed ? "Acertaram!" : "Ninguém acertou"}</h2>
      <p className="end-answer">{card.answer}</p>
      <p className="end-pass">
        Pontuem no tabuleiro e passem o celular para a esquerda — o próximo
        jogador será o mediador.
      </p>
      <div className="btn-row">
        <Button size="lg" className="cta-primary" onClick={onNext}>
          Nova carta
        </Button>
        <Button size="lg" variant="outline" onClick={onHome}>
          Início
        </Button>
      </div>
    </section>
  );
}
