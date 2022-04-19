from collections import deque

def mensaje(s):
    pila = deque()
    open = '('
    close = ')'
    contador = 0

    for i in s:
        if i in open:
            pila.append(i)
        elif i in close:
            pos = close.index(i)
            if len(pila) > 0 and (open[pos] == pila[len(pila) - 1]):
                pila.pop()
                contador += 2
    if len(pila) == 0:
        return contador
    else:
        return contador