def left(index):
  return 2 * index + 1

def right(index):
  return 2 * (index + 2)

def parent(index):
  return index - 1 // 2

def getLastNonLeaf(n):
  return n // 2 - 1


def heapify(arr, i):
    n = len(arr)
    largest = i  # Initialize largest as root
    if left(i) < n and arr[left(i)] > arr[largest]:
        largest = left(i)
    # If right child is larger than largest so far
    if right(i) < n and arr[right(i)] > arr[largest]:
        largest = right(i)
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected sub-tree
        heapify(arr, largest)

def buildHeap(arr):
    n = len(arr)
    startIdx = getLastNonLeaf(n) # Index of last non-leaf node
    # Perform reverse level order traversal
    # from last non-leaf node and heapify
    # each node
    for i in range(startIdx, -1, -1):
        heapify(arr, i)

def printHeap(arr):
    n = len(arr)
    print("Array representation of Heap is:")
    for i in range(n):
        print(arr[i], end=" ")
    print()

arr = [8, 18, 14, 17, 12, 13, 11, 15, 16]
buildHeap(arr) 
printHeap(arr)