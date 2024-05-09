from funciones_captura import leer_entero,limpiar_pantalla

#limpiar pantalla
limpiar_pantalla()

#Impresión de secuencia numerica entre 0 y 9
print("______________________________________________________________________")
print("Impresión de secuencia numerica entre 0 y 9")
for i in range(10):
    print(f"numero: {i}")
print("______________________________________________________________________")
print("Impresión de secuencia numerica pares entre 1 y 10")
for i in range(2,11,2):
    print(f"numero: {i}")
print("______________________________________________________________________")
print("Impresión de secuencia numerica impares entre 1 y 10")
for i in range(1,11,2):
    print(f"numero: {i}")    

#Secuencia de fibonacci
print("""
La serie o sucesión de Fibonacci es una secuencia de números que se obtiene comenzando con el 0 y el 1, 
prosigue con la suma de ellos: 0 +1=1, 
a continuación la suma de los dos anteriores: 1 + 1 = 2 y así sucesivamente.
""")
print("______________________________________________________________________")
numero = leer_entero("Ingresa la cantidad de terminos para generar la serie de fibonacci= \t","Debe ingresar un número entero 🛑")

a=1
b=1

if numero==1:
    print('0')
elif numero==2:
    print('0','1')
else:
    print('0')
    print(a)
    print(b)
    for i in range(numero-3):
        total = a + b
        b = a
        a = total
        print(total)