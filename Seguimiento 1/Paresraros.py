def pares(n,i):
    if n <= 1:
        return 0
    elif i == 6 or i == 8:
        return pares(n-2,i+2)
    else:
        print(i)
        return pares(n-2,i+2)

def main():
    n = int(input())
    i = 2
    pares(n,i)

main()

