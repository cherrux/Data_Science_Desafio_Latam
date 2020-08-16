

#funcion imprimir menu, se ingresan numeros para el menu del cajero

def imprimir_menu():
    print('Bienvenido al portal del Banco Amigo. Escoja una opción:')
    print('1. Consultar saldo')
    print('2. Hacer depósito')
    print('3. Realizar giro')
    print('4. Salir')

#funcion depositar 
def depositar(saldo, cantidad):
    saldo = saldo + cantidad
    return saldo

#funcion para girar,valida si tiene saldo igual o menor retira y resta del saldo en caso contrario no retira.
def girar(saldo, cantidad):
    if saldo >= cantidad:
        #print(f"Tu saldo :{saldo} es suficiente para retirar: {cantidad} \n")
        saldo = saldo - cantidad
        return saldo
    else:
        #print(f"Tu saldo :{saldo} es insuficiente para retirar: {cantidad} \n")
        return saldo


def mostrar_menu( saldo = 0):
    opt_menu = 0
    cantidad = 0
    while opt_menu != '4' or opt_menu != '4':
        saldo_actual = f"Tu saldo actual es :{saldo} \n"
        imprimir_menu()  # Se llama a la función

        opt_menu = input()

        if opt_menu == '1':
            print('Realizando acción 1')
            print(saldo_actual)
            
        elif opt_menu == '2':
            print('Realizando acción 2')
            print(saldo_actual)
            cantidad = int(input("ingrese cantidad a depositar \n"))
            saldo = (depositar (saldo, cantidad))
            print(f"Tu saldo actual es :{saldo} \n")
        
        elif opt_menu == '3':
            print('Realizando acción 3')
            print(saldo_actual)
            if saldo > 0 :
                cantidad = int(input("ingrese cantidad a girar \n"))
                saldo = (girar (saldo, cantidad))
            else:
                print("No puedes realizar giro. su saldo es 0")
            print(f"Tu saldo actual es :{saldo} \n")
        elif opt_menu == '4' or opt_menu == '4':
            print('Saliendo')
        else:
            print('Opción inválida')
            print()
mostrar_menu(0)