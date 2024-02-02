def esKmPositivo(kilometros):
    return kilometros > 0

try:
    ingresarKm = float(input("Ingresa la distancia en Kilómetros: "))

    if esKmPositivo(ingresarKm):
        milla = ingresarKm * 0.621371  
        print(f"La conversión de kilometros a millas es de: {round(milla, 2)} millas")
    else:
        print(f"El valor ingresado es de {ingresarKm} y tu valor no puede ser negativo")

except ValueError:
    print("Ingresa un valor valido para el programa")
