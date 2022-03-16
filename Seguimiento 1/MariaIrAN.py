# Tomado de internet
def Maria(N, arr, energia, saltos, indice, contador):
    if energia <= 0 or indice == len(arr) - 1:
        if indice + 1 == len(arr) or indice + saltos == N:
            return True
        else:
            return False
    else:
        if saltos >= 0:
            if arr[indice] < arr[indice + 1]:
                a = gastoDeEnergia(arr, indice, saltos)
                return Maria(N, arr, energia - a, saltos - 1, indice + saltos, contador + 1)
            elif arr[indice] >= arr[indice + 1]:
                a = gastoDeEnergia(arr, indice, saltos)
                return Maria(N, arr, energia - a, saltos, indice + 1, contador + 1)


def gastoDeEnergia(arr, i, k):
    return abs(arr[i] - arr[k + i])


def main():
    arr = []
    N = int(input())
    for i in range(N):
        arr.append(int(input()))
    energy = int(input())
    jumps = int(input())
    print(Maria(N, arr, energy, jumps, 0, 0))


main()