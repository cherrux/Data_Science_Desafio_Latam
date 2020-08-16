import sys
import random
ancho =int(sys.argv[1])

salida=""

for i  in range(1,10):
    rand_number  = random.randint(i, ancho)
    salida += " "* rand_number + "*" +"\n"

    for j in range(1, i):
        rand_number_2 = random.randint(j, ancho)
        salida += " "* rand_number_2 + "/" +"\n"
print(salida)
