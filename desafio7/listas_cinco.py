from velocidad import promedio, velocidad
from listas_uno import lista

lista_1 = []
lista_mayores = []
lista_mayores2 = []

for i in lista:
    lista_1.append(i[1])

#promedios_autos
promedios_autos=promedio(lista_1)

for i in lista:
    if i[1] > promedios_autos:
        lista_mayores.append(i[1])


lista_mayores2 =filter(lambda x: x > promedios_autos, lista_1)
print(lista_mayores)
#operación funcional 
print(list(lista_mayores2))