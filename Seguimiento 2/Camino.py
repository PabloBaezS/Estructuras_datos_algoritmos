import collections from collections

def obtenerLosVerticesQueSonVecinosDeUnVertice(matriz, vertice):
    laFilaDondeEstanLosVecinosDeUnVertice = matriz[vertice]
    laListaDeVecinosDeUnVertice = deque()
    for posicion in range(len(laFilaDondeEstanLosVecinosDeUnVertice)):
        if laFilaDondeEstanLosVecinosDeUnVertice[posicion] == 1:
            laListaDeVecinosDeUnVertice.append(posicion)
    return laListaDeVecinosDeUnVertice

def camino(matriz,origen,destino):
    conjuntoDeVisitados = set()
    return camino(matriz,origen,destino,conjuntoDeVisitados)

def camino(matriz,origen,destino,conjuntoDeVisitados):
    if origen == destino:
        return True
    conjuntoDeVisitados.add(origen)
    losVecinos = obtenerLosVerticesQueSonVecinosDeUnVertice(matriz,origen)
    for vecino in losVecinos:
        if vecino not in conjuntoDeVisitados:
            puedoLLegarDelVecinoAlDestino = camino(matriz,vecino,destino)
                if puedoLLegarDelVecinoAlDestino == True:
                    return True
        return False