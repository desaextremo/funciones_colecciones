'''
Ejemplo de uso de las funciones existentes en funciones_captura.py
Captura de números enteros, captura de flotantes, limipar pantalla y menu de opciones.

Todas las funciones que se utilizan en este programa se encuentran definidas en el archivo
funciones_captura.py que esta ubicado en el mismo diectorio.


'''
#Referencia a todos las funciones en el archivo .py
from funciones_captura import *

#variables globales
numero_entero=0
numero_flotante=0.0

#limpia pantalla
limpiar_pantalla()

#presenta menu de opciones
menu = '''Menu de opciones
1 Ingresar un número entero
2 Ingresar un número Flotante
3 Terminar
Seleccione una opción\t'''

while(True):
    limpiar_pantalla()
    opcion = presenta_menu(menu,1,3)
    print(f"Opcion seleccionada {opcion}")

    if(opcion==1):
        limpiar_pantalla()
        print(f"Selecciono ingresar entero...{opcion}")
        numero_entero = leer_entero("Ingrese un número entero:\t","el valor ingresado debe ser un número entero...")
        print(f"el número ingresado es: {numero_entero}")
        tiempo_espera(2.5)
    elif(opcion==2):
        limpiar_pantalla()
        print(f"Selecciono ingresar flotante...{opcion}")
        numero_flotante = leer_flotante("Ingrese un número flotante:\t","el valor ingresado debe ser un número flotante...")
        print(f"el número ingresado es: {numero_flotante}")
        tiempo_espera(2.5)
    elif(opcion==3):
        limpiar_pantalla()
        print(f"Selecciono terminar...{opcion}")
        tiempo_espera(2.5)
        break



