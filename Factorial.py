import dis
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        resultado = n * factorial(n-1)
        return resultado

def imprimirSapo():
    print("imprimir sapo")


print(factorial(5))
dis.dis(factorial)
dis.dis(imprimirSapo)