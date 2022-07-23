from __future__ import annotations
from typing import List, Dict, Tuple


class Vertice:
    
    def __init__(self, rotulo: str):
        self.rotulo = rotulo
        
    def __eq__(self, outro: Vertice) -> bool:
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
    
    def __init__(self, vertices: List[Vertice], arestas: List[Aresta], dirigido: bool=False):
        self.vertices: Dict[str, Vertice] = { v.rotulo: v for v in vertices } 
        self.arestas: Dict[Tuple[str, str], Aresta] = { (a.u.rotulo, a.v.rotulo): a for a in arestas }
        self.dirigido = dirigido
    
    def qtd_vertices(self) -> int:
        return len(self.vertices)
        
    def qtd_arestas(self) -> int:
        return len(self.arestas)
        
    def grau(self, v: Vertice) -> int:
        count = 0
        for aresta in self.arestas.values():
            if v in aresta.get_par():
                count += 1
        return count
        
    def peso(self, u: Vertice, v: Vertice) -> float:
        aresta = self.arestas.get((u.rotulo, v.rotulo))
        if aresta is not None:
            return aresta.peso
        
        if not self.dirigido:
            aresta = self.arestas.get((v.rotulo, u.rotulo))
            if aresta is not None:
                return aresta.peso
            
        raise Exception(f'A aresta {{{u}, {v}}} não existe.')
        
    def rotulo(self, v: Vertice) -> str:
        vertice = self.vertices.get(v.rotulo)
        if vertice is not None:
            return vertice.rotulo
        
    def vizinhos(self, v: Vertice) -> List[Vertice]:
        vizinhos = []
        for aresta in self.arestas.values():
            if v is aresta.u:
                vizinhos.append(aresta.v)
            elif not self.dirigido and v is aresta.v:
                vizinhos.append(aresta.u)
        return vizinhos
    
    def ha_aresta(self, u: Vertice, v: Vertice) -> bool:
        aresta = self.arestas.get((u.rotulo, v.rotulo))
        if not self.dirigido and aresta is None:
            aresta = self.arestas.get((v.rotulo, u.rotulo))
        return aresta is not None
        
    def get_aresta(self, u: Vertice, v: Vertice) -> Aresta | None:
        aresta = self.arestas.get((u.rotulo, v.rotulo))
        if not self.dirigido and aresta is None:
            aresta = self.arestas.get((v.rotulo, u.rotulo))
        return aresta
    
    def get_vertices(self) -> List[Vertice]:
        return list(self.vertices.values())
    
    def get_arestas(self) -> List[Aresta]:
        return list(self.arestas.values())
        
    def get_particoes(self) -> Tuple[List[Vertice], List[Vertice]]:
        particoes = ([], [])
        for aresta in self.get_arestas():
            particoes[0].append(aresta.u)
            particoes[1].append(aresta.v)
        return particoes
        
    def ler(arquivo: str) -> Grafo:
        with open(arquivo, 'r', encoding='utf8') as file:
            vertices = []
            arestas = []
            it_is_vertice_time_baby = True
            dirigido = False  # god forgive me
            for linha in file.readlines()[1:]:
                if linha.startswith('*edges') or linha.startswith('*arcs'):
                    if linha.startswith('*arcs'):
                        dirigido = True
                    it_is_vertice_time_baby = False
                    continue
                
                if it_is_vertice_time_baby:
                    _, rotulo = linha.split(' ', 1)
                    rotulo = rotulo[:-1]
                    vertices.append(Vertice(rotulo)) 
                else:
                    u_index, v_index, peso = linha.split(' ', 2)
                    u = vertices[int(u_index) - 1]
                    v = vertices[int(v_index) - 1]
                    arestas.append(Aresta(u, v, float(peso)))
                    
            return Grafo(vertices, arestas, dirigido=dirigido)
            
    def __str__(self):
        output = ''
        for vertice in self.vertices.values():
            output += f'V: {vertice.rotulo}\n'
            
        for aresta in self.arestas.values():
            output += f'E: ({aresta.u.rotulo}, {aresta.v.rotulo}, {aresta.peso})\n'
        
            
        return output
        