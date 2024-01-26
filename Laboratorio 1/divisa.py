def conversion_de_moneda(dolares, cambio):
    quetzales = dolares * cambio
    return quetzales

cambioactual = 7.83

ingresodolar = float(input("ingrese la cantidad de dolares para la conversión: "))

quetzalesoutput = conversion_de_moneda(ingresodolar,cambioactual)

print(f"{ingresodolar} dolares equivalen a {quetzalesoutput} Quetzales con un cambio de: {cambioactual}")
