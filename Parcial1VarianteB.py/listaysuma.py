def suma_lista(lista):
    suma = 0
    for elemento in lista:
        suma += elemento
    return suma

mi_lista = [10, 20, 30, 40, 50]
resultado = suma_lista(mi_lista)
print(resultado)  