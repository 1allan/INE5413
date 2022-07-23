from typing import Dict, List, Tuple
from queue import Queue
from lib import Grafo, Vertice


class VerticeInfo:

    def __init__(self, d: float | int = float('inf'), parceiro: Vertice = None, ref: Vertice = None):
        self.d = d
        self.parceiro: Vertice | None = parceiro
        self.ref: Vertice | None  = ref

# Este método é apenas para facilitar a usabilidade do `infos[None]`
def get_rotulo_ou_none(v: Vertice) -> str | None:
    return None if v is None else v.rotulo

def bfs(grafo: Grafo, infos: Dict[str, VerticeInfo]) -> bool:
    fila: Queue[Vertice] = Queue()
    particao1 = grafo.get_particoes()[0]

    for x in particao1:
        if infos[x.rotulo].parceiro is None:
            infos[x.rotulo].d = 0
            fila.put(x)
        else:
            infos[x.rotulo].d = float('inf')

    infos[None] = VerticeInfo()
    while not fila.empty():
        x = fila.get()
        info_x = infos[get_rotulo_ou_none(x)]
        if info_x.d < infos[None].d:
            for y in grafo.vizinhos(x):
                info_y = infos[y.rotulo]
                info_parceiro_y = infos[get_rotulo_ou_none(info_y.parceiro)]
                if info_parceiro_y.d == float('inf'):
                    info_parceiro_y.d = info_x.d + 1
                    fila.put(info_y.parceiro)

    return infos[None].d != float('inf')

def dfs(grafo: Grafo, x: Vertice, infos: Dict[str, VerticeInfo]) -> bool:
    if x is None:
        return True

    for y in grafo.vizinhos(x):
        parceiro_y = infos[y.rotulo].parceiro
        if infos[get_rotulo_ou_none(parceiro_y)].d == infos[x.rotulo].d + 1:
            if dfs(grafo, parceiro_y, infos):
                infos[y.rotulo].parceiro = x
                infos[x.rotulo].parceiro = y
                return True

    infos[x.rotulo].d = float('inf')
    return False


def hopcroft_karp(grafo: Grafo) -> Tuple[int, List[Vertice]]:
    particao1, _ = grafo.get_particoes()
    infos = { v.rotulo: VerticeInfo() for v in grafo.get_vertices() }
    m = 0

    while bfs(grafo, infos):
        for x in particao1:
            if infos[x.rotulo].parceiro is None:
                if dfs(grafo, x, infos):
                    m += 1
    parceiros = []
    parceiros_string = ""
    for k,v in infos.items():
        parssa = get_rotulo_ou_none(v.parceiro)
        if k not in parceiros and k != None and parssa != None:    
            parceiros.append(parssa)
            parceiros_string += f"{k}-{get_rotulo_ou_none(v.parceiro)} "
    return (m, parceiros_string)


if __name__ == '__main__':
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './tests/pequeno.net')
    
    g = Grafo.ler(filename)
    tamanho, parceiros = hopcroft_karp(g)
    print('Emparelhamento máximo:', tamanho)
    print(parceiros)
    