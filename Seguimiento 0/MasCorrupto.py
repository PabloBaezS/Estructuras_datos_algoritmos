def mascorrupto(lista):
    mas= 0
    x = 1
    cont = 0
    while cont < 3:
        if lista[x]>mas:
            mas=lista[x]
            x += 2
            cont += 1
        else:
            x += 2
            cont += 1
    nombreprev = lista.index(mas)
    nombre = lista[nombreprev - 1]
    return nombre
