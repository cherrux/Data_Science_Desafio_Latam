import sys
import math

precioventa = float(sys.argv[1])
usuariostotal = float(sys.argv[2])
usuariosp2 = float(sys.argv[3])
usuarios0 = float(sys.argv[4])
gastos2 = float(sys.argv[5])
utilidades2 = float()


if usuariostotal > (usuariosp2+usuarios0):
    usuariospagap1 = usuariostotal-usuariosp2-usuarios0
    print("if 1")
    print(usuariospagap1)
    utilidades2 = (precioventa*(usuariosp2*2+usuariospagap1)-gastos2)
    print('untilidades libre impuestos', utilidades2)
else:
    print('valores ingresado ', usuariospagap1,
          ' tiene que ser mayor a la suma de', usuariosp2, usuarios0)
if utilidades2 > 0:
    robodelestado = utilidades2*0.35
    utilidadedluegodelacomiciondelestado = utilidades2-robodelestado
    print('utilidades con impuestos:', utilidadedluegodelacomiciondelestado)
else:
    print(utilidades2)