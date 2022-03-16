def absoluta(n):
    numAb = abs(n)
    if numAb < 21:
        numFin = 2*(21-numAb)
        diferencia = abs(numFin)
        return diferencia
    else:
        diferencia = 21-numAb

def main():
    num = input()
    print(absoluta(num))

main()