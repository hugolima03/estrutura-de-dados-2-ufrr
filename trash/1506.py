class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        elif value > root.value:
            root.right = insert(root.right, value)
    return root

def getHeight(root):
    if root is None:
        return -1
    leftAns = getHeight(root.left)
    rightAns = getHeight(root.right)
    return max(leftAns, rightAns) + 1


def printTree(root, level=0):
    if root is not None:
        printTree(root.right, level+1)
        print(' ' * 4 * level + '-> ' + str(root.value))
        printTree(root.left, level+1)


root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)

printTree(root)
print(getHeight(root))
