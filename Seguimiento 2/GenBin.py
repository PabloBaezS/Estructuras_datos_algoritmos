from collections import deque

n = int(input())
lista = [0]*n
cola = deque()
cola.appendleft("1")
i = 0
for _ in range(n):
    if i < n-1:
        primero = cola.pop()
        lista[i] = primero
        cola.appendleft(primero+"0")
        cola.appendleft(primero+"1")
        i+=1
    elif i == n-1:
        primero = cola.pop()
        lista[i] = primero
        cola.appendleft(primero+"0")
        cola.appendleft(primero+"1")
        i+=1
print(lista)