numero_usuario = int(input("Ingrese un número\n"))
i = 1
suma = 0
while i <= numero_usuario:
    if i % 2 ==0:
        suma += i        
    i += 1
print(suma)