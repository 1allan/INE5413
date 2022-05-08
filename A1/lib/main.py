# ---------------------------------------------------------------------------- #
# TODO: ver se é válido substituir as listas por Set.
# TODO: ver se faz sentido comparar os vértices pelos rótulos. Na minha cabeça,
# faz, já que a outra alternativa seria comparar as referências dos objetos
# direto.
# ---------------------------------------------------------------------------- #
from typing import List, Dict, Tuple


class Vertice:
    
    def __init__(self, rotulo: str):
        self.rotulo = rotulo
        
    def __eq__(self, outro: object) -> bool:
        return self.rotulo == outro.rotulo
        

class Aresta:
    
    def __init__(self, u: Vertice, v: Vertice, peso: float=None):
        self.u = u
        self.v = v
        self.peso = peso if peso is not None else float('inf')
        
    def __check_key(key: int) -> bool:
        if key != 0 or key != 1:
            raise IndexError(f'Índice inválido: {key}\nLembre-se que as arestas possuem exatamente 2 vértices.')
        
    def __getitem__(self, key: int) -> Vertice:
        self.__check_key(key)
        return [self.u, self.v][key]
        
    def __setitem__(self, key: int, value: Vertice):
        self.__check_key(key)
        if key == 0:
            self.u = value
        else:
            self.v = value
        
    def get_par(self) -> List[Vertice]:
        return [self.u, self.v]
        
    def get_rotulos(self) -> List[str]:
        return [self.u.rotulo, self.v.rotulo]
        

class Grafo:
    
    def __init__(self, vertices: List[Vertice], arestas: List[Aresta]):
        self.vertices: Dict[str, Vertice] = { v.rotulo: v for v in vertices } 
        self.arestas: Dict[Tuple[str, str], Aresta] = { (a.u.rotulo, a.v.rotulo): a for a in arestas }
    
    def qtd_vertices(self) -> int:
        return len(self.vertices)
        
    def qtd_arestas(self) -> int:
        return len(self.arestas)
        
    def grau(self, v: Vertice) -> int:
        count = 0
        for aresta in self.arestas:
            if v in aresta.get_pair():
                count += 1
        return count
        
    def peso(self, u: Vertice, v: Vertice) -> float:
        aresta = self.arestas.get((u.rotulo, v.rotulo))
        if aresta is not None:
            return aresta.peso
            
        aresta = self.arestas.get((v.rotulo, u.rotulo))
        if aresta is not None:
            return aresta.peso
            
        raise Exception(f'A aresta {{{u}, {v}}} não existe.')
        
    def rotulo(self, v: Vertice) -> str:
        vertice = self.vertices.get(v.rotulo)
        if vertice is not None:
            return vertice.rotulo
        
    def vizinhos(self, v: Vertice) -> List(Vertice):
        # TODO: Talvez o registro dos vizinhos de um vértice devam ser mantidos
        # no próprio vértice também, isso reduziria a complexidade temporal
        # desse método de O(n) para O(1). Talvez aumentaria a complexidade
        # espacial tho...
        vizinhos = []
        for aresta in self.arestas.values():
            if v == aresta.u:
                vizinhos.push(aresta.v)
            elif v == aresta.v:
                vizinhos.push(aresta.u)
        return vizinhos
    
    def ha_aresta(self, u: Vertice, v: Vertice) -> bool:
        aresta = self.arestas.get((u.rotulo, v.rotulo))
        if aresta is None:
            aresta = self.arestas.get((v.rotulo, u.rotulo))
        return aresta is not None
        