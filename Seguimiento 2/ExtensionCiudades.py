def extension(arreglo,k):
    arr_ciudades = list(arreglo)
    contador = 0
    for i in range(len(arr_ciudades)):
        for j in range(len(arr_ciudades)-1):
            if i < len(arr_ciudades):
                resta = arr_ciudades[i] - arr_ciudades[j+1]
                if resta == k:
                    contador += 1
    print(contador)
    return contador


def main():
    arreglo = {1110, 956, 1780, 1030, 1020, 1120, 878}
    k = 10
    extension(arreglo, k)


main()
