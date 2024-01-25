import cmath 

def datos_para_resolver(a, b, c):
    
    interior = b**2 - 4*a*c

    
    raiz_1 = (-b + cmath.sqrt(interior)) / (2*a)
    raiz_2 = (-b - cmath.sqrt(interior)) / (2*a)

    return raiz_1, raiz_2

a = float(input("Ingrese el coeficiente 'a': "))
b = float(input("Ingrese el coeficiente 'b': "))
c = float(input("Ingrese el coeficiente 'c': "))

# Calcular e imprimir las raíces
raiz_1, raiz_2 = datos_para_resolver(a, b, c)

print(f"Las raíces de la ecuación cuadrática son: {raiz_1} y {raiz_2}")
