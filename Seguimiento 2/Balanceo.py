from collections import deque


def validar(mensaje):
    pila = deque()
    primeros_simbolos = ["[", "{", "("]
    ultimos_simbolos = ["]", "}", ")"]
    for i in mensaje:
        if i in primeros_simbolos:
            pila.append(i)
        elif i in ultimos_simbolos:
            pos = ultimos_simbolos.index(i)
            if len(pila) > 0 and (primeros_simbolos[pos] == pila[len(pila) - 1]):
                pila.pop()
            else:
                return "No"
    if len(pila) == 0:
        return "Yes"
    else:
        return "No"


def main():
    mensaje = input()
    validar(mensaje)
