def plantavieja(lista):
    mayor = 0
    cont = 0
    for i in lista:
        if i["antiguedad"] > mayor:
            mayor = i["antiguedad"]
            nombre = i['nombre']
    return nombre


