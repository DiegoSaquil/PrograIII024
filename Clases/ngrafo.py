class Grafo:
    def __init__(self):
        self.vertices = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def agregar_arista(self, inicio, fin):
        if inicio in self.vertices and fin in self.vertices:
            self.vertices[inicio].append(fin)
            self.vertices[fin].append(inicio)  # Para un grafo no dirigido

    def _str_(self):
        dot_code = "graph Grafo {\n"
        for vertice, adyacentes in self.vertices.items():
            dot_code += f"  {vertice};\n"
            for adyacente in adyacentes:
                if adyacente > vertice:  # Evitar duplicados en las aristas
                    dot_code += f"  {vertice} -- {adyacente};\n"
        dot_code += "}"
        return dot_code

# Ejemplo de uso
g = Grafo()
g.agregar_vertice('A')
g.agregar_vertice('B')
g.agregar_vertice('C')
g.agregar_vertice('D')
g.agregar_arista('A', 'B')
g.agregar_arista('D', 'A')
g.agregar_arista('C', 'A')
g.agregar_arista('C', 'D')

# Generar el archivo .dot
with open("grafo.dot", "w") as file:
    file.write(str(g))