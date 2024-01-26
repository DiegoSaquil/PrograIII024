entrada_usuario = input("Ingrese un valor: ")

try:
    valor = eval(entrada_usuario)
    tipo_dato = type(valor).__name__
    print("El valor ingresado es de tipo:", tipo_dato)
except:
    tipo_dato = type(entrada_usuario).__name__
    print("El valor ingresado es de tipo:", tipo_dato)

if tipo_dato == "int":
    print("¡El valor ingresado es un número entero!")
elif tipo_dato == "float":
    print("¡El valor ingresado es un número decimal!")
elif tipo_dato == "str":
    print("¡El valor ingresado es una cadena de texto!")
elif tipo_dato == "bool":
    print("¡El valor ingresado es de tipo booleano!")
else:
    print("¡Tipo de dato no identificado!")
