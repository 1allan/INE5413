from typing import Dict, List, Tuple
from queue import SimpleQueue
from .lib import Grafo, Vertice


class VerticeInfo:

    def __init__(self, d: float | int = float('inf'), parceiro: Vertice = None, ref: Vertice = None):
        self.d = d
        self.parceiro: Vertice | None = parceiro
        self.ref: Vertice | None  = ref


# TODO: acho que isso aqui deveria retornar outra coisa
def bfs(grafo: Grafo, infos: Dict[str, VerticeInfo]) -> bool:
    fila: SimpleQueue[Vertice] = SimpleQueue()
    particao1: List[Vertice] = grafo.get_particoes()[0]

    for x in particao1:
        if infos[x.rotulo].parceiro is None:
            infos[x.rotulo].d = 0
            fila.put(x)
        else:
            infos[x.rotulo].d = float('inf')

    infos[None] = VerticeInfo()
    while not fila.empty():
        x = fila.get()
        info_x = infos[x.rotulo]
        if info_x.d < infos[None].d:
            for y in grafo.vizinhos(x):
                info_y = infos[y.rotulo]
                info_parceiro_y = infos[info_y.parceiro.rotulo]
                if info_parceiro_y.d == float('inf'):
                    info_parceiro_y.d = info_x.d + 1
                    fila.put(info_y.parceiro)

    return infos[None].d != float('inf')

def dfs(grafo: Grafo, x: Vertice, infos: Dict[str, VerticeInfo]) -> bool:
    if x is None:
        return True

    for y in grafo.vizinhos(x):
        parceiro_y = infos[y.rotulo].parceiro
        if infos[parceiro_y.rotulo].d == infos[x.rotulo].d + 1:
            if dfs(grafo, parceiro_y, infos):
                infos[y.rotulo].parceiro = x
                infos[x.rotulo].parceiro = y
                return True

    infos[x.rotulo].d = float('inf')
    return False


def hopcroft_karp(grafo: Grafo) -> Tuple[int, List[Vertice]]:
    (particao1, particao2): Tuple[List[Vertice], List[Vertice]] = grafo.get_particoes()
    infos = { v.rotulo: VerticeInfo() for v in grafo.get_vertices() }
    m = 0

    while bfs(grafo, infos):
        for x in particao1:
            if infos[x.rotulo].parceiro is None:
                if dfs(grafo, x, infos):
                    m += 1

    parceiros = list([v.parceiro for v in infos.values()])
    return (m, parceiros)
