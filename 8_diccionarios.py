'''
Métodos principales:
• keys(): Devuelve una vista de todas las claves en el diccionario.
• values(): Devuelve una vista de todos los valores en el diccionario.
• items(): Devuelve una vista de tuplas que contienen las claves y los valores de 
cada par en el diccionario.
• get(clave, valor_predeterminado): Devuelve el valor asociado con la clave 
especificada, o un valor predeterminado si la clave no está presente.
• update(diccionario): Actualiza el diccionario con los pares clave-valor de otro 
diccionario.
• pop(clave[, valor_predeterminado]): Elimina la clave especificada y devuelve su 
valor, o devuelve un valor predeterminado si la clave no está presente
'''
from funciones_captura import limpiar_pantalla

#Se define un diccionario con llave numerica para identificar de forma única
#a cada elemento
usuarios = {
    1: {
        "id": 1,
        "nombres": "Juan",
        "apellidos": "Pérez",
        "direccion": "Calle 123",
        "movil": "123456789",
        "email": "juan@example.com",
        "sexo": "M"
    },
    2: {
        "id": 2,
        "nombres": "María",
        "apellidos": "González",
        "direccion": "Avenida 456",
        "movil": "987654321",
        "email": "maria@example.com",
        "sexo": "F"
    },
    # Agrega más usuarios aquí...
    10: {
        "id": 10,
        "nombres": "Luis",
        "apellidos": "Martínez",
        "direccion": "Plaza 789",
        "movil": "555555555",
        "email": "luis@example.com",
        "sexo": "M"
    }
}

#limipa pantalla
limpiar_pantalla()

#Recorrer las claves del diccionario:
print("Se accede a los datos del diccionario mediantes sus claves\nutilizando la notación diccionario[clave]")
print("______________________________________________________________________________________________________")
for clave in usuarios:
    # Acceder al valor asociado a la clave
    valor = usuarios[clave]
    # Realizar alguna operación con la clave y el valor
    print(clave, valor)

#Recorrer claves y valores al mismo tiempo
'''

'''
print("______________________________________________________________________________________________________")
print("\nSe accede a los datos del diccionario utilizando la notación clave, valor")
print("\nitems(): Devuelve una vista de tuplas que contienen las claves y los valores de cada par en el diccionario.")
print(usuarios.items())
print("______________________________________________________________________________________________________")
for clave, valor in usuarios.items():
    # Realizar alguna operación con la clave y el valor
    print(clave, valor)

print("\nRecorrer solo los valores del diccionario")
print("\nvalues(): Devuelve una vista de todos los valores almacenados en el diccionario. Esta vista de valores puede ser utilizada para recorrer los valores del diccionario en un bucle for u otras operaciones similares.")
print(usuarios.values())
print("______________________________________________________________________________________________________")
#Recorrer solo los valores del diccionario
for valor in usuarios.values():
    # Realizar alguna operación con el valor
    print(valor)