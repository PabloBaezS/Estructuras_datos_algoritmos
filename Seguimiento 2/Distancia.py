def minDist(arr, n, x, y):
    min_dist = 99999999
    print(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if (x == arr[i] and y == arr[j] or y == arr[i] and x == arr[j]) and min_dist > abs(i - j):
                min_dist = i - j
    return min_dist


def main():
    cantNum = int(input())
    numeros = list(map(int, input().split(" ")))
    n = len(numeros)
    for i in range(len(numeros)):
        x = numeros[i]
        y = numeros[i]
        minDist(numeros, n, x, y)


main()
