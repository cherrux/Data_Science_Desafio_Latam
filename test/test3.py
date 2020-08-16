n = 5
caja = ""

for i in range(n + 1):
    caja += "*" * i +"\n"
print(caja)

n = 5
caja=""

for i in range(n):
    print(i)
    for j in range(n - i):
            print(i+10)
            print(caja)
            caja += "*"
    caja += "\n"
print(caja)