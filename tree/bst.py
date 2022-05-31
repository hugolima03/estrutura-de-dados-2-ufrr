class Node:
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None

n10 = Node(10)
n8 = Node(8)
n25 = Node(25)
n15 = Node(15)

n10.right = n25
n10.left = n8
n25.left = n15

def printBST(root):
  if root:
    print(root.key)
    printBST(root.left)
    printBST(root.right)


printBST(n10)