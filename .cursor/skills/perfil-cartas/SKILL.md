---
name: perfil-cartas
description: >-
  Cria dicas novas de cartelas Perfil 7 (Grow) em PT-BR falado. Use com humanizar.
  paths: src/data/raw-*.json
---

# Cartelas Perfil 7 — escrita do zero

Complemento de domínio para `humanizar` em **modo_criacao**: não parafrasear dicas velhas; inventar 17 pistas novas a partir só da resposta.

## Formato

- 17 dicas por carta, **vago → específico** (1–5 abrem o tema, 6–12 fatos concretos, 13–17 quase entregam).
- Frases curtas, **tom de mediador lendo na mesa** (Brasil, informal leve, sem poesia de IA).
- **TRAVA FACTUAL:** só afirmar o que é verdade sobre a resposta; não inventar datas/números/nomes.

## Voz

- **PESSOA / COISA / DIGITAL:** 1ª pessoa (`Sou`, `Tenho`, `Uso`, `Entro`).
- **LUGAR:** 1ª pessoa do lugar (`Fico`, `Moro`, `Recebo turista`).
- **ANO:** o ano fala; misture eventos daquele ano com propriedades numéricas **sem copiar a mesma frase em toda carta** (varie: par/ímpar, século, soma dos dígitos, romano, bissexto).

## Estilo Grow (referência)

- Cena do cotidiano: ônibus, churrasco, escola, aeroporto.
- Uma ideia por frase; verbos simples.
- Última dica pode ser joguinho de palavras **sem** repetir a resposta literal.

## Proibido

- Meta de IA: “drama moderno”, “estado emocional”, “bolha pessoal”, “habito a rotina”.
- Enciclopédia: “sou considerado”, “marco fundamental”, “associado a”.
- Template clonado: mesmas 17 frases só trocando o ano em todas as cartas ANO.
- Travessão (—) como pontuação.

## Entrada / saída

- JSON: `{ "answer": "...", "clues": [17 strings] }` — **answer intacto**.
