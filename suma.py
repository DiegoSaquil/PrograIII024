primernum = float(input("Ingrese un número: "))
segundonum = float(input("ingrese un segundo numero: "))

suma = primernum + segundonum
resta = primernum - segundonum
multiplicación = primernum * segundonum

if segundonum != 0:
    division = primernum/segundonum

else:
    division = "NO SE PUEDE DIVIDIR ENTRE CERO"

print(suma)
print(resta)
print(multiplicación)
print(division)