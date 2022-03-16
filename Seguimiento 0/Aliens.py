from io import*
alien = open("aliens.txt", "r")
lista = alien.readlines()
i = 0
poder = 0
mayor = 0
nombre = ""

while i < len(lista):
    texto = lista[i][0:lista[i].find('\n')]
    lista[i] = texto
    lista[i] = lista[i].split(",")
    poder = int(lista[i][1])
    if poder > mayor:
        mayor = poder
        nombre = lista[i][0]
    i += 1
print(nombre)