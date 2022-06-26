from typing import List, Set
from lib import Grafo, Vertice, Aresta


def kruskal(g: Grafo) -> Set[Aresta]:
    agm_arestas: Set[Aresta] = set()
    arvores = { v.rotulo: { v.rotulo } for v in g.get_vertices() }
    arestas = sorted(g.get_arestas(), key=lambda e: e.peso)
    
    for (aresta) in arestas:
        u = aresta.u
        v = aresta.v
        if arvores[u.rotulo] != arvores[v.rotulo]:
            agm_arestas.add(aresta)
            x = arvores[u.rotulo].union(arvores[v.rotulo])
            for y in x:
                arvores[y] = x
    return agm_arestas


if __name__ == '__main__':
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './tests/teste_cfc.net')
    
    g = Grafo.ler(filename)
    agm = kruskal(g)
    
    print(sum([ a.peso for a in agm]))
    print(', '.join([f'{r.u.rotulo}-{r.v.rotulo}' for r in agm]))