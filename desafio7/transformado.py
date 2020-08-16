def to_minutes(lista):
    resultados = []
    for i in lista:
        resultados.append(i // 60)
    return resultados

secundos = [100,50,1000,5000,1000,500]

print(to_minutes(secundos))