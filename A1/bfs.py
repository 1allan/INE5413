from typing import List, TypedDict
from time import time

from lib import Vertice, Grafo


class VerticeInfo:
    
    def __init__(self, ref: Vertice|None = None):
        self.ref = ref
        self.visitado: bool = False
        self.distancia: int = 0
        self.antecessor: Vertice|None = None

    
def print_fila(nivel: int, fila: List[Vertice]):
    print(f'{nivel}:', ','.join([v.rotulo for v in fila]))

def bfs(g: Grafo, s: Vertice):
    vertices_infos = { v.rotulo: VerticeInfo() for v in g.get_vertices() }
    fila: List[VerticeInfo] = list()
    fila.append(s)
    
    nivel = 0
    while len(fila) > 0:
        print_fila(nivel, fila)
        u = fila.pop(0)
        for v in g.vizinhos(u):
            v_info: VerticeInfo = vertices_infos.get(v.rotulo)
            if (not v_info.visitado):
                v_info.visitado = True
                v_info.distancia += 1
                v_info.antecessor = u
                fila.append(v)
        nivel += 1


if __name__ == '__main__':
    g = Grafo.ler('./tests/polbooks.net')

    inicio = time()
    bfs(g, g.get_vertices()[0])

    print(f'Duração: {round(time() - inicio, 3)}s')
