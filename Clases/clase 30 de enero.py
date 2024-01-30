#Ejemplo de operación and:
condicion_and = (5>3) and (10<20)
#print(condicion_and)

#Ejemplo de operador or:
condicion_or = (5>3) and (10<20)
#print(condicion_or)

#Ejemplo de definir
def puede_votar(edad):
    return edad >=18

try: 
    edad_usuario = int(input("Ingresa tu edad: "))
    if puede_votar(edad_usuario):
        print ("PUEDES VOTAR")
    else: 
        print("NO PUEDE VOTAR")
except ValueError:
    print ("INGRESE UN VALOR DE EDAD VALIDO")
