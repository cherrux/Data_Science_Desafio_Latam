
n = int(input("ingrese tamaño de letra i "))

superior_inferior = ""
medio = ""
simple = 0
n_mitad =0
mitad =""
inpar =""

if n % 2 ==0:
    simple = 1

m_mitad = int(round(n/2, 0))

for i in range(m_mitad-simple):
    mitad += " "

for i in range(n):
    superior_inferior += "*"

for i in range(n):
    if simple != 0:
        inpar = "*"
    if i % 2 ==0:
        medio += mitad +inpar+"*\n"
print(superior_inferior)
print(medio)
print(superior_inferior)