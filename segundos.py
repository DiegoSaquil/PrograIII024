def calculodesegundos(hora, minutos, segundos):
    segundostotales = (hora * 3600) + (minutos * 60) + segundos
    return segundostotales

Bienvenida = print("buen día por favor coloque los siguientes datos: ")
horapresente = int(input("Ingrese la hora actual (en formato de 24 horas): "))
minutopresente = int(input("Ingrese los minutos actuales: "))
segundopresente = int(input("Ingrese los segundos actuales: "))

segundostotales = calculodesegundos(horapresente,minutopresente,segundopresente)

print(f"los segundos totales son:  {segundostotales}")
