class Node:
    def __init__(self, val : int):
        self.val = val
        self.next = None

def insertarAlInicio(head: Node, valor:int) -> Node:
    nuevo = Node(val = valor)
    nuevo.next = head
    return nuevo