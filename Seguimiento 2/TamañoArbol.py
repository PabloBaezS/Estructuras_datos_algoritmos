class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def TamañoArbol(root):
    if root is None:
        return 0
    elif root.left and root.right is not None:
        return 1 + TamañoArbol(root.left) + TamañoArbol(root.right) + 2
    elif root.left is not None:
        return TamañoArbol(root.left) + 1
    elif root.right is not None:
        return TamañoArbol(root.right) + 1
    else:
        return 0 