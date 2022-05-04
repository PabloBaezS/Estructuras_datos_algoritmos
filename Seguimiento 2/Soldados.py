from collections import deque
cola = deque()
for i in range(8):
    linea = input()
    if linea == "MANDA":
        if len(cola) == 0:
            print("IMPOSIBLE")
        else:
            print(cola.pop())
    else:
        parte1, parte2 = linea.split(" ")
        cola.appendleft(parte2)
        print(parte2)