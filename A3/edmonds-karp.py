from queue import SimpleQueue
from .lib import Grafo, Vertice


class VerticeInfo:
    
    def __init__(self, visitado: bool = False, antecessor: Vertice = None, ref: Vertice = None):
        self.visitado = visitado
        self.antecessor: Vertice | None = antecessor
        self.ref: Vertice | None  = ref


def edmonds_karp(grafo: Grafo, fonte: Vertice, sorvedouro: Vertice, rede_residual: Grafo) -> int | None:
    infos = { v.rotulo: VerticeInfo() for v in grafo.get_vertices() }
    fila = SimpleQueue()
    
    infos[fonte.rotulo].visitado = True
    fila.put(fonte)
    
    while not fila.empty():
        u = fila.get()
        for v in grafo.vizinhos(u):
            if not infos[v.rotulo].visitado and grafo.peso(u, v) > 0:
                infos[v.rotulo].visitado = True
                infos[v.rotulo].antecessor = u
                if v == sorvedouro:
                    caminho = SimpleQueue()
                    caminho.put(sorvedouro)
                    w = sorvedouro
                    while w != fonte:
                        w = infos[w.rotulo].antecessor
                        caminho.put(w)
                    return caminho
                fila.put(v)
    return None
    