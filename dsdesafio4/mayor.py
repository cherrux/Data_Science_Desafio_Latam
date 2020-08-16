import sys

#Se pide crear el programa mayor.py , este script debe tomar los 3 argumentos y determinar cuál es
#el mayor

print(" ingrese tres numeros int ej. 20 500 3")
n1=int(sys.argv[1])
n2=int(sys.argv[2])
n3=int(sys.argv[3])
print("primer numero ")
print(n1)
print("segundo numero ")
print(n2)
print("tercer numero ")
print(n3)

#los 3 numeros iguales
if n1==n2 and n3==n2:
    print(f"los tres numeros son iguales {n1}")
# n1 >n2  and n1 >n3 mayor n3
elif n1>n2 and n1>n3:
    print(f"primer numero es el mayor :{n1}")

elif n2>n1 and n2>n3:
    print(f"segundo numero  es el mayor :{n2}")
 #probar sin validacion   
else :
    print(f"tercer numero  es el mayor :{n3}")