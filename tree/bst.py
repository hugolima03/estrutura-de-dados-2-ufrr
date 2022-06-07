import queue

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

def deleteDeepest(root,d_node):
  q = []
  q.append(root)
  while(len(q)):
    temp = q.pop(0)
    if temp is d_node:
      temp = None
      return
    if temp.right:
      if temp.right is d_node:
        temp.right = None
        return
      else:
        q.append(temp.right)
    if temp.left:
      if temp.left is d_node:
        temp.left = None
        return
      else:
        q.append(temp.left)

def deletion(root, key):
  if root == None :
    return None
  if root.left == None and root.right == None:
    if root.key == key :
      return None
    else :
      return root
  key_node = None
  q = []
  q.append(root)
  temp = None
  while(len(q)):
    temp = q.pop(0)
    if temp.value == key:
      key_node = temp
    if temp.left:
      q.append(temp.left)
    if temp.right:
      q.append(temp.right)
  if key_node :
    x = temp.value
    deleteDeepest(root,temp)
    key_node.value = x
  return root

# PERCURSOS EM PROFUNDADE (DFS)
def inOrder(root):
  if root:
    inOrder(root.left)
    print(root.value, end = " ")
    inOrder(root.right)

def preOrdem(root):
  if root:
    print(root.value)
    preOrdem(root.left)
    preOrdem(root.right)

def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' * 4 * level + '-> ' + str(root.value))
    printTree(root.left, level+1)

def findMin(root):
  if root is None:
    return None
  while root.left != None:
    root = root.left
  return root.value

def findMax(root):
  if root is None:
    return None
  while root.right != None:
    root = root.right
  return root.value

def findHeight(root):
  if root is None:
    return -1
  leftH = findHeight(root.left)
  rightH = findHeight(root.right)
  return max(leftH, rightH) + 1

# Percurso em Level (BFS)
q = queue.Queue()

def levelOrder(root):
  if root is None:
    return None
  q.put(root)
  while not q.empty():
    current = q.queue[0]
    print(current.value, end=" ")
    if current.left is not None: q.put(current.left)
    if current.right is not None: q.put(current.right)
    q.get()

root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 35)
root = insert(root, 2)
root = insert(root, 8)
root = insert(root, 40)
root = insert(root, 38)
root = insert(root, 51)

printTree(root)
print('min: ', findMin(root))
print('max: ', findMax(root))
print('height: ', findHeight(root))
deletion(root, 35)
levelOrder(root)