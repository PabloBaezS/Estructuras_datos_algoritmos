def reemplazoXY(cadena: str) -> int:
    return replaceChar(cadena, "x", "y")


def replaceChar(inval, old, new):
    if inval == '':
        return ''
    if inval[0] == old:
        return new + replaceChar(inval[1:], old, new)
    return inval[0] + replaceChar(inval[1:], old, new)


def main():
    cadena = input()
    print(reemplazoXY(cadena))


main()