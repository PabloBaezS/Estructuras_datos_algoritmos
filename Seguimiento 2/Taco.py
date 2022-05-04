from collections import deque

totMenu = int(input())
cont = 0
acumClientes = []
clientes = 0
numTacos = []
tacosVen = 0
while(cont<totMenu):
    menu = list(map(int, input().split(" ")))
    if menu[0] == 1:
        num2 = menu[1]
        numTacos.append(num2)
        clientes += 1
        acumClientes.append(clientes)
        cont += 1
    elif menu[0] == 2:
        del acumClientes[0]
        tacosVen += numTacos[0]
        del numTacos[0]
        cont += 1
    elif menu[0] == 3:
        print(len(acumClientes))
        cont += 1
    elif menu[0] == 4:
        sum = 0
        for i in range(len(acumClientes)):
            sum += acumClientes[i]
        print(sum)
        cont += 1