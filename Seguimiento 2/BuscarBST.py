class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def BuscarBST(root,val):
    if(root):
        if(val == root.val):
            return "YES"
        if(val > root.val):
            return BuscarBST(root.right,val)
        elif(val < root.val):
            return BuscarBST(root.left,val)
        else:
            return "NO"
    else:
        return "NO"
