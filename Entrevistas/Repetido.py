num = int(input())
cifra = num[0]
numero = str(num)


def repetido(num, cifra):
    num1 = int(str(num[cifra-1]))
    result = 0
    if cifra == 0:
        return 0
    if cifra == num1:
        return repetido(num, cifra +1)
    else:
        result = cifra + result
    print(result)


print(repetido(numero, cifra))