def cantidaddex(cadena: str) -> int:
    return cantidaddexAUX(cadena, 0)


def cantidaddexAUX(cadena, i):
    if i == len(cadena):
        return 0
    else:
        sienihayx = 1 if cadena[i] == "x" else 0
        return cantidaddexAUX(cadena, i + 1) + sienihayx


def main():
    cadena = input()
    print(cantidaddex(cadena))


main()