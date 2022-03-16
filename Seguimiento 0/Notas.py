from io import *
notas = open("notas.txt", "r")
texto = notas.read()
lista = texto.split(",")
i = 0
sumatot = 0
while i < len(lista):
    num = float(lista[i])
    sumatot = sumatot + num
    i += 1
promedio = sumatot/len(lista)
print(promedio)