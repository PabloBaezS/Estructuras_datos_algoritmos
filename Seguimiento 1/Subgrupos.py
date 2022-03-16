def subgrupos(A, k):
    return g3(A, k, 0)


def g3(A, k, s) -> bool:
    return k == 0 if s == len(A) else g3(A, k, s + 1) or g3(A, k - A[s], s + 1)


def main():
    n, k = map(int, input().split(" "))
    A = list(map(int, input().split(" ")))
    r = subgrupos(A, k)
    print("YES") if r else print("NO")


main()