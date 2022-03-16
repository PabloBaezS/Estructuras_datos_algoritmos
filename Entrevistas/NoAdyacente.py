cant = int(input())
lista = []
while cant >= 1:
    num1 = int(input())
    lista.append(num1)
    cant = cant - 1
resultado = int(input())
respuestas = []

def f(result) -> bool:
    if cant == 0:
        return True
    if resultado < 0:
        print(0)
        return False
    temp = 0
    resp1 = 0
    resp2 = 0
    x = 0
    if x == 1:
        while temp < (len(lista)/2):
            resp1 = lista[temp]
            temp += 2
        respuestas.append(resp1)
    elif x == 2:
        temp = 1
        while temp < (len(lista)/2):
            resp2 = lista[temp]
            temp += 2
        respuestas.append(resp2)
    else:
        return False
    k = 0
    if k < len(respuestas):
        if respuestas[k] == resultado:
             return True
        else:
            k += 1


j = 1
while j <= resultado:
    f(j)
    j += 1

if resultado < 0:
    print(0)
else:
    print(f(resultado))

