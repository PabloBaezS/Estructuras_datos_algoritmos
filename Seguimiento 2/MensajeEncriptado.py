from collections import deque
def mensaje(s):
    pila = deque()
    parentesis = {'(': ')'}
    contador = 0
    for c in s:
        if (c in parentesis) == "(":
            pila.append(c)
        elif c in parentesis == ")":
            pila.pop()
            contador += 1
        if contador < 0:
            return 0
    return contador