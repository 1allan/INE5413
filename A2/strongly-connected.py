from typing import Dict, List
from lib import Grafo, Vertice, Aresta


Tempo = List[int]

class VerticeInfo:
    
    def __init__(self, ref: Vertice | None = None):
        self.ref = ref
        self.visitado = False
        self.inicio: int | float  = float('inf')
        self.fim: int | float  = float('inf')
        self.antecessor: Vertice | None = None


def strongly_connected(g: Grafo) -> List[Vertice | None]:
    infos = dfs(g)
    gt = transpor(g)
    
    print([t.rotulo + ' ' + str(infos[t.rotulo].fim) for t in [v.ref for v in infos.values()]])
    t_final_decresc = sorted([v.ref for v in infos.values()], key=lambda v: infos[v.rotulo].fim, reverse=True)
    print([t.rotulo + ' ' + str(infos[t.rotulo].fim) for t in t_final_decresc])
    infost = dfs(gt, vertices_ordenados=t_final_decresc)
    return list([vi.antecessor for vi in infost.values()])
    
def dfs(g: Grafo, vertices_ordenados: List[Vertice]=None) -> Dict[Vertice, VerticeInfo]:
    infos: Dict[str, VerticeInfo] = { v.rotulo: VerticeInfo(v) for v in g.get_vertices() }
    tempo: Tempo = [0]
    
    if vertices_ordenados is None:
        vertices = g.get_vertices()
    else:
        vertices = vertices_ordenados
        
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

def transpor(g: Grafo) -> Grafo:
    vertices = list([ Vertice(v.rotulo) for v in g.get_vertices()])
    arestas: List[Aresta] = []
    for a in g.get_arestas():
        arestas.append(Aresta(a.v, a.u, a.peso))
    return Grafo(vertices, arestas, dirigido=True)


if __name__ == '__main__':
    g = Grafo.ler('./tests/agm_tiny.net')
    result = strongly_connected(g)
    print(result)