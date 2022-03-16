class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def buscar(head: Node, k : int) -> int:
    if head == None:
        return -1
    if head.val == k:
        return 0
    else:
        laPosicionAPartirDelSiguiente = buscar(head.next ,k)
        if laPosicionAPartirDelSiguiente == -1:
            return -1
        else:
            return  laPosicionAPartirDelSiguiente + 1