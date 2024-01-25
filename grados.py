def celsius_a_farenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

celsius_input = float(input("Coloque la temperatura en grados celsius: "))

fahrenheit_output = celsius_a_farenheit(celsius_input)
print(f"{celsius_input} grados Celsius equivalen a {fahrenheit_output} grados fahrenheit ")