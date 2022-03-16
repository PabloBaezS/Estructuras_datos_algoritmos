class Node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

def maximo(head: Node) -> int:
    temp = 0
    tempNext = head.next
    if  head == None:
        return 0 #si no hay nada retorna 0
    else:
        primerValor = head.val
        MaximoDelSiguiente = maximo(head.next)
        return max(primerValor, MaximoDelSiguiente)
