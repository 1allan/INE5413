from time import time
from typing import Dict, List, Tuple

from lib import Vertice, Aresta, Grafo
    
    
class ArestaInfo:
    
    def __init__(self, ref: Aresta|None = None):
        self.visitada = False
        

def buscaSubcicloEuleriano(g: Grafo, v: Vertice, c: Dict[Aresta, ArestaInfo]) -> Tuple[bool, List[Vertice]]:
    ciclo = [v]
    temp = v
    while v is temp:
        visitadas: List[bool] = []
        for u in g.vizinhos(v):
            aresta = g.get_aresta(v, u)
            if aresta is not None:
                visitadas.append(c[aresta].visitada)

        if all(visitadas):
            return (False, None)
        
        for u in g.get_arestas():
            if not c[u].visitada:
                c[u].visitada = True
                v = u
                ciclo.append(v)
                break
        
        for x in ciclo:
            for w in g.vizinhos(x):
                aresta = g.get_aresta(x, w)
                visitada = c[aresta].visitada
                if not visitada:
                    tem_subciclo, sub_ciclo = buscaSubcicloEuleriano(g, x, c)
                    if not tem_subciclo:
                        return False, None
                    return True, sub_ciclo
        
        return True, ciclo
        

def hierholzer(g: Grafo) -> Tuple[bool, List[Vertice] | None]:
    aresta_infos = { a: ArestaInfo() for a in g.get_arestas() }
    v = g.get_vertices()[0]
    
    tem_ciclo, ciclo = buscaSubcicloEuleriano(g, v, aresta_infos)
    
    if not tem_ciclo:
        return False, None
    
    if any([not aresta_infos[a].visitada for a in g.get_arestas()]):
        return False, None
        
    return True, ciclo
    

if __name__ == '__main__':
    com_ciclo = Grafo.ler('./tests/ContemCicloEuleriano.net')
    inicio = time()
    print('Com ciclo euleriano:', hierholzer(com_ciclo))
    print(f'Duração: {round(time() - inicio, 3)}s')
    
    sem_ciclo = Grafo.ler('./tests/SemCicloEuleriano.net')
    inicio = time()
    print('Sem ciclo euleriano:', hierholzer(sem_ciclo))
    print(f'Duração: {round(time() - inicio, 3)}s')
