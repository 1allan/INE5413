from queue import Queue
from lib import Grafo, Vertice


class VerticeInfo:
    
    def __init__(self, visitado: bool = False, antecessor: Vertice = None, ref: Vertice = None):
        self.visitado = visitado
        self.antecessor: Vertice | None = antecessor
        self.ref: Vertice | None  = ref


def edmonds_karp(grafo: Grafo, fonte: Vertice, sorvedouro: Vertice, rede_residual: Grafo) -> Queue | None:
    infos = { v.rotulo: VerticeInfo() for v in grafo.get_vertices() }
    fila = Queue()
    
    infos[fonte.rotulo].visitado = True
    fila.put(fonte)
    
    while not fila.empty():
        u = fila.get()
        for v in grafo.vizinhos(u):
            if not infos[v.rotulo].visitado and grafo.peso(u, v) > 0:
                infos[v.rotulo].visitado = True
                infos[v.rotulo].antecessor = u
                if v == sorvedouro:
                    caminho = Queue()
                    caminho.put(sorvedouro)
                    w = sorvedouro
                    while w != fonte:
                        w = infos[w.rotulo].antecessor
                        caminho.put(w)
                    return caminho
                fila.put(v)
    return None
    
    
if __name__ == '__main__':
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './tests/wiki.net')
    
    g = Grafo.ler(filename)
    result = edmonds_karp(g, g.get_vertices()[0], g.get_vertices()[-1])
    print([v.rotulo for v in result.queue])