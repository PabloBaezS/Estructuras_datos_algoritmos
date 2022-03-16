def mcd_recur(a,b):
    if b == 0:
        return a
    return mcd_recur(b, a % b)

def main():
    n = int(input())
    n2 = int(input())
    print(mcd_recur(n,n2))

main()