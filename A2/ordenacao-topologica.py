from typing import Dict, List
from lib import Grafo, Vertice, Aresta

Tempo = List[int]

lista_ord_topologica = []  # lista para o retorno da Ord Topologica

class VerticeInfo:
    
    def __init__(self, ref: Vertice | None = None):
        self.ref = ref
        self.visitado = False
        self.inicio: int | float  = float('inf')
        self.fim: int | float  = float('inf')
        self.antecessor: Vertice | None = None


def ordenacao_topologica(g: Grafo):
    infos: Dict[str, VerticeInfo] = { v.rotulo: VerticeInfo(v) for v in g.get_vertices() }
    vertices = g.get_vertices()
    tempo: Tempo = [0]

    for u in vertices:
        if not infos[u.rotulo].visitado:
            dfs_visit(g, u, infos, tempo)
    
    return infos


def dfs_visit(g: Grafo, v: Vertice, infos: Dict[str, VerticeInfo], tempo: Tempo):
    infos[v.rotulo].visitado = True
    tempo[0] += 1
    infos[v.rotulo].inicio = tempo[0]
    for u in g.vizinhos(v):
        if not infos[u.rotulo].visitado:
            infos[u.rotulo].antecessor = v
            dfs_visit(g, u, infos, tempo)
    tempo[0] += 1
    infos[v.rotulo].fim = tempo[0]

    lista_ord_topologica.insert(0, v.rotulo[1:-1] + ' ->')



if __name__ == '__main__':
    g = Grafo.ler('./tests/simpsons_amizades1.net')
    result = ordenacao_topologica(g)
    a = ''
    for i in lista_ord_topologica:
        a+=i
    print(a)