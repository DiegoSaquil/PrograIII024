def suma_numeros_pares(lista):
    suma = 0
    for numero in lista:
        if numero % 2 == 0:
            suma += numero
    return suma

numeros = input("Ingresa una lista de números separados por espacios: ")
numeros_lista = [int(num) for num in numeros.split()]

suma_pares = suma_numeros_pares(numeros_lista)
print(f"La suma de los numeros pares es: {suma_pares} ")