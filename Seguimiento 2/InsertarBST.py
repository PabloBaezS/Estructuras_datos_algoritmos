class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


def InsertarBST(root, val):
    if root is None:
        root = val
    else:
        if root.value < val:
            if root.right is None:
                root.right = val
            else:
                InsertarBST(root.right, val)
        else:
            if root.left is None:
                root.left = val
            else:
                InsertarBST(root.left, val)
    return root
