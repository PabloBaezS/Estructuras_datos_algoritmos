def palindromo_recursivo(cadena, inicio, fin):
    if inicio >= fin:
        return True
    if cadena[inicio] == cadena[fin]:
        return palindromo_recursivo(cadena, inicio + 1, fin - 1)
    else:
        return False

def main():
    cadena = input()
    inicio = 0
    fin = len(cadena)-1
    print(palindromo_recursivo(cadena,inicio,fin))

main()