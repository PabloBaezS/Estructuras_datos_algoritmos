class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def compare(l1: Node, l2: Node) -> bool:
    primeraLista = l1
    segundaLista = l2
    while (primeraLista != None and segundaLista != None):
        if (primeraLista.val != segundaLista.val):
            return False
        primeraLista = primeraLista.next
        segundaLista = segundaLista.next
    return True

def main():
    nodo1 = Node(1)
    nodo2 = Node(2)
    nodo3 = Node(4)
    nodo7 = Node(5)
    nodo1.next = nodo2
    nodo2.next = nodo3
    nodo3.next = nodo7

    nodo4 = Node(1)
    nodo5 = Node(2)
    nodo6 = Node(4)
    nodo8 = Node(5)
    nodo4.next = nodo5
    nodo5.next = nodo6
    nodo6.next = nodo8
    print(compare(nodo1,nodo4))
main()