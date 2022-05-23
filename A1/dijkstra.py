from typing import List
from lib import Vertice, Grafo


class VerticeInfo:
    
    def __init__(self, ref: Vertice | None = None):
        self.ref = ref
        self.custo = float('inf')
        self.antecessor = None


def dijkstra(g: Grafo, s: Vertice):
    vertice_infos = { v.rotulo: VerticeInfo() for v in g.get_vertices() } 
    vertice_infos[s.rotulo].custo = 0
    
    for _ in range(len(g.get_vertices())):
        for aresta in g.get_arestas():
            if vertice_infos[aresta.v.rotulo].custo > vertice_infos[aresta.u.rotulo].custo + aresta.peso:
                vertice_infos[aresta.v.rotulo].custo = vertice_infos[aresta.u.rotulo].custo + aresta.peso
                vertice_infos[aresta.v.rotulo].antecessor = aresta.u
                
    for aresta in g.get_arestas():
        if vertice_infos[aresta.v.rotulo].custo > vertice_infos[aresta.u.rotulo].custo + aresta.peso:
            return False, None, None
    
    custos: List[float] = []
    antecessores: List[Vertice] = []
    for vi in vertice_infos.values():
        custos.append(vi.custo)
        antecessores.append(vi.antecessor)
    return True, custos, antecessores
    

if __name__ == '__main__':
    g = Grafo.ler('./tests/fln_pequena.net')

    print(dijkstra(g, g.get_vertices()[0]))
