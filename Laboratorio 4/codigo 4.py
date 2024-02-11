#importamos la clase "deque" desde el modulo "colllections" para usarla en la implementacion de la cola
from collections import deque

#definimos una clase llamada "colapila" que representa una cola implementada por 2 pilas
class colapila:
    #"__Init__" se inicializa dos listas vacias "self.pilaentra" y "self.pilasale" que seran utilizados como pila
    def __init__(self):
        self.pilaentra = []
        self.pilasale = []
    def enqueue (self, elemento):
        self.pilaentra.append(elemento)

    def dequeue(self):
        if not self.pilasale:
            while self.pilaentra:
                self.pilasale.append(self.pilaentra.pop())
        if self.pilasale:
            return self.pilasale.pop()
        else:
            return None


cola = colapila() #instanciamos
#Ingreso de datos en cola
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)

print(cola.dequeue()) #1
print(cola.dequeue()) #2
print(cola.dequeue()) #3
print(cola.dequeue()) #4
print(cola.dequeue()) #0
print(cola.dequeue()) #None
