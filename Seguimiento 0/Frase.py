from io import *
def guardarFrase():
    palabra = str(input())
    numero = int(input())
    frase = open("frase.txt", "w")
    texto = frase.write(palabra+str(numero))
