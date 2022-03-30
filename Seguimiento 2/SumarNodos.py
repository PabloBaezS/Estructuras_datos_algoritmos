class Node:
    def __init__(self, dato):
        self.dato = dato
        self.left = None
        self.right = None


def contarNodos(root, cantidad = 0):
    if root is None:
        return cantidad
    else:
        nodoIzquierda = contarNodos(root.left)
        nodosDerecha = contarNodos(root.right)
        yo = 1
        return nodoIzquierda + nodosDerecha + yo


def sumarNodos(root):
    if root is None:
        return 0
    else:
        i = 0
        while i < contarNodos(root, 0):
            i += root.value

    return i


root = Node(1)
nodo2= Node(2)
nodo3= Node(3)
nodo4= Node(4)
nodo5= Node(5)
nodo6= Node(6)
nodo7 = Node(7)

root.left = nodo2
root.right = nodo3
nodo3.left = nodo4
nodo3.right = nodo5
nodo2.left = nodo6
nodo2.right = nodo7

print(sumarNodos(root))