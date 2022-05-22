from typing import List
from time import time

from lib import Vertice, Grafo


class VerticeInfo(Vertice):
    
    def __init__(self, v: Vertice):
        self.ref = v
        self.visited = False
        self.distance = 0
        self.parent: Vertice|None = None
        super().__init__(v.rotulo)
        
    def __str__(self) -> str:
        output = (
            f'Vértice: {self.ref.rotulo}',
            f'Visitado: {self.visited}',
            f'Distância: {self.distance}',
            f'Antecessor: {self.parent}'
        )
        return '\n'.join(output)
        

def bfs(g: Grafo, s: Vertice):
    vertices_infos = list([VerticeInfo(v) for v in g.get_vertices()])
    queue: List[VerticeInfo] = list()
    queue.append(s)
    
    level = 0
    while len(queue) > 0:
        u = queue.pop(0)
        for v in g.vizinhos(u):
            v_info = vertices_infos[vertices_infos.index(v)]
            if (not v_info.visited):
                v_info.visited = True
                v_info.distance += 1
                v_info.parent = u
                queue.append(v)
                
        print(f'{level}:', ','.join([v.rotulo for v in queue]))
        level += 1


if __name__ == '__main__':
    g = Grafo.ler('./tests/polbooks.net')

    start_time = time()
    bfs(g, g.get_vertices()[0])

    print(f'Duration: {round(time() - start_time, 3)}s')
