

def adictos_a_redes2(lista):
    resultados =[]
    for i in lista:
        if i > 180:
            resultados.append("mal")
            resultados.append(i)
        elif i >= 90:
            resultados.append("maoma")
            resultados.append(i)
        else:
            resultados.append("bien")
            resultados.append(i)
    return resultados

listado_adictos =[122112,112,11,1111,33,12,0,12,55555]

print(adictos_a_redes2(listado_adictos))


