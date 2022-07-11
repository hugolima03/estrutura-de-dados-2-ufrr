class MaxHeap:
    def __init__(self):
        self.heap = []

    def getParentPosition(self, i):
        return int((i-1)/2)

    def getLeftChildPosition(self, i):
        return 2*i+1

    def getRightChildPosition(self, i):
        return 2*i+2

    def hasParent(self, i):
        return self.getParentPosition(i) < len(self.heap)

    def hasLeftChild(self, i):
        return self.getLeftChildPosition(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.getRightChildPosition(i) < len(self.heap)

    def insert(self, key):
        self.heap.append(key)
        self.heapify(len(self.heap) - 1)

    def getMax(self):
        return self.heap[0]
    
    def printHeap(self):
        print(self.heap) 

    def printLeftRootRight(self, low, high): # PROF! NÃO CONSEGUI FORMATAR O PRINT COM OS PARENTESES CORRETAMENTE
      if low > high:
        return
      self.printLeftRootRight(low*2 + 1, high)
      print("{left}/{right}".format(left = self.heap[low][0], right = self.heap[low][1]), end=" ")
      self.printLeftRootRight(low*2 + 2, high)

    def heapify(self, i):
        while(self.hasParent(i) and self.heap[i][1] > self.heap[self.getParentPosition(i)][1]): # Loops until it reaches a leaf node
            self.heap[i], self.heap[self.getParentPosition(i)] = self.heap[self.getParentPosition(i)], self.heap[i] # Swap the values
            i = self.getParentPosition(i) # Resets the new position

while True:
  heap = MaxHeap()
  data = input().split(' ')
  n = int(data[0])
  if (n == 0): break
  cases = data[1: n + 1]

  for val in cases:
    nodeval, priority = val.split('/')
    heap.insert((nodeval, priority))
  heap.printLeftRootRight(0, len(heap.heap) - 1)

# heap = MaxHeap()
# heap.insert(('a', 3))
# heap.insert(('b', 6))
# heap.insert(('c', 4))
# heap.insert(('d', 7))
# heap.insert(('e', 2))
# heap.insert(('f', 5))
# heap.insert(('g', 1))
# # heap.printHeap()
# heap.printLeftRootRight(0, len(heap.heap) - 1)



# maxHeap = MaxHeap(15)
# maxHeap.insert(5)
# maxHeap.insert(3)
# maxHeap.insert(17)
# maxHeap.insert(10)
# maxHeap.insert(84)
# maxHeap.insert(19)
# maxHeap.insert(6)
# maxHeap.insert(22)
# maxHeap.insert(9)


