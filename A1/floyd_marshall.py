from typing import List
from lib import Grafo

MatrizAdjacencia = List[List[float]]

def gera_matriz(g: Grafo) -> MatrizAdjacencia:
    output: MatrizAdjacencia = []
    vertices = g.get_vertices()
    for i in range(len(vertices)):
        output.append([])
        for j in range(len(vertices)):
            if vertices[i] is vertices[j]:
                output[i].append(0)
            else:
                aresta= g.get_aresta(vertices[i], vertices[j])
                if aresta is not None:
                    output[i].append(aresta.peso)
                else:
                    output[i].append(float('inf'))
    return output

def floyd_marshall(g: Grafo):
    matrizes = [gera_matriz(g)]
    
    for k in range(1, len(g.get_vertices())):
        matrizes.append(gera_matriz(g))
        for i in range(len(g.get_vertices())):
            for j in range(len(g.get_vertices())):
                matrizes[k][i][j] = min(matrizes[k - 1][i][j], matrizes[k - 1][i][k], matrizes[k - 1][k][j])
    return matrizes
    
def pprint(matrizes: List[MatrizAdjacencia]):
    for i, matriz in enumerate(matrizes):
        line = f'{i + 1}:'
        print(line + ','.join([str(peso) for peso in matriz[0]]))

if __name__ == '__main__':
    g = Grafo.ler('./tests/fln_pequena.net')

    pprint(floyd_marshall(g))
