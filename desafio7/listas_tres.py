from velocidad import promedio, velocidad
from listas_uno import lista

lista_1 = []

for i in lista:
    lista_1.append(i[1])

#promedios_autos
promedios_autos=promedio(lista_1)

for i in lista:
    if (i[1]) > promedios_autos:
        print(i[0])
        print(i[1])
