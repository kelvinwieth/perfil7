# Perfil 7 · Cartas novas

Baralho digital com **350 cartas novas** (70 por categoria) para jogar Perfil 7 com o **tabuleiro físico**.

O celular só substitui as cartelas: o mediador anuncia a categoria, abre os números pedidos e lê as dicas em voz alta. Peões, fichas e pontuação ficam no tabuleiro.

## Categorias

- PESSOA
- LUGAR
- COISA
- ANO
- DIGITAL

Cada carta tem 20 itens (17 dicas + 3 instruções de tabuleiro, no estilo do jogo).

## Como rodar

```bash
cd ~/src/repos/kelvinwieth/perfil7
npm install
npm run dev
```

Abra [http://127.0.0.1:43127](http://127.0.0.1:43127) no celular (ou no navegador).

## Fluxo na mesa

1. Escolham o mediador da rodada.
2. No app: sorteiem a carta (todas as categorias ou uma só).
3. Passe o celular só para o mediador.
4. Mediador anuncia a categoria e marca a ficha amarela no tabuleiro.
5. Jogadores pedem números; o mediador toca e lê.
6. Acertou? Marquem no app e avancem os peões no tabuleiro como sempre.
7. Passe o celular para a esquerda — próximo mediador.

Há também o modo **cartela-bônus** (casa “?”): até 5 números e um palpite.

## Dados

- `src/data/cards.json` — baralho final (350)
- `src/data/raw-*.json` — dicas por categoria (antes das ações)
- `scripts/assemble-cards.py` — remonta o baralho com as instruções

```bash
python3 scripts/assemble-cards.py
```
