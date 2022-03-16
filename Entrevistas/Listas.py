class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def printLista(head: Node) -> Node:
    temp = head
    while (temp != None):
        print(temp.val)
        temp = temp.next


def invertir(head: Node) -> Node:
    if head == None:
        return None
    anterior = None
    actual = head
    siguiente = head.next
    while (siguiente != None):
        actual.next = anterior  # invertir
        anterior = actual
        actual = siguiente
        siguiente = siguiente.next
    actual.next = anterior
    return actual


def main():
    nodo1 = Node(1)
    nodo2 = Node(2)
    nodo3 = Node(3)
    nodo4 = Node(4)
    nodo1.next = nodo2
    nodo2.next = nodo3
    nodo3.next = nodo4
    printLista(nodo1)
    print("...")
    inv = invertir(nodo1)
    printLista(inv)


main()