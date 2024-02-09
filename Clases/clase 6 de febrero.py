#cartas = []

#permitir insertar datos en la lista
#cartas.append('c')
#cartas.append('a')
#cartas.append('t')
#cartas.append('g')

#print(cartas, "\n")

#ultimo_elemento = cartas.pop(0)
#print(ultimo_elemento, "\n")

#ultimo_elemento = cartas.pop(2)
#print(ultimo_elemento, "\n")

#print(cartas, "\n")

#from collections import deque
#import time

#def simular_linea_espera(clientes):
#    queue = deque(clientes)
#    while queue:
        #print(("Atendiendo al cliente"), queue.popleft())
#        time.sleep(1)
#clientes_en_espera = ["cliente1", "cliente2", "cliente3", "cliente4"]

#print("Bienvenido al banco, se le atendera proximamente segun el orden")
#simular_linea_espera(clientes_en_espera)
#print("Todos los clientes han sido atendidos")


#Hacer una pila para revertir una lista
def revertir_lista(lista):
    pila = []
    #inserte en la pila
    for elemento in lista:
        pila.append(elemento)
    lista_revertida = []
    #extrae luego inserta
    while pila:
        lista_revertida.append(pila.pop())
    return lista_revertida

lista_original = [1,2,3,4,5]
lista_revertida = revertir_lista (lista_original)

print(lista_original,"\n")
print(lista_revertida,"\n")