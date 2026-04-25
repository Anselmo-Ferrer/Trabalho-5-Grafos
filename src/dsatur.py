class DSatur:
    """
    Heuristica DSatur para coloracao de grafos nao direcionados.

    A cada passo, escolhe o vertice nao colorido com maior grau de saturacao
    DS(v) = numero de cores distintas na vizinhanca de v.
    Empate: maior grau. Atribui a menor cor disponivel ao vertice escolhido.
    """

    def __init__(self, graph):
        self._graph = graph
        n = graph.V
        self._color = [-1] * n
        self._colored = [False] * n
        self._sat = [0] * n
        self._order = []
        self._num_colors = 0
        self._run()

    def _neighbor_colors(self, v):
        colors = set()
        for w in self._graph.adj[v]:
            if self._colored[w]:
                colors.add(self._color[w])
        return colors

    def _run(self):
        G = self._graph
        n = G.V

        # Passo 1: colorir o vertice de maior grau
        start = max(range(n), key=lambda v: G.degree(v))
        self._assign(start, 1)

        # Passo 2: colorir os demais vertices
        remaining = set(range(n))
        remaining.remove(start)

        while remaining:
            # Escolhe vertice com max DS; desempate por maior grau
            v = max(remaining, key=lambda u: (self._sat[u], G.degree(u)))

            # Menor cor disponivel que nao conflite com vizinhos
            used = self._neighbor_colors(v)
            k = 1
            while k in used:
                k += 1

            self._assign(v, k)
            remaining.remove(v)

    def _assign(self, v, color):
        self._color[v] = color
        self._colored[v] = True
        self._order.append(v)
        if color > self._num_colors:
            self._num_colors = color
        # Atualiza saturacao dos vizinhos nao coloridos
        for w in self._graph.adj[v]:
            if not self._colored[w]:
                self._sat[w] = len(self._neighbor_colors(w))

    def color(self, v):
        return self._color[v]

    def num_colors(self):
        return self._num_colors

    def coloring_order(self):
        return list(self._order)

    def is_valid(self):
        G = self._graph
        for v in range(G.V):
            for w in G.adj[v]:
                if self._color[v] == self._color[w]:
                    return False
        return True
