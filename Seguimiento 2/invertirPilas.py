from collections import deque
from typing import Any


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def reverse(self):
    prev = None
    current = self.head
    while(current is not None):
         next = current.next
         current.next = prev
         prev = current
         current = next
    self.head = prev




def invertir(head: Node, nuevo=None):
    pila = deque()
    n = 0
    if head is not None:
        while n < 5:
            pila.append(Node(head))
            nuevo.next = head
    print(pila)


""""
    class Node:
        def __init__(self, val: int):
            self.val = val
            self.next = None

    def insertarAlInicio(head: Node, valor: int) -> Node:
        nuevo = Node(val=valor)
        nuevo.next = head
        return nuevo
"""
