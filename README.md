# T5 – Coloração de Grafos com DSatur

**Disciplina:** Resolução de Problemas com Grafos  
**Orientador:** Prof. Me Ricardo Carubbi
**Grupo:**
- Anselmo Teixeira — 2410414
- João Marcelo Jucá — 2410392
- Thigo Victor Ferreira — 2410413

---

## Vídeo explicativo

> Link: https://drive.google.com/drive/folders/18lm9jzZqeqzmkQSFjW6nljg_9EilG3ly?usp=sharing

---

## Descrição

Programa que modela o mapa político do Brasil como um grafo não direcionado e aplica o algoritmo **DSatur** para colorir os estados com o menor número de cores possível, respeitando a restrição de que estados fronteiriços não podem ter a mesma cor.

## Estrutura do Projeto

```
T5/
├── README.md
├── dados/
│   └── brasil.txt       # grafo do Brasil no padrão algs4
└── src/
    ├── main.py          # ponto de entrada
    ├── graph.py         # classe Graph (algs4-py)
    ├── dsatur.py        # algoritmo DSatur
    ├── bag.py           # classe Bag (algs4-py)
    └── linklist.py      # lista encadeada (algs4-py)
```

## Mapeamento dos Vértices

| Índice | Estado | Índice | Estado | Índice | Estado |
|--------|--------|--------|--------|--------|--------|
| 0 | AC | 9 | MA | 18 | RJ |
| 1 | AL | 10 | MG | 19 | RN |
| 2 | AM | 11 | MS | 20 | RO |
| 3 | AP | 12 | MT | 21 | RR |
| 4 | BA | 13 | PA | 22 | RS |
| 5 | CE | 14 | PB | 23 | SC |
| 6 | DF | 15 | PE | 24 | SE |
| 7 | ES | 16 | PI | 25 | SP |
| 8 | GO | 17 | PR | 26 | TO |

## Como Executar

A partir da pasta raiz do projeto:

```bash
python src/main.py dados/brasil.txt
```
