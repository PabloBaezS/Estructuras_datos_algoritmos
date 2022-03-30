class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None


n1 = Nodo(1)
n2 = Nodo(2)
n3 = Nodo(3)
n4 = Nodo(4)
n5 = Nodo(5)

n1.izq = n2
n1.der = n3
n2.der = n4
n4.der = n5

