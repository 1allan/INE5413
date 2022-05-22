from lib import Grafo

g = Grafo.ler('./tests/polbooks.net')

print(g)
print('qtd_vertices() -> int\n', g.qtd_vertices())
print('qtd_arestas() -> int\n', g.qtd_arestas())
print('grau(v: Vertice) -> int\n', g.grau(list(g.vertices.values())[0]))
print('rotulo(v: Vertice) -> str\n', g.rotulo(list(g.vertices.values())[0]))
print('vizinhos(v: Vertice) -> List[Vertice]\n', g.vizinhos(list(g.vertices.values())[0]))
print('ha_aresta(v: Vertice, u: Vertice) -> bool\n', g.ha_aresta(list(g.vertices.values())[0], list(g.vertices.values())[1]))
print('peso(v: Vertice, u: Vertice) -> float\n', g.peso(list(g.vertices.values())[0], list(g.vertices.values())[1]))
