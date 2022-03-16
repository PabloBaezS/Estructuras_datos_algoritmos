from collections import deque


def main():
    n = int(input())
    numeros = map(int, input().split(" "))
    pila = deque()
    for numero in numeros:
        pila.append(numero)
    while len(pila) != 0:
        elNumero = pila.pop()
        print(elNumero)


main()
