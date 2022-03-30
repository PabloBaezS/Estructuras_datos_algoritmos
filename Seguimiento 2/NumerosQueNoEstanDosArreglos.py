def arreglo(arr1, arr2):
    c1 = set(arr1)
    c2 = set(arr2)
    diccionario = dict()

    nuevo = []

    for i in c1:
        if i in diccionario:
            diccionario[i] = +1
        else:
            diccionario[i] = 0

    for i in c2:
        if i in diccionario:
            diccionario[i] = +1
        else:
            diccionario[i] = 0

    for key, valor in diccionario.items():
        if valor == 0:
            nuevo.append(key)

    nuevo.sort()

    return nuevo