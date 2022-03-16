def ToH(n, A, B, C):
    if n == 1:
        print("Mover disco 1 de La vara", A, "a La vara", B)
        return
    ToH(n - 1, A, C, B)
    print("Mover disco", n, "de La vara", A, "a La vara", B)
    ToH(n - 1, C, B, A)


def main():
    n = int(input())
    A = 1
    B = 3
    C = 2
    ToH(n, A, B, C)
    pasos = (2 ** n) - 1
    print(pasos)


main()