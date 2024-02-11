class pila:
    def __init__(self):
        self.cosa = [] #Creamos una lista vacia para modificar los elementos
    def nada(self):
        return len(self.cosa) == 0 #Devuelve si la cola esta vacia o si tiene algun elemento
    def push(self, elemento): #Le indica a la lista vacia que agregara cosas
        self.cosa.append(elemento)
    def pop(self):
        if not self.nada():
            return self.cosa.pop() #El pop elimina y devuelve el elemento de la pila en la parte superior
        else:
            return None
    def peek(self): #peek devuelve el elemento en la parte superior sin eliminar
        if not self.nada():
            return self.cosa[-1]# el -1 devuelve el ultimo elemento de la lista
        else:
            return None

def invertido(cosa):
    #creamos una instancia
    npila = pila()
    for elemento in cosa:
        npila.push(elemento) #Los elementos se agregan a la pila en el orden inverso al original
    
    listainvertida = []
    while not npila.nada():
        listainvertida.append(npila.pop())
    return listainvertida

listaog = [3,5,8,10,11]
print (listaog)
listainvertida = invertido(listaog)
print (listainvertida)