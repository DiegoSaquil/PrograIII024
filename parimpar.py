def suma(numuno, numdos):
    adicion = numuno + numdos
    return adicion % 2 == 0
numuno = float(input("Por favor ingrese el primer numero: "))
numdos = float(input("Por favor ingrese el segundo numero: "))

resultado = suma(numuno,numdos)

print(f"La suma de los dos numeros es par: {resultado}")