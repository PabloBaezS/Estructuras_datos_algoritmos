def factorial(n) -> int:
    result = 0
    if n == 0 or n == 1:
        result = 1
    elif n>1:
        result = n * factorial(n-1)
        factorial(n-1)
    return result

def main():
    n = int(input())
    print(factorial(n))

main()