def kmamile(km):
    millastotales = km*0.621371
    return  millastotales

Inicio = float(input("Buen día, por favor ingrese los kilometros: "))

millastotales = kmamile(Inicio)
if Inicio > 0:
   
    print(f"Las millas totales son: {round(millastotales, 2)}")

else: 
    millastotales < 0
    print("POR FAVOR INGRESE UN NUMERO POSITIVO ")