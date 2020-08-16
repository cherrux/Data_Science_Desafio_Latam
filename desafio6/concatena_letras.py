import string

n_letras = int(input("ingrese el numero del abecederia para mostrar hasta esa letras"))

def gen (n_letras):
    return ( string.ascii_lowercase[0:n_letras])
print(gen(n_letras))