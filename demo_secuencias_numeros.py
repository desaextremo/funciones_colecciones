from funciones_captura import limpiar_pantalla,leer_entero

limpiar_pantalla()

print(f"Imprime los numeros entre 0 y 9")
for numero in range(0,10,1):
    print(f"Numero {numero}")
print(f"_________________________________")
print(f"Imprime los numeros entre 0 y 9")
for numero in range(10):
    print(f"Numero {numero}")
print(f"_________________________________")
print(f"Imprime los numeros entre 1 y 10")
for numero in range(1,11):
    print(f"Numero {numero}")

''' Esto lo haciamos con otros lenguajes
print(f"_________________________________")
print(f"Imprime los numeros pares entre 1 y 10")
for numero in range(1,11):
    if (numero % 2 == 0):
        print(f"Numero {numero}")
'''


limite = leer_entero("Ingresa el limite para generar los número pares:",
                     "☠️ Debes ingresar un número entero ☠️")
sumatoria_pares=0
print(f"_________________________________")
print(f"Imprime los numeros pares entre 1 y 10")
for numero in range(2,limite+1,2):
    print(f"Numero {numero}")
    sumatoria_pares = sumatoria_pares + numero

print(f"La sumatoria de los {limite} pares es : {sumatoria_pares}")
