# tomado de internet
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def invertir(head: Node) -> Node:
    if head == None:
        return None
    anterior = None
    actual = head
    siguiente = head.next
    while (siguiente != None):
        actual.next = anterior
        anterior = actual
        actual = siguiente
        siguiente = siguiente.next
    actual.next = anterior
    return actual


def imprimir(head: Node) -> None:
    while (head != None):
        print(head.val)
    head = head.next