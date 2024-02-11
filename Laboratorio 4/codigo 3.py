#Definimos una funcion llamada "balanceo" que toma una cadena como argumento
def balanceo(cadena):
    Pila = [] #Inicializa una lista vacia que se llama "pila"
#Itera sobre cada caracter en la cadena proporcionada como argumento
    for caracter in cadena:
        if caracter == '(': #Verifica si el caracter actual es un parentesis de apertura
            Pila.append(caracter)
        elif caracter == ')': #Verifica si el caracter actual es un paretesis de cierre
            if not Pila or Pila.pop() != '(': #Verifica si la pila esta vacia o si el ultimo elemento en la pila no es un parentesis abierto
             return False #Returna si alguna condicion cumple, la cadena esta desbalanceada y devuelve "false"
    return not Pila #Si la iteracion completa no encontro un desequilibrio y la pila esta vacia devuelve "true" 
cadena1 = "()"#true
cadena2 = ")([]{}" #False
cadena3 = ")(" #False
cadena4 = ")[()]" #False
cadena5 = "{[]}" #True

print(balanceo(cadena1))
print(balanceo(cadena2))
print(balanceo(cadena3))
print(balanceo(cadena4))
print(balanceo(cadena5))