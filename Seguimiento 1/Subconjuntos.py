# Nombre fichero subconjuntos.py
def subconjuntos(p:str) -> None:
    subconjuntosAUX(p,"")

def subconjuntosAUX(p:str,r:str) -> None:
    if len(p) == 0:
        print(r)
    else:
        primeraLetraDeLaPalabra = p[0]
        palabraSinLaPrimeraLetra = p[1:]
        subconjuntosAUX(palabraSinLaPrimeraLetra,r+primeraLetraDeLaPalabra)
        subconjuntosAUX(palabraSinLaPrimeraLetra,r)

palabra = input()
subconjuntos(palabra)