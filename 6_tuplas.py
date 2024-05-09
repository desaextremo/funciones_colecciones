''''
Tuplas:
Las tuplas son secuencias inmutables de elementos. Se definen utilizando paréntesis ( ).
Se utilizan cuando necesitas un conjunto de elementos que no cambiarán a lo largo del tiempo.
Ejemplo de definición: mi_tupla = (1, 2, 3, 4, 5)

Métodos principales:
index(valor): Devuelve el índice de la primera aparición del valor especificado.
count(valor): Devuelve el número de veces que aparece un valor en la tupla.
'''

#definir una tupla para los días de la semana
dias_semana=("LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO")

#imprimir la tupla
print(f"dias de la semana {dias_semana}")

#cantidad de elementos de la tupla
#El método index devuelve el índice de la primera aparición de un valor en la tupla.
indice = dias_semana.count("LUNES")
print(f"El índice de la primera aparición del valor LUNES es: {indice}")

# Usando el método count para contar cuántas veces aparece el valor 3 en la tupla
conteo = dias_semana.count("MIERCOLES")
print(f"El valor MIERCOLES aparece {conteo} veces en la tupla") 

#Acceder al valor en una posicion de la tupla
print(f"El contenido de la tupla en la posición 1 es {dias_semana[1]}")


print(f"Imprimir el contenido de la tupla")
#recorrer una tupla
for elemento in dias_semana:
    print(f"valor :{elemento}")

#Slicing (rebanado):
#Puedes obtener subconjuntos de elementos de una tupla utilizando la notación de slicing [inicio:fin].
subtupla = dias_semana[0:2]  # Obteniendo una subtupla desde el elemento 0 hasta el segundo elemento
print("Subtupla:", subtupla)

#Longitud de la tupla usando len(nombre tupla)
print(f"Cantidad de elementos de la tupla: {len(dias_semana)}")

#no puedes modificar el contenido de una tupla, si lo intentas obtendras un error
#dias_semana[0] = "temporal"

#puedes crear una lista a partir de una tupla (aunque veremos las listas mas tarde)
lista_dias_semana = list(dias_semana)
print("Lista creada a partir de la tupla:", lista_dias_semana) 

