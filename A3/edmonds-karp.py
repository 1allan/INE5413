from queue import Queue
from typing import Tuple
from lib import Grafo, Vertice


class VerticeInfo:
    
    def __init__(self, visitado: bool = False, antecessor: Vertice = None, ref: Vertice = None):
        self.visitado = visitado
        self.antecessor: Vertice | None = antecessor
        self.ref: Vertice | None  = ref

def edmonds_karp(grafo: Grafo, fonte: Vertice, sorvedouro: Vertice) -> Tuple[Queue | None, float]:
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
                    fluxo_maximo = g.get_aresta(infos[w.rotulo].antecessor, w).peso
                    while w != fonte:
                        w = infos[w.rotulo].antecessor
                        caminho.put(w)
                        aresta = None if w == fonte else g.get_aresta(infos[w.rotulo].antecessor, w)
                        if aresta and fluxo_maximo > aresta.peso:
                            fluxo_maximo = aresta.peso
                    return (caminho, fluxo_maximo)
                fila.put(v)
    return (None, -1.0)
    
    
if __name__ == '__main__':
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './tests/wiki.net')
    
    g = Grafo.ler(filename)
    caminho, fluxo_maximo = edmonds_karp(g, g.get_vertices()[0], g.get_vertices()[-1])
    print(fluxo_maximo)