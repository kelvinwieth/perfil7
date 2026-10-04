---
name: perfil-cartas
description: >-
  Reescreve dicas de cartelas Perfil 7 (Grow) em PT-BR falado, para leitura em
  voz alta na mesa. Use com humanizar. paths: src/data/raw-*.json
---

# Cartelas Perfil 7

Complemento de domínio para a skill `humanizar`.

## Formato

- 17 dicas por carta, ordem do mais vago ao mais específico.
- Frases curtas (ideal 6–16 palavras), ritmo de fala.
- TRAVA FACTUAL: mesmos fatos, datas, nomes e números; só muda a forma.

## Voz

- **PESSOA / COISA / DIGITAL:** 1ª pessoa (`Sou`, `Tenho`, `Nasci`, `Moro`).
- **LUGAR:** 1ª pessoa do lugar (`Fico`, `Sou`, `Meu nome`) ou frase direta sem “É um dos…” genérico.
- **ANO:** o ano fala (`Sou par`, `Neste ano…`); matemática em linguagem de mesa, não de prova.

## Evitar (AI slop)

- “marco fundamental”, “ídolo nacional”, “considerado”, “associado a”, “no contexto de”
- “Possuo N algarismo(s) distinto(s)”, “escrevo-me em algarismos romanos” → dizer naturalmente
- “É Patrimônio Mundial” sem verbo humano → “A UNESCO me declarou patrimônio”
- Três adjetivos, regra de três, travessão como pontuação
- “Muitos me chamam de o maior…” → encurtar ou trocar por fato concreto

## Manter

- Instruções de tabuleiro ficam fora destes arquivos (só dicas em `clues`).
