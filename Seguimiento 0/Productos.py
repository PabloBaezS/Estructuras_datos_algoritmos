def segundoyultimo(lista):
    if lista[1] > lista[len(lista)-1]:
        print(lista[1]*lista[len(lista)-1])
    if lista[1] < lista[len(lista)-1]:
        print(lista[1]+lista[len(lista)-1])