def caracter(cadena):
    mapa = {}

    if not cadena:
        return ""

    for c in cadena:
        if c == " ":
            continue
        if c not in mapa:
            mapa[c] = 1
        else:
            return c