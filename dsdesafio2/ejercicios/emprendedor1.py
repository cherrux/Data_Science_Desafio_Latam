import sys
import math

precioventa = float(sys.argv[1])
usuarios = float(sys.argv[2])
gastos = float(sys.argv[3])

utilidades = (precioventa*usuarios)-gastos

if utilidades > 0:
    impuestosonunrobo = utilidades*0.35
    utilidadesmenposrobodelestado = utilidades-impuestosonunrobo

print('utilidades son:', utilidades)
print(utilidadesmenposrobodelestado)