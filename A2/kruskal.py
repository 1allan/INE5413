from typing import List
from lib import Grafo, Vertice, Aresta


def kruskal(g: Grafo):
    a: List[Aresta] = []
    s = { v.rotulo: [] for v in g.get_vertices() }
    arestas = sorted(g.get_arestas(), key=lambda e: e.peso)
    
    for aresta in arestas:
        if s[aresta.u.rotulo] != s[aresta.v.rotulo]:
            a.append(aresta)
            x = s[aresta.u.rotulo] + s[aresta.v.rotulo]
            for y in x:
                s[y.rotulo] += x
                
    return a


if __name__ == '__main__':
    g = Grafo.ler('./tests/agm_tiny.net')
    result = kruskal(g)
    print(result)