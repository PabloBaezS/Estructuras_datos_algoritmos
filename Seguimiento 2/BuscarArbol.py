class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


def buscar(raizDeUnArbol: Nodo, loQueEstaBuscando: int):
    if raizDeUnArbol is None:
        return False
    if raizDeUnArbol.dato == loQueEstaBuscando:
        return True
    else:
        estaPorLaIzquierda = buscar(raizDeUnArbol.izq, loQueEstaBuscando)
        estaPorLaDerecha = buscar(raizDeUnArbol.der, loQueEstaBuscando)
        if estaPorLaIzquierda:
            return True
        if estaPorLaDerecha:
            return True
        return False


n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)

n1.izq = n2
n1.der = n3
n2.der = n4
n4.der = n5

print(buscar(n1, 3))
print(buscar(n1, 9))
