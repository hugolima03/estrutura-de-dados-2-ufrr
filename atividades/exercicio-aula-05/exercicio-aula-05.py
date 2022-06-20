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

def altura(root):
  if root is None:
    return -1
  leftAns = altura(root.left)
  rightAns = altura(root.right)
  return max(leftAns, rightAns) + 1

def printTree(root, level=0):
  if root is not None:
    printTree(root.right, level+1)
    print(' ' * 4 * level + '-> ' + str(root.value))
    printTree(root.left, level+1)

def maximo(root):
  if root is None:
    return float('-inf')
  res = root.value
  lres = findMax(root.left)
  rres = findMax(root.right)
  if (lres > res):
    res = lres
  elif (rres > res):
    res = rres
  return res

def minimo(root):
  if root is None:
    return ''
  res = root.value
  lres = minimo(root.left)
  rres = minimo(root.right)
  if (lres < res):
    res = lres
  elif (rres < res):
    res = rres
  return res

def deleteNode(root, value):
  if root is None:
      return None
  elif value < root.value:
      root.left = deleteNode(root.left, value)
  elif value > root.value:
      root.right = deleteNode(root.right, value)
  else:  # No foi encontrado
      # Caso 1: No folha
      if root.left and root.right is None:
          root = None
      # Caso 2: No tem um filho
      elif root.left is None:
          temp = root
          root = root.right
          temp = None
      elif root.right is None:
          temp = root
          root = root.left
          temp = None
      # Caso 3: No tem dois filhos
      else:
          minNode = findMin(root.right)
          root.value = minNode.value
          root.right = deleteNode(root.right, minNode.value)
  return root

root = None
root = insert(root, 10)
root = insert(root, 5)
root = insert(root, 15)
root = insert(root, 20)
root = insert(root, 2)
deleteNode(root, 20)

printTree(root)
print(altura(root))
print(minimo(root))
  