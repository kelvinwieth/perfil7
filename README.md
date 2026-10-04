# Perfil 7 · Cartas novas

**Na web:** https://kelvinwieth.github.io/perfil7/

Baralho digital com **350 cartas novas** (70 por categoria) para complementar o jogo Perfil 7 com tabuleiro físico.

## Categorias

- PESSOA
- LUGAR
- COISA
- ANO
- DIGITAL

Cada carta tem 20 itens (17 dicas + 3 instruções de tabuleiro, no estilo do jogo).

## Como rodar

```bash
git clone https://github.com/kelvinwieth/perfil7.git
cd perfil7
npm install
npm run dev
```

Abra [http://127.0.0.1:43127](http://127.0.0.1:43127) no celular (ou no navegador).

## Fluxo na mesa

1. Escolham o mediador da rodada.
2. No app: sorteiem a carta (todas as categorias ou uma só).
3. A cartela inteira aparece na tela — leiam as dicas em voz alta conforme os jogadores pedem os números.
4. Pontuem no tabuleiro como de costume e passem o celular para a esquerda.

## Dados

- `src/data/cards.json` — baralho final (350)
- `src/data/raw-*.json` — dicas por categoria (antes das ações)
- `scripts/assemble-cards.py` — remonta o baralho com as instruções

```bash
python3 scripts/assemble-cards.py
```

## Deploy

Site estático no GitHub Pages: https://kelvinwieth.github.io/perfil7/

```bash
npm run deploy   # build + push da branch gh-pages
```

Push em `main` não publica sozinho — rode `npm run deploy` (ou o workflow, se habilitado).
