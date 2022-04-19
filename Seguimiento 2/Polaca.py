from collections import deque

def laPolaca(pila, ultimo):
    if ultimo == "+":
        n1 = pila.pop()
        if type(n1) == str:
            result = laPolaca(pila,n1)
            operacion = pila.pop()
            return laPolaca(pila, operacion) + result
        else:
            n2 = pila.pop()
            return laPolaca(pila,n1) + laPolaca(pila,n2)
    elif ultimo == "-":
        n1 = pila.pop()
        if type(n1) == str:
            result = laPolaca(pila,n1)
            operacion = pila.pop()
            return laPolaca(pila, operacion) - result
        else:
            n2 = pila.pop()
            return laPolaca(pila,n2) - laPolaca(pila,n1)
    elif ultimo == "*":
        n1 = pila.pop()
        if type(n1) == str:
            result = laPolaca(pila,n1)
            operacion = pila.pop()
            return laPolaca(pila, operacion) * result
        else:
            n2 = pila.pop()
            return laPolaca(pila,n1) * laPolaca(pila,n2)
    elif ultimo == "/":
        n1 = pila.pop()
        if type(n1) == str:
            result = laPolaca(pila,n1)
            operacion = pila.pop()
            return laPolaca(pila, operacion) / result
        else:
            n2 = pila.pop()
            return laPolaca(pila,n2) / laPolaca(pila,n1)
    else:
        return ultimo

numeros = map(str, input().split(" "))
stack= deque()
for numero in numeros:
    if numero == "/" or numero == "*" or numero == "+" or numero == "-":
        stack.append(numero)
    else :
        stack.append(int(numero))
ultimo = stack.pop()
print(laPolaca(stack, ultimo))