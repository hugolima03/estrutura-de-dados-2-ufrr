def isMaxHeap(array):
   n = len(array)
   for i in range(n):
      m = i * 2
      num = array[i]
      if m + 1 < n:
         if num < array[m + 1]:
            return False
      if m + 2 < n:
         if num < array[m + 2]:
            return False
   return True

array = [8, 6, 4, 2, 0, 3]
print(isMaxHeap(array))