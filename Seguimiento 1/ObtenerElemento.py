class Node:
    def _init_(self, val):
        self.val = val
        self.next = None

def posicion(head: Node, i: int) -> int:
    NodoActual = head
    if NodoActual == None:
        return 0
    else:
        for index in range(i-1):
            NodoActual = head.next
        return NodoActual.val