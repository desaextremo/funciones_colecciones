'''
Genera números pares entre 1 y 10
'''
from funciones_captura import *

limpiar_pantalla()

#for <variable> in <iterable>:
#range(inicio,fin,paso o cada cuantos)

print("Secuencia de números entre 0 y 9")
for par in range(10):
	print(f"número :\t{par}")

print("____________________________________________________")
#range(inicio,fin,paso o cada cuantos)
print("Secuencia de números entre 1 y 10")
for par in range(1,11):
	print(f"número :\t{par}")


limite = leer_entero("Ingrese el valor límite para generar la sumatoria de #ros pares:",
"Debe ingresar un número entrero 🛑...\t")
print("____________________________________________________")
#range(inicio,fin,paso o cada cuantos)
sumatoria_pares = 0
print(f"Secuencia de números pares entre 1 y {limite}")

for par in range(2,limite + 1,2):
    print(f"número :\t{par}")
    sumatoria_pares =sumatoria_pares + par

print(f"La suma de los {limite} número pares es:\t {sumatoria_pares}")    