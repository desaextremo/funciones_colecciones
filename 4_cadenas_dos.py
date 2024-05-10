'''
Recorrido de una cadena
'''
from funciones_captura import limpiar_pantalla, leer_cadena

#cadena = input("Ingresa una cadena de caracteres:\n")
cadena = leer_cadena("Ingresa una cadena de caracteres....",
                    "🛑Debe ingresar una cadena de caracteres... 🛑")

print(f"Cadena de caracteres ingresada\n{cadena}")

for caracter in cadena:
    print(caracter)


print(f"Contenido de la posición 1 : {cadena[1]} \nContenido de la posición -1(última) : {cadena[-1]}")