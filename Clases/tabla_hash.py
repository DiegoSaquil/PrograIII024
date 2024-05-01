def contar_frecuencia_palabras(texto):
    # Creamos un diccionario para almacenar las frecuencias de las palabras
    frecuencia_palabras = {}

    # Dividimos el texto en palabras utilizando el espacio como separador
    palabras = texto.split()

    # Iteramos sobre cada palabra en el texto
    for palabra in palabras:
        # Si la palabra ya está en el diccionario, incrementamos su frecuencia
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        # Si la palabra no está en el diccionario, la agregamos con frecuencia 1
        else:
            frecuencia_palabras[palabra] = 1

    # Retornamos el diccionario con las frecuencias de las palabras
    return frecuencia_palabras

# Ejemplo de uso
texto_ejemplo = "Python es un lenguaje de programación, y Python es fácil de aprender."
frecuencia = contar_frecuencia_palabras(texto_ejemplo)
print("Frecuencia de palabras:")
for palabra, frecuencia in frecuencia.items():
    print(f"{palabra}: {frecuencia}")



'''Salida:
Frecuencia de palabras:
Python: 2
es: 1
un: 1
lenguaje: 1
de: 1
programación,: 1
y: 1
fácil: 1
aprender.: 1


Este ejemplo utiliza un diccionario (frecuencia_palabras) como una tabla hash para almacenar la frecuencia de cada palabra en el texto. Cada palabra actúa como una clave y su frecuencia como el valor asociado. El programa itera sobre cada palabra en el texto, actualizando su frecuencia en el diccionario. Finalmente, se imprime la frecuencia de cada palabra.
'''



