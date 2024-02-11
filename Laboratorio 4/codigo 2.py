class Cola: #Definí una clase llamada "COLA" que 
#Definimos el metodo "__init__" que es el que contruye la clase, se inicia una nueva instancia de la cola vacia en una lista vacia que servira como cola
    def __init__(self):
        self.listanada = []
#Definimos el metodo "enqueue" que agrega un elemento al final de la cola
    def enqueue(self, elemento):
        self.listanada.append(elemento)
#Definimos el metodo "dequeue" que elimina y devuelve el elemento en el frente de la cola(el primer elemento que fue agregado)
    def dequeue(self):
        if not self.colaVacia():
            return self.listanada.pop(0)
        else:
            return None
#Defini el metodo "front" que devuelve el elemento en el frente de la cola sin eliminarlo
    def front(self):
        if not self.colaVacia():
            return self.listanada[0]
        else:
            return None
#Aqui verifica el codigo si la cola esta vacia
    def colaVacia(self):
        return len(self.listanada) == 0
#Define una funcion que se llama "gente" que toma una lista de elementos como un argumento
def gente(elementos):
    fila = Cola()
#Iteramos sobre cada elemento en la lista "elementos"
    for elemento in elementos:
        fila.enqueue(elemento)
#Imprime un mensaje que indica a quien se atiende en los elementos de la fija con un while que itera mientras la cola"fila" no está vacia
    print("Atención en la fila: ")
    while not fila.colaVacia():
        siguienteElemento = fila.dequeue()
        print("Atendiendo a:", siguienteElemento)
#definimos la lista llamada elementos con algunos cliente y llama a la funcion gente pasando la lista "elementos" como argumento, lo que simula la atencion de los clientes en la fila.
elementos = ["primer cliente", "segundo cliente", "tercer cliente", "cuarto cliente", "quinto cliente"]
gente(elementos)