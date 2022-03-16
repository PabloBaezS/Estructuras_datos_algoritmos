def mascorrupto(lista):
    mas= 0
    x = 1
    cont = 0
    c = 0
    c2 = 0
    if lista[x]>mas:
        mas=lista[x]
        while c == 0 or c == 1:
            lista.pop(c2)
            c += 1
    else:
        while c == 0 or c == 1:
            lista.pop(c2)
            c += 1
    nombreprev = lista.index(mas)
    nombre = lista[nombreprev - 1]

    mascorrupto(lista)
    return nombre



def main():
    lista=["Calvarini",100,"Pinturosky",200,"Tajardini",400]
    print(mascorrupto(lista))

main()