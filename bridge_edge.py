import os
import sys

class Grafo:
    def __init__(self, grafo=None):
        self.vertices = set()
        if grafo:
            self.grafo = grafo
            self.atualizar_vertices()
        else:
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

        self.vertices.add(u)
        self.vertices.add(v)

    def atualizar_vertices(self):
        for u in self.grafo:
            self.vertices.add(u)
            for v in self.grafo[u]:
                self.vertices.add(v)

    def carregar_grafo_de_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():
                        source, destination = map(int, line.strip().split())
                        self.adicionar_aresta(source, destination)
        except FileNotFoundError:
            print(f"O arquivo '{arquivo}' não foi encontrado. Usando o grafo predefinido no código.")

    def dfs(self, vertice, visitados):
        visitados.add(vertice)
        num_componentes = 1
        for vizinho in self.grafo.get(vertice, []):
            if vizinho not in visitados:
                num_componentes += self.dfs(vizinho, visitados)
        return num_componentes

    def numero_componentes_conectados(self):
        visitados = set()
        numero_componentes = 0
        for vertice in self.vertices:
            if vertice not in visitados:
                numero_componentes += 1
                self.dfs(vertice, visitados)
        return numero_componentes

    def verifica_ponte(self, u, v):
        if u not in self.grafo or v not in self.grafo[u]:
            print(f"A aresta ({u}, {v}) não existe no grafo.")
            sys.exit() 

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


    def carregar_grafo_de_arquivo(self, arquivo):
        try:
            with open(arquivo, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    if len(parts) == 2:
                        try:
                            source, destination = map(int, parts)
                            self.adicionar_aresta(source, destination)
                        except ValueError:
                            print(f"A linha '{line.strip()}' não possui dois números inteiros válidos e será ignorada.")
                    else:
                        print(f"A linha '{line.strip()}' não possui o formato esperado (dois números inteiros separados por espaço) e será ignorada.")
        except FileNotFoundError:
            print(f"O arquivo '{arquivo}' não foi encontrado. Usando o grafo predefinido no código.")

def main():
    grafo = Grafo()

    # Verificar se o arquivo 'grafo.txt' existe
    if os.path.isfile("grafo.txt"):
        # Caso 1: Carregar grafo de arquivo
        grafo.carregar_grafo_de_arquivo("grafo.txt")
        print("Carregando grafo do arquivo 'grafo.txt'")
        
        # Verificar se o grafo carregado está vazio
        if not grafo.grafo:
            print("O grafo carregado a partir do arquivo está vazio. Usando o grafo predefinido no código.")
            grafo.adicionar_aresta(0, 1)
            grafo.adicionar_aresta(1, 2)
            grafo.adicionar_aresta(2, 3)
    else:
        # Caso 2: Usar grafo predefinido no código
        grafo.adicionar_aresta(0, 1)
        grafo.adicionar_aresta(1, 2)
        grafo.adicionar_aresta(2, 3)
        print("Usando grafo predefinido no código")

    # Forneça a aresta que deseja testar
    aresta_teste = (1, 2)

    if grafo.verifica_ponte(*aresta_teste):
        print(f"A aresta {aresta_teste} é uma ponte.")
    else:
        print(f"A aresta {aresta_teste} não é uma ponte.")

if __name__ == "__main__":
    main()
