articulos = ["celular", "LG K10", "90000", "tablet", "Galaxy TAB", "80000", "smart tv", "LED 43",
             "Samsung", "485000", "celular", "Galaxy J7", "120000", "celular", "Huawei Y5", "59900", "notebook",
             "Lenovo ideapad", "250000", "tablet", "Huawei media", "139000", "notebook", "Acer", "145000"] 
celulares = []
tablets =[]
smart_tv = []
notebooks = []
aux =""

for index, elemento in enumerate(articulos):
    if index == 0 or index % 3 == 0:
    #es categoria
    aux = elemento
    elif (index - 1) % 3 == 0:
    # es nombre
    elif (index - 2) % 3 == 0:

        