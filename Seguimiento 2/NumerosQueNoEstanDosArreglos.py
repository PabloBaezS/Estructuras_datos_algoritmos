from collections import defaultdict


def arreglo(arr1, arr2):
    c1 = set(arr1)
    c2 = set(arr2)
    # diccionario= {}

    nuevo = [0] * max(len(c1, c2))

    diccionario = defaultdict(int)
    for i in range(len(c1)):
        diccionario[arr1[i]] = +1

    for i in range(len(c2)):
        diccionario[arr2[i]] = +1

    for i in diccionario.values():
        if i == 1:
            nuevo[i] = i