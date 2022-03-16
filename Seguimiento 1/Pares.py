def pares(n,i):
    if n <= 0:
        return 0
    else:
        print(i)
        return pares(n-2,i+2)

def main():
    n = int(input())
    i = 2
    pares(n,i)

main()

