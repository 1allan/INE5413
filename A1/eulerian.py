from typing import Dict, List, Tuple

from lib import Vertice, Aresta, Grafo
    
    
class ArestaInfo:
    
    def __init__(self, ref: Aresta|None = None):
        self.visitada = False
        

def buscaSubcicloEuleriano(g: Grafo, v: Vertice, c: Dict[Aresta, ArestaInfo]) -> Tuple[bool, List[Vertice]]:
    ciclo = [v]
    temp = v
    while v is temp:
        tinha_nao_visitada = False
        for u in g.vizinhos(v):
            aresta = g.get_aresta(u, v)
            if aresta is not None and not c[aresta].visitada:
                c[aresta].visitada = True
                v = u
                ciclo.append(v)
                tinha_nao_visitada = True
        
        if not tinha_nao_visitada:
            return False, None
        
    for x in ciclo:
        for w in g.vizinhos(x):
            aresta = g.get_aresta(x, w)
            visitada = c[aresta].visitada
            if not visitada:
                tem_subciclo, subciclo = buscaSubcicloEuleriano(g, x, c)
                if not tem_subciclo:
                    return False, None
                
                ciclo = ciclo[:ciclo.index(x)] + subciclo + ciclo[ciclo.index(x) + 1:]
    
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
    tem, ciclo = hierholzer(com_ciclo)
    print(1 if tem else 0)
    print(','.join(list([c.rotulo for c in ciclo[:-1]])))
    
    sem_ciclo = Grafo.ler('./tests/SemCicloEuleriano.net')
    tem, ciclo = hierholzer(sem_ciclo)
    print(1 if tem else 0)
    print(','.join(list([c.rotulo for c in ciclo[:-1]])))
