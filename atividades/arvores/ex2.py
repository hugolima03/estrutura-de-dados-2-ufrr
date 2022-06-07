class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def countSubTree(root, count):
    if root is None:
        return True
    left = countSubTree(root.left, count)
    right = countSubTree(root.right, count)
    if left == False or right == False:
        return False
    if root.left and root.val != root.left.val:
        return False
    if root.right and root.val != root.right.val:
        return False
    count[0] += 1
    return True

def countTrees(root):
    count = [0]
    countSubTree(root, count)
    return count[0]

root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
#   0
#  /\
# 1  0
#   / \
#  1   0
# / \
# 1  1

print("Numero de subarvores univais ", countTrees(root))
