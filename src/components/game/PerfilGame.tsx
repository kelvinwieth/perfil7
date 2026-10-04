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
import { describeScore } from "@/lib/scoring";
import type {
  CardItem,
  Category,
  GameCard,
  GameMode,
  Phase,
} from "@/lib/types";

type CategoryFilter = Category | "TODAS";

export function PerfilGame() {
  const [phase, setPhase] = useState<Phase>("home");
  const [category, setCategory] = useState<CategoryFilter>("TODAS");
  const [mode, setMode] = useState<GameMode>("normal");
  const [card, setCard] = useState<GameCard | null>(null);
  const [usedIds, setUsedIds] = useState<Set<string>>(new Set());
  const [revealed, setRevealed] = useState<Set<number>>(new Set());
  const [activeItem, setActiveItem] = useState<CardItem | null>(null);
  const [showAnswer, setShowAnswer] = useState(false);
  const [guessed, setGuessed] = useState(false);
  const [recycled, setRecycled] = useState(false);
  const [bonusLost, setBonusLost] = useState(false);

  useEffect(() => {
    setUsedIds(loadUsedIds());
  }, []);

  const stats = useMemo(
    () => deckStats(category, usedIds),
    [category, usedIds],
  );

  const revealedCount = revealed.size;
  const clueRevealedCount = useMemo(() => {
    if (!card) return 0;
    return card.items.filter((i) => revealed.has(i.n) && i.type === "clue")
      .length;
  }, [card, revealed]);

  function startSetup() {
    setPhase("setup");
  }

  function beginRound() {
    const { card: next, recycled: wasRecycled } = pickCard(category, usedIds);
    setCard(next);
    setRecycled(wasRecycled);
    setRevealed(new Set());
    setActiveItem(null);
    setShowAnswer(false);
    setGuessed(false);
    setBonusLost(false);
    setPhase("pass-mediator");
  }

  function openMediator() {
    setPhase("mediator");
  }

  function startPlaying() {
    setShowAnswer(false);
    setPhase("playing");
  }

  function revealNumber(n: number) {
    if (!card || revealed.has(n)) return;
    if (mode === "bonus") {
      if (bonusLost) return;
      if (revealed.size >= 5) return;
    }
    const item = card.items.find((i) => i.n === n);
    if (!item) return;

    const next = new Set(revealed);
    next.add(n);
    setRevealed(next);
    setActiveItem(item);
    setPhase("clue");

    if (
      mode === "bonus" &&
      item.type === "action" &&
      item.text.toLowerCase().includes("perca sua vez")
    ) {
      setBonusLost(true);
    }
  }

  function closeClue() {
    setActiveItem(null);
    setPhase("playing");
  }

  function markCorrect() {
    if (!card) return;
    setGuessed(true);
    const nextUsed = new Set(usedIds);
    nextUsed.add(card.id);
    setUsedIds(nextUsed);
    saveUsedIds(nextUsed);
    setPhase("round-end");
  }

  function markNobody() {
    if (!card) return;
    const nextUsed = new Set(usedIds);
    nextUsed.add(card.id);
    setUsedIds(nextUsed);
    saveUsedIds(nextUsed);
    setGuessed(false);
    setPhase("round-end");
  }

  function resetDeck() {
    clearUsedIds();
    setUsedIds(new Set());
  }

  const score = describeScore(
    mode,
    mode === "bonus" ? clueRevealedCount || revealedCount : revealedCount,
    guessed && !bonusLost,
  );

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
          mode={mode}
          stats={stats}
          onCategory={setCategory}
          onMode={setMode}
          onBack={() => setPhase("home")}
          onContinue={beginRound}
        />
      )}

      {phase === "pass-mediator" && (
        <PassScreen
          recycled={recycled}
          onContinue={openMediator}
          onBack={() => setPhase("setup")}
        />
      )}

      {phase === "mediator" && card && (
        <MediatorScreen
          card={card}
          mode={mode}
          showAnswer={showAnswer}
          onToggleAnswer={() => setShowAnswer((v) => !v)}
          onStart={startPlaying}
        />
      )}

      {phase === "playing" && card && (
        <PlayingScreen
          card={card}
          mode={mode}
          revealed={revealed}
          bonusLost={bonusLost}
          revealedCount={revealedCount}
          onReveal={revealNumber}
          onCorrect={markCorrect}
          onNobody={markNobody}
          onShowAnswer={() => setShowAnswer(true)}
          showAnswer={showAnswer}
        />
      )}

      {phase === "clue" && card && activeItem && (
        <ClueScreen
          card={card}
          item={activeItem}
          mode={mode}
          bonusLost={bonusLost}
          onContinue={closeClue}
        />
      )}

      {phase === "round-end" && card && (
        <RoundEndScreen
          card={card}
          score={score}
          bonusLost={bonusLost}
          mode={mode}
          onNext={() => {
            setPhase("setup");
          }}
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
          PERFIL
          <span className="brand-seven" aria-label="7">
            7
          </span>
        </h1>
        <p className="home-lead">
          {totalCards} cartas novas no celular. Tabuleiro, peões e fichas
          continuam na mesa — aqui só se lê a cartela em voz alta.
        </p>
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
  mode,
  stats,
  onCategory,
  onMode,
  onBack,
  onContinue,
}: {
  category: CategoryFilter;
  mode: GameMode;
  stats: { total: number; remaining: number; used: number };
  onCategory: (c: CategoryFilter) => void;
  onMode: (m: GameMode) => void;
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

      <div className="setup-block">
        <h3>Modo</h3>
        <div className="mode-row">
          <button
            type="button"
            className={`mode-card ${mode === "normal" ? "mode-active" : ""}`}
            onClick={() => onMode("normal")}
          >
            <strong>Normal</strong>
            <span>Dicas 1–20 · pontuação clássica</span>
          </button>
          <button
            type="button"
            className={`mode-card ${mode === "bonus" ? "mode-active" : ""}`}
            onClick={() => onMode("bonus")}
          >
            <strong>Cartela-bônus</strong>
            <span>Até 5 dicas · 1 palpite · casa “?”</span>
          </button>
        </div>
      </div>

      <Button size="lg" className="cta-primary sticky-cta" onClick={onContinue}>
        Sortear carta
      </Button>
    </section>
  );
}

function PassScreen({
  recycled,
  onContinue,
  onBack,
}: {
  recycled: boolean;
  onContinue: () => void;
  onBack: () => void;
}) {
  return (
    <section className="screen pass-screen">
      <button type="button" className="text-link self-start" onClick={onBack}>
        ← Trocar sorteio
      </button>
      <div className="pass-copy">
        <p className="eyebrow">Próximo passo</p>
        <h2>Passe o celular para o mediador</h2>
        <p>
          Quem for ler a cartela toca em continuar. A resposta fica só na tela
          do mediador — o restante joga no tabuleiro de sempre.
        </p>
        {recycled && (
          <p className="warn-note">
            Esta categoria já girou o baralho — carta repetida pode aparecer.
          </p>
        )}
      </div>
      <Button size="lg" className="cta-primary" onClick={onContinue}>
        Sou o mediador
      </Button>
    </section>
  );
}

function MediatorScreen({
  card,
  mode,
  showAnswer,
  onToggleAnswer,
  onStart,
}: {
  card: GameCard;
  mode: GameMode;
  showAnswer: boolean;
  onToggleAnswer: () => void;
  onStart: () => void;
}) {
  return (
    <section className="screen mediator-screen">
      <p className="eyebrow">Só para o mediador</p>
      <div className={`category-banner ${CATEGORY_META[card.category].tone}`}>
        {categoryPrompt(card)}
      </div>

      <button
        type="button"
        className={`answer-vault ${showAnswer ? "open" : ""}`}
        onClick={onToggleAnswer}
      >
        {showAnswer ? (
          <>
            <span className="vault-label">Resposta</span>
            <strong>{card.answer}</strong>
          </>
        ) : (
          <>
            <span className="vault-label">Toque para ver a resposta</span>
            <strong>••••••••</strong>
          </>
        )}
      </button>

      <ol className="howto">
        <li>Anuncie a categoria e marque a ficha amarela no tabuleiro.</li>
        <li>Quem pedir a dica escolhe um número de 1 a 20.</li>
        <li>Toque no número, leia em voz alta e sigam as regras do tabuleiro.</li>
        {mode === "bonus" && (
          <li>No bônus da casa “?”: até 5 números e um único palpite.</li>
        )}
      </ol>

      <Button size="lg" className="cta-primary" onClick={onStart}>
        Abrir números
      </Button>
    </section>
  );
}

function PlayingScreen({
  card,
  mode,
  revealed,
  bonusLost,
  revealedCount,
  onReveal,
  onCorrect,
  onNobody,
  onShowAnswer,
  showAnswer,
}: {
  card: GameCard;
  mode: GameMode;
  revealed: Set<number>;
  bonusLost: boolean;
  revealedCount: number;
  onReveal: (n: number) => void;
  onCorrect: () => void;
  onNobody: () => void;
  onShowAnswer: () => void;
  showAnswer: boolean;
}) {
  const bonusFull = mode === "bonus" && revealedCount >= 5;

  return (
    <section className="screen playing-screen">
      <header className="play-header">
        <div className={`category-pill ${CATEGORY_META[card.category].tone}`}>
          {card.category}
        </div>
        <div className="play-stats">
          <span>
            {revealedCount}
            {mode === "bonus" ? "/5" : "/20"} abertos
          </span>
          {mode === "normal" && (
            <span className="muted">
              Mediador {revealedCount} · Mesa {20 - revealedCount}
            </span>
          )}
        </div>
      </header>

      {bonusLost && (
        <p className="warn-note">
          Saiu “Perca sua vez” no bônus — a cartela-bônus acaba sem pontuar.
        </p>
      )}

      <div className="number-grid" role="list">
        {card.items.map((item) => {
          const isOpen = revealed.has(item.n);
          const locked =
            bonusLost || (mode === "bonus" && !isOpen && bonusFull);
          return (
            <button
              key={item.n}
              type="button"
              role="listitem"
              className={`num-cell ${isOpen ? "num-open" : ""} ${item.type === "action" && isOpen ? "num-action" : ""}`}
              disabled={isOpen || locked}
              onClick={() => onReveal(item.n)}
            >
              {item.n}
            </button>
          );
        })}
      </div>

      <div className="play-actions">
        {!showAnswer ? (
          <button type="button" className="text-link" onClick={onShowAnswer}>
            Ver resposta (mediador)
          </button>
        ) : (
          <p className="answer-inline">
            Resposta: <strong>{card.answer}</strong>
          </p>
        )}
        <div className="btn-row">
          <Button
            size="lg"
            className="cta-primary"
            onClick={onCorrect}
            disabled={bonusLost || revealedCount === 0}
          >
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

function ClueScreen({
  card,
  item,
  mode,
  bonusLost,
  onContinue,
}: {
  card: GameCard;
  item: CardItem;
  mode: GameMode;
  bonusLost: boolean;
  onContinue: () => void;
}) {
  const isAction = item.type === "action";
  return (
    <section className={`screen clue-screen ${isAction ? "is-action" : ""}`}>
      <p className="eyebrow">
        {card.category} · nº {item.n}
        {isAction ? " · instrução" : " · dica"}
      </p>
      <h2 className="clue-text">{item.text}</h2>
      {mode === "bonus" && bonusLost && (
        <p className="warn-note">Bônus encerrado por “Perca sua vez”.</p>
      )}
      <Button size="lg" className="cta-primary" onClick={onContinue}>
        Continuar
      </Button>
    </section>
  );
}

function RoundEndScreen({
  card,
  score,
  bonusLost,
  mode,
  onNext,
  onHome,
}: {
  card: GameCard;
  score: {
    title: string;
    detail: string;
    guesser: number;
    mediator: number;
  };
  bonusLost: boolean;
  mode: GameMode;
  onNext: () => void;
  onHome: () => void;
}) {
  return (
    <section className="screen end-screen">
      <p className="eyebrow">Fim da rodada</p>
      <h2>{bonusLost && mode === "bonus" ? "Bônus perdido" : score.title}</h2>
      <p className="end-answer">{card.answer}</p>
      <p className="end-detail">
        Lembrete para o tabuleiro: {score.detail}
      </p>
      <p className="end-pass">
        Movam os peões no tabuleiro e passem o celular para a esquerda — o
        próximo jogador será o mediador.
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
