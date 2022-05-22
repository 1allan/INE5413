from typing import List
from time import time

from lib import Vertice, Grafo


class VerticeInfo(Vertice):
    
    def __init__(self, v: Vertice):
        self.ref = v
        self.visitado = False
        self.distancia = 0
        self.antecessor: Vertice|None = None
        super().__init__(v.rotulo)
        
    def __str__(self) -> str:
        output = (
            f'Vértice: {self.ref.rotulo}',
            f'Visitado: {self.visitado}',
            f'Distância: {self.distancia}',
            f'Antecessor: {self.antecessor}'
        )
        return '\n'.join(output)
        

def bfs(g: Grafo, s: Vertice):
    vertices_infos = list([VerticeInfo(v) for v in g.get_vertices()])
    fila: List[VerticeInfo] = list()
    fila.append(s)
    
    nivel = 0
    while len(fila) > 0:
        print(f'{nivel}:', ','.join([v.rotulo for v in fila]))
        u = fila.pop(0)
        for v in g.vizinhos(u):
            v_info = vertices_infos[vertices_infos.index(v)]
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
