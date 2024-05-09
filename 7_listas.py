'''
Métodos principales:
• append(elemento): Agrega un elemento al final de la lista.
• insert(posición, elemento): Inserta un elemento en la posición especificada.
• remove(valor): Elimina la primera aparición del valor especificado.
• pop([índice]): Elimina y devuelve el elemento en la posición especificada (o el 
                 último si no se especifica ninguna posición).
• index(valor): Devuelve el índice de la primera aparición del valor especificado.
• count(valor): Devuelve el número de veces que aparece un valor en la lista.
• sort(): Ordena la lista de forma ascendente.
• reverse(): Invierte el orden de los elementos en la lista.
'''
from funciones_captura import limpiar_pantalla

#Invoca la función para borrado de pantalla
limpiar_pantalla()

#definir una lista
numeros = [1,2,3,4,5]

#imprimir una lista
print(f"imprimir una lista:\t{numeros}")

#acceder a un elemento de la lista
print("numeros[0] elemento en la posicion 0")
print(f"Elemento de la lista en la posicion 0 es:\t {numeros[0]}")

#obtendremos un error si intentamos acceder a un elemento de la lista que no existe
#print(f" elemento de la lista en la posicion 0 {numeros[5]}")

#lista de valores fijos de 12 posiciones para almacenar las cuotas de cada mes
#de esta manera también es posible crear una lista
cuotas = [0] * 12
print("_________________________________________________________________________")
#imprime lista
print("Esta instrucción crea una lista vacia de 12 posiciones:\t'cuotas = [0] * 12'")
print(f" lista de cuotas {cuotas} de su ahorro")

#solicita el valor de la cuota para cada uno de los 12 meses
for mes in range(12):
    cuota = float(input(f"Ingresa el valor de la cuota para el mes {mes + 1} :\t "))
    #almacena la cuota en la lista
    cuotas[mes] = cuota
print("_________________________________________________________________________")
#imprime la lista
print("imprime la lista 'cuotas'")
print(f" lista de cuotas {cuotas}")

iterador=1
#Recorre e imprime la lista
print(f"Contenido de la lista: indice: valor")
for valor_cuota_mes in cuotas:
    print(f"Cuota del mes \"{iterador} \" es: \"{valor_cuota_mes}\"")
    iterador=iterador+1

#unir listas: concatenar listas
dias_semana = [1,2,3,4,5,6,7]
nombres_meses=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
dias_semana +=nombres_meses
print("_________________________________________________________________________")
print("se une la lista 'dias_semana' con la lista 'nombres_meses'")
print(dias_semana)

#Crear lista vacia, otra forma
salarios = list()
diez = list(range(10))
diez_v2 = list(range(1,11))
print("_________________________________________________________________________")
print(f"Lista 'salarios' vacia ")
print(salarios)
print("_________________________________________________________________________")
print(f"Lista 'diez' conformada por los números entre 0 y 9 ")
print(diez)
print("_________________________________________________________________________")
print(f"Lista 'diez_v2' conformada por los números entre 1 y 10 ")
print(diez_v2)

#Slicing: acceso a elementos de ua lista
'''
La sintaxis básica del slicing es [start:stop:step], donde:

start: El índice inicial desde el cual comenzar a extraer elementos. 
       Por defecto, es 0 (el primer elemento).
stop:  El índice final hasta el cual extraer elementos.
       Por defecto, es el tamaño de la lista (el último elemento).
step:  El paso o incremento utilizado para seleccionar elementos.
       Por defecto, es 1.
'''

#acceso a partes de una lista
print("_________________________________________________________________________")
print(f"sub lista de 3 elementos iniciando en posicion 0:\t{diez_v2[0:3]}")
print(f"sub lista de elementos pares:\t{diez_v2[::2]}")

#Seleccionar un rango de elementos
lista_uno = [1, 2, 3, 4, 5]
sublista_uno = lista_uno[1:4]  # Selecciona elementos desde el índice 1 hasta el índice 3 (no incluido)
print("_________________________________________________________________________")
print(f"Seleccionar un rango de elementos\nsublista_uno: Salida: [2, 3, 4]")
print(sublista_uno)  # Salida: [2, 3, 4]

#Especificar un paso
lista_dos = [1, 2, 3, 4, 5]
sublista_dos = lista_dos[::2]  # Selecciona cada segundo elemento
print(f"Especificar un paso(desde inicio a fin de 2 en 2):\n{sublista_dos}")  # Salida: [1, 3, 5]

#Seleccionar elementos desde el final:
#indices negativos
lista_tres = [1, 2, 3, 4, 5]
sublista_tres = lista_tres[-3:]  # Selecciona los últimos tres elementos
print(sublista_tres)  # Salida: [3, 4, 5]
