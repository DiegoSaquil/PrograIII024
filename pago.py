nombre = str(input("por favor coloque su nombre completo: " ))
horaslaborales = float(input("Por favor coloque el numero de horas que trabaja: "))
costodehora = float(input("Por favor coloque cuanto gana por hora: "))
semana = int(5)
mes = int (4)

sueldopordia = (costodehora * horaslaborales)
sueldo = (sueldopordia*semana*mes)

print(f"Buen día {nombre} a usted le corresponde un pago de: Q{sueldopordia} por día y un sueldo de: Q{sueldo} al mes.")