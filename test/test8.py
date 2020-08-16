import random

def fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    print("La temperatura es de {} grados Celsius".format(celsius))
fahrenheit(random.randint(1, 100))
