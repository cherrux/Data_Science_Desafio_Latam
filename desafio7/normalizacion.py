import math

def modulo(lista):
    suma = 0

    for i in lista:
        suma = suma + i ** 2

    return math.sqrt(suma)

def normalizar(lista):
    m = modulo(lista)
    normalizada = []

    for i in lista:
        normalizada.append(i / m)

    return normalizada

output = normalizar([1, 2, 3])
print(output)

suma = 0
for i in output:
    suma += i ** 2
print(suma)

