#Importamos la clase "deque" desde el modulo "collections", "deque" se utilizara para implementar una cola de doble extrema
from collections import deque
#definimos una funcion revertirmitad que toma "cola" como argumento
def revertirmitad(cola):
    pila = []
#Calcula la longitud de la cola y la divide por dos para obtener la mitad de la longitud
    longitud = len(cola)
    mitad = longitud // 2
#Transfiere la primera parte de los elementos de la cola a la pila utilizando el metodo.poplef() que elimina y devuelve el mas antiguo
    for _ in range(mitad):
        pila.append(cola.popleft())
#Transfiere la segunda parte de los elementos de la cola a la pila utilizando el metodo.pop() que elimina y devuelve el ultimo elemento de la cola 
    for _ in range(mitad):
        pila.append(cola.pop())
#Si la longitud de la cola es impar, extrae el ultimo elemento de la pila y lo agrega de nuevo a la cola
    if longitud % 2 !=0:
        cola.append(pila.pop())
#Transfiere todos los elementos de la pila de nuevo a la cola utilizando .appendleft(pila.pop())
    while pila:
        cola.appendleft(pila.pop())
#devuelve la cola modificada
    return cola

en_cola = deque([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Cola original:", en_cola)
en_cola = revertirmitad(en_cola)
print("Cola con la mitad revertida:", en_cola)  