class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = {}
    
    def adicionar_aresta(self, u, v):
        if u in self.grafo:
            self.grafo[u].append(v)
        else:
            self.grafo[u] = [v]
        
        if v in self.grafo:
            self.grafo[v].append(u)
        else:
            self.grafo[v] = [u]
    
    def dfs(self, vertice, visitados):
        visitados[vertice] = True
        num_componentes = 1
        for vizinho in self.grafo[vertice]:
            if not visitados[vizinho]:
                num_componentes += self.dfs(vizinho, visitados)
        return num_componentes
    
    def numero_componentes_conectados(self):
        visitados = [False] * self.vertices
        numero_componentes = 0
        for vertice in range(self.vertices):
            if not visitados[vertice]:
                numero_componentes += 1
                self.dfs(vertice, visitados)
        return numero_componentes
    
    def verifica_ponte(self, u, v):
        if u not in self.grafo or v not in self.grafo[u]:
            return False  # Aresta não existe no grafo
        
        num_componentes_antes = self.numero_componentes_conectados()
        
        # Remova temporariamente a aresta para verificar o número de componentes após a remoção
        self.grafo[u].remove(v)
        self.grafo[v].remove(u)
        
        num_componentes_depois = self.numero_componentes_conectados()
        
        # Restaure a aresta
        self.adicionar_aresta(u, v)
        
        print(f"O grafo tem {num_componentes_antes} componente(s) conectado(s) antes da remoção da aresta.")
        print(f"O grafo tem {num_componentes_depois} componente(s) conectado(s) após a remoção da aresta.")
        
        return num_componentes_antes != num_componentes_depois

# Exemplo de uso

#Numero de vértices do grafo
grafo = Grafo(4)

#Arestas do grafo
grafo.adicionar_aresta(0, 1)
grafo.adicionar_aresta(1, 2)
grafo.adicionar_aresta(2, 3)

# Forneça a aresta que deseja testar
aresta_teste = (1, 2) 

if grafo.verifica_ponte(*aresta_teste):
    print(f"A aresta {aresta_teste} é uma ponte.")
else:
    print(f"A aresta {aresta_teste} não é uma ponte.")
