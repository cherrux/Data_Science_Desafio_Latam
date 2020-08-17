from functools import reduce
from velocidad import promedio
velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
             11, 11, 12, 12, 12, 12, 13, 13,
             13, 13, 14, 14, 14, 14, 15, 15,
             15, 16, 16, 17, 17, 17, 18, 18,
             18, 18, 19, 19, 19, 20, 20, 20,
             20, 20, 22, 23, 24, 24, 24, 24, 25]
distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
             17, 28, 14, 20, 24, 28, 26, 34, 34,
             46, 26, 36, 60, 80, 20, 26, 54, 32,
             40, 32, 40, 50, 42, 56, 76, 84, 36,
             46, 68, 32, 48, 52, 56, 64, 66, 54,
             70, 92, 93, 120, 85]

def zip1 (promedio,velocidad_1,distancia_1):
    velocidad_distancia = []
    velocidad_promedio = promedio(velocidad)
    distancia_promedio = promedio(distancia)



    for i in zip(velocidad_1, distancia_1):
        velocidad_distancia.append((i[0],i[1]))

    print(f" \nvelocidad promedio : {velocidad_promedio} \n")
    print(f"distancia promedio : {distancia_promedio} \n")

    print(f"1 Cantidad de  velocidades bajo promedio  total :{len((list(filter(lambda x: x[0] < velocidad_promedio, velocidad_distancia))))} \n")
    print(f"1 Cantidad de  velocidades bajo promedio y distancia sobre promedio  total :{len((list(filter(lambda x: x[0] < velocidad_promedio and x[1] > distancia_promedio, velocidad_distancia))))} \n")
    print(f"1 Cantidad de  velocidades SOBRE promedio  total :{len((list(filter(lambda x: x[0] > velocidad_promedio, velocidad_distancia))))} \n")
    print(f"1 Cantidad de  velocidades SOBRE promedio y distancia bajo promedio  total :{len((list(filter(lambda x: x[0] > velocidad_promedio and x[1] < distancia_promedio, velocidad_distancia))))} \n")

    # for i in  velocidad_distancia:
    #     if  ((i[0]) < velocidad_promedio) and  ((i[1]) > distancia_promedio):
    #         print(((i[0],i[1])))
    #         c2 += 1
    # print(f"Velocidad bajo el promedio y distancia sobre el promedio son:{c2}\n \n ")

    

    # print(f" distancia superiores al promedio :{(list(filter(lambda x: x > distancia_promedio, distancia_1)))} \n")
    
    # print(f" velocidades superiores al promedio :{(list(filter(lambda x: x > velocidad_promedio, velocidad_1)))} \n")  
    # print(f"distancia promedio : {distancia_promedio} \n")
    

zip1(promedio,velocidad,distancia)