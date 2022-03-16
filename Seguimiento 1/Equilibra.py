def equilibra(personas):
    personasOrdenado = sorted(personas)
    i = 0
    return equilibraAux(personasOrdenado, i)


def equilibraAux(personasOrdenado, i):
    total = sum(personasOrdenado)
    gr1 = []
    gr2 = []
    if i < (len(personasOrdenado)) / 2:
        gr1.insert(i, personasOrdenado[i])
        gr1.insert(i + 1, personasOrdenado[len(personasOrdenado)-(i+1)])
        gr2.insert(i, personasOrdenado[i + 1])
        gr2.insert(i + 1, personasOrdenado[len(personasOrdenado) - (i+2)])
    return equilibraAux(personasOrdenado, i + 1)

def main():
    personas = list(input())
    equilibra(personas)

main()