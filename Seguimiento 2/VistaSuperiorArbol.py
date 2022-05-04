class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def vistaSup(root):
    return vistaSupAux(root)
def vistaSupAux(root):
    values=[root.val]
    tree1=root
    tree2=root
    while not tree1:
        values.append(tree1.val)
        tree1=tree1.left
    while not tree2:
        values.append(tree2.val)
        tree2=tree2.left
    return values