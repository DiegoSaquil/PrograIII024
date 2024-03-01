#Primera serie:
#1-Diferencia entre lista y diccionario y de un ejemplo: 
#R// Una lista es una coleccion ordenada y mutable de elementos y un diccionario 
# y un diccionario es una coleccion no ordenada y mutable

lista = [1,2,3,4,5]
diiccionario = {
    'clave1' : 'valor1',
    'clave2' : 'valor2',
    'clave3' : 'valor3'
}

#2-Como funciona un ciclo for y de un ejemplo de su uso:
#Es una iteracion donde nosotros establecemos la cantidad de veces que se va a ejecutar, esto se puede hacer en 
#listas, diccionarios, duplas, arreglos, etc

for numero in lista:
    print(numero)

#3-Diferencia entre una funcion y una variable en python:
#Una funcion es un bloque de codigo que se puede llamar varias veces
#Las variables son contenedores para almacenar datos 

##variables
x = 1
y = 4
##Funcion
def suma(num1,num2):
    resultado = num1 + num2
    return resultado 

suma(x,y)

#4-Para que nos es util github y como se puede usar:
#Es una plataforma de desarrollo colaborativa


#5-Escriba una funcion en python que reciba un lista como parametro
#y devuelva la suma de todos los elementos de la lista

def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma+=elemento ##suma = suma + elemento
    return suma 
suma_lista(lista)

#6-Escriba un programa que pida a el usuario una lista de numeros y luego imprima la suma 
#de los numeros pares de la lista
numeros = input("Ingrese una lista de numeros separados por espacios").split
numeros = [int(num)for num in numeros]
suma_pares = suma(num for num in numeros)
print("La suma de los numeros pares es: ",suma_pares)