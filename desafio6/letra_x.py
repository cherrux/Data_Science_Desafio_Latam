
n = int(input("ingrese tamaño de letra X \n"))
i = 1
j = 1
for i in range(n):
    for j in range(n):
        # si i es igual a j imprime * esto se da en \ de x
        # negativo si i es igual a j imprime * esto se da en / de x, para que de esto hay restar - 1 a J inicia en 0
        if (i == j) or ((n - j-1) == i):
        #  test  print('*', end = f"{i}{j}"  end para conservarlo en la linia en p3 )
            print('*', end = f" ")
        else:
        #   test print("_", end = f"{i}{j}")
            print(" ", end = f" ")
    print('')