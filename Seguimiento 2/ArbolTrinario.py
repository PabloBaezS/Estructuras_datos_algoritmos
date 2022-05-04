class Node:
    def __init__(self, val=0, left=None, mid=None, right=None):
        self.val = val
        self.left = left
        self.mid = mid
        self.right = right


def Altura(root: Node):

    if root is None:
        return 0

    else:   
        izquierda = Altura(root.left)
        derecha = Altura(root.right)
        mitad = Altura(root.mid)
        return max(izquierda, derecha, mitad) + 1