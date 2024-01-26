#primer metodo capitalize
texto = "hola mundo"
resultado = texto.capitalize()
#print(resultado)

#segundo metodo finds
texto = "que tal gente"
resultado = texto.find("gente")
#print(resultado)

#tercer metodo center (centra el textoe en un conjunto de caracteres)
texto = "Hola mundo"
resultado = texto.center(500,'*')
#print(resultado)

#cuarto metodo isalnum() devuelve true si todos los caracteres son alfanumericos
texto = "Diego12345"
resultado = texto.isalnum()
#print(resultado)

#quinto metodo isdigit() devuelve true los caracteres si son digitos
texto = "150294"
resultado = texto.isdigit()
#print (resultado)

#sexto metodo islower() devuelve true si todos los caracteres estan en minuscula
texto = "Diego"
resultado = texto.islower()
#print(resultado)

#septimo metodo isspace() devuelve true si todos los caracteres son espacios en blanco
texto = "           "
resultado = texto.isspace()
#print(resultado)

#octavo metodo lstrip () elimina los espacios en blanco
texto = "             diego fernando          "
resultado = texto.lstrip()
#print(resultado)

#noveno metodo replace() devuelve una copia de la cadena con los blancos iniciales donde se han sustitudo todas las apariciones de la cadena v or n
texto = "metodo "
resultado = texto.replace("metodo", "Hola")
#print(resultado)

