from collections import deque


input()
cadenaConLaSegundaLinea = input()
listaDeElementos = cadenaConLaSegundaLinea.split(" ")
cola = deque()
for elemento in listaDeElementos:
    cola.appendleft(elemento)
while len(cola) != 0:
    elemento = cola.pop()
    print(elemento)