'''
Recorrido de una cadena
'''
from funciones_captura import limpiar_pantalla, leer_cadena, tiempo_espera

limpiar_pantalla()

#cadena = input("Ingresa una cadena de caracteres:\n")
cadena = leer_cadena("Ingresa una cadena de caracteres....",
                    "🛑Debe ingresar una cadena de caracteres... 🛑")

print(f"Cadena de caracteres ingresada\n{cadena}")

#contar vocales
contador_vocales=0
for caracter in cadena:
    print(caracter)
    if ((caracter.upper() == "A") or 
        (caracter.upper() == "E") or 
        (caracter.upper() == "I") or 
        (caracter.upper() == "O") or 
        (caracter.upper() == "U")):
        contador_vocales = contador_vocales + 1
        tiempo_espera(1)


print(f"La cantidad de vocales en la cadena {cadena}\nEs:{contador_vocales}")
try:
    print(f"Contenido de la posición 1 : {cadena[5]} \nContenido de la posición -1(última) : {cadena[-1]}")
except IndexError as ie:
    print(f"No existe la posición 5 en la cadena {cadena}\n{ie}")

