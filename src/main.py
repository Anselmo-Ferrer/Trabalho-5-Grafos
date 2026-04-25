import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from graph import Graph
from dsatur import DSatur

STATES = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF",
    "ES", "GO", "MA", "MG", "MS", "MT", "PA",
    "PB", "PE", "PI", "PR", "RJ", "RN", "RO",
    "RR", "RS", "SC", "SE", "SP", "TO"
]


def build_graph(filepath):
    with open(filepath) as f:
        V = int(f.readline())
        E = int(f.readline())
        g = Graph(V)
        for _ in range(E):
            v, w = f.readline().split()
            g.add_edge(v, w)
    return g


def main():
    if len(sys.argv) != 2:
        print("Uso: python src/main.py dados/brasil.txt")
        sys.exit(1)

    filepath = sys.argv[1]
    g = build_graph(filepath)

    print("=" * 50)
    print("GRAFO DO BRASIL - Lista de Adjacencia")
    print("=" * 50)
    print(f"{g.V} vertices, {g.E} arestas")
    for v in range(g.V):
        neighbors = " ".join(STATES[w] for w in g.adj[v])
        print(f"  {v:2d} {STATES[v]}: {neighbors}")
    print()

    ds = DSatur(g)

    print("=" * 50)
    print("ORDEM DE COLORACAO (DSatur)")
    print("=" * 50)
    for i, v in enumerate(ds.coloring_order(), 1):
        print(f"  Passo {i:2d}: {STATES[v]:2s} (vertice {v:2d}, grau={g.degree(v):2d}) "
              f"-> cor {ds.color(v)}")
    print()

    print("=" * 50)
    print("COLORACAO FINAL POR ESTADO")
    print("=" * 50)
    for v in range(g.V):
        print(f"  {STATES[v]:2s} (vertice {v:2d}): cor {ds.color(v)}")
    print()

    print(f"Total de cores utilizadas: {ds.num_colors()}")
    valid = ds.is_valid()
    print(f"Coloracao valida: {'Sim' if valid else 'Nao'}")
    print("=" * 50)


if __name__ == "__main__":
    main()
