

def adictos_a_redes(lista):
    resultados =[]
    for i in lista:
        if i > 90:
            resultados.append("mal")
            resultados.append(i)
        else:
            resultados.append("bien")
            resultados.append(i)
    return resultados

listado_adictos =[122112,112,11,1111,33,12,0,12]

print(adictos_a_redes(listado_adictos))


