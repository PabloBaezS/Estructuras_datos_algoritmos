class Node:
    def __init__(self, dato):
        self.dato = dato
        self.left = None
        self.right = None


def buscarBST(root, elemento):
    if root is None:
        return False
    if root.dato == elemento:
        return True
    else:
        buscarIzq = buscarBST(root.left, elemento)
        buscarDer = buscarBST(root.right, elemento)
        if buscarIzq or buscarDer:
            return True
        else:
            return False


def buscarBST2(root, el):
    if root is None:
        return False
    if root.valor == el:
        return True

    if el < root.valor:
        return buscarBST2(root.left, el)
    else:
        return buscarBST2(root.right, el)


root = Node(1)
nodo2 = Node(2)
nodo3 = Node(3)
nodo4 = Node(4)
nodo5 = Node(5)
nodo6 = Node(6)
nodo7 = Node(7)

root.left = nodo2
root.right = nodo3
nodo3.left = nodo4
nodo3.right = nodo5
nodo2.left = nodo6
nodo2.right = nodo7

print(buscarBST(root,7))
