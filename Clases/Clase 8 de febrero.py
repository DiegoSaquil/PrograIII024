#lista

numero = [1,2,3,4,5,6,7,8,9]
print (numero)
nombre = ["Stevens", "Diego", "Alvaro", "Alejas"]
print (nombre)

mixlista = ["Diego", 1,2,3,4,5]
print (mixlista)

#Diccionario
personas = {
    "Juan" : 20,
    "Diego" : 20,
    "Profesion" : "ingeniero",
    "Salario" : "$2000"
}

print (personas)

edades = {"Juan" : 30, "Maria" : 25, "Lucas" : 18}
print (edades)

#ejemplo de pila
pila = []
pila.append(pila)
sacarlemento = pila.pop()

print ("Pila sin elementos:" , pila)

#Ejemplo de una cola

from collections import deque

cola= deque([11,2,3,4,5])

elemensacar = cola.popleft()

for valor in cola:
    print("Elemento sacando de la cola: \n", valor) 