import sys
import math
from random import seed
from random import randint

#Para que el computador pueda jugar escogerá un número al azar entre 1 y 3, siendo:
# 1: piedra
# 2: papel
# 3: tijera
# print("ingresa piedra,papel o tijera")
usuario = str(sys.argv[1])
if usuario == "piedra":
    mano = int(1)
elif usuario == "papel":
    mano = int(2)
elif usuario == "tijera":
    mano = int(3)
else:
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
    mano = 0
# jugador computador
computador = randint(1, 3)

pctext = str()
if computador == 1:
    pctext = "piedra"
if computador == 2:
    pctext = "papel"
if computador == 3:
    pctext = "tijera"


if computador == mano:
    print("Computador juega "+pctext)
    print("Empataste")

# pc piedra y usuario papel gana humano
elif computador == 1 and mano == 2:
    print("Computador juega "+pctext)
    print("Ganaste")
# pc piedra y usuario tijera pierde humano
elif computador == 1 and mano == 3:
    print("Computador juega "+pctext)
    print("Perdiste")
# pc papel y usuario piedra piedre humano
elif computador == 2 and mano == 1:
    print("Computador juega "+pctext)
    print("Perdiste")
# pc  papel y usuario tijera gana humano
elif computador == 2 and mano == 3:
    print("Computador juega "+pctext)
    print("Ganaste")
# pc tijera y usuario piedra gana humano
elif computador == 3 and mano == 1:
    print("Computador juega "+pctext)
    print("Ganaste")
# pc tijera y usuario  papel pierde humano
elif computador == 3 and mano == 2:
    print("Computador juega "+pctext)
    print("Perdiste")