#Impresión de secuencia numerica entre 0 y 9
print("Impresión de secuencia numerica entre 0 y 9")
for i in range(10):
    print(f"numero: {i}")

print("Impresión de secuencia numerica pares entre 1 y 10")
for i in range(2,11,2):
    print(f"numero: {i}")

print("Impresión de secuencia numerica impares entre 1 y 10")
for i in range(1,11,2):
    print(f"numero: {i}")    

numero=0
anterior = 0
print("Impresión de secuencia numerica impares entre 1 y 10")
for i in range(10):
    anterior = numero
    numero = numero + anterior

    print(numero)

    0
    1
    1
    2