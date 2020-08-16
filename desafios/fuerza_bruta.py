from itertools import chain
texto =""
intento = 0
salir = 0
clave_usuario = str(input("Ingrese su clave\n")).lower()

def character_range(char1, char2):
    for char in range(ord(char1), ord(char2)+1):
        yield (char)

for letter1 in character_range('a', 'z'): 
    if salir == 1:
        break
    for letter2 in character_range('a', 'z'):
        comparacion = str(chr(letter1)+chr(letter2))
        if  comparacion == clave_usuario:
            print("su clave es: " + comparacion+ "\n")
            print(f"{intento} Intentos")
            salir = 1
            break
        for letter3 in character_range('a', 'z'):
            comparacion = str(chr(letter1)+chr(letter2)+chr(letter3))
            if  comparacion == clave_usuario:
                print("su clave es: " + comparacion+ "\n")
                print(f"{intento} Intentos")
                salir = 1
                break
            for letter4 in character_range('a', 'z'):
                comparacion = str(chr(letter1)+chr(letter2)+chr(letter3)+chr(letter4))
                intento += 1
                if  comparacion == clave_usuario:
                    print("su clave es: " + comparacion+ "\n")
                    print(f"{intento} Intentos")
                    salir = 1
                    break
# creo que tenia que pasar arreglo la palabra ingresada x usuario, pero ya es tarde